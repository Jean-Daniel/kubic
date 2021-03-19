from collections import defaultdict
from typing import Optional, Tuple, List

from .k8s import QualifiedName
from .parser import Parser, ApiGroup
from .types import ApiResourceType, ObjectType, AnonymousType, Type, ApiType


class CRDGroup(ApiGroup):
    def __init__(self, name: str, version: str):
        super().__init__(name, version)
        self.aliases = set()

    def __contains__(self, item):
        if item.group in self.aliases:
            return True
        return super().__contains__(item)

    def add(self, api_type: ApiType):
        super().add(api_type)
        self.aliases.add(api_type.group)


class CRDParser(Parser):
    def __init__(self, group: str, version: str, annotations: dict):
        super().__init__()
        self.group = CRDGroup(group, version)
        # patching root schema
        self.annotations = annotations

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        return self.group

    def annotations_for_type(self, obj_type: ObjectType) -> Optional[dict]:
        if not self.annotations:
            return None

        # Look up by fullname first
        if isinstance(obj_type, AnonymousType):
            annotations = self.annotations.get(obj_type.fullname)
            if annotations:
                return annotations
        # obj_type is the root type -> lookup annotation for that type
        return self.annotations.get(obj_type.name)

    def process(self, *resources: Tuple[QualifiedName, dict]) -> ApiGroup:
        for fqn, schema in resources:
            schema["properties"]["metadata"] = {
                "$ref": "io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta"
            }
            # may contains items from remapped groups
            self._register_type(
                ApiResourceType(fqn, schema.get("x-scoped", True)), schema
            )

        for obj_type, schema in self.pendings:
            self.import_resource(obj_type, schema)
        self.group.finalize()
        return self.group

    def import_property(
        self, obj_type: ObjectType, prop_name: str, schema: dict
    ) -> Type:
        ref = schema.get("$ref")
        if ref:
            # for ref -> import type recursively
            fqn = QualifiedName.parse(ref)
            # ApiType is just a TypeRef
            return ApiType(fqn)
        return super().import_property(obj_type, prop_name, schema)

    def import_base_property(
        self, obj_type: ApiType, prop_name: str, schema: dict, prop_type: str
    ) -> Type:
        # common pattern matching
        if schema.get("type") == "object":
            if is_label_selector(schema):
                return ApiType(QualifiedName("LabelSelector", "meta", "v1"))

        return super().import_base_property(obj_type, prop_name, schema, prop_type)


def is_label_selector(schema: dict) -> bool:
    properties = schema.get("properties")
    if not properties:
        return False
    if len(properties) != 2:
        return False

    if "matchExpressions" not in properties or "matchLabels" not in properties:
        return False

    return (
        properties["matchExpressions"].get("type") == "array"
        and "additionalProperties" in properties["matchLabels"]
    )


def import_crds(annotations, *crds: Tuple[QualifiedName, dict]) -> List[ApiGroup]:
    groups = annotations.get("groups") or {}
    # in case there is CRDs from many groups/versions.
    crds_by_groups = defaultdict(list)
    for fqn, schema in crds:
        group = groups.get(fqn.group, fqn.group)
        crds_by_groups[(group, fqn.version)].append((fqn, schema))

    groups = []
    for (group, version), crds in crds_by_groups.items():
        parser = CRDParser(group, version, annotations.get(group))
        groups.append(parser.process(*crds))

    return groups
