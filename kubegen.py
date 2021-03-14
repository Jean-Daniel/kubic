import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from functools import cache
from typing import NamedTuple, List, TextIO

import yaml
from yaml import CSafeDumper, CSafeLoader

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "schemas")


def shortkey(key: str):
    return key.rsplit(".", maxsplit=1)[1].lower()


def snake_to_camel(name: str) -> str:
    components = name.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


# used to fix camel_to_snake edge cases (URLs -> _url_s for instance)
ACRONYMES = {"URLs": "_urls", "WWNs": "_wwns"}


@cache
def camel_to_snake(name: str):
    snake = name
    # edge cases
    for orig, replace in ACRONYMES.items():
        snake = snake.replace(orig, replace)

    snake = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", snake)
    snake = re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake).lower()
    return snake


def type_name(name: str):
    if name.endswith("s"):
        name = name.removesuffix("s")
    if name.startswith("tls"):
        return "TLS" + name[3:]
    return name[0].upper() + name[1:]


class Property(NamedTuple):
    name: str
    type: str
    required: bool

    @property
    def snake_name(self):
        return camel_to_snake(self.name)


class Object:
    def __init__(self, name: str):
        self.name = name
        self.properties: List[Property] = []

    def __eq__(self, other):
        return self.name == other.name and self.properties == other.properties

    def __repr__(self):
        return f"{self.name}: {self.properties}"

    @property
    def required_properties(self):
        return (prop for prop in self.properties if prop.required)

    @property
    def optional_properties(self):
        return (prop for prop in self.properties if not prop.required)


class ApiResource(Object):
    def __init__(self, name: str, version: str, kind: str, scoped: bool = True):
        super().__init__(name)
        self.version = version
        self.kind = kind
        self.scoped = scoped


class Schema:
    def __init__(self, path: str):
        if path:
            with open(path) as f:
                self.schema = json.load(f)["definitions"]
        else:
            self.schema = {}

        self.index = {}
        self.ambiguous = defaultdict(list)
        for key in self.schema.keys():
            short = shortkey(key)
            if short in self.index:
                self.ambiguous[short].append(key)
            else:
                self.index[short] = key

        self.prefix = ""
        self.stack = set()
        self.requested = {}

    def request_type(self, ty: str, schema: dict = None) -> Object:
        key = self.index.get(ty.lower(), ty)
        if key == ty and not schema and key not in self.schema:
            raise ValueError(f"unknown type {key} requested")

        if ty.lower() in self.ambiguous:
            print(
                f"ambiguous short key {ty}: using {key} (other: {', '.join(self.ambiguous[ty.lower()])})"
            )

        if key in self.requested:
            assert key not in self.stack, "circular dependency -> need forward declaration"
            return self.requested[key]

        if not schema:
            schema = self.schema[key]

        self.stack.add(key)
        name = key.rsplit(".", 1)[1] if "." in key else key
        self.requested[key] = ty = self.parse(name, schema)
        self.stack.remove(key)
        return ty

    def parse(self, name, schema) -> Object:
        gvk = schema.get("x-kubernetes-group-version-kind")
        if gvk:
            obj = ApiResource(name, gvk[0]["version"], gvk[0]["kind"], schema.get("x-scoped", True))
        else:
            obj = Object(name)

        # parse properties
        required = schema.get("required", [])
        assert "properties" in schema, f"{name} does not have properties"
        for prop, value in schema["properties"].items():
            # for REST API only
            if prop == "status":
                continue

            # skip prepopulated values
            if prop == "apiVersion" or prop == "kind" and gvk is not None:
                continue

            obj.properties.append(
                Property(prop, self.get_type(value, name, prop), prop in required)
            )

        return obj

    def get_type(self, schema: dict, class_name: str, prop_name: str, ref_name: str = None):
        ref = schema.get("$ref")
        if ref:
            ref = ref.removeprefix("#/definitions/")
            return self.get_type(self.schema[ref], class_name, prop_name, ref)

        ty = schema.get("type")
        if isinstance(ty, list):
            assert ty[1] == 'null'
            ty = ty[0]

        if ty == "object":
            # if no propoerties, this is just an alias for generic object
            if "properties" in schema:
                if ref_name:
                    # parse dependency
                    typename = ref_name.rsplit(".", 1)[1]
                    self.request_type(ref_name)
                else:
                    if not self.prefix:
                        raise ValueError(f"anonymous type for property {prop_name} but no prefix set")
                    typename = self.prefix + type_name(prop_name)
                    if typename in self.requested:
                        typename = class_name + type_name(prop_name)
                    if typename in self.requested:
                        raise ValueError(f"generated name conflict: {typename}")
                    self.request_type(typename, schema)
                return typename
            if "additionalProperties" in schema:
                return f'Dict[str, {self.get_type(schema["additionalProperties"], class_name, prop_name)}]'
            return "object"

        if ty == "integer":
            return "int"

        if ty == "boolean":
            return "bool"

        if ty == "string":
            return "bytes" if schema.get("format") == "bytes" else "str"

        if ty == "number":
            return "float" if schema.get("format") == "double" else "int"

        if ty == "array":
            details = schema.get("items")
            if details:
                return f"List[{self.get_type(details, class_name, prop_name)}]"
            return "list"

        if ty:
            assert isinstance(ty, str), f"unsupported type: {ty}"
            return ty

        union = schema.get("oneOf")
        if not union:
            union = schema.get("anyOf")
        if union:
            types = [self.get_type(item, prop_name) for item in union]
            return f"Union[{', '.join(types)}]"

        if schema.get("x-kubernetes-preserve-unknown-fields", False):
            return "Any"
        assert False, f"type not supported: {schema}"


