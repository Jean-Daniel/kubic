import sys
from collections import defaultdict
from collections.abc import Iterable

from .k8s import QualifiedName, module_for_group, type_name_from_property_name
from .types import (
    TypeAlias,
    ApiResourceType,
    ObjectType,
    Property,
    Type,
    AnonymousType,
    GenericType,
    ApiType,
    ApiTypeRef,
    NamedProperty,
)

TimeType = TypeAlias(
    QualifiedName("Time", "meta", "v1"),
    "str",
    description="ISO date-time")

QuantityType = TypeAlias(
    QualifiedName("Quantity", "core", "v1"),
    "str | int | float",
    description="Quantity is a fixed-point representation of a number. "
                "It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors.",
)

IntOrStringType = TypeAlias(
    QualifiedName("IntOrString", "core", "v1"),
    "int | str",
    description="IntOrString is a type that can hold an int32 or a string.",
)

Base64Type = TypeAlias(
    QualifiedName("Base64", "core", "v1"),
    "str",
    description="binary data encoded in base64",
)


class ApiGroup:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

        # group types
        self.types: list[ApiType] = []

        self._types: dict[str, ApiType] = {}
        self._anonymous: dict[str, list[AnonymousType]] = defaultdict(list)

        # imports
        self.use_typing: bool = False
        self._refs: set[str] = set()
        self._base_types: set[str] = set()

    def __repr__(self):
        return f"ApiGroup {{ name: {self.name}, {len(self._types)} types: }}"

    def __contains__(self, item: ApiType):
        if item.group and item.group != self.name:
            return False

        return item.name in self._types

    def get(self, fqn: QualifiedName) -> ApiType | None:
        return self._types.get(fqn.name)

    def _quote(self, value: str, quote: bool):
        return f'"{value}"' if quote else value

    def qualified_name(self, ty, parent_type=None) -> str:
        if isinstance(ty, ApiType):
            if ty not in self:
                return f"{module_for_group(ty.group)}.{ty.name}"
            return self._quote(ty.name, ty == parent_type)

        if isinstance(ty, GenericType):
            types = (self.qualified_name(value, parent_type) for value in ty.parameters)
            return f"{ty.base_type}[{', '.join(types)}]"

        return str(ty)

    def add(self, api_type: ApiType):
        if isinstance(api_type, AnonymousType):
            self._anonymous[api_type.name].append(api_type)
        else:
            assert api_type.name not in self._types
            self._types[api_type.name] = api_type

    @property
    def base_types(self) -> Iterable[str]:
        return self._base_types

    @property
    def refs(self) -> Iterable[str]:
        return self._refs

    def _rename(self, item: AnonymousType):
        item.fqn = QualifiedName(item.fullname, item.group, item.version)
        # ensure uniqueness
        idx = 1
        fullname = item.name
        while item.name in self._types:
            item.fqn = QualifiedName(f"{fullname}{idx}", item.group, item.version)
            idx += 1

        assert item.name not in self._types, item.name
        self._types[item.name] = item

    # list of items with the same name
    def rename_duplicated(self, items: list[AnonymousType]):
        types: list[list[AnonymousType]] = []

        # Count effective number of ≠ types
        for duplicated in items:
            # Try to group items by matching type
            for atypes in types:
                if atypes[0] == duplicated:
                    atypes.append(duplicated)
                    break
            else:
                types.append([duplicated])

        # This is a effectively a single type use at different places
        if len(types) == 1:
            # no conflict, add type
            base = types[0][0]
            if base.name in self._types:
                # a base type with this name already exists
                # FIXME: should guess a common name.
                self._rename(base)
                # Apply change to other matching types
                for ty in types[0][1:]:
                    ty.fqn = base.fqn
            else:
                self._types[base.name] = base
        else:
            # There is multiples conflicting types with the same name
            counter = 1
            types.sort(key=lambda i: len(i), reverse=True)
            for typs in types:
                # We are supposed to use fullname,
                # but if there is more than 1 item, and items have ≠ fullname, use indexed base name instead.
                # else we may end up having incoherent fullname for renamed items.
                fullname = typs[0].fullname
                if any(ty.fullname != fullname for ty in typs[1:]):
                    base = typs[0]
                    # For the type with most matching types -> use the original name
                    if counter > 1 or base.name in self._types:
                        name = f"{base.name}{counter}"
                        for ty in typs:
                            ty.fqn = QualifiedName(name, base.group, base.version)
                    assert base.name not in self._types
                    self._types[base.name] = base
                    counter += 1
                else:
                    self._rename(typs[0])
                    for ty in typs[1:]:
                        ty.fqn = typs[0].fqn

    def finalize(self):
        for name, items in self._anonymous.items():
            if len(items) == 1:
                item = items[0]
                if item.name in self._types:
                    # a base type with this name already exists
                    self._rename(item)
                else:
                    self._types[item.name] = item
                continue

            self.rename_duplicated(items)

        # Sort types by dependency
        types = []
        dones = set()
        for ty in sorted(self._types.values(), key=lambda k: k.name):
            if ty.name in dones:
                continue
            dones.add(ty.name)

            self.add_imports_for_type(ty)
            # insert all dependencies
            dependencies = self._fetch_dependencies(ty, dones)
            dependencies.extend(types)
            types = dependencies

        self.types = reversed(types)

    def add_imports_for_type(self, ty):
        if isinstance(ty, ApiType):
            if ty in self:
                if isinstance(ty, ObjectType):
                    self._base_types.add(ty.kubic_type)
                elif sys.version_info >= (3, 10) and isinstance(ty, TypeAlias):
                    self.use_typing = True
            elif ty.group:
                self._refs.add(ty.group)
        else:
            if ty == "t.Any":
                self.use_typing = True

    def _fetch_generic_params(self, ty: GenericType, into: list):
        self.add_imports_for_type(ty)
        for param in ty.parameters:
            if isinstance(param, GenericType):
                self._fetch_generic_params(param, into)
            else:
                into.append(param)

    def _fetch_dependencies(self, ty: ApiType, dones: set) -> list[ApiType]:
        dependencies = []

        # resolve internal reference
        if isinstance(ty, ApiTypeRef):
            # _fetch_dependencies assumes ty is a type internal to the group
            ty = self._types[ty.name]

        if isinstance(ty, ObjectType):
            properties = (prop.type for prop in ty.properties)
        else:
            assert isinstance(ty, TypeAlias), f"depends on type: {type(ty)}"
            properties = [ty.type]

        for prop_type in properties:
            if isinstance(prop_type, GenericType):
                self._fetch_generic_params(prop_type, dependencies)
                dependencies.extend(prop_type.parameters)
            else:
                dependencies.append(prop_type)

        types = []
        for dependency in dependencies:
            self.add_imports_for_type(dependency)

            if not isinstance(dependency, ApiType):
                continue

            # if type is not part of the group -> skip it (external type like IntOrString)
            if dependency not in self:
                continue

            if dependency.name in dones:
                continue
            dones.add(dependency.name)

            subtypes = self._fetch_dependencies(dependency, dones)
            # prepend subtypes to types
            subtypes.extend(types)
            types = subtypes

        types.insert(0, ty)
        return types


