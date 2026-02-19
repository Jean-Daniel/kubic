import typing as t
from collections import defaultdict
from collections.abc import Callable

from pykapi.k8s import module_for_group

from .annotations import AnnotationProvider
from .k8s import QualifiedName
from .parser import ApiGroup, Parser
from .types import AnonymousType, ApiResourceType, ApiType, ApiTypeRef, ObjectType, Type


class CRDGroup(ApiGroup):
    def __init__(self, name: str, version: str, module: str):
        super().__init__(name, version, module)
        self.aliases = set()

    def __contains__(self, item):
        if item.group in self.aliases:
            return True
        return super().__contains__(item)

    def add(self, api_type: ApiType):
        super().add(api_type)
        self.aliases.add(api_type.group)


class CRDParser(Parser):
    def __init__(self, group: str, version: str, module: str, annotations: dict):
        super().__init__()
        self.group = CRDGroup(group, version, module)
        # patching root schema
        self.annotations = annotations

    def group_for_type(self, fqn: QualifiedName) -> ApiGroup:
        return self.group

    def annotations_for_type(self, obj_type: ObjectType) -> dict | None:
        if not self.annotations:
            return None

        # Look up by fullname first
        if isinstance(obj_type, AnonymousType):
            # TODO: refactor to use a tree for annotations and fetch by type full path instead
            # FIXME: should use qualified name instead (root.property.property…)
            annotations = self.annotations.get(obj_type.fullname)
            if annotations:
                return annotations
        # obj_type is the root type -> lookup annotation for that type
        return self.annotations.get(obj_type.name)

    def process(self, *resources: tuple[QualifiedName, dict]) -> ApiGroup:
        for fqn, schema in resources:
            schema["properties"]["metadata"] = {"$ref": "io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta"}
            # may contains items from remapped groups
            self._register_type(
                ApiResourceType(fqn, schema.get("description"), schema.get("x-scoped", True)),
                schema,
            )

        for obj_type, schema in self.pendings:
            self.import_resource(obj_type, schema)
        self.group.finalize()
        return self.group

    def import_resource(self, obj_type: ObjectType, schema: dict):
        # on CRD, remove status only if defined as a generic object
        if isinstance(obj_type, ApiResourceType):
            schema["properties"].pop("status", None)
            # status = schema["properties"].get("status")
            # if status and "properties" not in status:
            #     schema["properties"].pop("status", None)

        super().import_resource(obj_type, schema)

    def import_property(self, obj_type: ObjectType, prop_name: str, schema: dict, is_plural: bool) -> Type:
        ref = schema.get("$ref")
        if ref:
            # ref to existing type
            fqn = QualifiedName.parse(ref)
            return ApiTypeRef(fqn)

        return super().import_property(obj_type, prop_name, schema, is_plural)

    def import_base_property(self, obj_type: ApiType, prop_name: str, schema: dict, prop_type: str, is_plural: bool) -> Type:
        # common pattern matching
        if schema.get("type") == "object":
            if k8s_type := infer_k8s_type(prop_name, schema):
                return k8s_type
        return super().import_base_property(obj_type, prop_name, schema, prop_type, is_plural)


def is_label_selector(properties: dict) -> bool:
    if len(properties) != 2:
        return False

    if "matchExpressions" not in properties or "matchLabels" not in properties:
        return False

    return properties["matchExpressions"].get("type") == "array" and "additionalProperties" in properties["matchLabels"]


def is_key_selector(properties: dict) -> bool:
    if len(properties) != 3:
        return False

    if "key" not in properties or "name" not in properties or "optional" not in properties:
        return False

    return (
            properties["key"].get("type") == "string"
            and properties["name"].get("type") == "string"
            and properties["optional"].get("type") == "boolean"
    )


def is_local_object_reference(properties: dict) -> bool:
    if len(properties) != 1:
        return False

    return "name" in properties


def is_typed_object_reference(properties: dict) -> bool:
    if len(properties) != 4:
        return False

    return "namespace" in properties and "api_group" in properties and "kind" in properties and "name" in properties


