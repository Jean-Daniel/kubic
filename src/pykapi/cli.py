import argparse
import logging
import os
import pathlib
import subprocess
import sys
import tempfile
import typing as t
from importlib import resources
from os import fdopen
from tempfile import mktemp
from urllib.request import urlretrieve

import yaml
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
            annotations,
            "Namespace",
            "Role",
            "RoleBinding",
            "ClusterRole",
            "ClusterRoleBinding",
            "ConfigMap",
            "Secret",
            "Deployment",
            "StatefulSet",
            "DaemonSet",
            "Job",
            "CronJob",
            "StorageClass",
            "VolumeAttachment",
            "NetworkPolicy",
            "ResourceQuota",
            "PersistentVolume",
            "PodSecurityPolicy",
            "PodDisruptionBudget",
            "PriorityClass",
            "HorizontalPodAutoscaler",
            "CrossVersionObjectReference",
            "MutatingWebhookConfiguration",
            "ValidatingWebhookConfiguration",
            "Service",
            "Endpoints",
            "EndpointSlice",
            "ServiceAccount",
            "Ingress",
            "IngressClass",
            "CustomResourceDefinition",
        )

        print_groups(groups, args.output)
    finally:
        if tmp:
            os.remove(tmp)


def print_groups(groups: t.List[ApiGroup], output: str, api_module: str = "."):
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
    spec = schema["spec"]
    kind = spec["names"]["kind"]
    group = spec["group"]
    # default to using the storage version, ignoring other versions
    vers: t.Dict[str, t.Any] = {}
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


def read_crds(paths: t.List[pathlib.Path], crds: list):
    for path in paths:
        if path.is_dir():
            for entry in path.iterdir():
                if entry.name.startswith("."):
                    continue

                with entry.open("rb") as f:
                    for schema in yaml.load_all(f, yaml.CSafeLoader):
                        crds.append(create_crd(schema))
        else:
            with path.open("rb") as f:
                for schema in yaml.load_all(f, yaml.CSafeLoader):
                    crds.append(create_crd(schema))


class AnnotationFactory:

    def __init__(self, dir_path: pathlib.Path):
        self.dir = dir_path
        self.cached = {}
        self.builtin = resources.files("pykapi").joinpath("annotations")

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
            builtin = self.builtin.joinpath(filename)
            if builtin.is_file():
                with builtin.open() as f:
                    annotations = yaml.load(f, yaml.CSafeLoader)

        if annotations is None:
            annotations = {}

        self.cached[group] = annotations
        return annotations


def import_custom_resources(args):
    files = []
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

        content = subprocess.run(
            ["kubectl", "get", f"crds/{crd}", "-o", "json"],
            check=True,
            capture_output=True,
        ).stdout
        schema = yaml.load(content, CSafeLoader)
        # remove noise from live schema
        schema.pop("status", None)
        schema["metadata"].pop("annotations", None)
        schema["metadata"].pop("managedFields", None)

        with cached.open("w") as f:
            yaml.dump(schema, f, yaml.CSafeDumper, indent=2)

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
    schema.add_argument("--version", type=str, default="1.23")
    schema.add_argument("-o", "--output", type=argparse.FileType('w', encoding='UTF-8'), default="-")

    args = parser.parse_args()
    if args.action == "api":
        import_k8s_api(args)
    elif args.action == "schema":
        download_schema(args.version, args.output)
    else:
        import_custom_resources(args)
