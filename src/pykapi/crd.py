from typing import Optional, NamedTuple, TextIO

from .k8s import QualifiedName
from .parser import Parser, ApiGroup
from .printer import TypePrinter
from .types import ApiResourceType, ObjectType, AnonymousType, Type, TypeAlias, ApiType


class CRDParser(Parser):
    def __init__(self, api_type: ApiResourceType, schema: dict, annotations: dict):
        super().__init__()
        self.group = ApiGroup(api_type.group, api_type.version)
        self.group.add(api_type)

        # patching root schema
        schema["properties"]["metadata"] = {
            "!ref": "io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta"
        }
        self.annotations = annotations

        self._register_type(api_type, schema)

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        return self.group

    def annotations_for_type(self, obj_type: ObjectType) -> Optional[dict]:
        if isinstance(obj_type, AnonymousType):
            base = self.annotations_for_type(obj_type.parent)
        else:
            base = self.annotations
        return base.get(obj_type.name) if base else None

    def process(self) -> ApiGroup:
        for obj_type, schema in self.pendings:
            self.import_resource(obj_type, schema)
        self.group.finalize()
        return self.group

    def import_property(
        self, obj_type: ObjectType, prop_name: str, schema: dict
    ) -> Type:
        # API Importer only
        ref = schema.get("!ref")
        if ref:
            # for ref -> import type recursively
            fqn = QualifiedName.parse(ref)
            return ApiType(fqn)
        return super().import_property(obj_type, prop_name, schema)


class CRD(NamedTuple):
    type: ApiResourceType
    group: ApiGroup


class CRDPrinter(TypePrinter):
    def __init__(self, crd: CRD):
        super().__init__("..")
        self.crd = crd

    def print(self, output: str):
        self.print_group(self.crd.group, output)

    def print_types(self, group: ApiGroup, stream: TextIO):
        super().print_types(group, stream)
        self.print_type_alias(
            group, TypeAlias(QualifiedName("New", "", ""), self.crd.type), stream
        )


def import_crd(fqn: QualifiedName, schema: dict, annotations) -> CRD:
    api_type = ApiResourceType(fqn, schema.get("x-scoped", True))
    parser = CRDParser(api_type, schema, annotations)
    return CRD(api_type, parser.process())
