import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from functools import cache
from typing import NamedTuple, List, Union, Iterable, Dict, Set, Any, TextIO
from urllib.request import urlretrieve

import yaml
from yaml import CSafeLoader

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "schemas")

# List of types that are not scoped to namespace
CLUSTER_OBJECTS = {
    "ComponentStatus",
    "Namespace",
    "Node",
    "PersistentVolume",
    "MutatingWebhookConfiguration",
    "ValidatingWebhookConfiguration",
    "CustomResourceDefinition",
    "APIService",
    "TokenReview",
    "SelfSubjectAccessReview",
    "SelfSubjectRulesReview",
    "SubjectAccessReview",
    "ClusterIssuer",
    "CertificateSigningRequest",
    "CiliumClusterwideNetworkPolicy",
    "CiliumExternalWorkload",
    "CiliumIdentity",
    "CiliumNode",
    "FlowSchema",
    "PriorityLevelConfiguration",
    "NodeMetrics",
    "IngressClass",
    "RuntimeClass",
    "ObjectBucket",
    "PodSecurityPolicy",
    "ClusterRoleBinding",
    "ClusterRole",
    "PriorityClass",
    "CSIDriver",
    "CSINode",
    "StorageClass",
    "VolumeAttachment",
}


def simplename(key: str) -> str:
    return key.rsplit(".", maxsplit=1)[1] if "." in key else key


def shortkey(key: str):
    return simplename(key).lower()


def snake_to_camel(name: str) -> str:
    components = name.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


# used to fix camel_to_snake edge cases (URLs -> _url_s for instance)
PLURALS = {"URLs": "_urls", "WWNs": "_wwns", "CIDRs": "_cidrs"}

KEYWORDS = {
    "if",
    "for",
    "def",
    "class",
    "from",
    "import",
    "except",
    "break",
    "continue",
}


def naive_camel_to_snake(name: str) -> str:
    return "".join("_" + i.lower() if i.isupper() else i for i in name).lstrip("_")


@cache
def camel_to_snake(name: str):
    # cilium node for instance uses '-' in vars
    snake = name.replace("-", "_")
    # edge cases
    for orig, replace in PLURALS.items():
        snake = snake.replace(orig, replace)

    snake = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", snake)
    snake = re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake).lower()
    # avoid conflict with keywords
    if snake in KEYWORDS:
        snake += "_"
    return snake


ACRONYMES = {"tls", "ipam"}


def type_name_from_property_name(name: str):
    # assuming 2 and 3 letters words are acronyms
    if len(name) <= 3:
        return name.upper()

    # egress for instance
    if name.endswith("s") and not name.endswith("ss"):
        name = name.removesuffix("s")

    for ac in ACRONYMES:
        if name.startswith(ac):
            return ac.upper() + name[len(ac) :]
    return name[0].upper() + name[1:]


class ListType(NamedTuple):
    value_type: Any

    def __str__(self):
        return f"List[{str(self.value_type)}]"


class DictType(NamedTuple):
    value_type: Any

    def __str__(self):
        return f"Dict[str, {str(self.value_type)}]"


class TypeAlias:
    def __init__(self, name: str, ty: Any):
        self.name = name
        self.type = ty

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __str__(self):
        return self.name


class Property(NamedTuple):
    name: str
    type: Any
    required: bool

    @property
    def base_type(self) -> Any:
        if isinstance(self.type, (ListType, DictType)):
            return self.type.value_type
        return self.type

    @property
    def type_name(self) -> str:
        return str(self.type)

    @property
    def snake_name(self):
        return camel_to_snake(self.name)


GROUP_MAPPING = {
    "io.k8s.api.core": "",
    "io.k8s.api.networking": "networking.k8s.io",
    "io.k8s.api.rbac": "rbac.authorization.k8s.io",
    "io.k8s.api.admissionregistration": "admissionregistration.k8s.io",
}


class QualifiedName(NamedTuple):
    name: str
    group: str
    version: str

    def __str__(self):
        return self.name

    @classmethod
    def from_string(cls, name):
        parts = name.rsplit(".", maxsplit=2)
        if len(parts) == 3:
            group = GROUP_MAPPING.get(parts[0])
            if group is None:
                group = parts[0].removeprefix("io.k8s.api.")
            return QualifiedName(parts[2], group, parts[1])

        return QualifiedName(name, "", "")


