import argparse
import logging
import os
import pathlib
import sys
import tempfile
import typing as t
from os import fdopen
from tempfile import mktemp
from urllib.request import urlretrieve

import yaml
from kubernetes import config, client
from yaml import CSafeLoader

from .api import import_api_types
from .crd import import_crds
from .k8s import QualifiedName, module_for_group
from .parser import ApiGroup
from .printer import TypePrinter

logger = logging.getLogger("cli")


def download_schema(version: str, output: t.TextIO):
    tmp, headers = urlretrieve(f"https://github.com/kubernetes/kubernetes/raw/release-{version}/api/openapi-spec/swagger.json")
    with open(tmp, "rb") as f:
        data = yaml.load(f, yaml.CSafeLoader)
    data.pop("paths", None)
    data.pop("security", None)
    data.pop("securityDefinitions", None)
    yaml.dump(data, output, yaml.CSafeDumper, indent=2)
    output.flush()


def import_k8s_api(args):
    # import kubernetes types
    tmp = None
    schema = args.schema
    try:
        if not schema:
            fd, tmp = tempfile.mkstemp(text=True)
            with fdopen(fd, "w") as f:
                download_schema(args.version, f)
            schema = tmp

        annotations = None
        if args.annotations:
            with args.annotations.open("rb") as f:
                annotations = yaml.load(f, CSafeLoader)

        groups = import_api_types(
            schema,
            annotations
        )

        print_groups(groups, args.output)
    finally:
        if tmp:
            os.remove(tmp)


def print_groups(groups: list[ApiGroup], output: str, api_module: str = "."):
    printer = TypePrinter(api_module=api_module)
    for group in groups:
        filename = output
        if filename != "-":
            module = module_for_group(group.name)
            filename = os.path.join(filename, f"{module}.py")
        printer.print_group(group, filename)


class CRD(t.NamedTuple):
    fqn: QualifiedName
    schema: dict


def create_crd(schema: dict) -> CRD:
    if schema.get("kind") != "CustomResourceDefinition":
        raise ValueError("Not a CustomResourceDefinition")

    spec = schema["spec"]
    kind = spec["names"]["kind"]
    group = spec["group"]
    # default to using the storage version, ignoring other versions
    vers: dict[str, t.Any] = {}
    if "versions" in spec:
        # find best version
        storage = None
        version = None
        for v in spec["versions"]:
            if v["storage"]:
                storage = v["name"]
            if not version or version < v["name"]:
                version = v["name"]
                vers = v
        if storage and storage != version:
            logger.warning(f"[{group}.{kind}] latest version ({version}) is not defined as the storage version ({storage}).")
    else:
        version = spec["version"]

    if "schema" in vers:
        openapi = vers["schema"]["openAPIV3Schema"]
    else:
        openapi = spec["validation"]["openAPIV3Schema"]

    if "x-kubernetes-group-version-kind" not in openapi:
        openapi["x-kubernetes-group-version-kind"] = [{"group": group, "kind": kind, "version": version}]
    openapi["x-scoped"] = spec.get("scope") == "Namespaced"

    return CRD(QualifiedName(kind, group, version), openapi)


def read_crds(paths: list[pathlib.Path], crds: list):
    for path in paths:
        if path.is_dir():
            for entry in path.iterdir():
                if entry.name.startswith("."):
                    continue

                with entry.open("rb") as f:
                    for schema in yaml.load_all(f, yaml.CSafeLoader):
                        try:
                            crds.append(create_crd(schema))
                        except ValueError:
                            logger.warning("skipping non CRD file: %s", entry.name)
        else:
            with path.open("rb") as f:
                for schema in yaml.load_all(f, yaml.CSafeLoader):
                    try:
                        crds.append(create_crd(schema))
                    except ValueError:
                        logger.warning("skipping non CRD file: %s", path)


class AnnotationFactory:

    def __init__(self, dir_path: pathlib.Path):
        self.dir = dir_path
        self.cached = {}

    def __call__(self, group: str) -> dict:
        if group in self.cached:
            return self.cached[group]

        filename = group + ".yaml"

        # lookup in annotations dirs first
        annotations = None
        if self.dir:
            try:
                with self.dir.joinpath(filename).open("rb") as f:
                    annotations = yaml.load(f, yaml.CSafeLoader)
            except FileNotFoundError:
                pass

        if annotations is None:
            annotations = {}

        self.cached[group] = annotations
        return annotations


