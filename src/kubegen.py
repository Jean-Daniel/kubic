import argparse
import json
import os
import subprocess
from urllib.request import urlretrieve

import yaml
from yaml import CSafeLoader

import pykapi.crd
from pykapi.api import import_api_types
from pykapi.crd import CRDPrinter
from pykapi.k8s import camel_to_snake, QualifiedName
from pykapi.printer import TypePrinter


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

    groups = import_api_types(
        file,
        annotations,
        "Namespace",
        "io.k8s.api.rbac.v1.Role",
        "io.k8s.api.rbac.v1.RoleBinding",
        "io.k8s.api.rbac.v1.ClusterRole",
        "io.k8s.api.rbac.v1.ClusterRoleBinding",
        "ConfigMap",
        "Secret",
        "Deployment",
        "StatefulSet",
        "DaemonSet",
        "Job",
        "io.k8s.api.batch.v1beta1.CronJob",
        "io.k8s.api.storage.v1.StorageClass",
        "NetworkPolicy",
        "ResourceQuota",
        "PersistentVolume",
        "PodSecurityPolicy",
        "PodDisruptionBudget",
        "io.k8s.api.autoscaling.v1.HorizontalPodAutoscaler",
        "io.k8s.api.autoscaling.v1.CrossVersionObjectReference",
        "io.k8s.api.admissionregistration.v1.MutatingWebhookConfiguration",
        "Service",
        "ServiceAccount",
        "io.k8s.api.networking.v1.Ingress",
        "io.k8s.api.networking.v1.IngressClass",
    )

    printer = TypePrinter()
    for group in groups:
        output = args.output
        if output != "-":
            module = group.name.removesuffix(".k8s.io").replace(".", "_")
            output = os.path.join(args.output, f"{module}.py")
        printer.print_group(group, output)


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

    with open(annotations, "rb") as f:
        annotations = yaml.load(f, CSafeLoader).get(crd["metadata"]["name"])

    crd = pykapi.crd.import_crd(
        QualifiedName(kind, group, version), openapi, annotations
    )

    # automatically generate filename if output is a dir
    if output != "-" and os.path.isdir(output):
        output = os.path.join(output, f"{camel_to_snake(crd.type.name)}.py")

    CRDPrinter(crd).print(output)


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


SCHEMA_DIR = os.path.join(os.path.dirname(__file__), "schemas")


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