class ObjectType:
    def __init__(self):
        self.properties: List[Property] = []

    def __eq__(self, other):
        return self.properties == other.properties

    @property
    def required_properties(self):
        return (prop for prop in self.properties if prop.required)

    @property
    def optional_properties(self):
        return (prop for prop in self.properties if not prop.required)


class ResourceType(ObjectType):
    def __init__(self, fqn: QualifiedName):
        super().__init__()
        self.fqn = fqn

    @property
    def name(self):
        return self.fqn.name

    @property
    def group(self):
        return self.fqn.group

    @property
    def version(self):
        return self.fqn.version

    def __eq__(self, other):
        return self.name == other.name and super().__eq__(other)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name}: {self.properties}"


class ApiResourceType(ResourceType):
    def __init__(self, name: QualifiedName, scoped: bool):
        super().__init__(name)
        self.scoped = scoped

    @property
    def kind(self):
        return self.fqn.name


class AnonymousType(ObjectType):
    def __init__(self, name: str, class_name: str):
        super().__init__()
        self.name = name
        self.class_name = class_name

    def __eq__(self, other):
        return self.name == other.name and super().__eq__(other)


TypeDef = Union[TypeAlias, ResourceType, ApiResourceType, AnonymousType]

BASE_OBJECT_TYPE = "KubernetesObject"
RESOURCE_OBJECT_TYPE = "KubernetesApiResource"


