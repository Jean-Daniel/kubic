import sys
from collections import defaultdict
from typing import List, Iterable, Tuple, Optional, Dict, Set

from .k8s import QualifiedName, module_for_group
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

TimeType = TypeAlias(QualifiedName("Time", "meta", "v1"), "str", description="ISO date-time")

QuantityType = TypeAlias(
    QualifiedName("Quantity", "core", "v1"),
    GenericType("Union", ["str", "int", "float"]),
    description="Quantity is a fixed-point representation of a number. "
                "It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors.",
)

IntOrStringType = TypeAlias(
    QualifiedName("IntOrString", "core", "v1"),
    GenericType("Union", ["str", "int"]),
    description="IntOrString is a type that can hold an int32 or a string.",
)
IDNHostname = TypeAlias(QualifiedName("IDNHostname", "core", "v1"), "str", description="")
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
        self.types: List[ApiType] = []
        self._types: Dict[str, ApiType] = {}
        self._anonymous: Dict[str, List[AnonymousType]] = defaultdict(list)

        # imports
        self._refs: Set[str] = set()
        self._typing: Set[str] = set()
        self._base_types: Set[str] = set()

    def __repr__(self):
        return f"ApiGroup {{ name: {self.name}, {len(self._types)} types: }}"

    def __contains__(self, item: ApiType):
        if item.group and item.group != self.name:
            return False

        return item.name in self._types

    def get(self, fqn: QualifiedName) -> Optional[ApiType]:
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
    def typing(self) -> Iterable[str]:
        return self._typing

    @property
    def base_types(self) -> Iterable[str]:
        return self._base_types

    @property
    def refs(self) -> Iterable[str]:
        return self._refs

    def _rename(self, item):
        item.fqn = QualifiedName(item.fullname, item.group, item.version)
        assert item.name not in self._types, item.name
        self._types[item.name] = item

    def rename_duplicated(self, items: List[AnonymousType]):
        types: List[List[AnonymousType]] = []

        for duplicated in items:
            # Try to group items by matching type
            for atypes in types:
                if atypes[0] == duplicated:
                    atypes.append(duplicated)
                    break
            else:
                types.append([duplicated])

        # all types match
        if len(types) == 1:
            # no conflict, add type
            base = types[0][0]
            if base.name in self._types:
                # a base type with this name already exists
                self._rename(base)
            else:
                self._types[base.name] = base
        else:
            types.sort(key=lambda i: len(i), reverse=True)
            for idx, ty in enumerate(types):
                # generate indexed names if names do not match.
                if len(ty) > 1 and any(t.fullname != ty[0].fullname for t in ty):
                    base = ty[0]
                    # For the type with most matching types -> use the original name
                    if idx > 0 or base.name in self._types:
                        name = f"{base.name}{idx + 1}"
                        for t in ty:
                            t.fqn = QualifiedName(name, base.group, base.version)
                    assert base.name not in self._types
                    self._types[base.name] = base
                else:
                    self._rename(ty[0])
                    for t in ty[1:]:
                        t.fqn = ty[0].fqn

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
        for ty in sorted(self._types.values(), key=lambda t: t.name):
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
        if isinstance(ty, GenericType):
            self._typing.add(ty.base_type)
        elif isinstance(ty, ApiType):
            if ty in self:
                if isinstance(ty, ObjectType):
                    self._base_types.add(ty.kubic_type)
                elif sys.version_info >= (3, 10) and isinstance(ty, TypeAlias):
                    self._typing.add("TypeAlias")
            elif ty.group:
                self._refs.add(ty.group)
        else:
            if ty == "Any":
                self._typing.add("Any")

    def _fetch_generic_params(self, ty: GenericType, into: list):
        self.add_imports_for_type(ty)
        for param in ty.parameters:
            if isinstance(param, GenericType):
                self._fetch_generic_params(param, into)
            else:
                into.append(param)

    def _fetch_dependencies(self, ty: ApiType, dones: set) -> List[ApiType]:
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
        self._pendings: List[Tuple[ObjectType, dict]] = []

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        raise NotImplementedError()

    def annotations_for_type(self, obj_type: ObjectType) -> Optional[dict]:
        return None

    @property
    def pendings(self) -> Iterable[Tuple[ObjectType, dict]]:
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
                    if value.get("type") == "array":
                        overwrite = {"type": "array", "items": {"$ref": overwrite}}
                    else:
                        overwrite = {"$ref": overwrite}

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
            prop_type = self.import_property(obj_type, prop, value)
            if prop_type:
                obj_type.properties.append(
                    NamedProperty(prop, prop_type, prop in required, snake_name)
                    if snake_name
                    else Property(prop, prop_type, prop in required)
                )
        obj_type.properties.sort()

    def import_property(self, obj_type: ApiType, prop_name: str, schema: dict) -> Type:
        ty = schema.get("type")
        if ty:
            return self.import_base_property(obj_type, prop_name, schema, ty)

        return self.import_complex_property(obj_type, prop_name, schema)

    def import_base_property(self, obj_type: ApiType, prop_name: str, schema: dict, prop_type: str) -> Type:
        if prop_type == "object":
            # if no properties, this is just an alias for generic object
            if "properties" in schema:
                assert isinstance(obj_type, ObjectType)
                # this is an anonymous type -> register it for parsing later
                ty = AnonymousType.with_property(schema.get("_type_name_", prop_name), obj_type)
                ty.description = schema.get("description")
                self._register_type(ty, schema)
                return ty

            if "additionalProperties" in schema:
                details = schema["additionalProperties"]
                if "_type_name_" in schema:
                    details["_type_name_"] = schema["_type_name_"]
                vtype = self.import_property(obj_type, prop_name, details)
                return GenericType("Dict", ("str", vtype))

            return GenericType("Dict", ("str", "Any"))

        if prop_type == "integer":
            return "int"

        if prop_type == "boolean":
            return "bool"

        if prop_type == "string":
            fmt = schema.get("format")
            if fmt == "int-or-string":
                return GenericType("Union", ("int", "str"))
            if fmt == "byte":
                return Base64Type
            if fmt == "date-time":
                return TimeType
            # cilium cluster wide network policy
            if fmt == "idn-hostname":
                return IDNHostname

            assert not fmt, f"string format {fmt} not supported"
            return "str"

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
                vtype = self.import_property(obj_type, prop_name, details)
                return GenericType("List", (vtype,))
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
            return "Any"

        if schema.get("x-kubernetes-int-or-string", False):
            return IntOrStringType

        raise NotImplementedError(f"type not supported: {schema}")