def print_type(ty: Object, stream: TextIO):
    stream.write("class ")
    stream.write(ty.name)
    if isinstance(ty, ApiResource):
        stream.write("(ApiResource)")
    else:
        stream.write("(Resource)")
    stream.write(":\n")
    stream.write("    __slots__ = ()\n")

    # write fields mapping
    fields = {}
    for prop in ty.properties:
        snake = prop.snake_name
        if prop.name != snake_to_camel(snake):
            fields[snake] = prop.name

    if fields:
        stream.write("    _field_names_ = {\n")
        for snake, camel in fields.items():
            stream.write(f'      "{snake}": "{camel}",\n')
        stream.write("    }\n")

    stream.write("\n")
    for prop in ty.properties:
        stream.write("    ")
        stream.write(prop.snake_name)
        stream.write(": ")
        stream.write(prop.type)
        stream.write("\n")

    required = [prop.snake_name for prop in ty.required_properties]
    if required:
        stream.write('\n    _required_ = ["')
        stream.write('", "'.join(required))
        stream.write('"]\n')

    stream.write("\n    def __init__(self")
    if isinstance(ty, ApiResource):
        stream.write(", name: str")
        if ty.scoped:
            stream.write(", namespace: str = None")
    for prop in ty.properties:
        stream.write(", ")
        stream.write(prop.snake_name)
        stream.write(": ")
        stream.write(prop.type)
        stream.write(" = None")
    stream.write("):\n")
    stream.write("        super().__init__(")
    if isinstance(ty, ApiResource):
        stream.write(f'"{ty.version}"')
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

    stream.write(")\n")

    stream.write("\n\n")


def print_api(types: List, output: str):
    if output == "-":
        stream = sys.stdout
    else:
        stream = open(output, 'w')
    try:
        stream.write("from typing import Any, List, Dict, Union\n\n")
        stream.write("from .base import Resource, ApiResource\n\n\n")

        for ty in types:
            print_type(ty, stream)
    finally:
        if stream is not sys.stdout:
            stream.close()