class BaseImporter:
    def __init__(self, schema: Union[str, dict]):
        if isinstance(schema, str):
            with open(schema) as f:
                schema = yaml.load(f, CSafeLoader)

        if "definitions" in schema:
            self.components = schema["definitions"]
        else:
            self.components = schema["components"]["schemas"]

        self.imports = set()

        # generated resources
        self.resources: Dict[str, TypeDef] = {}
        self.stack: List[str] = []  # loop detection

        self.conflicts: Dict[str, List[AnonymousType]] = {}
        self.anonymous: Set[str] = set()

    @property
    def types(self) -> Iterable[TypeDef]:
        return self.resources.values()

    def _import_type(self, fqn: str, schema: dict, anonymous: bool = False) -> TypeDef:
        ty = self.resources.get(fqn) if not anonymous else None
        if ty:
            assert (
                fqn not in self.stack
            ), "circular dependency -> needs forward declaration"
            return ty

        name = QualifiedName.from_string(fqn)

        self.stack.append(fqn)
        ty = self._parse_type(name, schema, anonymous)
        self.stack.pop()

        if anonymous:
            # name may have been updated by generator
            type_name = str(ty.name)
            if type_name in self.anonymous:
                existing = self.resources[type_name]
                if type_name not in self.conflicts:
                    self.conflicts[type_name] = [existing, ty]
                else:
                    self.conflicts[type_name].append(ty)

                # if ty != existing:
                #    raise ValueError(f"{fqn} types conflicts: {ty.class_name} and {existing.class_name}")
                return ty

            self.anonymous.add(type_name)

        self.resources[fqn] = ty
        return ty

    # Create a (api)resource and populate its properties
    def _parse_type(self, fqn: QualifiedName, schema: dict, anonymous: bool) -> TypeDef:
        assert "$ref" not in schema

        if schema["type"] == "object" and "properties" in schema:
            return self._parse_resource(fqn, schema, anonymous)

        # anonymous alias are not possible, so prop_name should not be relevant here
        typename = self._get_type(schema, "")

        # In practice, controller accept numbers for Quantity
        if fqn.name == "Quantity" and "str" == typename:
            self.imports.add("Union")
            typename = "Union[str, int, float]"

        if sys.version_info >= (3, 10):
            self.imports.add("TypeAlias")
        return TypeAlias(fqn.name, typename)

    def _parse_resource(
        self, fqn: QualifiedName, schema: dict, anonymous: bool
    ) -> ResourceType:
        gvk = schema.get("x-kubernetes-group-version-kind")
        if gvk:
            assert (
                fqn.name == gvk[0]["kind"]
            ), f"extract kind {fqn.name} does not match type declared kind {gvk[0]['kind']}"
            assert (
                fqn.group == gvk[0]["group"]
            ), f"extract group {fqn.group} does not match type declared group {gvk[0]['group']}"
            assert (
                fqn.version == gvk[0]["version"]
            ), f"extract version {fqn.version} does not match type declared version {gvk[0]['version']}"
            obj = ApiResourceType(
                fqn, schema.get("x-scoped", fqn.name not in CLUSTER_OBJECTS)
            )
        elif anonymous:
            if len(self.stack) == 2:
                # child of root element -> use qualified name by default ?
                root = simplename(self.stack[0])
                name = root + fqn.name
            obj = AnonymousType(fqn.name, simplename(self.stack[-2]))
        else:
            obj = ResourceType(fqn)

        # parse properties
        required = schema.get("required", [])
        assert "properties" in schema, f"{fqn.name} does not have properties"

        for prop, value in schema["properties"].items():
            # for REST API only
            if gvk and prop == "status":
                continue

            # skip prepopulated values
            if (prop == "apiVersion" or prop == "kind") and gvk is not None:
                continue

            prop_type = self._get_type(value, prop)
            if prop_type:
                obj.properties.append(Property(prop, prop_type, prop in required))
        obj.properties.sort()
        return obj

    def _get_type(
        self, schema: dict, prop_name: str, generic_param: bool = False
    ) -> Any:
        ref = schema.get("$ref")
        if ref:
            # for ref -> import type recursively
            ref = ref.removeprefix("#/definitions/")
            return self._import_type(ref, self.components[ref])

        ty = schema.get("type")
        if ty:
            return self._get_base_type(ty, schema, prop_name)

        return self._get_complex_type(ty, schema, prop_name)

    def _get_base_type(self, ty, schema: dict, prop_name: str) -> Any:
        if ty == "object":
            # if no properties, this is just an alias for generic object
            if "properties" in schema:
                return self._import_type(
                    type_name_from_property_name(prop_name), schema, anonymous=True
                )

            if "additionalProperties" in schema:
                self.imports.add("Dict")
                return DictType(
                    self._get_type(
                        schema["additionalProperties"], prop_name, generic_param=True
                    )
                )

            self.imports.add("Dict")
            self.imports.add("Any")
            return DictType("Any")

        if ty == "integer":
            return "int"

        if ty == "boolean":
            return "bool"

        if ty == "string":
            fmt = schema.get("format")
            if fmt == "int-or-string":
                self.imports.add("Union")
                return "Union[int, str]"
            if fmt == "byte":
                return self._import_type("Base64", {"type": "string"})
            if fmt == "date-time":
                # in API, only Time uses date-time format.
                if self.stack[-1] == "io.k8s.apimachinery.pkg.apis.meta.v1.Time":
                    return "str"
                # but keep a fallback for CRDs
                return self._import_type(
                    "io.k8s.apimachinery.pkg.apis.meta.v1.Time", {"type": "string"}
                )
            # cilium cluster wide network policy
            if fmt == "idn-hostname":
                return self._import_type("IDNHostname", {"type": "string"})
            assert not fmt, f"string format {fmt} not supported"
            return "str"

        if ty == "number":
            fmt = schema.get("format")
            if fmt == "double":
                return "float"
            assert not fmt, f"number format {fmt} not supported"
            return "int"

        if ty == "array":
            details = schema.get("items")
            if details:
                self.imports.add("List")
                return ListType(self._get_type(details, prop_name, generic_param=True))
            return "list"

        raise NotImplementedError(f"{ty} base type not supported")

    def _get_complex_type(self, ty, schema: dict, prop_name: str) -> Any:
        # union = schema.get("oneOf")
        # if not union:
        #     union = schema.get("anyOf")
        #
        # if union:
        #     types = [self._get_type_name(item, prop_name) for item in union]
        #     return f"Union[{', '.join(types)}]"

        if schema.get("x-kubernetes-preserve-unknown-fields", False):
            self.imports.add("Any")
            return "Any"

        if schema.get("x-kubernetes-int-or-string", False):
            return self._import_type(
                "io.k8s.apimachinery.pkg.util.intstr.IntOrString",
                {"type": "string", "format": "int-or-string"},
            )

        raise NotImplementedError(f"type not supported: {schema}")

    def print_api(self, output: str, crd: bool = False):
        if output == "-":
            stream = sys.stdout
        else:
            stream = open(output, "w")
        try:
            if self.imports:
                stream.write("from typing import ")
                stream.write(", ".join(sorted(self.imports)))
                stream.write("\n\n")
            if crd:
                stream.write(
                    f"from ..base import {BASE_OBJECT_TYPE}, {RESOURCE_OBJECT_TYPE}\n"
                )
                stream.write("from .. import api\n")
            else:
                stream.write(
                    f"from .base import {BASE_OBJECT_TYPE}, {RESOURCE_OBJECT_TYPE}\n"
                )
            stream.write("\n\n")

            for ty in self.types:
                if isinstance(ty, ResourceType):
                    print_type(ty, stream)
                else:
                    print_type_alias(ty, stream)
                stream.write("\n")
        finally:
            if stream is not sys.stdout:
                stream.close()


