from collections import defaultdict
from typing import List, Iterable, Tuple, Optional, Dict, Set, Union

from .k8s import QualifiedName, type_name_from_property_name
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

IntOrStringType = TypeAlias(
    QualifiedName("IntOrString", "core", "v1"), "Union[str, int]"
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
        self._typing: Set[str] = set()
        self._refs: Set[str] = set()

    def __repr__(self):
        return f"ApiGroup {{ name: {self.name}, {len(self._types)} types: }}"

    def get(self, fqn: QualifiedName) -> Optional[ApiType]:
        return self._types.get(fqn.name)

    def add(self, api_type: ApiType):
        if isinstance(api_type, AnonymousType):
            self._anonymous[api_type.name].append(api_type)
        else:
            self._types[api_type.name] = api_type

    @property
    def refs(self) -> Iterable[str]:
        return self._refs

    def import_type(self, api_type: Union[ApiType, QualifiedName]):
        if api_type.group != self.name:
            self._refs.add(api_type.group)

    @property
    def typing(self) -> Iterable[str]:
        return self._typing

    def import_typing(self, symbol: str):
        self._typing.add(symbol)

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
                            item.parent_name + item.name, item.group, item.version
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

            if isinstance(ty, ObjectType):
                # insert all dependencies
                dependencies = self._fetch_dependencies(ty, dones)
                dependencies.extend(types)
                types = dependencies
            else:
                types.insert(0, ty)

        self.types = reversed(types)

    def _fetch_dependencies(self, ty: ObjectType, dones: set) -> List[ApiType]:
        types = []
        for prop in ty.properties:
            dependency = prop.type
            if isinstance(dependency, GenericType):
                dependency = dependency.value_type
            if not isinstance(dependency, ApiType):
                continue

            # if type is not part of the group -> skip it (external type like IntOrString)
            member = self._types.get(dependency.name)
            if not member or member != dependency:
                continue

            if dependency.name in dones:
                continue
            dones.add(dependency.name)

            if isinstance(dependency, ObjectType):
                subtypes = self._fetch_dependencies(dependency, dones)
                # prepend subtypes to types
                subtypes.extend(types)
                types = subtypes
            else:
                # prepend dependency
                types.insert(0, dependency)

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
            # for REST API only
            if is_api_resource and prop == "status":
                continue

            # skip prepopulated values
            if is_api_resource and (prop == "apiVersion" or prop == "kind"):
                continue

            if patch:
                value = patch.get(prop, value)
                if not value:
                    continue

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
                # this is an anonymous type -> register it for parsing later
                assert isinstance(obj_type, ObjectType)
                ty = AnonymousType(
                    QualifiedName(type_name_from_property_name(prop_name), "", ""),
                    obj_type,
                )
                self._register_type(ty, schema)
                return ty

            group = self.group_for_type(obj_type.fqn)
            if "additionalProperties" in schema:
                group.import_typing("Dict")
                return GenericType(
                    "Dict",
                    self.import_property(
                        obj_type, prop_name, schema["additionalProperties"]
                    ),
                )

            group.import_typing("Dict")
            group.import_typing("Any")
            return GenericType("Dict", "Any")

        if prop_type == "integer":
            return "int"

        if prop_type == "boolean":
            return "bool"

        if prop_type == "string":
            fmt = schema.get("format")
            if fmt == "int-or-string":
                self.group_for_type(obj_type.fqn).import_typing("Union")
                return "Union[int, str]"
            if fmt == "byte":
                self.group_for_type(obj_type.fqn).import_type(Base64Type)
                return Base64Type
            if fmt == "date-time":
                self.group_for_type(obj_type.fqn).import_type(TimeType)
                return TimeType
            # cilium cluster wide network policy
            if fmt == "idn-hostname":
                self.group_for_type(obj_type.fqn).import_type(IDNHostname)
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
                self.group_for_type(obj_type.fqn).import_typing("List")
                return GenericType(
                    "List", self.import_property(obj_type, prop_name, details)
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
        group = self.group_for_type(obj_type.fqn)
        if schema.get("x-kubernetes-preserve-unknown-fields", False):
            group.import_typing("Any")
            return "Any"

        if schema.get("x-kubernetes-int-or-string", False):
            group.import_type(IntOrStringType)
            return IntOrStringType

        raise NotImplementedError(f"type not supported: {schema}")