class Parser:
    def __init__(self):
        self._pendings: list[tuple[ObjectType, dict]] = []
        self._string_fmts: dict[str, TypeAlias] = {
            "int-or-string": IntOrStringType,
            "byte": Base64Type,
            "date-time": TimeType,
        }

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        raise NotImplementedError()

    def annotations_for_type(self, obj_type: ObjectType) -> dict | None:
        return None

    @property
    def pendings(self) -> Iterable[tuple[ObjectType, dict]]:
        def iterator():
            while self._pendings:
                yield self._pendings.pop()

        return iterator()

    def _register_type(self, obj_type: ObjectType, schema: dict):
        self.group_for_type(obj_type.fqn).add(obj_type)
        self._pendings.append((obj_type, schema))

    # Parse object schema and create properties
    def import_resource(self, obj_type: ObjectType, schema: dict):
        assert "$ref" not in schema
        assert "properties" in schema, f"{obj_type.name} does not have properties"

        # parse properties
        required = schema.get("required", [])
        patch = self.annotations_for_type(obj_type)
        is_api_resource = isinstance(obj_type, ApiResourceType)
        for prop, value in schema["properties"].items():
            # skip prepopulated values
            if is_api_resource and (prop == "apiVersion" or prop == "kind"):
                continue

            snake_name = None
            if patch:
                overwrite = patch.get(prop, value)
                if not overwrite:
                    continue

                # shortcut as this is the most common case
                if isinstance(overwrite, str):
                    ref = {"type": "object"} if overwrite == "object" else {"$ref": overwrite}
                    if value.get("type") == "array":
                        overwrite = {"type": "array", "items": ref}
                    else:
                        overwrite = ref

                special = 0
                # type override (for anonymous prop only)
                name = overwrite.get("type_name")
                if name:
                    value["_type_name_"] = name
                    special += 1

                snake_name = overwrite.get("snake_name")
                if snake_name:
                    special += 1

                if len(overwrite) > special:
                    # make sure array are replaced by array
                    assert (
                            value.get("type") != "array" or overwrite.get("type") == "array"
                    ), f"{obj_type.name}.{prop}: {value.get('type')} ≠ {overwrite.get('type')}"
                    value = overwrite
            prop_type = self.import_property(obj_type, prop, value, is_plural=False)
            if prop_type:
                obj_type.properties.append(
                    NamedProperty(prop, prop_type, prop in required, value.get("description"), snake_name)
                    if snake_name
                    else Property(prop, prop_type, prop in required, value.get("description"))
                )
        obj_type.properties.sort()

    def import_property(self, obj_type: ApiType, prop_name: str, schema: dict, is_plural: bool) -> Type:
        ty = schema.get("type")
        if ty:
            return self.import_base_property(obj_type, prop_name, schema, ty, is_plural)

        return self.import_complex_property(obj_type, prop_name, schema)

    def import_base_property(self, obj_type: ApiType, prop_name: str, schema: dict, prop_type: str, is_plural: bool) -> Type:
        if prop_type == "object":
            # if no properties, this is just an alias for generic object
            if "properties" in schema:
                assert isinstance(obj_type, ObjectType)
                # this is an anonymous type -> register it for parsing later
                ty = AnonymousType.with_property(schema.get("_type_name_", prop_name), obj_type, is_plural)
                self._register_type(ty, schema)
                return ty

            if "additionalProperties" in schema:
                details = schema["additionalProperties"]
                if "_type_name_" in schema:
                    details["_type_name_"] = schema["_type_name_"]
                vtype = self.import_property(obj_type, prop_name, details, is_plural=True)
                return GenericType("dict", ("str", vtype))

            return GenericType("dict", ("str", "t.Any"))

        if prop_type == "integer":
            return "int"

        if prop_type == "boolean":
            return "bool"

        if prop_type == "string":
            fmt = schema.get("format")
            if not fmt:
                return "str"

            ty = self._string_fmts.get(fmt)
            if ty:
                return ty

            name = type_name_from_property_name(fmt, is_plural=False)
            ty = TypeAlias(
                QualifiedName(name, obj_type.fqn.group, obj_type.fqn.version),
                "str", description="")
            self._string_fmts[fmt] = ty
            return ty

        if prop_type == "number":
            fmt = schema.get("format")
            if fmt == "double":
                return "float"
            assert not fmt, f"number format {fmt} not supported"
            return "int"

        if prop_type == "array":
            details = schema.get("items")
            if details:
                if "_type_name_" in schema:
                    details["_type_name_"] = schema["_type_name_"]
                vtype = self.import_property(obj_type, prop_name, details, is_plural=True)
                return GenericType("list", (vtype,))
            return "list"

        raise NotImplementedError(f"{prop_type} base type not supported")

    def import_complex_property(self, obj_type: ApiType, prop_name: str, schema: dict):
        # union = schema.get("oneOf")
        # if not union:
        #     union = schema.get("anyOf")
        #
        # if union:
        #     types = [self._get_type_name(item, prop_name) for item in union]
        #     return f"Union[{', '.join(types)}]"
        if schema.get("x-kubernetes-preserve-unknown-fields", False):
            return "t.Any"

        if schema.get("x-kubernetes-int-or-string", False):
            return IntOrStringType

        raise NotImplementedError(f"type not supported: {schema}")
