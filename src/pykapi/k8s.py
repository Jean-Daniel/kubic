import re
from functools import cache
from typing import NamedTuple

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

GROUP_MAPPING = {
    "io.k8s.api.core": "core",
    "io.k8s.apimachinery.pkg.api": "core",  # Quantity
    "io.k8s.apimachinery.pkg.util": "core",  # IntOrString
    "io.k8s.api.apps": "apps",
    "io.k8s.api.batch": "batch",
    "io.k8s.api.policy": "policy",
    "io.k8s.api.autoscaling": "autoscaling",
    "io.k8s.api.storage": "storage.k8s.io",
    "io.k8s.apimachinery.pkg.apis.meta": "meta",
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
    def parse(cls, name):
        parts = name.rsplit(".", maxsplit=2)
        if len(parts) == 3:
            group = GROUP_MAPPING.get(parts[0])
            assert group is not None, f"unknown group {parts[0]} / {parts[2]}"
            return QualifiedName(parts[2], group, parts[1])

        return QualifiedName(name, "", "")


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
            return ac.upper() + name[len(ac):]
    return name[0].upper() + name[1:]