def is_typed_local_object_reference(properties: dict) -> bool:
    if len(properties) != 3:
        return False

    return "api_group" in properties and "kind" in properties and "name" in properties


def is_secret_ref(properties: dict) -> bool:
    if len(properties) != 2:
        return False

    if "name" not in properties or "namespace" not in properties:
        return False

    return properties["name"].get("type") == "string" and properties["namespace"].get("type") == "string"


# loosy matching of common types based on field names only.
BUILTIN_TYPE_MAPPING: dict[str, tuple[str, set[str]]] = {
    "affinity": ("io.k8s.api.core.v1.Affinity", {"nodeAffinity", "podAffinity", "podAntiAffinity"}),
    # containers: "resizePolicy",
    "containers": (
        "io.k8s.api.core.v1.Container",
        {
            "args",
            "command",
            "env",
            "envFrom",
            "image",
            "imagePullPolicy",
            "lifecycle",
            "livenessProbe",
            "name",
            "ports",
            "readinessProbe",
            "resources",
            "securityContext",
            "startupProbe",
            "stdin",
            "stdinOnce",
            "terminationMessagePath",
            "terminationMessagePolicy",
            "tty",
            "volumeDevices",
            "volumeMounts",
            "workingDir",
        },
    ),
    "env": ("io.k8s.api.core.v1.EnvVar", {"name", "value", "valueFrom"}),
    "imagePullSecrets": ("io.k8s.api.core.v1.LocalObjectReference", {"name"}),
    "matchExpressions": ("io.k8s.api.core.v1.NodeSelectorRequirement", {"key", "operator", "values"}),
    # resources: "claims"
    "resources": ("io.k8s.api.core.v1.ResourceRequirements", {"limits", "requests"}),
    "securityContext": (
        "io.k8s.api.core.v1.PodSecurityContext",
        {
            "fsGroup",
            "fsGroupChangePolicy",
            "runAsGroup",
            "runAsNonRoot",
            "runAsUser",
            "seLinuxOptions",
            "seccompProfile",
            "supplementalGroups",
            "sysctls",
            "windowsOptions",
        },
    ),
    "tolerations": ("io.k8s.api.core.v1.Toleration", {"effect", "key", "operator", "tolerationSeconds", "value"}),
    # topologySpreadConstraints: "matchLabelKeys", "nodeAffinityPolicy", "nodeTaintsPolicy"
    "topologySpreadConstraints": (
        "io.k8s.api.core.v1.TopologySpreadConstraint",
        {"labelSelector", "maxSkew", "minDomains", "topologyKey", "whenUnsatisfiable"},
    ),
    "volumeMounts": ("io.k8s.api.core.v1.VolumeMount", {"mountPath", "mountPropagation", "name", "readOnly", "subPath", "subPathExpr"}),
    "volumes": (
        "io.k8s.api.core.v1.Volume",
        {
            "awsElasticBlockStore",
            "azureDisk",
            "azureFile",
            "cephfs",
            "cinder",
            "configMap",
            "csi",
            "downwardAPI",
            "emptyDir",
            "ephemeral",
            "fc",
            "flexVolume",
            "flocker",
            "gcePersistentDisk",
            "gitRepo",
            "glusterfs",
            "hostPath",
            "iscsi",
            "name",
            "nfs",
            "persistentVolumeClaim",
            "photonPersistentDisk",
            "portworxVolume",
            "projected",
            "quobyte",
            "rbd",
            "scaleIO",
            "secret",
            "storageos",
            "vsphereVolume",
        },
    ),
}
BUILTIN_TYPE_MAPPING["initContainers"] = BUILTIN_TYPE_MAPPING["containers"]


def is_volume_claim_spec(properties: dict):
    return all(
        ty in properties
        for ty in {"accessModes", "dataSource", "dataSourceRef", "resources", "selector", "storageClassName", "volumeMode", "volumeName"}
    )