def import_k8s_api(args):
    # import kubernetes types
    schema = Schema(os.path.join(SCHEMA_DIR, "_definitions.json"))

    schema.request_type("Namespace")
    schema.request_type("io.k8s.api.rbac.v1.Role")
    schema.request_type("io.k8s.api.rbac.v1.RoleBinding")
    schema.request_type("io.k8s.api.rbac.v1.ClusterRoleBinding")

    schema.request_type("ConfigMap")
    schema.request_type("Secret")

    schema.request_type("Deployment")
    schema.request_type("StatefulSet")
    schema.request_type("Job")
    schema.request_type("io.k8s.api.batch.v1beta1.CronJob")
    schema.request_type("PodDisruptionBudget")
    schema.request_type("HorizontalPodAutoscaler")

    schema.request_type("Service")
    schema.request_type("ServiceAccount")
    schema.request_type("io.k8s.api.networking.v1.Ingress")
    schema.request_type("io.k8s.api.networking.v1.IngressClass")

    print_api(schema.types, args.output)


def import_single(path: str, output: str):
    with open(path, "rb") as f:
        spec = yaml.load(f, CSafeLoader)
    schema = Schema("")
    gvk = spec["x-kubernetes-group-version-kind"][0]
    schema.prefix = gvk['kind']
    typename = f"{gvk['group']}.{gvk['kind']}"
    schema.request_type(typename, spec)

    print_api(schema.types, output)


def import_crd_object(crd: dict, output: str):
    spec = crd["spec"]
    kind = spec["names"]["kind"]
    group = spec["group"]
    # default to using the storage version, ignoring other versions
    if "versions" in spec:
        vers = next(vers for vers in spec["versions"] if vers["storage"])
        version_name = vers["name"]
        openapi = vers["schema"]["openAPIV3Schema"]
    else:
        version_name = spec["version"]
        openapi = spec["validation"]["openAPIV3Schema"]

    if "x-kubernetes-group-version-kind" not in openapi:
        openapi["x-kubernetes-group-version-kind"] = [{
            "group": group,
            "kind": kind,
            "version": version_name
        }]
    openapi["x-scoped"] = spec.get("scope") == "Namespaced"
    schema = {
        "openapi": "3.0.2",
        "components": {
            "schemas": {
                f"{group}.{kind}": openapi
            }
        }
    }
    tmpdir = tempfile.mkdtemp()
    try:
        fd, tmp = tempfile.mkstemp("_schema.yml", dir=tmpdir)
        tmpfile = os.path.join(tmpdir, tmp)
        with os.fdopen(fd, "w") as f:
            yaml.dump(schema, f, CSafeDumper)
        subprocess.run(["openapi2jsonschema", "--kubernetes", tmpfile], check=True, cwd=tmpdir)
        json_schema = os.path.join(tmpdir, "schemas", kind.lower() + ".json")
        os.rename(json_schema, output)
    finally:
        shutil.rmtree(tmpdir)


def import_crd(schema_dir: str, crd: str, output: str):
    filename, ext = os.path.splitext(crd)
    if ext.lower() in (".yml", ".yaml", ".json"):
        with open(crd, "rb") as f:
            spec = yaml.load(f, yaml.CSafeLoader)
        cached = os.path.join(schema_dir, filename + ".json")
        import_crd_object(spec, cached)
        return import_single(cached, output)

    cached = os.path.join(schema_dir, crd + ".json")
    if os.path.exists(cached):
        return import_single(cached, output)

    spec = subprocess.run(["kubectl", "get", f"crds/{crd}", "-o", "json"], capture_output=True).stdout
    import_crd_object(yaml.load(spec, yaml.CSafeLoader), cached)
    return import_single(cached, output)


def main():
    parser = argparse.ArgumentParser("pykapi", description="Generate python API for Kubernetes Objects")
    parser.add_argument("-o", "--output", type=str, default='-')
    parser.add_argument("crds", nargs="*", type=str)

    args = parser.parse_args()

    if args.crds:
        for crd in args.crds:
            import_crd(SCHEMA_DIR, crd, args.output)
    else:
        import_k8s_api(args)


if __name__ == "__main__":
    main()
