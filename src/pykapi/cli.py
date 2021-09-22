import argparse
import json
import logging
import os
import subprocess
import sys
from typing import List, NamedTuple
from urllib.request import urlretrieve

import yaml
from yaml import CSafeLoader

from .api import import_api_types
from .crd import import_crds
from .k8s import QualifiedName, module_for_group
from .parser import ApiGroup
from .printer import TypePrinter


def import_k8s_api(args):
    # import kubernetes types
    version = args.version
    file = os.path.join(args.schemas, f"{version}.json")
    if not os.path.exists(file):
        tmp, headers = urlretrieve(f"https://github.com/kubernetes/kubernetes/raw/release-{version}/api/openapi-spec/swagger.json")
        with open(tmp, "rb") as f:
            data = json.load(f)
        data.pop("paths", None)
        data.pop("security", None)
        data.pop("securityDefinitions", None)
        with open(file, "w") as f:
            json.dump(data, f, indent="  ", sort_keys=True)

    try:
        with open(args.annotations or os.path.join(args.schemas, "annotations.yaml"), "rb") as f:
            annotations = yaml.load(f, CSafeLoader)
    except FileNotFoundError:
        if args.annotations:
            raise

    groups = import_api_types(
        file,
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
        "ServiceAccount",
        "Ingress",
        "IngressClass",
        "CustomResourceDefinition",
    )

    print_groups(groups, args.output)


def print_groups(groups: List[ApiGroup], output: str, api_module: str = "."):
    printer = TypePrinter(api_module=api_module)
    for group in groups:
        filename = output
        if filename != "-":
            # module = group.name.removesuffix(".k8s.io").replace(".", "_")
            module = module_for_group(group.name)
            filename = os.path.join(filename, f"{module}.py")
        printer.print_group(group, filename)


class CRD(NamedTuple):
    fqn: QualifiedName
    schema: dict


def import_crd_files(paths: List[str], annotations: dict, output: str, api_module):
    crds = []

    for path in paths:
        with open(path, "rb") as f:
            for schema in yaml.load_all(f, CSafeLoader):
                spec = schema["spec"]
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
                    openapi["x-kubernetes-group-version-kind"] = [{"group": group, "kind": kind, "version": version}]
                openapi["x-scoped"] = spec.get("scope") == "Namespaced"

                crds.append(CRD(QualifiedName(kind, group, version), openapi))

    groups = import_crds(annotations, *crds)

    print_groups(groups, output, api_module=api_module)


def import_custom_resources(args, crds: List[str]):
    files = []
    for crd in crds:
        filename, ext = os.path.splitext(crd)
        if ext.lower() in (".yml", ".yaml", ".json"):
            files.append(crd)
            continue

        cached = os.path.join(args.schemas, crd + ".json")
        if os.path.exists(cached):
            files.append(cached)
            continue

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

        with open(cached, "w") as f:
            json.dump(schema, f, indent="  ")

        files.append(cached)

    annotations = {}
    try:
        with open(args.annotations or os.path.join(args.schemas, "annotations.yaml"), "rb") as f:
            annotations = yaml.load(f, CSafeLoader).get("crds")
    except FileNotFoundError:
        if args.annotations:
            raise

    import_crd_files(files, annotations, args.output, args.api_module)


SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "schemas")


def main():
    logging.root.addHandler(logging.StreamHandler(sys.stderr))
    logging.root.setLevel(logging.INFO)

    parser = argparse.ArgumentParser("pykapi", description="Generate python API for Kubernetes Objects")
    parser.add_argument("-o", "--output", type=str, default="-")
    parser.add_argument("-s", "--schemas", type=str, default=SCHEMA_DIR)
    parser.add_argument("--annotations", type=str)
    parser.add_argument("--api_module", type=str, default="kubic")
    parser.add_argument("--version", type=str, default="1.22")
    parser.add_argument("crds", nargs="*", type=str)

    args = parser.parse_args()

    if args.crds:
        import_custom_resources(
            args,
            args.crds)
    else:
        import_k8s_api(args)
