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
)

TimeType = TypeAlias(QualifiedName("Time", "meta", "v1"), "str")

QuantityType = TypeAlias(
    QualifiedName("Quantity", "core", "v1"),
    GenericType("Union", ["str", "int", "float"]),
)

IntOrStringType = TypeAlias(
    QualifiedName("IntOrString", "core", "v1"), GenericType("Union", ["str", "int"])
)
IDNHostname = TypeAlias(QualifiedName("IDNHostname", "core", "v1"), "str")
Base64Type = TypeAlias(QualifiedName("Base64", "core", "v1"), "str")


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

    def qualified_name(self, ty) -> str:
        if isinstance(ty, ApiType):
            if ty not in self:
                return f"{module_for_group(ty.group)}.{ty.name}"
            return ty.name

        if isinstance(ty, GenericType):
            types = (self.qualified_name(value) for value in ty.parameters)
            return f"{ty.base_type}[{', '.join(types)}]"

        return str(ty)

    def add(self, api_type: ApiType):
        if isinstance(api_type, AnonymousType):
            self._anonymous[api_type.name].append(api_type)
        else:
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

    def finalize(self):
        for name, items in self._anonymous.items():
            base = items[0]
            if len(items) == 1:
                self._types[base.name] = base
                continue

            for duplicated in items[1:]:
                if duplicated != base:
                    # Mark all items as conflicting and fix the output type list
                    for item in items:
                        item.fqn = QualifiedName(
                            item.fullname, item.group, item.version
                        )
                        if (
                            item.name in self._types and self._types[item.name] != item
                        ) or (
                            item.name in self._anonymous
                            and self._anonymous[item.name] != item
                        ):
                            raise ValueError(f"{item.name} still conflicting")
                        self._types[item.name] = item

                    # We are done for this conflict
                    break
            else:
                # no conflict, add type
                self._types[base.name] = base

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
        if isinstance(ty, ObjectType):
            properties = (prop.type for prop in ty.properties)
        else:
            assert isinstance(ty, TypeAlias)
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

                # type override (for anonymous prop only)
                name = overwrite.pop("type_name", None)
                if name:
                    value["_type_name_"] = name

                if overwrite:
                    # make sure array are replaced by array
                    assert (
                        value.get("type") != "array" or overwrite.get("type") == "array"
                    ), f"{obj_type.name}.{prop}: {value.get('type')} ≠ {overwrite.get('type')}"
                    value = overwrite
            prop_type = self.import_property(obj_type, prop, value)
            if prop_type:
                obj_type.properties.append(Property(prop, prop_type, prop in required))
        obj_type.properties.sort()

    def import_property(self, obj_type: ApiType, prop_name: str, schema: dict) -> Type:
        ty = schema.get("type")
        if ty:
            return self.import_base_property(obj_type, prop_name, schema, ty)

        return self.import_complex_property(obj_type, prop_name, schema)

    def import_base_property(
        self, obj_type: ApiType, prop_name: str, schema: dict, prop_type: str
    ) -> Type:
        if prop_type == "object":
            # if no properties, this is just an alias for generic object
            if "properties" in schema:
                assert isinstance(obj_type, ObjectType)
                # this is an anonymous type -> register it for parsing later
                ty = AnonymousType.with_property(
                    schema.get("_type_name_", prop_name), obj_type
                )
                self._register_type(ty, schema)
                return ty

            if "additionalProperties" in schema:
                return GenericType(
                    "Dict",
                    (
                        "str",
                        self.import_property(
                            obj_type, prop_name, schema["additionalProperties"]
                        ),
                    ),
                )

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
                return GenericType(
                    "List", (self.import_property(obj_type, prop_name, details),)
                )
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