def print_type_alias(ty: TypeAlias, stream: TextIO):
    stream.write(ty.name)
    if sys.version_info >= (3, 10):
        stream.write(": TypeAlias = ")
    else:
        stream.write(" = ")
    stream.write(str(ty.type))
    stream.write("\n\n")


def print_type(ty: ResourceType, stream: TextIO):
    stream.write("class ")
    stream.write(ty.name)
    if isinstance(ty, ApiResourceType):
        stream.write(f"({RESOURCE_OBJECT_TYPE})")
    else:
        stream.write(f"({BASE_OBJECT_TYPE})")
    stream.write(":\n")
    stream.write("    __slots__ = ()\n")

    if isinstance(ty, ResourceType):
        stream.write(f'\n    _group_ = "{ty.group}"\n')
        stream.write(f'    _version_ = "{ty.version}"\n')

    required = [prop.snake_name for prop in ty.required_properties]
    if required:
        stream.write('\n    _required_ = ["')
        stream.write('", "'.join(required))
        stream.write('"]\n')

    # write fields mapping
    fields = {}
    revfields = {}
    for prop in ty.properties:
        snake = prop.snake_name
        if prop.name != snake_to_camel(snake):
            fields[snake] = prop.name
        if naive_camel_to_snake(prop.name) != snake:
            revfields[prop.name] = snake

    if fields:
        stream.write("\n    _field_names_ = {\n")
        for snake, camel in fields.items():
            stream.write(f'        "{snake}": "{camel}",\n')
        stream.write("    }\n")

    if revfields:
        if not fields:
            stream.write("\n")
        stream.write("    _revfield_names_ = {\n")
        for camel, snake in revfields.items():
            stream.write(f'        "{camel}": "{snake}",\n')
        stream.write("    }\n")

    stream.write("\n")
    for prop in ty.properties:
        stream.write("    ")
        stream.write(prop.snake_name)
        stream.write(": ")
        stream.write(prop.type_name)
        stream.write("\n")

    stream.write("\n    def __init__(self")
    if isinstance(ty, ApiResourceType):
        stream.write(", name: str")
        if ty.scoped:
            stream.write(", namespace: str = None")
    for prop in ty.properties:
        stream.write(", ")
        stream.write(prop.snake_name)
        stream.write(": ")
        stream.write(prop.type_name)
        stream.write(" = None")
    stream.write("):\n")
    stream.write("        super().__init__(")
    if isinstance(ty, ApiResourceType):
        stream.write('"')
        if ty.group:
            stream.write(f"{ty.group}/")
        stream.write(f'{ty.version}"')
        stream.write(", ")
        stream.write(f'"{ty.kind}"')
        stream.write(", name")
        if ty.scoped:
            stream.write(", namespace")
        else:
            stream.write(', ""')
        if ty.properties:
            stream.write(", ")
    for idx, prop in enumerate(ty.properties):
        if idx != 0:
            stream.write(", ")
        stream.write(prop.snake_name)
        stream.write("=")
        stream.write(prop.snake_name)

    stream.write(")\n\n")