def _sanitize_crd(crd: dict) -> dict:
    crd.pop("status", None)
    crd["metadata"].pop("annotations", None)
    crd["metadata"].pop("managedFields", None)
    crd["metadata"].pop("ownerReference", None)
    return crd


def import_custom_resources(args):
    files = []
    v1: client.ApiextensionsV1Api | None = None
    api_groups: dict[str, list[str]] = {}
    for crd in args.crds:
        filename, ext = os.path.splitext(crd)
        if ext.lower() in (".yml", ".yaml", ".json") or os.path.isdir(crd):
            files.append(pathlib.Path(crd))
            continue

        if args.cache_dir:
            cached: pathlib.Path = args.cache_dir.joinpath(crd + ".yaml")
            if cached.exists():
                files.append(cached)
                continue
        else:
            cached: pathlib.Path = pathlib.Path(mktemp(f"-{crd}.yaml"))

        if v1 is None:
            config.load_kube_config()
            v1 = client.ApiextensionsV1Api()

        # Try to interpret it as a CRD first
        try:
            response = v1.read_custom_resource_definition(crd)
            schemas = [_sanitize_crd(v1.api_client.sanitize_for_serialization(response))]
        except client.exceptions.ApiException as e:
            if e.status != 404:
                raise e

            if not api_groups:
                for api in client.ApisApi().get_api_versions().groups:
                    group, _, _ = api.preferred_version.group_version.rpartition('/')
                    api_groups[group] = sorted(version.version for version in api.versions)
            v = api_groups.get(crd)
            if not v:
                raise ValueError(f"'{crd}' is neither a CRD nor an API Group.")

            # Iterate over all version, as a group can have resources in multiple versions
            schemas = []
            fetched = set()
            for version in v:
                response = client.CustomObjectsApi().get_api_resources(group=crd, version=version)
                for rsrc in response.resources:
                    # Skip already fetched (in case a CRD is declared in more than one version)
                    if '/' in rsrc.name or rsrc.name in fetched:
                        continue
                    fetched.add(rsrc.name)
                    crd_schema = v1.read_custom_resource_definition(f"{rsrc.name}.{crd}")
                    schemas.append(_sanitize_crd(v1.api_client.sanitize_for_serialization(crd_schema)))

        with cached.open("w") as f:
            yaml.dump_all(schemas, f, yaml.CSafeDumper, indent=2)

        files.append(cached)

    crds = []
    read_crds(files, crds)
    annotations = AnnotationFactory(args.annotations)
    groups = import_crds(crds, annotations)

    print_groups(groups, args.output, api_module=args.api_module)


def main():
    logging.root.addHandler(logging.StreamHandler(sys.stderr))
    logging.root.setLevel(logging.INFO)

    parser = argparse.ArgumentParser("pykapi", description="Generate python API for Kubernetes Objects")

    subparsers = parser.add_subparsers(title="mode", required=True, dest="action")

    # API Command
    api = subparsers.add_parser("api")
    group = api.add_mutually_exclusive_group(required=True)
    group.add_argument("--version", type=str, help="Kubernetes release version (like 1.23)")
    group.add_argument("-s", "--schema", type=pathlib.Path)
    api.add_argument("--annotations", type=str)
    api.add_argument("-o", "--output", type=str, default="-")

    crd = subparsers.add_parser("crd")
    crd.add_argument("--api_module", type=str, required=True)
    crd.add_argument("--annotations", type=pathlib.Path, help="annotations directory")
    crd.add_argument("--cache_dir", type=pathlib.Path)
    crd.add_argument("crds", nargs="*", type=str)
    crd.add_argument("-o", "--output", type=str, default="-")

    schema = subparsers.add_parser("schema")
    schema.add_argument("--version", type=str, required=True)
    schema.add_argument("-o", "--output", type=argparse.FileType('w', encoding='UTF-8'), default="-")

    args = parser.parse_args()
    if args.action == "api":
        import_k8s_api(args)
    elif args.action == "schema":
        download_schema(args.version, args.output)
    else:
        import_custom_resources(args)