def is_volume_claim_template(properties: dict):
    # PersistentVolumeClaim
    # PersistentVolumeClaimTemplate
    spec = properties.get("spec")
    if not spec or not spec.get("type") == "object":
        return False

    spec_properties = spec.get("properties")
    return spec_properties and is_volume_claim_spec(spec_properties)


def is_probe(properties: dict):
    return all(
        ty in properties
        for ty in {
            "exec",
            "failureThreshold",
            "grpc",
            "httpGet",
            "initialDelaySeconds",
            "periodSeconds",
            "successThreshold",
            "tcpSocket",
            "terminationGracePeriodSeconds",
            "timeoutSeconds",
        }
    )


# Trying to infer custom type
def infer_k8s_type(prop_name: str, schema: dict) -> ApiTypeRef | None:
    properties = schema.get("properties")
    if not properties:
        return None

    # Simple type inferrence based only on prop_name and first level field names.
    builtin_type = BUILTIN_TYPE_MAPPING.get(prop_name)
    if builtin_type and all(ty in properties for ty in builtin_type[1]):
        fqn = QualifiedName.parse(builtin_type[0])
        return ApiTypeRef(fqn)

    if is_label_selector(properties):
        return ApiTypeRef(QualifiedName("LabelSelector", "meta", "v1"))

    low_name = prop_name.lower()
    if is_key_selector(properties):
        if any(kw in low_name for kw in ["secret", "username", "password", "key", "credentials"]):
            return ApiTypeRef(QualifiedName("SecretKeySelector", "core", "v1"))
        return ApiTypeRef(QualifiedName("ConfigMapKeySelector", "core", "v1"))

    if is_local_object_reference(properties):
        if any(kw in low_name for kw in ["secret", "reference"]):
            return ApiTypeRef(QualifiedName("LocalObjectReference", "core", "v1"))

    if is_typed_object_reference(properties):
        return ApiTypeRef(QualifiedName("TypedObjectReference", "core", "v1"))

    if is_typed_local_object_reference(properties):
        return ApiTypeRef(QualifiedName("TypedLocalObjectReference", "core", "v1"))

    if low_name.endswith("probe") and is_probe(properties):
        return ApiTypeRef(QualifiedName("Probe", "core", "v1"))

    if "secret" in low_name and is_secret_ref(properties):
        return ApiTypeRef(QualifiedName("SecretReference", "core", "v1"))

    if "volumeclaimspec" in low_name and is_volume_claim_spec(properties):
        return ApiTypeRef(QualifiedName("PersistentVolumeClaimSpec", "core", "v1"))

    if "volumeclaimtemplate" in low_name and is_volume_claim_template(properties):
        ty = "PersistentVolumeClaim" if "kind" in properties else "PersistentVolumeClaimTemplate"
        return ApiTypeRef(QualifiedName(ty, "core", "v1"))

    #     nodeAffinity: "io.k8s.api.core.v1.NodeAffinity"
    #     podAffinity: "io.k8s.api.core.v1.PodAffinity"
    #     podAntiAffinity: "io.k8s.api.core.v1.PodAntiAffinity"
    return None


def import_crds(crds: list[tuple[QualifiedName, dict]], annotations: AnnotationProvider) -> list[ApiGroup]:
    # in case there is CRDs from many groups/versions.
    # FIXME: disable group by version as some CRDs have etherogenous version (cilium)
    modules = {}
    crds_by_groups = defaultdict(list)
    patches_by_group = defaultdict(dict)
    for fqn, schema in crds:
        a = annotations(fqn.group)
        group = a.get("group", fqn.group)
        module = a.get("module")
        if module or (group not in modules):
            modules[group] = module or module_for_group(group)

        crds_by_groups[group].append((fqn, schema))
        # merge all patches into a single map
        patches = a.get("patches")
        if patches:
            patches_by_group[group].update(patches)
        # crds_by_groups[(group, fqn.version)].append((fqn, schema))

    groups = []
    for group, crds in crds_by_groups.items():
        parser = CRDParser(group, version="", module=modules[group], annotations=patches_by_group[group])
        groups.append(parser.process(*crds))

    return groups