class ApiImporter(BaseImporter):
    def __init__(self, schema: Union[str, dict], annotations: dict = None):
        super().__init__(schema)

        self.annotations = annotations

        # short name to fqn map
        self.index = {}
        self.ambiguous = defaultdict(list)

        for key in self.components.keys():
            short = shortkey(key)
            if short in self.index:
                self.ambiguous[short].append(key)
            else:
                self.index[short] = key

    def import_type(self, ty: str) -> TypeDef:
        fqn = self.index.get(ty.lower(), ty)
        if fqn == ty and fqn not in self.components:
            raise ValueError(f"unknown type {fqn} requested")

        if ty.lower() in self.ambiguous:
            raise ValueError(
                f"ambiguous short key {ty}: {fqn}, {', '.join(self.ambiguous[ty.lower()])}"
            )
        return self._import_type(fqn, self.components[fqn])

    def _get_type(
        self, schema: dict, prop_name: str, generic_param: bool = False
    ) -> Any:
        fqn = self.stack[-1]
        # _get_type may be call twice for the same property when parsing generics
        # handle overwrite only on first call (to avoid infinite recursion)
        if not generic_param:
            overwrite = self.annotations.get(fqn)
            if overwrite:
                schema = overwrite.get(prop_name, schema)
                # empty schema means skip this property.
                if not schema:
                    return None

        return super()._get_type(schema, prop_name, generic_param)


class CRDImporter(BaseImporter):
    def __init__(self, schema: dict, annotations: dict = None):
        super().__init__(schema)

        self.annotations = annotations
        self.overwrite = [annotations]

    def _import_type(self, fqn: str, schema: dict, anonymous: bool = False) -> TypeDef:
        # root type -> patch metadata
        if not self.stack:
            schema["properties"]["metadata"] = {"$ref": "api.ObjectMeta"}

        if self.overwrite[-1]:
            self.overwrite.append(self.overwrite[-1].get(fqn))
        else:
            self.overwrite.append(None)
        ty = super()._import_type(fqn, schema, anonymous)
        self.overwrite.pop()
        return ty

    def _get_type(
        self, schema: dict, prop_name: str, generic_param: bool = False
    ) -> Any:
        ref = schema.get("$ref")
        if ref:
            return ref

        if not generic_param and self.overwrite[-1]:
            overwrite = self.overwrite[-1].get(prop_name)
            if overwrite:
                return overwrite
        return super()._get_type(schema, prop_name, generic_param)

    def import_crd(self) -> ResourceType:
        assert len(self.components) == 1, "CRD must contains a single item"
        for ty, schema in self.components.items():
            crd = self._import_type(ty, schema)
            assert isinstance(crd, ApiResourceType) and crd.properties

        self.resolve_conflicts()

    def resolve_conflicts(self):
        has_conflict = False
        for name, items in self.conflicts.items():
            base = items[0]
            for duplicated in items[1:]:
                if duplicated != base:
                    has_conflict = True
                    # remove base resource
                    del self.resources[name]
                    # Mark all items as conflicting and fix the output type list
                    for item in items:
                        item.name = item.class_name + item.name
                        existing = self.resources.get(item.name)
                        if existing and existing != item:
                            raise ValueError(f"{item.name} still conflicting")
                        self.resources[item.name] = item

                    # We are done for this conflict
                    break

        if has_conflict:
            # We have to resort types
            types = {}
            while self.resources:
                name, item = next(iter(self.resources.items()))
                del self.resources[name]
                self.get_dependencies(item, self.resources, types)
                types[name] = item

            self.resources = types

    def get_dependencies(self, ty: Any, src, dest):
        if not isinstance(ty, ResourceType):
            return
        for prop in ty.properties:
            ty = prop.base_type
            dep = src.pop(str(ty), None)
            if dep:
                self.get_dependencies(prop.type, src, dest)
                dest[str(ty)] = dep


