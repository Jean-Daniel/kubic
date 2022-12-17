import logging
import os
from collections import defaultdict
from collections.abc import Iterable

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

logger = logging.getLogger("api")


def _is_greater_version(v1: str, v2: str) -> bool:
    if v2[1] > v1[1]:
        return True
    elif v1[1] > v2[1]:
        return False
    # no alpha/beta qualifier -> stable
    if len(v1) == 2:
        return False
    elif len(v2) == 2:
        return True
    return v2 > v1


class ApiParser(Parser):
    def __init__(self, schema: str | dict, annotations: dict):
        super().__init__()
        self.annotations = annotations
        self._groups: dict[str, ApiGroup] = {}

        if isinstance(schema, (str, os.PathLike)):
            with open(schema) as f:
                schema = yaml.load(f, yaml.CSafeLoader)

        if "definitions" in schema:
            self.components = schema["definitions"]
        else:
            self.components = schema["components"]["schemas"]

        # short name to fqn map
        self.index: dict[str, QualifiedName] = {}
        self.ambiguous: dict[str, set[str]] = defaultdict(set)
        for key in self.components.keys():
            group, version, name = key.rsplit(".", maxsplit=2)
            fqn = QualifiedName(name, group, version)
            shortname = fqn.name.lower()

            existing = self.index.get(shortname)
            if existing:
                self.ambiguous[shortname].add(fqn.version)
                self.ambiguous[shortname].add(existing.version)
                if _is_greater_version(existing.version, fqn.version):
                    self.index[shortname] = fqn
            else:
                self.index[shortname] = fqn

    @property
    def groups(self) -> Iterable[ApiGroup]:
        return self._groups.values()

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        group = self._groups.get(fqn.group)
        if not group:
            group = ApiGroup(fqn.group, fqn.version)
            self._groups[fqn.group] = group
        return group

    def annotations_for_type(self, obj_type: ObjectType) -> dict | None:
        return self.annotations.get(f"{obj_type.group}.{obj_type.version}.{obj_type.name}")

    def import_types(self, names: Iterable[str]) -> list[ApiGroup]:
        # register builtin types
        for t in (IntOrStringType, QuantityType, Base64Type, TimeType, IDNHostname):
            self.group_for_type(t).add(t)

        if not names:
            names = self.components.keys()

        for name in names:
            ref = name if name in self.components else None
            if not ref and "." not in name:
                fqn = self.index.get(name.lower())
                if fqn:
                    ref = f"{fqn.group}.{fqn.version}.{fqn.name}"
                    if name.lower() in self.ambiguous:
                        logger.info(
                            "Using version %s for %s. Existing version: %s",
                            fqn.version,
                            name,
                            ", ".join(self.ambiguous[name.lower()]),
                        )

            if not ref:
                raise ValueError(f"unknown type '{name}' requested")
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

    def import_ref(self, ref: str) -> Type:
        fqn = QualifiedName.parse(ref)
        group = self.group_for_type(fqn)

        typedecl = group.get(fqn)
        if typedecl:
            return typedecl

        schema = self.components[ref]

        assert "$ref" not in schema
        if "type" not in schema:
            logger.warning(f"unsupported type {schema}")
            return "t.Any"

        if schema["type"] == "object" and "properties" in schema:
            # Create ObjectType or ApiResourceType

            gvk = schema.get("x-kubernetes-group-version-kind")
            if gvk:
                # dirty schema fixup
                assert fqn.name == gvk[0]["kind"], f"extract kind {fqn.name} does not match type declared kind {gvk[0]['kind']}"
                group = gvk[0]["group"]
                if not group and fqn.group in ("core", "meta"):
                    group = fqn.group
                assert fqn.group == group, f"extract group '{fqn.group}' does not match type declared group '{gvk[0]['group']}': {ref}"
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
        alias = TypeAlias(fqn, "", schema.get("description"))
        alias.type = self.import_property(alias, fqn.name, schema)
        group.add(alias)
        return alias


def import_api_types(schema: str, annotations: dict, *names) -> list[ApiGroup]:
    if annotations is None:
        # Default API Annotations
        annotations = {
            "meta.v1.ObjectMeta": {
                "managedFields": None
            },
            "apiextensions.k8s.io.v1.CustomResourceValidation": {
                "openAPIV3Schema": {"snake_name": "openapi_v3_schema"}
            }
        }

    parser = ApiParser(schema, annotations)
    return parser.import_types(names)
