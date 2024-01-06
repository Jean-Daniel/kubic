import re
import typing as t
from functools import cache

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
    "io.k8s.api.node": "node.k8s.io",
    "io.k8s.api.apps": "apps",
    "io.k8s.api.meta": "meta",
    "io.k8s.api.batch": "batch",
    "io.k8s.api.policy": "policy",
    "io.k8s.api.extensions": "extensions",
    "io.k8s.api.events": "events.k8s.io",
    "io.k8s.api.autoscaling": "autoscaling",
    "io.k8s.api.storage": "storage.k8s.io",
    "io.k8s.api.resource": "resource.k8s.io",
    "io.k8s.api.discovery": "discovery.k8s.io",
    "io.k8s.apimachinery.pkg.apis.meta": "meta",
    "io.k8s.api.networking": "networking.k8s.io",
    "io.k8s.api.scheduling": "scheduling.k8s.io",
    "io.k8s.api.rbac": "rbac.authorization.k8s.io",
    "io.k8s.api.certificates": "certificates.k8s.io",
    "io.k8s.api.coordination": "coordination.k8s.io",
    "io.k8s.api.authorization": "authorization.k8s.io",
    "io.k8s.api.authentication": "authentication.k8s.io",
    "io.k8s.api.flowcontrol": "flowcontrol.apiserver.k8s.io",
    "io.k8s.api.apiserverinternal": "internal.apiserver.k8s.io",
    "io.k8s.api.admissionregistration": "admissionregistration.k8s.io",
    "io.k8s.kube-aggregator.pkg.apis.apiregistration": "apiregistration.k8s.io",
    "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions": "apiextensions.k8s.io",
}


class QualifiedName(t.NamedTuple):
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
            if group is None:
                if name == "io.k8s.apimachinery.pkg.api.resource.Quantity":
                    return QualifiedName("Quantity", "core", "v1")
                elif name == "io.k8s.apimachinery.pkg.runtime.RawExtension":
                    return QualifiedName("RawExtension", "core", "v1")
                elif name == "io.k8s.apimachinery.pkg.util.intstr.IntOrString":
                    return QualifiedName("IntOrString", "core", "v1")
                elif name == "io.k8s.apimachinery.pkg.version.Info":
                    return QualifiedName("Info", "core", "v1")

            assert group is not None, f"unknown group {parts[0]} / {parts[2]}: {name}"
            return QualifiedName(parts[2], group, parts[1])

        return QualifiedName(name, "", "")


# FIXME: should find a way to inject annotations
MODULE_NAMES = {"operator.victoriametrics.com": "victoriametrics"}


def module_for_group(group) -> str:
    return MODULE_NAMES.get(group) or group.split(".", maxsplit=1)[0].replace("-", "_")


KEYWORDS = {
    "if",
    "not",
    "for",
    "def",
    "class",
    "from",
    "import",
    "except",
    "break",
    "global",
    "continue",
}

# used to fix camel_to_snake edge cases (URLs -> _url_s for instance)
PLURALS = re.compile("(.*?)([A-Z]+s)")


@cache
def camel_to_snake(name: str):
    # cilium node for instance uses '-' in vars
    snake = name.replace("-", "_")
    # edge cases
    if name[-1] == "s" and name[-2].isupper():
        prefix, suffix = PLURALS.match(snake).groups()
        snake = prefix + "_" + suffix.lower()

    snake = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", snake)
    snake = re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake).lower()
    # avoid conflict with keywords
    if snake in KEYWORDS:
        snake += "_"
    if snake.startswith("$"):
        snake = snake[1:] + "_"
    return snake


ACRONYMES = {"tls", "ipam", "api"}
PLURALS_EXCEPTION = {"kerberos", "status", "tls"}


def type_name_from_property_name(name: str):
    # true when type_name is specified in annotation
    if name[0].isupper():
        return name

    # assuming 2 and 3 letters words are acronyms (do it before remote trailing S)
    if len(name) <= 3:
        return name.upper()

    # egress for instance
    low_name = name.lower()
    if name.endswith("s") and not name.endswith("ss") and not any(low_name.endswith(excluded) for excluded in PLURALS_EXCEPTION):
        name = name.removesuffix("s")
        # just in case
        if len(name) <= 3:
            return name.upper()
        if name.endswith("ie"):  # policies, entries, …
            name = name[:-2] + "y"

    if "-" in name:
        parts = name.split("-")
        name = "".join(type_name_from_property_name(p) for p in parts)

    for ac in ACRONYMES:
        if name.startswith(ac):
            return ac.upper() + name[len(ac):]
    return name[0].upper() + name[1:]