def import_k8s_api(args, annotations):
    # import kubernetes types
    file = os.path.join(args.schemas, "1.20.json")
    if not os.path.exists(file):
        tmp, headers = urlretrieve(
            "https://github.com/kubernetes/kubernetes/raw/release-1.20/api/openapi-spec/swagger.json"
        )
        with open(tmp, "rb") as f:
            data = json.load(f)
        data.pop("paths", None)
        data.pop("security", None)
        data.pop("securityDefinitions", None)
        with open(file, "w") as f:
            json.dump(data, f, indent="  ", sort_keys=True)

    if annotations:
        with open(annotations, "rb") as f:
            annotations = yaml.load(f, CSafeLoader)

    schema = ApiImporter(file, annotations)

    schema.import_type("Namespace")
    schema.import_type("io.k8s.api.rbac.v1.Role")
    schema.import_type("io.k8s.api.rbac.v1.RoleBinding")
    schema.import_type("io.k8s.api.rbac.v1.ClusterRole")
    schema.import_type("io.k8s.api.rbac.v1.ClusterRoleBinding")

    schema.import_type("ConfigMap")
    schema.import_type("Secret")

    schema.import_type("Deployment")
    schema.import_type("StatefulSet")
    schema.import_type("DaemonSet")
    schema.import_type("Job")
    schema.import_type("io.k8s.api.batch.v1beta1.CronJob")
    schema.import_type("NetworkPolicy")
    schema.import_type("ResourceQuota")
    schema.import_type("PersistentVolume")
    schema.import_type("PodSecurityPolicy")
    schema.import_type("PodDisruptionBudget")
    schema.import_type("io.k8s.api.autoscaling.v1.HorizontalPodAutoscaler")
    schema.import_type("io.k8s.api.autoscaling.v1.CrossVersionObjectReference")
    schema.import_type(
        "io.k8s.api.admissionregistration.v1.MutatingWebhookConfiguration"
    )

    schema.import_type("Service")
    schema.import_type("ServiceAccount")
    schema.import_type("io.k8s.api.networking.v1.Ingress")
    schema.import_type("io.k8s.api.networking.v1.IngressClass")

    schema.print_api(args.output)


def import_crd_file(path: str, annotations: str, output: str):
    with open(path, "rb") as f:
        crd = yaml.load(f, CSafeLoader)

    spec = crd["spec"]
    kind = spec["names"]["kind"]
    group = spec["group"]
    # default to using the storage version, ignoring other versions
    vers = {}
    if "versions" in spec:
        vers = next(vers for vers in spec["versions"] if vers["storage"])
        version = vers["name"]
    else:
        version = spec["version"]

    if "schema" in vers:
        openapi = vers["schema"]["openAPIV3Schema"]
    else:
        openapi = spec["validation"]["openAPIV3Schema"]

    if "x-kubernetes-group-version-kind" not in openapi:
        openapi["x-kubernetes-group-version-kind"] = [
            {"group": group, "kind": kind, "version": version}
        ]
    openapi["x-scoped"] = spec.get("scope") == "Namespaced"
    schema = {
        "openapi": "3.0.2",
        "components": {"schemas": {f"{group}.{version}.{kind}": openapi}},
    }

    with open(annotations, "rb") as f:
        annotations = yaml.load(f, CSafeLoader).get(crd["metadata"]["name"])

    importer = CRDImporter(schema, annotations)
    importer.import_crd()

    importer.print_api(output, crd=True)


def import_crd(schema_dir: str, crd: str, annotations: str, output: str):
    filename, ext = os.path.splitext(crd)
    if ext.lower() in (".yml", ".yaml", ".json"):
        return import_crd_file(crd, annotations, output)

    cached = os.path.join(schema_dir, crd + ".json")
    if os.path.exists(cached):
        return import_crd_file(cached, annotations, output)

    content = subprocess.run(
        ["kubectl", "get", f"crds/{crd}", "-o", "json"], check=True, capture_output=True
    ).stdout
    schema = yaml.load(content, CSafeLoader)
    schema.pop("status", None)
    schema["metadata"].pop("annotations", None)
    schema["metadata"].pop("managedFields", None)

    with open(cached, "w") as f:
        json.dump(schema, f, indent="  ")

    return import_crd_file(cached, annotations, output)


def main():
    parser = argparse.ArgumentParser(
        "pykapi", description="Generate python API for Kubernetes Objects"
    )
    parser.add_argument("-o", "--output", type=str, default="-")
    parser.add_argument("-s", "--schemas", type=str, default=SCHEMA_DIR)
    parser.add_argument("crd", nargs="?", type=str)

    args = parser.parse_args()

    if args.crd:
        import_crd(
            args.schemas,
            args.crd,
            os.path.join(args.schemas, "annotations.yaml"),
            args.output,
        )
    else:
        import_k8s_api(args, os.path.join(args.schemas, "annotations.yaml"))


if __name__ == "__main__":
    main()
