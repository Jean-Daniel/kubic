from collections import defaultdict
from typing import Dict, Union, Iterable, List, Optional

import yaml

from pykapi.k8s import QualifiedName, CLUSTER_OBJECTS
from pykapi.parser import (
    Parser,
    ApiGroup,
    IntOrStringType,
    Base64Type,
    TimeType,
    IDNHostname,
    QuantityType,
)
from pykapi.types import Type, ApiType, TypeAlias, ApiResourceType, ObjectType


def simplename(key: str) -> str:
    return key.rsplit(".", maxsplit=1)[1] if "." in key else key


def shortkey(key: str):
    return simplename(key).lower()


class ApiParser(Parser):
    def __init__(self, schema: Union[str, dict], annotations: dict):
        super().__init__()
        self.annotations = annotations
        self._groups: Dict[str, ApiGroup] = {}

        if isinstance(schema, str):
            with open(schema) as f:
                schema = yaml.load(f, yaml.CSafeLoader)

        if "definitions" in schema:
            self.components = schema["definitions"]
        else:
            self.components = schema["components"]["schemas"]

        # short name to fqn map
        self.index: Dict[str, str] = {}
        self.ambiguous: Dict[str, List[str]] = defaultdict(list)
        for key in self.components.keys():
            short = shortkey(key)
            if short in self.index:
                self.ambiguous[short].append(key)
            else:
                self.index[short] = key

    @property
    def groups(self) -> Iterable[ApiGroup]:
        return self._groups.values()

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        group = self._groups.get(fqn.group)
        if not group:
            group = ApiGroup(fqn.group, fqn.version)
            self._groups[fqn.group] = group
        return group

    def annotations_for_type(self, obj_type: ObjectType) -> Optional[dict]:
        return self.annotations.get(
            f"{obj_type.group}.{obj_type.version}.{obj_type.name}"
        )

    def import_types(self, names: Iterable[str]) -> List[ApiGroup]:
        # register builtin types
        for t in (IntOrStringType, QuantityType, Base64Type, TimeType, IDNHostname):
            self.group_for_type(t).add(t)

        if not names:
            names = self.components.keys()

        for name in names:
            ref = self.index.get(name.lower(), name)
            if ref == name and ref not in self.components:
                raise ValueError(f"unknown type {ref} requested")

            if ref.startswith("io.k8s.apiextensions-apiserver.pkg.apis.apiextensions"):
                continue

            if name.lower() in self.ambiguous:
                raise ValueError(
                    f"ambiguous short key {name}: {ref}, {', '.join(self.ambiguous[name.lower()])}"
                )
            self.import_ref(ref)

        for pending, schema in self.pendings:
            self.import_resource(pending, schema)

        # finalize groups
        for group in self._groups.values():
            group.finalize()

        return list(self._groups.values())

    def import_resource(self, obj_type: ObjectType, schema: dict):
        if isinstance(obj_type, ApiResourceType):
            schema["properties"].pop("status", None)

        super().import_resource(obj_type, schema)

    def import_property(self, obj_type: ApiType, prop_name: str, schema: dict) -> Type:
        # API Importer only
        ref = schema.get("$ref")
        if ref:
            # for ref -> import type recursively
            ty = self.import_ref(ref.removeprefix("#/definitions/"))
            return ty

        return super().import_property(obj_type, prop_name, schema)

    def import_ref(self, ref: str) -> ApiType:
        fqn = QualifiedName.parse(ref)
        group = self.group_for_type(fqn)

        typedecl = group.get(fqn)
        if typedecl:
            return typedecl

        schema = self.components[ref]

        assert "$ref" not in schema
        assert "type" in schema, f"unsupported type {schema}"
        if schema["type"] == "object" and "properties" in schema:
            # Create ObjectType or ApiResourceType

            gvk = schema.get("x-kubernetes-group-version-kind")
            if gvk:
                # dirty schema fixup
                assert (
                    fqn.name == gvk[0]["kind"]
                ), f"extract kind {fqn.name} does not match type declared kind {gvk[0]['kind']}"
                group = gvk[0]["group"]
                if not group and fqn.group in ("core", "meta"):
                    group = fqn.group
                assert fqn.group == (
                    group
                ), f"extract group '{fqn.group}' does not match type declared group '{gvk[0]['group']}': {ref}"
                assert (
                    fqn.version == gvk[0]["version"]
                ), f"extract version {fqn.version} does not match type declared version {gvk[0]['version']}"
                typedecl = ApiResourceType(
                    fqn,
                    schema.get("description"),
                    schema.get("x-scoped", fqn.name not in CLUSTER_OBJECTS),
                )
            else:
                typedecl = ObjectType(fqn, schema.get("description"))

            self._register_type(typedecl, schema)
            return typedecl

        # Type Alias

        # Create alias type
        alias = TypeAlias(fqn, "", schema.get("description"))
        alias.type = self.import_property(alias, fqn.name, schema)
        group.add(alias)
        return alias


def import_api_types(
    schema: Union[str, dict], annotations: dict, *names
) -> List[ApiGroup]:
    parser = ApiParser(schema, annotations)
    return parser.import_types(names)
