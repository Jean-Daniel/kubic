import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class AWSElasticBlockStoreVolumeSource(KubernetesObject):
    """
    Represents a Persistent Disk resource in AWS.

    An AWS EBS disk must exist before mounting to a container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.
    """

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    """ fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """
    partition: int
    """ partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). """
    read_only: bool
    """ readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """
    volume_id: str
    """ volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """

    def __init__(self, fs_type: str = None, partition: int = None, read_only: bool = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, partition=partition, read_only=read_only, volume_id=volume_id)


class NodeSelectorRequirement(KubernetesObject):
    """A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "operator"]

    key: str
    """ The label key that the selector applies to. """
    operator: str
    """ Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. """
    values: list[str]
    """ An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. """

    def __init__(self, key: str = None, operator: str = None, values: list[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class NodeSelectorTerm(KubernetesObject):
    """A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm."""

    __slots__ = ()

    _api_version_ = "v1"

    match_expressions: list[NodeSelectorRequirement]
    """ A list of node selector requirements by node's labels. """
    match_fields: list[NodeSelectorRequirement]
    """ A list of node selector requirements by node's fields. """

    def __init__(self, match_expressions: list[NodeSelectorRequirement] = None, match_fields: list[NodeSelectorRequirement] = None):
        super().__init__(match_expressions=match_expressions, match_fields=match_fields)


class PreferredSchedulingTerm(KubernetesObject):
    """An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op)."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["preference", "weight"]

    preference: NodeSelectorTerm
    """ A node selector term, associated with the corresponding weight. """
    weight: int
    """ Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. """

    def __init__(self, preference: NodeSelectorTerm = None, weight: int = None):
        super().__init__(preference=preference, weight=weight)


class NodeSelector(KubernetesObject):
    """A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["node_selector_terms"]

    node_selector_terms: list[NodeSelectorTerm]
    """ Required. A list of node selector terms. The terms are ORed. """

    def __init__(self, node_selector_terms: list[NodeSelectorTerm] = None):
        super().__init__(node_selector_terms=node_selector_terms)


class NodeAffinity(KubernetesObject):
    """Node affinity is a group of node affinity scheduling rules."""

    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: list[PreferredSchedulingTerm]
    """ The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. """
    required_during_scheduling_ignored_during_execution: NodeSelector
    """ If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node. """

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: list[PreferredSchedulingTerm] = None,
        required_during_scheduling_ignored_during_execution: NodeSelector = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAffinityTerm(KubernetesObject):
    """Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["topology_key"]

    label_selector: meta.LabelSelector
    """ A label query over a set of resources, in this case pods. If it's null, this PodAffinityTerm matches with no Pods. """
    match_label_keys: list[str]
    """ MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate. """
    mismatch_label_keys: list[str]
    """ MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate. """
    namespace_selector: meta.LabelSelector
    """ A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. """
    namespaces: list[str]
    """ namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace". """
    topology_key: str
    """ This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. """

    def __init__(
        self,
        label_selector: meta.LabelSelector = None,
        match_label_keys: list[str] = None,
        mismatch_label_keys: list[str] = None,
        namespace_selector: meta.LabelSelector = None,
        namespaces: list[str] = None,
        topology_key: str = None,
    ):
        super().__init__(
            label_selector=label_selector,
            match_label_keys=match_label_keys,
            mismatch_label_keys=mismatch_label_keys,
            namespace_selector=namespace_selector,
            namespaces=namespaces,
            topology_key=topology_key,
        )


class WeightedPodAffinityTerm(KubernetesObject):
    """The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["pod_affinity_term", "weight"]

    pod_affinity_term: PodAffinityTerm
    """ Required. A pod affinity term, associated with the corresponding weight. """
    weight: int
    """ weight associated with matching the corresponding podAffinityTerm, in the range 1-100. """

    def __init__(self, pod_affinity_term: PodAffinityTerm = None, weight: int = None):
        super().__init__(pod_affinity_term=pod_affinity_term, weight=weight)


class PodAffinity(KubernetesObject):
    """Pod affinity is a group of inter pod affinity scheduling rules."""

    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm]
    """ The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. """
    required_during_scheduling_ignored_during_execution: list[PodAffinityTerm]
    """ If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. """

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm] = None,
        required_during_scheduling_ignored_during_execution: list[PodAffinityTerm] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAntiAffinity(KubernetesObject):
    """Pod anti affinity is a group of inter pod anti affinity scheduling rules."""

    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm]
    """ The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. """
    required_during_scheduling_ignored_during_execution: list[PodAffinityTerm]
    """ If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. """

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm] = None,
        required_during_scheduling_ignored_during_execution: list[PodAffinityTerm] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class Affinity(KubernetesObject):
    """Affinity is a group of affinity scheduling rules."""

    __slots__ = ()

    _api_version_ = "v1"

    node_affinity: NodeAffinity
    """ Describes node affinity scheduling rules for the pod. """
    pod_affinity: PodAffinity
    """ Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)). """
    pod_anti_affinity: PodAntiAffinity
    """ Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)). """

    def __init__(self, node_affinity: NodeAffinity = None, pod_affinity: PodAffinity = None, pod_anti_affinity: PodAntiAffinity = None):
        super().__init__(node_affinity=node_affinity, pod_affinity=pod_affinity, pod_anti_affinity=pod_anti_affinity)


class AppArmorProfile(KubernetesObject):
    """AppArmorProfile defines a pod or container's AppArmor settings."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["type"]

    localhost_profile: str
    """ localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost". """
    type: str
    """ 
    type indicates which kind of AppArmor profile will be applied. Valid options are:
      Localhost - a profile pre-loaded on the node.
      RuntimeDefault - the container runtime's default profile.
      Unconfined - no AppArmor enforcement.
     """

    def __init__(self, localhost_profile: str = None, type: str = None):
        super().__init__(localhost_profile=localhost_profile, type=type)


class AttachedVolume(KubernetesObject):
    """AttachedVolume describes a volume attached to a node"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["device_path", "name"]

    device_path: str
    """ DevicePath represents the device path where the volume should be available """
    name: str
    """ Name of the attached volume """

    def __init__(self, device_path: str = None, name: str = None):
        super().__init__(device_path=device_path, name=name)


class AzureDiskVolumeSource(KubernetesObject):
    """AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["disk_name", "disk_uri"]

    _field_names_ = {
        "disk_uri": "diskURI",
    }
    _revfield_names_ = {
        "diskURI": "disk_uri",
    }

    caching_mode: str
    """ cachingMode is the Host Caching mode: None, Read Only, Read Write. """
    disk_name: str
    """ diskName is the Name of the data disk in the blob storage """
    disk_uri: str
    """ diskURI is the URI of data disk in the blob storage """
    fs_type: str
    """ fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """
    kind: str
    """ kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob disk per storage account  Managed: azure managed data disk (only in managed availability set). defaults to shared """
    read_only: bool
    """ readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """

    def __init__(
        self,
        caching_mode: str = None,
        disk_name: str = None,
        disk_uri: str = None,
        fs_type: str = None,
        kind: str = None,
        read_only: bool = None,
    ):
        super().__init__(caching_mode=caching_mode, disk_name=disk_name, disk_uri=disk_uri, fs_type=fs_type, kind=kind, read_only=read_only)


class AzureFilePersistentVolumeSource(KubernetesObject):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["secret_name", "share_name"]

    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_name: str
    """ secretName is the name of secret that contains Azure Storage Account Name and Key """
    secret_namespace: str
    """ secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod """
    share_name: str
    """ shareName is the azure Share Name """

    def __init__(self, read_only: bool = None, secret_name: str = None, secret_namespace: str = None, share_name: str = None):
        super().__init__(read_only=read_only, secret_name=secret_name, secret_namespace=secret_namespace, share_name=share_name)


class AzureFileVolumeSource(KubernetesObject):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["secret_name", "share_name"]

    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_name: str
    """ secretName is the  name of secret that contains Azure Storage Account Name and Key """
    share_name: str
    """ shareName is the azure share Name """

    def __init__(self, read_only: bool = None, secret_name: str = None, share_name: str = None):
        super().__init__(read_only=read_only, secret_name=secret_name, share_name=share_name)


Base64: t.TypeAlias = str
""" binary data encoded in base64 """


class ObjectReference(KubernetesObject):
    """ObjectReference contains enough information to let you inspect or modify the referred object."""

    __slots__ = ()

    _api_version_ = "v1"

    api_version: str
    """ API version of the referent. """
    field_path: str
    """ If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. """
    kind: str
    """ Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """
    name: str
    """ Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    namespace: str
    """ Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ """
    resource_version: str
    """ Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency """
    uid: str
    """ UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids """

    def __init__(
        self,
        api_version: str = None,
        field_path: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        resource_version: str = None,
        uid: str = None,
    ):
        super().__init__(
            api_version=api_version,
            field_path=field_path,
            kind=kind,
            name=name,
            namespace=namespace,
            resource_version=resource_version,
            uid=uid,
        )


class Binding(KubernetesApiResource):
    """Binding ties one object to another; for example, a pod is bound to a node by a scheduler. Deprecated in 1.7, please use the bindings subresource of pods instead."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Binding"
    _scope_ = "namespace"

    _required_ = ["target"]

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    target: ObjectReference
    """ The target object that you want to bind to the standard object. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, target: ObjectReference = None):
        super().__init__(name, namespace, metadata=metadata, target=target)


class SecretReference(KubernetesObject):
    """SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace"""

    __slots__ = ()

    _api_version_ = "v1"

    name: str
    """ name is unique within a namespace to reference a secret resource. """
    namespace: str
    """ namespace defines the space within which the secret name must be unique. """

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class CSIPersistentVolumeSource(KubernetesObject):
    """Represents storage that is managed by an external CSI volume driver (Beta feature)"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver", "volume_handle"]

    controller_expand_secret_ref: SecretReference
    """ controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """
    controller_publish_secret_ref: SecretReference
    """ controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """
    driver: str
    """ driver is the name of the driver to use for this volume. Required. """
    fs_type: str
    """ fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". """
    node_expand_secret_ref: SecretReference
    """ nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed. """
    node_publish_secret_ref: SecretReference
    """ nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """
    node_stage_secret_ref: SecretReference
    """ nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed. """
    read_only: bool
    """ readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). """
    volume_attributes: dict[str, str]
    """ volumeAttributes of the volume to publish. """
    volume_handle: str
    """ volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. """

    def __init__(
        self,
        controller_expand_secret_ref: SecretReference = None,
        controller_publish_secret_ref: SecretReference = None,
        driver: str = None,
        fs_type: str = None,
        node_expand_secret_ref: SecretReference = None,
        node_publish_secret_ref: SecretReference = None,
        node_stage_secret_ref: SecretReference = None,
        read_only: bool = None,
        volume_attributes: dict[str, str] = None,
        volume_handle: str = None,
    ):
        super().__init__(
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            driver=driver,
            fs_type=fs_type,
            node_expand_secret_ref=node_expand_secret_ref,
            node_publish_secret_ref=node_publish_secret_ref,
            node_stage_secret_ref=node_stage_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
            volume_handle=volume_handle,
        )


class LocalObjectReference(KubernetesObject):
    """LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace."""

    __slots__ = ()

    _api_version_ = "v1"

    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class CSIVolumeSource(KubernetesObject):
    """Represents a source location of a volume to mount, managed by an external CSI driver"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    """ driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. """
    fs_type: str
    """ fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. """
    node_publish_secret_ref: LocalObjectReference
    """ nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. """
    read_only: bool
    """ readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). """
    volume_attributes: dict[str, str]
    """ volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values. """

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        node_publish_secret_ref: LocalObjectReference = None,
        read_only: bool = None,
        volume_attributes: dict[str, str] = None,
    ):
        super().__init__(
            driver=driver,
            fs_type=fs_type,
            node_publish_secret_ref=node_publish_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
        )


class Capabilities(KubernetesObject):
    """Adds and removes POSIX capabilities from running containers."""

    __slots__ = ()

    _api_version_ = "v1"

    add: list[str]
    """ Added capabilities """
    drop: list[str]
    """ Removed capabilities """

    def __init__(self, add: list[str] = None, drop: list[str] = None):
        super().__init__(add=add, drop=drop)


class CephFSPersistentVolumeSource(KubernetesObject):
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["monitors"]

    monitors: list[str]
    """ monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    path: str
    """ path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """
    read_only: bool
    """ readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    secret_file: str
    """ secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    secret_ref: SecretReference
    """ secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    user: str
    """ user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """

    def __init__(
        self,
        monitors: list[str] = None,
        path: str = None,
        read_only: bool = None,
        secret_file: str = None,
        secret_ref: SecretReference = None,
        user: str = None,
    ):
        super().__init__(monitors=monitors, path=path, read_only=read_only, secret_file=secret_file, secret_ref=secret_ref, user=user)


class CephFSVolumeSource(KubernetesObject):
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["monitors"]

    monitors: list[str]
    """ monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    path: str
    """ path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / """
    read_only: bool
    """ readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    secret_file: str
    """ secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    secret_ref: LocalObjectReference
    """ secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """
    user: str
    """ user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it """

    def __init__(
        self,
        monitors: list[str] = None,
        path: str = None,
        read_only: bool = None,
        secret_file: str = None,
        secret_ref: LocalObjectReference = None,
        user: str = None,
    ):
        super().__init__(monitors=monitors, path=path, read_only=read_only, secret_file=secret_file, secret_ref=secret_ref, user=user)


class CinderPersistentVolumeSource(KubernetesObject):
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    """ fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """
    read_only: bool
    """ readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """
    secret_ref: SecretReference
    """ secretRef is Optional: points to a secret object containing parameters used to connect to OpenStack. """
    volume_id: str
    """ volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """

    def __init__(self, fs_type: str = None, read_only: bool = None, secret_ref: SecretReference = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_id=volume_id)


class CinderVolumeSource(KubernetesObject):
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """
    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """
    secret_ref: LocalObjectReference
    """ secretRef is optional: points to a secret object containing parameters used to connect to OpenStack. """
    volume_id: str
    """ volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """

    def __init__(self, fs_type: str = None, read_only: bool = None, secret_ref: LocalObjectReference = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_id=volume_id)


class ClaimSource(KubernetesObject):
    """
    ClaimSource describes a reference to a ResourceClaim.

    Exactly one of these fields should be set.  Consumers of this type must treat an empty object as if it has an unknown value.
    """

    __slots__ = ()

    _api_version_ = "v1"

    resource_claim_name: str
    """ ResourceClaimName is the name of a ResourceClaim object in the same namespace as this pod. """
    resource_claim_template_name: str
    """ 
    ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this pod.
    
    The template will be used to create a new ResourceClaim, which will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The pod name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.
    
    This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.
     """

    def __init__(self, resource_claim_name: str = None, resource_claim_template_name: str = None):
        super().__init__(resource_claim_name=resource_claim_name, resource_claim_template_name=resource_claim_template_name)


class ClientIPConfig(KubernetesObject):
    """ClientIPConfig represents the configurations of Client IP based session affinity."""

    __slots__ = ()

    _api_version_ = "v1"

    timeout_seconds: int
    """ timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value must be >0 && <=86400(for 1 day) if ServiceAffinity == "ClientIP". Default value is 10800(for 3 hours). """

    def __init__(self, timeout_seconds: int = None):
        super().__init__(timeout_seconds=timeout_seconds)


class ClusterTrustBundleProjection(KubernetesObject):
    """ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    label_selector: meta.LabelSelector
    """ Select all ClusterTrustBundles that match this label selector.  Only has effect if signerName is set.  Mutually-exclusive with name.  If unset, interpreted as "match nothing".  If set but empty, interpreted as "match everything". """
    name: str
    """ Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector. """
    optional: bool
    """ If true, don't block pod startup if the referenced ClusterTrustBundle(s) aren't available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. """
    path: str
    """ Relative path from the volume root to write the bundle. """
    signer_name: str
    """ Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated. """

    def __init__(
        self, label_selector: meta.LabelSelector = None, name: str = None, optional: bool = None, path: str = None, signer_name: str = None
    ):
        super().__init__(label_selector=label_selector, name=name, optional=optional, path=path, signer_name=signer_name)


class ComponentCondition(KubernetesObject):
    """Information about the condition of a component."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    error: str
    """ Condition error code for a component. For example, a health check error code. """
    message: str
    """ Message about the condition for a component. For example, information about a health check. """
    status: str
    """ Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown". """
    type: str
    """ Type of condition for a component. Valid value: "Healthy" """

    def __init__(self, error: str = None, message: str = None, status: str = None, type: str = None):
        super().__init__(error=error, message=message, status=status, type=type)


class ComponentStatus(KubernetesApiResource):
    """ComponentStatus (and ComponentStatusList) holds the cluster validation info. Deprecated: This API is deprecated in v1.19+"""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ComponentStatus"
    _scope_ = "cluster"

    conditions: list[ComponentCondition]
    """ List of component conditions observed """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """

    def __init__(self, name: str, conditions: list[ComponentCondition] = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, "", conditions=conditions, metadata=metadata)


class ConfigMap(KubernetesApiResource):
    """ConfigMap holds configuration data for pods to consume."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ConfigMap"
    _scope_ = "namespace"

    binary_data: dict[str, Base64]
    """ BinaryData contains the binary data. Each key must consist of alphanumeric characters, '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys stored in BinaryData must not overlap with the ones in the Data field, this is enforced during validation process. Using this field will require 1.10+ apiserver and kubelet. """
    data: dict[str, str]
    """ Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_' or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in Data must not overlap with the keys in the BinaryData field, this is enforced during validation process. """
    immutable: bool
    """ Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        binary_data: dict[str, Base64] = None,
        data: dict[str, str] = None,
        immutable: bool = None,
        metadata: meta.ObjectMeta = None,
    ):
        super().__init__(name, namespace, binary_data=binary_data, data=data, immutable=immutable, metadata=metadata)


class ConfigMapEnvSource(KubernetesObject):
    """
    ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.

    The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.
    """

    __slots__ = ()

    _api_version_ = "v1"

    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ Specify whether the ConfigMap must be defined """

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class ConfigMapKeySelector(KubernetesObject):
    """Selects a key from a ConfigMap."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key"]

    key: str
    """ The key to select. """
    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ Specify whether the ConfigMap or its key must be defined """

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class ConfigMapNodeConfigSource(KubernetesObject):
    """ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["kubelet_config_key", "name", "namespace"]

    kubelet_config_key: str
    """ KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases. """
    name: str
    """ Name is the metadata.name of the referenced ConfigMap. This field is required in all cases. """
    namespace: str
    """ Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases. """
    resource_version: str
    """ ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """
    uid: str
    """ UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. """

    def __init__(
        self, kubelet_config_key: str = None, name: str = None, namespace: str = None, resource_version: str = None, uid: str = None
    ):
        super().__init__(kubelet_config_key=kubelet_config_key, name=name, namespace=namespace, resource_version=resource_version, uid=uid)


class KeyToPath(KubernetesObject):
    """Maps a string key to a path within a volume."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "path"]

    key: str
    """ key is the key to project. """
    mode: int
    """ mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """
    path: str
    """ path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'. """

    def __init__(self, key: str = None, mode: int = None, path: str = None):
        super().__init__(key=key, mode=mode, path=path)


class ConfigMapProjection(KubernetesObject):
    """
    Adapts a ConfigMap into a projected volume.

    The contents of the target ConfigMap's Data field will be presented in a projected volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. Note that this is identical to a configmap volume source without the default mode.
    """

    __slots__ = ()

    _api_version_ = "v1"

    items: list[KeyToPath]
    """ items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """
    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ optional specify whether the ConfigMap or its keys must be defined """

    def __init__(self, items: list[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(items=items, name=name, optional=optional)


class ConfigMapVolumeSource(KubernetesObject):
    """
    Adapts a ConfigMap into a volume.

    The contents of the target ConfigMap's Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.
    """

    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    """ defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """
    items: list[KeyToPath]
    """ items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """
    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ optional specify whether the ConfigMap or its keys must be defined """

    def __init__(self, default_mode: int = None, items: list[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(default_mode=default_mode, items=items, name=name, optional=optional)


class ObjectFieldSelector(KubernetesObject):
    """ObjectFieldSelector selects an APIVersioned field of an object."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["field_path"]

    api_version: str
    """ Version of the schema the FieldPath is written in terms of, defaults to "v1". """
    field_path: str
    """ Path of the field to select in the specified API version. """

    def __init__(self, api_version: str = None, field_path: str = None):
        super().__init__(api_version=api_version, field_path=field_path)


Quantity: t.TypeAlias = str | int | float
""" Quantity is a fixed-point representation of a number. It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors. """


class ResourceFieldSelector(KubernetesObject):
    """ResourceFieldSelector represents container resources (cpu, memory) and their output format"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["resource"]

    container_name: str
    """ Container name: required for volumes, optional for env vars """
    divisor: Quantity
    """ Specifies the output format of the exposed resources, defaults to "1" """
    resource: str
    """ Required: resource to select """

    def __init__(self, container_name: str = None, divisor: Quantity = None, resource: str = None):
        super().__init__(container_name=container_name, divisor=divisor, resource=resource)


class SecretKeySelector(KubernetesObject):
    """SecretKeySelector selects a key of a Secret."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key"]

    key: str
    """ The key of the secret to select from.  Must be a valid secret key. """
    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ Specify whether the Secret or its key must be defined """

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class EnvVarSource(KubernetesObject):
    """EnvVarSource represents a source for the value of an EnvVar."""

    __slots__ = ()

    _api_version_ = "v1"

    config_map_key_ref: ConfigMapKeySelector
    """ Selects a key of a ConfigMap. """
    field_ref: ObjectFieldSelector
    """ Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. """
    resource_field_ref: ResourceFieldSelector
    """ Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. """
    secret_key_ref: SecretKeySelector
    """ Selects a key of a secret in the pod's namespace """

    def __init__(
        self,
        config_map_key_ref: ConfigMapKeySelector = None,
        field_ref: ObjectFieldSelector = None,
        resource_field_ref: ResourceFieldSelector = None,
        secret_key_ref: SecretKeySelector = None,
    ):
        super().__init__(
            config_map_key_ref=config_map_key_ref, field_ref=field_ref, resource_field_ref=resource_field_ref, secret_key_ref=secret_key_ref
        )


class EnvVar(KubernetesObject):
    """EnvVar represents an environment variable present in a Container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    """ Name of the environment variable. Must be a C_IDENTIFIER. """
    value: str
    """ Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". """
    value_from: EnvVarSource
    """ Source for the environment variable's value. Cannot be used if value is not empty. """

    def __init__(self, name: str = None, value: str = None, value_from: EnvVarSource = None):
        super().__init__(name=name, value=value, value_from=value_from)


class SecretEnvSource(KubernetesObject):
    """
    SecretEnvSource selects a Secret to populate the environment variables with.

    The contents of the target Secret's Data field will represent the key-value pairs as environment variables.
    """

    __slots__ = ()

    _api_version_ = "v1"

    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ Specify whether the Secret must be defined """

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class EnvFromSource(KubernetesObject):
    """EnvFromSource represents the source of a set of ConfigMaps"""

    __slots__ = ()

    _api_version_ = "v1"

    config_map_ref: ConfigMapEnvSource
    """ The ConfigMap to select from """
    prefix: str
    """ An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. """
    secret_ref: SecretEnvSource
    """ The Secret to select from """

    def __init__(self, config_map_ref: ConfigMapEnvSource = None, prefix: str = None, secret_ref: SecretEnvSource = None):
        super().__init__(config_map_ref=config_map_ref, prefix=prefix, secret_ref=secret_ref)


class ExecAction(KubernetesObject):
    """ExecAction describes a "run in container" action."""

    __slots__ = ()

    _api_version_ = "v1"

    command: list[str]
    """ Command is the command line to execute inside the container, the working directory for the command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. """

    def __init__(self, command: list[str] = None):
        super().__init__(command=command)


class HTTPHeader(KubernetesObject):
    """HTTPHeader describes a custom header to be used in HTTP probes"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name", "value"]

    name: str
    """ The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. """
    value: str
    """ The header field value """

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


IntOrString: t.TypeAlias = int | str
""" IntOrString is a type that can hold an int32 or a string. """


class HTTPGetAction(KubernetesObject):
    """HTTPGetAction describes an action based on HTTP Get requests."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    host: str
    """ Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead. """
    http_headers: list[HTTPHeader]
    """ Custom headers to set in the request. HTTP allows repeated headers. """
    path: str
    """ Path to access on the HTTP server. """
    port: IntOrString
    """ Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """
    scheme: str
    """ Scheme to use for connecting to the host. Defaults to HTTP. """

    def __init__(
        self, host: str = None, http_headers: list[HTTPHeader] = None, path: str = None, port: IntOrString = None, scheme: str = None
    ):
        super().__init__(host=host, http_headers=http_headers, path=path, port=port, scheme=scheme)


class SleepAction(KubernetesObject):
    """SleepAction describes a "sleep" action."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["seconds"]

    seconds: int
    """ Seconds is the number of seconds to sleep. """

    def __init__(self, seconds: int = None):
        super().__init__(seconds=seconds)


class TCPSocketAction(KubernetesObject):
    """TCPSocketAction describes an action based on opening a socket"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    host: str
    """ Optional: Host name to connect to, defaults to the pod IP. """
    port: IntOrString
    """ Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. """

    def __init__(self, host: str = None, port: IntOrString = None):
        super().__init__(host=host, port=port)


class LifecycleHandler(KubernetesObject):
    """LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified."""

    __slots__ = ()

    _api_version_ = "v1"

    exec: ExecAction
    """ Exec specifies the action to take. """
    http_get: HTTPGetAction
    """ HTTPGet specifies the http request to perform. """
    sleep: SleepAction
    """ Sleep represents the duration that the container should sleep before being terminated. """
    tcp_socket: TCPSocketAction
    """ Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified. """

    def __init__(
        self, exec: ExecAction = None, http_get: HTTPGetAction = None, sleep: SleepAction = None, tcp_socket: TCPSocketAction = None
    ):
        super().__init__(exec=exec, http_get=http_get, sleep=sleep, tcp_socket=tcp_socket)


class Lifecycle(KubernetesObject):
    """Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted."""

    __slots__ = ()

    _api_version_ = "v1"

    post_start: LifecycleHandler
    """ PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks """
    pre_stop: LifecycleHandler
    """ PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks """

    def __init__(self, post_start: LifecycleHandler = None, pre_stop: LifecycleHandler = None):
        super().__init__(post_start=post_start, pre_stop=pre_stop)


class GRPCAction(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    port: int
    """ Port number of the gRPC service. Number must be in the range 1 to 65535. """
    service: str
    """ 
    Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).
    
    If this is not specified, the default behavior is defined by gRPC.
     """

    def __init__(self, port: int = None, service: str = None):
        super().__init__(port=port, service=service)


class Probe(KubernetesObject):
    """Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic."""

    __slots__ = ()

    _api_version_ = "v1"

    exec: ExecAction
    """ Exec specifies the action to take. """
    failure_threshold: int
    """ Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. """
    grpc: GRPCAction
    """ GRPC specifies an action involving a GRPC port. """
    http_get: HTTPGetAction
    """ HTTPGet specifies the http request to perform. """
    initial_delay_seconds: int
    """ Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """
    period_seconds: int
    """ How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. """
    success_threshold: int
    """ Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. """
    tcp_socket: TCPSocketAction
    """ TCPSocket specifies an action involving a TCP port. """
    termination_grace_period_seconds: int
    """ Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. """
    timeout_seconds: int
    """ Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """

    def __init__(
        self,
        exec: ExecAction = None,
        failure_threshold: int = None,
        grpc: GRPCAction = None,
        http_get: HTTPGetAction = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: TCPSocketAction = None,
        termination_grace_period_seconds: int = None,
        timeout_seconds: int = None,
    ):
        super().__init__(
            exec=exec,
            failure_threshold=failure_threshold,
            grpc=grpc,
            http_get=http_get,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            tcp_socket=tcp_socket,
            termination_grace_period_seconds=termination_grace_period_seconds,
            timeout_seconds=timeout_seconds,
        )


class ContainerPort(KubernetesObject):
    """ContainerPort represents a network port in a single container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["container_port"]

    _field_names_ = {
        "host_ip": "hostIP",
    }
    _revfield_names_ = {
        "hostIP": "host_ip",
    }

    container_port: int
    """ Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536. """
    host_ip: str
    """ What host IP to bind the external port to. """
    host_port: int
    """ Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. """
    name: str
    """ If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. """
    protocol: str
    """ Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP". """

    def __init__(self, container_port: int = None, host_ip: str = None, host_port: int = None, name: str = None, protocol: str = None):
        super().__init__(container_port=container_port, host_ip=host_ip, host_port=host_port, name=name, protocol=protocol)


class ContainerResizePolicy(KubernetesObject):
    """ContainerResizePolicy represents resource resize policy for the container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["resource_name", "restart_policy"]

    resource_name: str
    """ Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. """
    restart_policy: str
    """ Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. """

    def __init__(self, resource_name: str = None, restart_policy: str = None):
        super().__init__(resource_name=resource_name, restart_policy=restart_policy)


class ResourceClaim(KubernetesObject):
    """ResourceClaim references one entry in PodSpec.ResourceClaims."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    """ Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class ResourceRequirements(KubernetesObject):
    """ResourceRequirements describes the compute resource requirements."""

    __slots__ = ()

    _api_version_ = "v1"

    claims: list[ResourceClaim]
    """ 
    Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.
    
    This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.
    
    This field is immutable. It can only be set for containers.
     """
    limits: dict[str, Quantity]
    """ Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """
    requests: dict[str, Quantity]
    """ Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """

    def __init__(self, claims: list[ResourceClaim] = None, limits: dict[str, Quantity] = None, requests: dict[str, Quantity] = None):
        super().__init__(claims=claims, limits=limits, requests=requests)


class SELinuxOptions(KubernetesObject):
    """SELinuxOptions are the labels to be applied to the container"""

    __slots__ = ()

    _api_version_ = "v1"

    level: str
    """ Level is SELinux level label that applies to the container. """
    role: str
    """ Role is a SELinux role label that applies to the container. """
    type: str
    """ Type is a SELinux type label that applies to the container. """
    user: str
    """ User is a SELinux user label that applies to the container. """

    def __init__(self, level: str = None, role: str = None, type: str = None, user: str = None):
        super().__init__(level=level, role=role, type=type, user=user)


class SeccompProfile(KubernetesObject):
    """SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["type"]

    localhost_profile: str
    """ localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type. """
    type: str
    """ 
    type indicates which kind of seccomp profile will be applied. Valid options are:
    
    Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.
     """

    def __init__(self, localhost_profile: str = None, type: str = None):
        super().__init__(localhost_profile=localhost_profile, type=type)


class WindowsSecurityContextOptions(KubernetesObject):
    """WindowsSecurityContextOptions contain Windows-specific options and credentials."""

    __slots__ = ()

    _api_version_ = "v1"

    gmsa_credential_spec: str
    """ GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. """
    gmsa_credential_spec_name: str
    """ GMSACredentialSpecName is the name of the GMSA credential spec to use. """
    host_process: bool
    """ HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. """
    run_as_user_name: str
    """ The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """

    def __init__(
        self,
        gmsa_credential_spec: str = None,
        gmsa_credential_spec_name: str = None,
        host_process: bool = None,
        run_as_user_name: str = None,
    ):
        super().__init__(
            gmsa_credential_spec=gmsa_credential_spec,
            gmsa_credential_spec_name=gmsa_credential_spec_name,
            host_process=host_process,
            run_as_user_name=run_as_user_name,
        )


class SecurityContext(KubernetesObject):
    """SecurityContext holds security configuration that will be applied to a container. Some fields are present in both SecurityContext and PodSecurityContext.  When both are set, the values in SecurityContext take precedence."""

    __slots__ = ()

    _api_version_ = "v1"

    allow_privilege_escalation: bool
    """ AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. """
    app_armor_profile: AppArmorProfile
    """ appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod's appArmorProfile. Note that this field cannot be set when spec.os.name is windows. """
    capabilities: Capabilities
    """ The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. """
    privileged: bool
    """ Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. """
    proc_mount: str
    """ procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. """
    read_only_root_filesystem: bool
    """ Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. """
    run_as_group: int
    """ The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """
    run_as_non_root: bool
    """ Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """
    run_as_user: int
    """ The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """
    se_linux_options: SELinuxOptions
    """ The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. """
    seccomp_profile: SeccompProfile
    """ The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. """
    windows_options: WindowsSecurityContextOptions
    """ The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. """

    def __init__(
        self,
        allow_privilege_escalation: bool = None,
        app_armor_profile: AppArmorProfile = None,
        capabilities: Capabilities = None,
        privileged: bool = None,
        proc_mount: str = None,
        read_only_root_filesystem: bool = None,
        run_as_group: int = None,
        run_as_non_root: bool = None,
        run_as_user: int = None,
        se_linux_options: SELinuxOptions = None,
        seccomp_profile: SeccompProfile = None,
        windows_options: WindowsSecurityContextOptions = None,
    ):
        super().__init__(
            allow_privilege_escalation=allow_privilege_escalation,
            app_armor_profile=app_armor_profile,
            capabilities=capabilities,
            privileged=privileged,
            proc_mount=proc_mount,
            read_only_root_filesystem=read_only_root_filesystem,
            run_as_group=run_as_group,
            run_as_non_root=run_as_non_root,
            run_as_user=run_as_user,
            se_linux_options=se_linux_options,
            seccomp_profile=seccomp_profile,
            windows_options=windows_options,
        )


class VolumeDevice(KubernetesObject):
    """volumeDevice describes a mapping of a raw block device within a container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["device_path", "name"]

    device_path: str
    """ devicePath is the path inside of the container that the device will be mapped to. """
    name: str
    """ name must match the name of a persistentVolumeClaim in the pod """

    def __init__(self, device_path: str = None, name: str = None):
        super().__init__(device_path=device_path, name=name)


class VolumeMount(KubernetesObject):
    """VolumeMount describes a mounting of a Volume within a container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["mount_path", "name"]

    mount_path: str
    """ Path within the container at which the volume should be mounted.  Must not contain ':'. """
    mount_propagation: str
    """ mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None). """
    name: str
    """ This must match the Name of a Volume. """
    read_only: bool
    """ Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. """
    recursive_read_only: str
    """ 
    RecursiveReadOnly specifies whether read-only mounts should be handled recursively.
    
    If ReadOnly is false, this field has no meaning and must be unspecified.
    
    If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only.  If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.
    
    If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).
    
    If this field is not specified, it is treated as an equivalent of Disabled.
     """
    sub_path: str
    """ Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root). """
    sub_path_expr: str
    """ Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive. """

    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        recursive_read_only: str = None,
        sub_path: str = None,
        sub_path_expr: str = None,
    ):
        super().__init__(
            mount_path=mount_path,
            mount_propagation=mount_propagation,
            name=name,
            read_only=read_only,
            recursive_read_only=recursive_read_only,
            sub_path=sub_path,
            sub_path_expr=sub_path_expr,
        )


class Container(KubernetesObject):
    """A single application container that you want to run within a pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    args: list[str]
    """ Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """
    command: list[str]
    """ Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """
    env: list[EnvVar]
    """ List of environment variables to set in the container. Cannot be updated. """
    env_from: list[EnvFromSource]
    """ List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. """
    image: str
    """ Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets. """
    image_pull_policy: str
    """ Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images """
    lifecycle: Lifecycle
    """ Actions that the management system should take in response to container lifecycle events. Cannot be updated. """
    liveness_probe: Probe
    """ Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """
    name: str
    """ Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated. """
    ports: list[ContainerPort]
    """ List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated. """
    readiness_probe: Probe
    """ Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """
    resize_policy: list[ContainerResizePolicy]
    """ Resources resize policy for the container. """
    resources: ResourceRequirements
    """ Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """
    restart_policy: str
    """ RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed. """
    security_context: SecurityContext
    """ SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/ """
    startup_probe: Probe
    """ StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes """
    stdin: bool
    """ Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. """
    stdin_once: bool
    """ Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false """
    termination_message_path: str
    """ Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. """
    termination_message_policy: str
    """ Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. """
    tty: bool
    """ Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. """
    volume_devices: list[VolumeDevice]
    """ volumeDevices is the list of block devices to be used by the container. """
    volume_mounts: list[VolumeMount]
    """ Pod volumes to mount into the container's filesystem. Cannot be updated. """
    working_dir: str
    """ Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. """

    def __init__(
        self,
        args: list[str] = None,
        command: list[str] = None,
        env: list[EnvVar] = None,
        env_from: list[EnvFromSource] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: Probe = None,
        name: str = None,
        ports: list[ContainerPort] = None,
        readiness_probe: Probe = None,
        resize_policy: list[ContainerResizePolicy] = None,
        resources: ResourceRequirements = None,
        restart_policy: str = None,
        security_context: SecurityContext = None,
        startup_probe: Probe = None,
        stdin: bool = None,
        stdin_once: bool = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        tty: bool = None,
        volume_devices: list[VolumeDevice] = None,
        volume_mounts: list[VolumeMount] = None,
        working_dir: str = None,
    ):
        super().__init__(
            args=args,
            command=command,
            env=env,
            env_from=env_from,
            image=image,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness_probe=liveness_probe,
            name=name,
            ports=ports,
            readiness_probe=readiness_probe,
            resize_policy=resize_policy,
            resources=resources,
            restart_policy=restart_policy,
            security_context=security_context,
            startup_probe=startup_probe,
            stdin=stdin,
            stdin_once=stdin_once,
            termination_message_path=termination_message_path,
            termination_message_policy=termination_message_policy,
            tty=tty,
            volume_devices=volume_devices,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )


class ContainerImage(KubernetesObject):
    """Describe a container image"""

    __slots__ = ()

    _api_version_ = "v1"

    names: list[str]
    """ Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"] """
    size_bytes: int
    """ The size of the image in bytes. """

    def __init__(self, names: list[str] = None, size_bytes: int = None):
        super().__init__(names=names, size_bytes=size_bytes)


class ContainerStateRunning(KubernetesObject):
    """ContainerStateRunning is a running state of a container."""

    __slots__ = ()

    _api_version_ = "v1"

    started_at: meta.Time
    """ Time at which the container was last (re-)started """

    def __init__(self, started_at: meta.Time = None):
        super().__init__(started_at=started_at)


class ContainerStateTerminated(KubernetesObject):
    """ContainerStateTerminated is a terminated state of a container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["exit_code"]

    _field_names_ = {
        "container_id": "containerID",
    }
    _revfield_names_ = {
        "containerID": "container_id",
    }

    container_id: str
    """ Container's ID in the format '<type>://<container_id>' """
    exit_code: int
    """ Exit status from the last termination of the container """
    finished_at: meta.Time
    """ Time at which the container last terminated """
    message: str
    """ Message regarding the last termination of the container """
    reason: str
    """ (brief) reason from the last termination of the container """
    signal: int
    """ Signal from the last termination of the container """
    started_at: meta.Time
    """ Time at which previous execution of the container started """

    def __init__(
        self,
        container_id: str = None,
        exit_code: int = None,
        finished_at: meta.Time = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        started_at: meta.Time = None,
    ):
        super().__init__(
            container_id=container_id,
            exit_code=exit_code,
            finished_at=finished_at,
            message=message,
            reason=reason,
            signal=signal,
            started_at=started_at,
        )


class ContainerStateWaiting(KubernetesObject):
    """ContainerStateWaiting is a waiting state of a container."""

    __slots__ = ()

    _api_version_ = "v1"

    message: str
    """ Message regarding why the container is not yet running. """
    reason: str
    """ (brief) reason the container is not yet running. """

    def __init__(self, message: str = None, reason: str = None):
        super().__init__(message=message, reason=reason)


class ContainerState(KubernetesObject):
    """ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting."""

    __slots__ = ()

    _api_version_ = "v1"

    running: ContainerStateRunning
    """ Details about a running container """
    terminated: ContainerStateTerminated
    """ Details about a terminated container """
    waiting: ContainerStateWaiting
    """ Details about a waiting container """

    def __init__(
        self, running: ContainerStateRunning = None, terminated: ContainerStateTerminated = None, waiting: ContainerStateWaiting = None
    ):
        super().__init__(running=running, terminated=terminated, waiting=waiting)


class VolumeMountStatus(KubernetesObject):
    """VolumeMountStatus shows status of volume mounts."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["mount_path", "name"]

    mount_path: str
    """ MountPath corresponds to the original VolumeMount. """
    name: str
    """ Name corresponds to the name of the original VolumeMount. """
    read_only: bool
    """ ReadOnly corresponds to the original VolumeMount. """
    recursive_read_only: str
    """ RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result. """

    def __init__(self, mount_path: str = None, name: str = None, read_only: bool = None, recursive_read_only: str = None):
        super().__init__(mount_path=mount_path, name=name, read_only=read_only, recursive_read_only=recursive_read_only)


class ContainerStatus(KubernetesObject):
    """ContainerStatus contains details for the current status of this container."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "image_id", "name", "ready", "restart_count"]

    _field_names_ = {
        "container_id": "containerID",
        "image_id": "imageID",
    }
    _revfield_names_ = {
        "containerID": "container_id",
        "imageID": "image_id",
    }

    allocated_resources: dict[str, Quantity]
    """ AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize. """
    container_id: str
    """ ContainerID is the ID of the container in the format '<type>://<container_id>'. Where type is a container runtime identifier, returned from Version call of CRI API (for example "containerd"). """
    image: str
    """ Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images. """
    image_id: str
    """ ImageID is the image ID of the container's image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime. """
    last_state: ContainerState
    """ LastTerminationState holds the last termination state of the container to help debug container crashes and restarts. This field is not populated if the container is still running and RestartCount is 0. """
    name: str
    """ Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated. """
    ready: bool
    """ 
    Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).
    
    The value is typically used to determine whether a container is ready to accept traffic.
     """
    resources: ResourceRequirements
    """ Resources represents the compute resource requests and limits that have been successfully enacted on the running container after it has been started or has been successfully resized. """
    restart_count: int
    """ RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative. """
    started: bool
    """ Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false. """
    state: ContainerState
    """ State holds details about the container's current condition. """
    volume_mounts: list[VolumeMountStatus]
    """ Status of volume mounts. """

    def __init__(
        self,
        allocated_resources: dict[str, Quantity] = None,
        container_id: str = None,
        image: str = None,
        image_id: str = None,
        last_state: ContainerState = None,
        name: str = None,
        ready: bool = None,
        resources: ResourceRequirements = None,
        restart_count: int = None,
        started: bool = None,
        state: ContainerState = None,
        volume_mounts: list[VolumeMountStatus] = None,
    ):
        super().__init__(
            allocated_resources=allocated_resources,
            container_id=container_id,
            image=image,
            image_id=image_id,
            last_state=last_state,
            name=name,
            ready=ready,
            resources=resources,
            restart_count=restart_count,
            started=started,
            state=state,
            volume_mounts=volume_mounts,
        )


class DaemonEndpoint(KubernetesObject):
    """DaemonEndpoint contains information about a single Daemon endpoint."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    _field_names_ = {
        "port": "Port",
    }
    _revfield_names_ = {
        "Port": "port",
    }

    port: int
    """ Port number of the given endpoint. """

    def __init__(self, port: int = None):
        super().__init__(port=port)


class DownwardAPIVolumeFile(KubernetesObject):
    """DownwardAPIVolumeFile represents information to create the file containing the pod field"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    field_ref: ObjectFieldSelector
    """ Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported. """
    mode: int
    """ Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """
    path: str
    """ Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..' """
    resource_field_ref: ResourceFieldSelector
    """ Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. """

    def __init__(
        self, field_ref: ObjectFieldSelector = None, mode: int = None, path: str = None, resource_field_ref: ResourceFieldSelector = None
    ):
        super().__init__(field_ref=field_ref, mode=mode, path=path, resource_field_ref=resource_field_ref)


class DownwardAPIProjection(KubernetesObject):
    """Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode."""

    __slots__ = ()

    _api_version_ = "v1"

    items: list[DownwardAPIVolumeFile]
    """ Items is a list of DownwardAPIVolume file """

    def __init__(self, items: list[DownwardAPIVolumeFile] = None):
        super().__init__(items=items)


class DownwardAPIVolumeSource(KubernetesObject):
    """DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    """ Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """
    items: list[DownwardAPIVolumeFile]
    """ Items is a list of downward API volume file """

    def __init__(self, default_mode: int = None, items: list[DownwardAPIVolumeFile] = None):
        super().__init__(default_mode=default_mode, items=items)


class EmptyDirVolumeSource(KubernetesObject):
    """Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    medium: str
    """ medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """
    size_limit: Quantity
    """ sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """

    def __init__(self, medium: str = None, size_limit: Quantity = None):
        super().__init__(medium=medium, size_limit=size_limit)


class EndpointAddress(KubernetesObject):
    """EndpointAddress is a tuple that describes single IP address."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["ip"]

    hostname: str
    """ The Hostname of this endpoint """
    ip: str
    """ The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16). """
    node_name: str
    """ Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. """
    target_ref: ObjectReference
    """ Reference to object providing the endpoint. """

    def __init__(self, hostname: str = None, ip: str = None, node_name: str = None, target_ref: ObjectReference = None):
        super().__init__(hostname=hostname, ip=ip, node_name=node_name, target_ref=target_ref)


class EndpointPort(KubernetesObject):
    """EndpointPort is a tuple that describes a single port."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    app_protocol: str
    """ 
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:
    
    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).
    
    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455
    
    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
     """
    name: str
    """ The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined. """
    port: int
    """ The port number of the endpoint. """
    protocol: str
    """ The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. """

    def __init__(self, app_protocol: str = None, name: str = None, port: int = None, protocol: str = None):
        super().__init__(app_protocol=app_protocol, name=name, port=port, protocol=protocol)


class EndpointSubset(KubernetesObject):
    """
    EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:

        {
          Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
          Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
        }

    The resulting set of endpoints can be viewed as:

        a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
        b: [ 10.10.1.1:309, 10.10.2.2:309 ]
    """

    __slots__ = ()

    _api_version_ = "v1"

    addresses: list[EndpointAddress]
    """ IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize. """
    not_ready_addresses: list[EndpointAddress]
    """ IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. """
    ports: list[EndpointPort]
    """ Port numbers available on the related IP addresses. """

    def __init__(
        self, addresses: list[EndpointAddress] = None, not_ready_addresses: list[EndpointAddress] = None, ports: list[EndpointPort] = None
    ):
        super().__init__(addresses=addresses, not_ready_addresses=not_ready_addresses, ports=ports)


class Endpoints(KubernetesApiResource):
    """
    Endpoints is a collection of endpoints that implement the actual service. Example:

         Name: "mysvc",
         Subsets: [
           {
             Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
             Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
           },
           {
             Addresses: [{"ip": "10.10.3.3"}],
             Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
           },
        ]
    """

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Endpoints"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    subsets: list[EndpointSubset]
    """ The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, subsets: list[EndpointSubset] = None):
        super().__init__(name, namespace, metadata=metadata, subsets=subsets)


class EphemeralContainer(KubernetesObject):
    """
    An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.

    To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.
    """

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    args: list[str]
    """ Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """
    command: list[str]
    """ Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell """
    env: list[EnvVar]
    """ List of environment variables to set in the container. Cannot be updated. """
    env_from: list[EnvFromSource]
    """ List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. """
    image: str
    """ Container image name. More info: https://kubernetes.io/docs/concepts/containers/images """
    image_pull_policy: str
    """ Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images """
    lifecycle: Lifecycle
    """ Lifecycle is not allowed for ephemeral containers. """
    liveness_probe: Probe
    """ Probes are not allowed for ephemeral containers. """
    name: str
    """ Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers. """
    ports: list[ContainerPort]
    """ Ports are not allowed for ephemeral containers. """
    readiness_probe: Probe
    """ Probes are not allowed for ephemeral containers. """
    resize_policy: list[ContainerResizePolicy]
    """ Resources resize policy for the container. """
    resources: ResourceRequirements
    """ Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod. """
    restart_policy: str
    """ Restart policy for the container to manage the restart behavior of each container within a pod. This may only be set for init containers. You cannot set this field on ephemeral containers. """
    security_context: SecurityContext
    """ Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. """
    startup_probe: Probe
    """ Probes are not allowed for ephemeral containers. """
    stdin: bool
    """ Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. """
    stdin_once: bool
    """ Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false """
    target_container_name: str
    """ 
    If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.
    
    The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined.
     """
    termination_message_path: str
    """ Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. """
    termination_message_policy: str
    """ Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. """
    tty: bool
    """ Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false. """
    volume_devices: list[VolumeDevice]
    """ volumeDevices is the list of block devices to be used by the container. """
    volume_mounts: list[VolumeMount]
    """ Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. """
    working_dir: str
    """ Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated. """

    def __init__(
        self,
        args: list[str] = None,
        command: list[str] = None,
        env: list[EnvVar] = None,
        env_from: list[EnvFromSource] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: Probe = None,
        name: str = None,
        ports: list[ContainerPort] = None,
        readiness_probe: Probe = None,
        resize_policy: list[ContainerResizePolicy] = None,
        resources: ResourceRequirements = None,
        restart_policy: str = None,
        security_context: SecurityContext = None,
        startup_probe: Probe = None,
        stdin: bool = None,
        stdin_once: bool = None,
        target_container_name: str = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        tty: bool = None,
        volume_devices: list[VolumeDevice] = None,
        volume_mounts: list[VolumeMount] = None,
        working_dir: str = None,
    ):
        super().__init__(
            args=args,
            command=command,
            env=env,
            env_from=env_from,
            image=image,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness_probe=liveness_probe,
            name=name,
            ports=ports,
            readiness_probe=readiness_probe,
            resize_policy=resize_policy,
            resources=resources,
            restart_policy=restart_policy,
            security_context=security_context,
            startup_probe=startup_probe,
            stdin=stdin,
            stdin_once=stdin_once,
            target_container_name=target_container_name,
            termination_message_path=termination_message_path,
            termination_message_policy=termination_message_policy,
            tty=tty,
            volume_devices=volume_devices,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )


class TypedLocalObjectReference(KubernetesObject):
    """TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["kind", "name"]

    api_group: str
    """ APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """
    kind: str
    """ Kind is the type of resource being referenced """
    name: str
    """ Name is the name of resource being referenced """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class TypedObjectReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["kind", "name"]

    api_group: str
    """ APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """
    kind: str
    """ Kind is the type of resource being referenced """
    name: str
    """ Name is the name of resource being referenced """
    namespace: str
    """ Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace)


class VolumeResourceRequirements(KubernetesObject):
    """VolumeResourceRequirements describes the storage resource requirements for a volume."""

    __slots__ = ()

    _api_version_ = "v1"

    limits: dict[str, Quantity]
    """ Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """
    requests: dict[str, Quantity]
    """ Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ """

    def __init__(self, limits: dict[str, Quantity] = None, requests: dict[str, Quantity] = None):
        super().__init__(limits=limits, requests=requests)


class PersistentVolumeClaimSpec(KubernetesObject):
    """PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes"""

    __slots__ = ()

    _api_version_ = "v1"

    access_modes: list[str]
    """ accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 """
    data_source: TypedLocalObjectReference
    """ dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. """
    data_source_ref: TypedObjectReference
    """ 
    dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef
      allows any non-core object, as well as PersistentVolumeClaim objects.
    * While dataSource ignores disallowed values (dropping them), dataSourceRef
      preserves all values, and generates an error if a disallowed value is
      specified.
    * While dataSource only allows local objects, dataSourceRef allows objects
      in any namespaces.
    (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.
     """
    resources: VolumeResourceRequirements
    """ resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources """
    selector: meta.LabelSelector
    """ selector is a label query over volumes to consider for binding. """
    storage_class_name: str
    """ storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 """
    volume_attributes_class_name: str
    """ volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ (Alpha) Using this field requires the VolumeAttributesClass feature gate to be enabled. """
    volume_mode: str
    """ volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. """
    volume_name: str
    """ volumeName is the binding reference to the PersistentVolume backing this claim. """

    def __init__(
        self,
        access_modes: list[str] = None,
        data_source: TypedLocalObjectReference = None,
        data_source_ref: TypedObjectReference = None,
        resources: VolumeResourceRequirements = None,
        selector: meta.LabelSelector = None,
        storage_class_name: str = None,
        volume_attributes_class_name: str = None,
        volume_mode: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            access_modes=access_modes,
            data_source=data_source,
            data_source_ref=data_source_ref,
            resources=resources,
            selector=selector,
            storage_class_name=storage_class_name,
            volume_attributes_class_name=volume_attributes_class_name,
            volume_mode=volume_mode,
            volume_name=volume_name,
        )


class PersistentVolumeClaimTemplate(KubernetesObject):
    """PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """
    spec: PersistentVolumeClaimSpec
    """ The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. """

    def __init__(self, metadata: meta.ObjectMeta = None, spec: PersistentVolumeClaimSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class EphemeralVolumeSource(KubernetesObject):
    """Represents an ephemeral volume that is handled by a normal storage driver."""

    __slots__ = ()

    _api_version_ = "v1"

    volume_claim_template: PersistentVolumeClaimTemplate
    """ 
    Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).
    
    An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.
    
    This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.
    
    Required, must not be nil.
     """

    def __init__(self, volume_claim_template: PersistentVolumeClaimTemplate = None):
        super().__init__(volume_claim_template=volume_claim_template)


class EventSeries(KubernetesObject):
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time."""

    __slots__ = ()

    _api_version_ = "v1"

    count: int
    """ Number of occurrences in this series up to the last heartbeat time """
    last_observed_time: meta.MicroTime
    """ Time of the last occurrence observed """

    def __init__(self, count: int = None, last_observed_time: meta.MicroTime = None):
        super().__init__(count=count, last_observed_time=last_observed_time)


class EventSource(KubernetesObject):
    """EventSource contains information for an event."""

    __slots__ = ()

    _api_version_ = "v1"

    component: str
    """ Component from which the event is generated. """
    host: str
    """ Node name on which the event is generated. """

    def __init__(self, component: str = None, host: str = None):
        super().__init__(component=component, host=host)


class Event(KubernetesApiResource):
    """Event is a report of an event somewhere in the cluster.  Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Event"
    _scope_ = "namespace"

    _required_ = ["involved_object", "metadata"]

    action: str
    """ What action was taken/failed regarding to the Regarding object. """
    count: int
    """ The number of times this event has occurred. """
    event_time: meta.MicroTime
    """ Time when this Event was first observed. """
    first_timestamp: meta.Time
    """ The time at which the event was first recorded. (Time of server receipt is in TypeMeta.) """
    involved_object: ObjectReference
    """ The object that this event is about. """
    last_timestamp: meta.Time
    """ The time at which the most recent occurrence of this event was recorded. """
    message: str
    """ A human-readable description of the status of this operation. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    reason: str
    """ This should be a short, machine understandable string that gives the reason for the transition into the object's current status. """
    related: ObjectReference
    """ Optional secondary object for more complex actions. """
    reporting_component: str
    """ Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. """
    reporting_instance: str
    """ ID of the controller instance, e.g. `kubelet-xyzf`. """
    series: EventSeries
    """ Data about the Event series this event represents or nil if it's a singleton Event. """
    source: EventSource
    """ The component reporting this event. Should be a short machine understandable string. """
    type: str
    """ Type of this event (Normal, Warning), new types could be added in the future """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        action: str = None,
        count: int = None,
        event_time: meta.MicroTime = None,
        first_timestamp: meta.Time = None,
        involved_object: ObjectReference = None,
        last_timestamp: meta.Time = None,
        message: str = None,
        metadata: meta.ObjectMeta = None,
        reason: str = None,
        related: ObjectReference = None,
        reporting_component: str = None,
        reporting_instance: str = None,
        series: EventSeries = None,
        source: EventSource = None,
        type: str = None,
    ):
        super().__init__(
            name,
            namespace,
            action=action,
            count=count,
            event_time=event_time,
            first_timestamp=first_timestamp,
            involved_object=involved_object,
            last_timestamp=last_timestamp,
            message=message,
            metadata=metadata,
            reason=reason,
            related=related,
            reporting_component=reporting_component,
            reporting_instance=reporting_instance,
            series=series,
            source=source,
            type=type,
        )


class FCVolumeSource(KubernetesObject):
    """Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "target_wwns": "targetWWNs",
    }
    _revfield_names_ = {
        "targetWWNs": "target_wwns",
    }

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """
    lun: int
    """ lun is Optional: FC target lun number """
    read_only: bool
    """ readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    target_wwns: list[str]
    """ targetWWNs is Optional: FC target worldwide names (WWNs) """
    wwids: list[str]
    """ wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. """

    def __init__(
        self, fs_type: str = None, lun: int = None, read_only: bool = None, target_wwns: list[str] = None, wwids: list[str] = None
    ):
        super().__init__(fs_type=fs_type, lun=lun, read_only=read_only, target_wwns=target_wwns, wwids=wwids)


class FlexPersistentVolumeSource(KubernetesObject):
    """FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    """ driver is the name of the driver to use for this volume. """
    fs_type: str
    """ fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """
    options: dict[str, str]
    """ options is Optional: this field holds extra command options if any. """
    read_only: bool
    """ readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_ref: SecretReference
    """ secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: dict[str, str] = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
    ):
        super().__init__(driver=driver, fs_type=fs_type, options=options, read_only=read_only, secret_ref=secret_ref)


class FlexVolumeSource(KubernetesObject):
    """FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    """ driver is the name of the driver to use for this volume. """
    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. """
    options: dict[str, str]
    """ options is Optional: this field holds extra command options if any. """
    read_only: bool
    """ readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_ref: LocalObjectReference
    """ secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. """

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: dict[str, str] = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
    ):
        super().__init__(driver=driver, fs_type=fs_type, options=options, read_only=read_only, secret_ref=secret_ref)


class FlockerVolumeSource(KubernetesObject):
    """Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "dataset_uuid": "datasetUUID",
    }
    _revfield_names_ = {
        "datasetUUID": "dataset_uuid",
    }

    dataset_name: str
    """ datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated """
    dataset_uuid: str
    """ datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset """

    def __init__(self, dataset_name: str = None, dataset_uuid: str = None):
        super().__init__(dataset_name=dataset_name, dataset_uuid=dataset_uuid)


class GCEPersistentDiskVolumeSource(KubernetesObject):
    """
    Represents a Persistent Disk resource in Google Compute Engine.

    A GCE PD must exist before mounting to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can only be mounted as read/write once or read-only many times. GCE PDs support ownership management and SELinux relabeling.
    """

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["pd_name"]

    fs_type: str
    """ fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """
    partition: int
    """ partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """
    pd_name: str
    """ pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """
    read_only: bool
    """ readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """

    def __init__(self, fs_type: str = None, partition: int = None, pd_name: str = None, read_only: bool = None):
        super().__init__(fs_type=fs_type, partition=partition, pd_name=pd_name, read_only=read_only)


class GitRepoVolumeSource(KubernetesObject):
    """
    Represents a volume that is populated with the contents of a git repository. Git repo volumes do not support ownership management. Git repo volumes support SELinux relabeling.

    DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.
    """

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["repository"]

    directory: str
    """ directory is the target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. """
    repository: str
    """ repository is the URL """
    revision: str
    """ revision is the commit hash for the specified revision. """

    def __init__(self, directory: str = None, repository: str = None, revision: str = None):
        super().__init__(directory=directory, repository=repository, revision=revision)


class GlusterfsPersistentVolumeSource(KubernetesObject):
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["endpoints", "path"]

    endpoints: str
    """ endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """
    endpoints_namespace: str
    """ endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """
    path: str
    """ path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """
    read_only: bool
    """ readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """

    def __init__(self, endpoints: str = None, endpoints_namespace: str = None, path: str = None, read_only: bool = None):
        super().__init__(endpoints=endpoints, endpoints_namespace=endpoints_namespace, path=path, read_only=read_only)


class GlusterfsVolumeSource(KubernetesObject):
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["endpoints", "path"]

    endpoints: str
    """ endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """
    path: str
    """ path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """
    read_only: bool
    """ readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod """

    def __init__(self, endpoints: str = None, path: str = None, read_only: bool = None):
        super().__init__(endpoints=endpoints, path=path, read_only=read_only)


class HostAlias(KubernetesObject):
    """HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["ip"]

    hostnames: list[str]
    """ Hostnames for the above IP address. """
    ip: str
    """ IP address of the host file entry. """

    def __init__(self, hostnames: list[str] = None, ip: str = None):
        super().__init__(hostnames=hostnames, ip=ip)


class HostIP(KubernetesObject):
    """HostIP represents a single IP address allocated to the host."""

    __slots__ = ()

    _api_version_ = "v1"

    ip: str
    """ IP is the IP address assigned to the host """

    def __init__(self, ip: str = None):
        super().__init__(ip=ip)


class HostPathVolumeSource(KubernetesObject):
    """Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    path: str
    """ path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """
    type: str
    """ type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """

    def __init__(self, path: str = None, type: str = None):
        super().__init__(path=path, type=type)


class ISCSIPersistentVolumeSource(KubernetesObject):
    """ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["iqn", "lun", "target_portal"]

    chap_auth_discovery: bool
    """ chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """
    chap_auth_session: bool
    """ chapAuthSession defines whether support iSCSI Session CHAP authentication """
    fs_type: str
    """ fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """
    initiator_name: str
    """ initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """
    iqn: str
    """ iqn is Target iSCSI Qualified Name. """
    iscsi_interface: str
    """ iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """
    lun: int
    """ lun is iSCSI Target Lun number. """
    portals: list[str]
    """ portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """
    read_only: bool
    """ readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """
    secret_ref: SecretReference
    """ secretRef is the CHAP Secret for iSCSI target and initiator authentication """
    target_portal: str
    """ targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """

    def __init__(
        self,
        chap_auth_discovery: bool = None,
        chap_auth_session: bool = None,
        fs_type: str = None,
        initiator_name: str = None,
        iqn: str = None,
        iscsi_interface: str = None,
        lun: int = None,
        portals: list[str] = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        target_portal: str = None,
    ):
        super().__init__(
            chap_auth_discovery=chap_auth_discovery,
            chap_auth_session=chap_auth_session,
            fs_type=fs_type,
            initiator_name=initiator_name,
            iqn=iqn,
            iscsi_interface=iscsi_interface,
            lun=lun,
            portals=portals,
            read_only=read_only,
            secret_ref=secret_ref,
            target_portal=target_portal,
        )


class ISCSIVolumeSource(KubernetesObject):
    """Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["iqn", "lun", "target_portal"]

    chap_auth_discovery: bool
    """ chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication """
    chap_auth_session: bool
    """ chapAuthSession defines whether support iSCSI Session CHAP authentication """
    fs_type: str
    """ fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi """
    initiator_name: str
    """ initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection. """
    iqn: str
    """ iqn is the target iSCSI Qualified Name. """
    iscsi_interface: str
    """ iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp). """
    lun: int
    """ lun represents iSCSI Target Lun number. """
    portals: list[str]
    """ portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """
    read_only: bool
    """ readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. """
    secret_ref: LocalObjectReference
    """ secretRef is the CHAP Secret for iSCSI target and initiator authentication """
    target_portal: str
    """ targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). """

    def __init__(
        self,
        chap_auth_discovery: bool = None,
        chap_auth_session: bool = None,
        fs_type: str = None,
        initiator_name: str = None,
        iqn: str = None,
        iscsi_interface: str = None,
        lun: int = None,
        portals: list[str] = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        target_portal: str = None,
    ):
        super().__init__(
            chap_auth_discovery=chap_auth_discovery,
            chap_auth_session=chap_auth_session,
            fs_type=fs_type,
            initiator_name=initiator_name,
            iqn=iqn,
            iscsi_interface=iscsi_interface,
            lun=lun,
            portals=portals,
            read_only=read_only,
            secret_ref=secret_ref,
            target_portal=target_portal,
        )


class Info(KubernetesObject):
    """Info contains versioning information. how we'll want to distribute that information."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["build_date", "compiler", "git_commit", "git_tree_state", "git_version", "go_version", "major", "minor", "platform"]

    build_date: str
    compiler: str
    git_commit: str
    git_tree_state: str
    git_version: str
    go_version: str
    major: str
    minor: str
    platform: str

    def __init__(
        self,
        build_date: str = None,
        compiler: str = None,
        git_commit: str = None,
        git_tree_state: str = None,
        git_version: str = None,
        go_version: str = None,
        major: str = None,
        minor: str = None,
        platform: str = None,
    ):
        super().__init__(
            build_date=build_date,
            compiler=compiler,
            git_commit=git_commit,
            git_tree_state=git_tree_state,
            git_version=git_version,
            go_version=go_version,
            major=major,
            minor=minor,
            platform=platform,
        )


class LimitRangeItem(KubernetesObject):
    """LimitRangeItem defines a min/max usage limit for any resource that matches on kind."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["type"]

    default: dict[str, Quantity]
    """ Default resource requirement limit value by resource name if resource limit is omitted. """
    default_request: dict[str, Quantity]
    """ DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. """
    max: dict[str, Quantity]
    """ Max usage constraints on this kind by resource name. """
    max_limit_request_ratio: dict[str, Quantity]
    """ MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. """
    min: dict[str, Quantity]
    """ Min usage constraints on this kind by resource name. """
    type: str
    """ Type of resource that this limit applies to. """

    def __init__(
        self,
        default: dict[str, Quantity] = None,
        default_request: dict[str, Quantity] = None,
        max: dict[str, Quantity] = None,
        max_limit_request_ratio: dict[str, Quantity] = None,
        min: dict[str, Quantity] = None,
        type: str = None,
    ):
        super().__init__(
            default=default, default_request=default_request, max=max, max_limit_request_ratio=max_limit_request_ratio, min=min, type=type
        )


class LimitRangeSpec(KubernetesObject):
    """LimitRangeSpec defines a min/max usage limit for resources that match on kind."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["limits"]

    limits: list[LimitRangeItem]
    """ Limits is the list of LimitRangeItem objects that are enforced. """

    def __init__(self, limits: list[LimitRangeItem] = None):
        super().__init__(limits=limits)


class LimitRange(KubernetesApiResource):
    """LimitRange sets resource usage limits for each kind of resource in a Namespace."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "LimitRange"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: LimitRangeSpec
    """ Spec defines the limits enforced. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: LimitRangeSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PortStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port", "protocol"]

    error: str
    """ 
    Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use
      CamelCase names
    - cloud provider specific error values must have names that comply with the
      format foo.example.com/CamelCase.
     """
    port: int
    """ Port is the port number of the service port of which status is recorded here """
    protocol: str
    """ Protocol is the protocol of the service port of which status is recorded here The supported values are: "TCP", "UDP", "SCTP" """

    def __init__(self, error: str = None, port: int = None, protocol: str = None):
        super().__init__(error=error, port=port, protocol=protocol)


class LoadBalancerIngress(KubernetesObject):
    """LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point."""

    __slots__ = ()

    _api_version_ = "v1"

    hostname: str
    """ Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) """
    ip: str
    """ IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) """
    ip_mode: str
    """ IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field is specified. Setting this to "VIP" indicates that traffic is delivered to the node with the destination set to the load-balancer's IP and port. Setting this to "Proxy" indicates that traffic is delivered to the node or pod with the destination set to the node's IP and node port or the pod's IP and port. Service implementations may use this information to adjust traffic routing. """
    ports: list[PortStatus]
    """ Ports is a list of records of service ports If used, every port defined in the service should have an entry in it """

    def __init__(self, hostname: str = None, ip: str = None, ip_mode: str = None, ports: list[PortStatus] = None):
        super().__init__(hostname=hostname, ip=ip, ip_mode=ip_mode, ports=ports)


class LoadBalancerStatus(KubernetesObject):
    """LoadBalancerStatus represents the status of a load-balancer."""

    __slots__ = ()

    _api_version_ = "v1"

    ingress: list[LoadBalancerIngress]
    """ Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. """

    def __init__(self, ingress: list[LoadBalancerIngress] = None):
        super().__init__(ingress=ingress)


class LocalVolumeSource(KubernetesObject):
    """Local represents directly-attached storage with node affinity (Beta feature)"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    fs_type: str
    """ fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default value is to auto-select a filesystem if unspecified. """
    path: str
    """ path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...). """

    def __init__(self, fs_type: str = None, path: str = None):
        super().__init__(fs_type=fs_type, path=path)


class ModifyVolumeStatus(KubernetesObject):
    """ModifyVolumeStatus represents the status object of ControllerModifyVolume operation"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status"]

    status: str
    """ 
    status is the status of the ControllerModifyVolume operation. It can be in any of following states:
     - Pending
       Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as
       the specified VolumeAttributesClass not existing.
     - InProgress
       InProgress indicates that the volume is being modified.
     - Infeasible
      Infeasible indicates that the request has been rejected as invalid by the CSI driver. To
    	  resolve the error, a valid VolumeAttributesClass needs to be specified.
    Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.
     """
    target_volume_attributes_class_name: str
    """ targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled """

    def __init__(self, status: str = None, target_volume_attributes_class_name: str = None):
        super().__init__(status=status, target_volume_attributes_class_name=target_volume_attributes_class_name)


class NFSVolumeSource(KubernetesObject):
    """Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path", "server"]

    path: str
    """ path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """
    read_only: bool
    """ readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """
    server: str
    """ server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """

    def __init__(self, path: str = None, read_only: bool = None, server: str = None):
        super().__init__(path=path, read_only=read_only, server=server)


class NamespaceSpec(KubernetesObject):
    """NamespaceSpec describes the attributes on a Namespace."""

    __slots__ = ()

    _api_version_ = "v1"

    finalizers: list[str]
    """ Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """

    def __init__(self, finalizers: list[str] = None):
        super().__init__(finalizers=finalizers)


class Namespace(KubernetesApiResource):
    """Namespace provides a scope for Names. Use of multiple namespaces is optional."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Namespace"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: NamespaceSpec
    """ Spec defines the behavior of the Namespace. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: NamespaceSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class NamespaceCondition(KubernetesObject):
    """NamespaceCondition contains details about state of namespace."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of namespace controller condition. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class NamespaceStatus(KubernetesObject):
    """NamespaceStatus is information about the current status of a Namespace."""

    __slots__ = ()

    _api_version_ = "v1"

    conditions: list[NamespaceCondition]
    """ Represents the latest available observations of a namespace's current state. """
    phase: str
    """ Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ """

    def __init__(self, conditions: list[NamespaceCondition] = None, phase: str = None):
        super().__init__(conditions=conditions, phase=phase)


class NodeConfigSource(KubernetesObject):
    """NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22"""

    __slots__ = ()

    _api_version_ = "v1"

    config_map: ConfigMapNodeConfigSource
    """ ConfigMap is a reference to a Node's ConfigMap """

    def __init__(self, config_map: ConfigMapNodeConfigSource = None):
        super().__init__(config_map=config_map)


class Taint(KubernetesObject):
    """The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["effect", "key"]

    effect: str
    """ Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. """
    key: str
    """ Required. The taint key to be applied to a node. """
    time_added: meta.Time
    """ TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. """
    value: str
    """ The taint value corresponding to the taint key. """

    def __init__(self, effect: str = None, key: str = None, time_added: meta.Time = None, value: str = None):
        super().__init__(effect=effect, key=key, time_added=time_added, value=value)


class NodeSpec(KubernetesObject):
    """NodeSpec describes the attributes that a node is created with."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "external_id": "externalID",
        "pod_cidr": "podCIDR",
        "pod_cidrs": "podCIDRs",
        "provider_id": "providerID",
    }
    _revfield_names_ = {
        "externalID": "external_id",
        "podCIDR": "pod_cidr",
        "podCIDRs": "pod_cidrs",
        "providerID": "provider_id",
    }

    config_source: NodeConfigSource
    """ Deprecated: Previously used to specify the source of the node's configuration for the DynamicKubeletConfig feature. This feature is removed. """
    external_id: str
    """ Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966 """
    pod_cidr: str
    """ PodCIDR represents the pod IP range assigned to the node. """
    pod_cidrs: list[str]
    """ podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6. """
    provider_id: str
    """ ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID> """
    taints: list[Taint]
    """ If specified, the node's taints. """
    unschedulable: bool
    """ Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration """

    def __init__(
        self,
        config_source: NodeConfigSource = None,
        external_id: str = None,
        pod_cidr: str = None,
        pod_cidrs: list[str] = None,
        provider_id: str = None,
        taints: list[Taint] = None,
        unschedulable: bool = None,
    ):
        super().__init__(
            config_source=config_source,
            external_id=external_id,
            pod_cidr=pod_cidr,
            pod_cidrs=pod_cidrs,
            provider_id=provider_id,
            taints=taints,
            unschedulable=unschedulable,
        )


class Node(KubernetesApiResource):
    """Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd)."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Node"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: NodeSpec
    """ Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: NodeSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class NodeAddress(KubernetesObject):
    """NodeAddress contains information for the node's address."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["address", "type"]

    address: str
    """ The node address. """
    type: str
    """ Node address type, one of Hostname, ExternalIP or InternalIP. """

    def __init__(self, address: str = None, type: str = None):
        super().__init__(address=address, type=type)


class NodeCondition(KubernetesObject):
    """NodeCondition contains condition information for a node."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_heartbeat_time: meta.Time
    """ Last time we got an update on a given condition. """
    last_transition_time: meta.Time
    """ Last time the condition transit from one status to another. """
    message: str
    """ Human readable message indicating details about last transition. """
    reason: str
    """ (brief) reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of node condition. """

    def __init__(
        self,
        last_heartbeat_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_heartbeat_time=last_heartbeat_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class NodeConfigStatus(KubernetesObject):
    """NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource."""

    __slots__ = ()

    _api_version_ = "v1"

    active: NodeConfigSource
    """ Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error. """
    assigned: NodeConfigSource
    """ Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned. """
    error: str
    """ Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions. """
    last_known_good: NodeConfigSource
    """ LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future. """

    def __init__(
        self,
        active: NodeConfigSource = None,
        assigned: NodeConfigSource = None,
        error: str = None,
        last_known_good: NodeConfigSource = None,
    ):
        super().__init__(active=active, assigned=assigned, error=error, last_known_good=last_known_good)


class NodeDaemonEndpoints(KubernetesObject):
    """NodeDaemonEndpoints lists ports opened by daemons running on the Node."""

    __slots__ = ()

    _api_version_ = "v1"

    kubelet_endpoint: DaemonEndpoint
    """ Endpoint on which Kubelet is listening. """

    def __init__(self, kubelet_endpoint: DaemonEndpoint = None):
        super().__init__(kubelet_endpoint=kubelet_endpoint)


class NodeRuntimeHandlerFeatures(KubernetesObject):
    """NodeRuntimeHandlerFeatures is a set of runtime features."""

    __slots__ = ()

    _api_version_ = "v1"

    recursive_read_only_mounts: bool
    """ RecursiveReadOnlyMounts is set to true if the runtime handler supports RecursiveReadOnlyMounts. """

    def __init__(self, recursive_read_only_mounts: bool = None):
        super().__init__(recursive_read_only_mounts=recursive_read_only_mounts)


class NodeRuntimeHandler(KubernetesObject):
    """NodeRuntimeHandler is a set of runtime handler information."""

    __slots__ = ()

    _api_version_ = "v1"

    features: NodeRuntimeHandlerFeatures
    """ Supported features. """
    name: str
    """ Runtime handler name. Empty for the default runtime handler. """

    def __init__(self, features: NodeRuntimeHandlerFeatures = None, name: str = None):
        super().__init__(features=features, name=name)


class NodeSystemInfo(KubernetesObject):
    """NodeSystemInfo is a set of ids/uuids to uniquely identify the node."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = [
        "architecture",
        "boot_id",
        "container_runtime_version",
        "kernel_version",
        "kube_proxy_version",
        "kubelet_version",
        "machine_id",
        "operating_system",
        "os_image",
        "system_uuid",
    ]

    _field_names_ = {
        "boot_id": "bootID",
        "machine_id": "machineID",
        "system_uuid": "systemUUID",
    }
    _revfield_names_ = {
        "bootID": "boot_id",
        "machineID": "machine_id",
        "systemUUID": "system_uuid",
    }

    architecture: str
    """ The Architecture reported by the node """
    boot_id: str
    """ Boot ID reported by the node. """
    container_runtime_version: str
    """ ContainerRuntime Version reported by the node through runtime remote API (e.g. containerd://1.4.2). """
    kernel_version: str
    """ Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64). """
    kube_proxy_version: str
    """ KubeProxy Version reported by the node. """
    kubelet_version: str
    """ Kubelet Version reported by the node. """
    machine_id: str
    """ MachineID reported by the node. For unique machine identification in the cluster this field is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html """
    operating_system: str
    """ The Operating System reported by the node """
    os_image: str
    """ OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). """
    system_uuid: str
    """ SystemUUID reported by the node. For unique machine identification MachineID is preferred. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid """

    def __init__(
        self,
        architecture: str = None,
        boot_id: str = None,
        container_runtime_version: str = None,
        kernel_version: str = None,
        kube_proxy_version: str = None,
        kubelet_version: str = None,
        machine_id: str = None,
        operating_system: str = None,
        os_image: str = None,
        system_uuid: str = None,
    ):
        super().__init__(
            architecture=architecture,
            boot_id=boot_id,
            container_runtime_version=container_runtime_version,
            kernel_version=kernel_version,
            kube_proxy_version=kube_proxy_version,
            kubelet_version=kubelet_version,
            machine_id=machine_id,
            operating_system=operating_system,
            os_image=os_image,
            system_uuid=system_uuid,
        )


class NodeStatus(KubernetesObject):
    """NodeStatus is information about the current status of a node."""

    __slots__ = ()

    _api_version_ = "v1"

    addresses: list[NodeAddress]
    """ List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node's address in its own status or consumers of the downward API (status.hostIP). """
    allocatable: dict[str, Quantity]
    """ Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. """
    capacity: dict[str, Quantity]
    """ Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity """
    conditions: list[NodeCondition]
    """ Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition """
    config: NodeConfigStatus
    """ Status of the config assigned to the node via the dynamic Kubelet config feature. """
    daemon_endpoints: NodeDaemonEndpoints
    """ Endpoints of daemons running on the Node. """
    images: list[ContainerImage]
    """ List of container images on this node """
    node_info: NodeSystemInfo
    """ Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info """
    phase: str
    """ NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated. """
    runtime_handlers: list[NodeRuntimeHandler]
    """ The available runtime handlers. """
    volumes_attached: list[AttachedVolume]
    """ List of volumes that are attached to the node. """
    volumes_in_use: list[str]
    """ List of attachable volumes in use (mounted) by the node. """

    def __init__(
        self,
        addresses: list[NodeAddress] = None,
        allocatable: dict[str, Quantity] = None,
        capacity: dict[str, Quantity] = None,
        conditions: list[NodeCondition] = None,
        config: NodeConfigStatus = None,
        daemon_endpoints: NodeDaemonEndpoints = None,
        images: list[ContainerImage] = None,
        node_info: NodeSystemInfo = None,
        phase: str = None,
        runtime_handlers: list[NodeRuntimeHandler] = None,
        volumes_attached: list[AttachedVolume] = None,
        volumes_in_use: list[str] = None,
    ):
        super().__init__(
            addresses=addresses,
            allocatable=allocatable,
            capacity=capacity,
            conditions=conditions,
            config=config,
            daemon_endpoints=daemon_endpoints,
            images=images,
            node_info=node_info,
            phase=phase,
            runtime_handlers=runtime_handlers,
            volumes_attached=volumes_attached,
            volumes_in_use=volumes_in_use,
        )


class VolumeNodeAffinity(KubernetesObject):
    """VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from."""

    __slots__ = ()

    _api_version_ = "v1"

    required: NodeSelector
    """ required specifies hard node constraints that must be met. """

    def __init__(self, required: NodeSelector = None):
        super().__init__(required=required)


class PhotonPersistentDiskVolumeSource(KubernetesObject):
    """Represents a Photon Controller persistent disk resource."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["pd_id"]

    _field_names_ = {
        "pd_id": "pdID",
    }
    _revfield_names_ = {
        "pdID": "pd_id",
    }

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """
    pd_id: str
    """ pdID is the ID that identifies Photon Controller persistent disk """

    def __init__(self, fs_type: str = None, pd_id: str = None):
        super().__init__(fs_type=fs_type, pd_id=pd_id)


class PortworxVolumeSource(KubernetesObject):
    """PortworxVolumeSource represents a Portworx volume resource."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    """ fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. """
    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    volume_id: str
    """ volumeID uniquely identifies a Portworx volume """

    def __init__(self, fs_type: str = None, read_only: bool = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, read_only=read_only, volume_id=volume_id)


class QuobyteVolumeSource(KubernetesObject):
    """Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["registry", "volume"]

    group: str
    """ group to map volume access to Default is no group """
    read_only: bool
    """ readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. """
    registry: str
    """ registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes """
    tenant: str
    """ tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin """
    user: str
    """ user to map volume access to Defaults to serivceaccount user """
    volume: str
    """ volume is a string that references an already created Quobyte volume by name. """

    def __init__(
        self, group: str = None, read_only: bool = None, registry: str = None, tenant: str = None, user: str = None, volume: str = None
    ):
        super().__init__(group=group, read_only=read_only, registry=registry, tenant=tenant, user=user, volume=volume)


class RBDPersistentVolumeSource(KubernetesObject):
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "monitors"]

    fs_type: str
    """ fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """
    image: str
    """ image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    keyring: str
    """ keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    monitors: list[str]
    """ monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    pool: str
    """ pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    read_only: bool
    """ readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    secret_ref: SecretReference
    """ secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    user: str
    """ user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """

    def __init__(
        self,
        fs_type: str = None,
        image: str = None,
        keyring: str = None,
        monitors: list[str] = None,
        pool: str = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        user: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            image=image,
            keyring=keyring,
            monitors=monitors,
            pool=pool,
            read_only=read_only,
            secret_ref=secret_ref,
            user=user,
        )


class ScaleIOPersistentVolumeSource(KubernetesObject):
    """ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["gateway", "secret_ref", "system"]

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs" """
    gateway: str
    """ gateway is the host address of the ScaleIO API Gateway. """
    protection_domain: str
    """ protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """
    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_ref: SecretReference
    """ secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """
    ssl_enabled: bool
    """ sslEnabled is the flag to enable/disable SSL communication with Gateway, default false """
    storage_mode: str
    """ storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """
    storage_pool: str
    """ storagePool is the ScaleIO Storage Pool associated with the protection domain. """
    system: str
    """ system is the name of the storage system as configured in ScaleIO. """
    volume_name: str
    """ volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """

    def __init__(
        self,
        fs_type: str = None,
        gateway: str = None,
        protection_domain: str = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        ssl_enabled: bool = None,
        storage_mode: str = None,
        storage_pool: str = None,
        system: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            gateway=gateway,
            protection_domain=protection_domain,
            read_only=read_only,
            secret_ref=secret_ref,
            ssl_enabled=ssl_enabled,
            storage_mode=storage_mode,
            storage_pool=storage_pool,
            system=system,
            volume_name=volume_name,
        )


class StorageOSPersistentVolumeSource(KubernetesObject):
    """Represents a StorageOS persistent volume resource."""

    __slots__ = ()

    _api_version_ = "v1"

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """
    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_ref: ObjectReference
    """ secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted. """
    volume_name: str
    """ volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. """
    volume_namespace: str
    """ volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. """

    def __init__(
        self,
        fs_type: str = None,
        read_only: bool = None,
        secret_ref: ObjectReference = None,
        volume_name: str = None,
        volume_namespace: str = None,
    ):
        super().__init__(
            fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_name=volume_name, volume_namespace=volume_namespace
        )


class VsphereVirtualDiskVolumeSource(KubernetesObject):
    """Represents a vSphere volume resource."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_path"]

    _field_names_ = {
        "storage_policy_id": "storagePolicyID",
    }
    _revfield_names_ = {
        "storagePolicyID": "storage_policy_id",
    }

    fs_type: str
    """ fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """
    storage_policy_id: str
    """ storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. """
    storage_policy_name: str
    """ storagePolicyName is the storage Policy Based Management (SPBM) profile name. """
    volume_path: str
    """ volumePath is the path that identifies vSphere volume vmdk """

    def __init__(self, fs_type: str = None, storage_policy_id: str = None, storage_policy_name: str = None, volume_path: str = None):
        super().__init__(
            fs_type=fs_type, storage_policy_id=storage_policy_id, storage_policy_name=storage_policy_name, volume_path=volume_path
        )


class PersistentVolumeSpec(KubernetesObject):
    """PersistentVolumeSpec is the specification of a persistent volume."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "scale_io": "scaleIO",
    }
    _revfield_names_ = {
        "scaleIO": "scale_io",
    }

    access_modes: list[str]
    """ accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes """
    aws_elastic_block_store: AWSElasticBlockStoreVolumeSource
    """ awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """
    azure_disk: AzureDiskVolumeSource
    """ azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. """
    azure_file: AzureFilePersistentVolumeSource
    """ azureFile represents an Azure File Service mount on the host and bind mount to the pod. """
    capacity: dict[str, Quantity]
    """ capacity is the description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity """
    cephfs: CephFSPersistentVolumeSource
    """ cephFS represents a Ceph FS mount on the host that shares a pod's lifetime """
    cinder: CinderPersistentVolumeSource
    """ cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """
    claim_ref: ObjectReference
    """ claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding """
    csi: CSIPersistentVolumeSource
    """ csi represents storage that is handled by an external CSI driver (Beta feature). """
    fc: FCVolumeSource
    """ fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod. """
    flex_volume: FlexPersistentVolumeSource
    """ flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. """
    flocker: FlockerVolumeSource
    """ flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running """
    gce_persistent_disk: GCEPersistentDiskVolumeSource
    """ gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """
    glusterfs: GlusterfsPersistentVolumeSource
    """ glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://examples.k8s.io/volumes/glusterfs/README.md """
    host_path: HostPathVolumeSource
    """ hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """
    iscsi: ISCSIPersistentVolumeSource
    """ iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. """
    local: LocalVolumeSource
    """ local represents directly-attached storage with node affinity """
    mount_options: list[str]
    """ mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options """
    nfs: NFSVolumeSource
    """ nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """
    node_affinity: VolumeNodeAffinity
    """ nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume. """
    persistent_volume_reclaim_policy: str
    """ persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming """
    photon_persistent_disk: PhotonPersistentDiskVolumeSource
    """ photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine """
    portworx_volume: PortworxVolumeSource
    """ portworxVolume represents a portworx volume attached and mounted on kubelets host machine """
    quobyte: QuobyteVolumeSource
    """ quobyte represents a Quobyte mount on the host that shares a pod's lifetime """
    rbd: RBDPersistentVolumeSource
    """ rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md """
    scale_io: ScaleIOPersistentVolumeSource
    """ scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. """
    storage_class_name: str
    """ storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass. """
    storageos: StorageOSPersistentVolumeSource
    """ storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://examples.k8s.io/volumes/storageos/README.md """
    volume_attributes_class_name: str
    """ Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is an alpha field and requires enabling VolumeAttributesClass feature. """
    volume_mode: str
    """ volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec. """
    vsphere_volume: VsphereVirtualDiskVolumeSource
    """ vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine """

    def __init__(
        self,
        access_modes: list[str] = None,
        aws_elastic_block_store: AWSElasticBlockStoreVolumeSource = None,
        azure_disk: AzureDiskVolumeSource = None,
        azure_file: AzureFilePersistentVolumeSource = None,
        capacity: dict[str, Quantity] = None,
        cephfs: CephFSPersistentVolumeSource = None,
        cinder: CinderPersistentVolumeSource = None,
        claim_ref: ObjectReference = None,
        csi: CSIPersistentVolumeSource = None,
        fc: FCVolumeSource = None,
        flex_volume: FlexPersistentVolumeSource = None,
        flocker: FlockerVolumeSource = None,
        gce_persistent_disk: GCEPersistentDiskVolumeSource = None,
        glusterfs: GlusterfsPersistentVolumeSource = None,
        host_path: HostPathVolumeSource = None,
        iscsi: ISCSIPersistentVolumeSource = None,
        local: LocalVolumeSource = None,
        mount_options: list[str] = None,
        nfs: NFSVolumeSource = None,
        node_affinity: VolumeNodeAffinity = None,
        persistent_volume_reclaim_policy: str = None,
        photon_persistent_disk: PhotonPersistentDiskVolumeSource = None,
        portworx_volume: PortworxVolumeSource = None,
        quobyte: QuobyteVolumeSource = None,
        rbd: RBDPersistentVolumeSource = None,
        scale_io: ScaleIOPersistentVolumeSource = None,
        storage_class_name: str = None,
        storageos: StorageOSPersistentVolumeSource = None,
        volume_attributes_class_name: str = None,
        volume_mode: str = None,
        vsphere_volume: VsphereVirtualDiskVolumeSource = None,
    ):
        super().__init__(
            access_modes=access_modes,
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            capacity=capacity,
            cephfs=cephfs,
            cinder=cinder,
            claim_ref=claim_ref,
            csi=csi,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            local=local,
            mount_options=mount_options,
            nfs=nfs,
            node_affinity=node_affinity,
            persistent_volume_reclaim_policy=persistent_volume_reclaim_policy,
            photon_persistent_disk=photon_persistent_disk,
            portworx_volume=portworx_volume,
            quobyte=quobyte,
            rbd=rbd,
            scale_io=scale_io,
            storage_class_name=storage_class_name,
            storageos=storageos,
            volume_attributes_class_name=volume_attributes_class_name,
            volume_mode=volume_mode,
            vsphere_volume=vsphere_volume,
        )


class PersistentVolume(KubernetesApiResource):
    """PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes"""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PersistentVolume"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: PersistentVolumeSpec
    """ spec defines a specification of a persistent volume owned by the cluster. Provisioned by an administrator. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: PersistentVolumeSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class PersistentVolumeClaim(KubernetesApiResource):
    """PersistentVolumeClaim is a user's request for and claim to a persistent volume"""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PersistentVolumeClaim"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: PersistentVolumeClaimSpec
    """ spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PersistentVolumeClaimSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PersistentVolumeClaimCondition(KubernetesObject):
    """PersistentVolumeClaimCondition contains details about state of pvc"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_probe_time: meta.Time
    """ lastProbeTime is the time we probed the condition. """
    last_transition_time: meta.Time
    """ lastTransitionTime is the time the condition transitioned from one status to another. """
    message: str
    """ message is the human-readable message indicating details about last transition. """
    reason: str
    """ reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "Resizing" that means the underlying persistent volume is being resized. """
    status: str
    type: str

    def __init__(
        self,
        last_probe_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_probe_time=last_probe_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class PersistentVolumeClaimStatus(KubernetesObject):
    """PersistentVolumeClaimStatus is the current status of a persistent volume claim."""

    __slots__ = ()

    _api_version_ = "v1"

    access_modes: list[str]
    """ accessModes contains the actual access modes the volume backing the PVC has. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 """
    allocated_resource_statuses: dict[str, str]
    """ 
    allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:
    	* Un-prefixed keys:
    		- storage - the capacity of the volume.
    	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource"
    Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.
    
    ClaimResourceStatus can be in any of following states:
    	- ControllerResizeInProgress:
    		State set when resize controller starts resizing the volume in control-plane.
    	- ControllerResizeFailed:
    		State set when resize has failed in resize controller with a terminal error.
    	- NodeResizePending:
    		State set when resize controller has finished resizing the volume but further resizing of
    		volume is needed on the node.
    	- NodeResizeInProgress:
    		State set when kubelet starts resizing the volume.
    	- NodeResizeFailed:
    		State set when resizing has failed in kubelet with a terminal error. Transient errors don't set
    		NodeResizeFailed.
    For example: if expanding a PVC for more capacity - this field can be one of the following states:
    	- pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress"
         - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress"
         - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed"
    When this field is not set, it means that no resize operation is in progress for the given PVC.
    
    A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.
    
    This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
     """
    allocated_resources: dict[str, Quantity]
    """ 
    allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either:
    	* Un-prefixed keys:
    		- storage - the capacity of the volume.
    	* Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource"
    Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.
    
    Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.
    
    A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.
    
    This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
     """
    capacity: dict[str, Quantity]
    """ capacity represents the actual resources of the underlying volume. """
    conditions: list[PersistentVolumeClaimCondition]
    """ conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'. """
    current_volume_attributes_class_name: str
    """ currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is an alpha field and requires enabling VolumeAttributesClass feature. """
    modify_volume_status: ModifyVolumeStatus
    """ ModifyVolumeStatus represents the status object of ControllerModifyVolume operation. When this is unset, there is no ModifyVolume operation being attempted. This is an alpha field and requires enabling VolumeAttributesClass feature. """
    phase: str
    """ phase represents the current phase of PersistentVolumeClaim. """

    def __init__(
        self,
        access_modes: list[str] = None,
        allocated_resource_statuses: dict[str, str] = None,
        allocated_resources: dict[str, Quantity] = None,
        capacity: dict[str, Quantity] = None,
        conditions: list[PersistentVolumeClaimCondition] = None,
        current_volume_attributes_class_name: str = None,
        modify_volume_status: ModifyVolumeStatus = None,
        phase: str = None,
    ):
        super().__init__(
            access_modes=access_modes,
            allocated_resource_statuses=allocated_resource_statuses,
            allocated_resources=allocated_resources,
            capacity=capacity,
            conditions=conditions,
            current_volume_attributes_class_name=current_volume_attributes_class_name,
            modify_volume_status=modify_volume_status,
            phase=phase,
        )


class PersistentVolumeClaimVolumeSource(KubernetesObject):
    """PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system)."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["claim_name"]

    claim_name: str
    """ claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """
    read_only: bool
    """ readOnly Will force the ReadOnly setting in VolumeMounts. Default false. """

    def __init__(self, claim_name: str = None, read_only: bool = None):
        super().__init__(claim_name=claim_name, read_only=read_only)


class PersistentVolumeStatus(KubernetesObject):
    """PersistentVolumeStatus is the current status of a persistent volume."""

    __slots__ = ()

    _api_version_ = "v1"

    last_phase_transition_time: meta.Time
    """ lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is a beta field and requires the PersistentVolumeLastPhaseTransitionTime feature to be enabled (enabled by default). """
    message: str
    """ message is a human-readable message indicating details about why the volume is in this state. """
    phase: str
    """ phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase """
    reason: str
    """ reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. """

    def __init__(self, last_phase_transition_time: meta.Time = None, message: str = None, phase: str = None, reason: str = None):
        super().__init__(last_phase_transition_time=last_phase_transition_time, message=message, phase=phase, reason=reason)


class PodDNSConfigOption(KubernetesObject):
    """PodDNSConfigOption defines DNS resolver options of a pod."""

    __slots__ = ()

    _api_version_ = "v1"

    name: str
    """ Required. """
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class PodDNSConfig(KubernetesObject):
    """PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy."""

    __slots__ = ()

    _api_version_ = "v1"

    nameservers: list[str]
    """ A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed. """
    options: list[PodDNSConfigOption]
    """ A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy. """
    searches: list[str]
    """ A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed. """

    def __init__(self, nameservers: list[str] = None, options: list[PodDNSConfigOption] = None, searches: list[str] = None):
        super().__init__(nameservers=nameservers, options=options, searches=searches)


class PodOS(KubernetesObject):
    """PodOS defines the OS parameters of a pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    """ Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class PodReadinessGate(KubernetesObject):
    """PodReadinessGate contains the reference to a pod condition"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["condition_type"]

    condition_type: str
    """ ConditionType refers to a condition in the pod's condition list with matching type. """

    def __init__(self, condition_type: str = None):
        super().__init__(condition_type=condition_type)


class PodResourceClaim(KubernetesObject):
    """PodResourceClaim references exactly one ResourceClaim through a ClaimSource. It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    """ Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. """
    source: ClaimSource
    """ Source describes where to find the ResourceClaim. """

    def __init__(self, name: str = None, source: ClaimSource = None):
        super().__init__(name=name, source=source)


class PodSchedulingGate(KubernetesObject):
    """PodSchedulingGate is associated to a Pod to guard its scheduling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    """ Name of the scheduling gate. Each scheduling gate must have a unique name field. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class Sysctl(KubernetesObject):
    """Sysctl defines a kernel parameter to be set"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name", "value"]

    name: str
    """ Name of a property to set """
    value: str
    """ Value of a property to set """

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class PodSecurityContext(KubernetesObject):
    """PodSecurityContext holds pod-level security attributes and common container settings. Some fields are also present in container.securityContext.  Field values of container.securityContext take precedence over field values of PodSecurityContext."""

    __slots__ = ()

    _api_version_ = "v1"

    app_armor_profile: AppArmorProfile
    """ appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows. """
    fs_group: int
    """ 
    A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:
    
    1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----
    
    If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.
     """
    fs_group_change_policy: str
    """ fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows. """
    run_as_group: int
    """ The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """
    run_as_non_root: bool
    """ Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. """
    run_as_user: int
    """ The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """
    se_linux_options: SELinuxOptions
    """ The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. """
    seccomp_profile: SeccompProfile
    """ The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows. """
    supplemental_groups: list[int]
    """ A list of groups applied to the first process run in each container, in addition to the container's primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows. """
    sysctls: list[Sysctl]
    """ Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. """
    windows_options: WindowsSecurityContextOptions
    """ The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. """

    def __init__(
        self,
        app_armor_profile: AppArmorProfile = None,
        fs_group: int = None,
        fs_group_change_policy: str = None,
        run_as_group: int = None,
        run_as_non_root: bool = None,
        run_as_user: int = None,
        se_linux_options: SELinuxOptions = None,
        seccomp_profile: SeccompProfile = None,
        supplemental_groups: list[int] = None,
        sysctls: list[Sysctl] = None,
        windows_options: WindowsSecurityContextOptions = None,
    ):
        super().__init__(
            app_armor_profile=app_armor_profile,
            fs_group=fs_group,
            fs_group_change_policy=fs_group_change_policy,
            run_as_group=run_as_group,
            run_as_non_root=run_as_non_root,
            run_as_user=run_as_user,
            se_linux_options=se_linux_options,
            seccomp_profile=seccomp_profile,
            supplemental_groups=supplemental_groups,
            sysctls=sysctls,
            windows_options=windows_options,
        )


class Toleration(KubernetesObject):
    """The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>."""

    __slots__ = ()

    _api_version_ = "v1"

    effect: str
    """ Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute. """
    key: str
    """ Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys. """
    operator: str
    """ Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. """
    toleration_seconds: int
    """ TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system. """
    value: str
    """ Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string. """

    def __init__(self, effect: str = None, key: str = None, operator: str = None, toleration_seconds: int = None, value: str = None):
        super().__init__(effect=effect, key=key, operator=operator, toleration_seconds=toleration_seconds, value=value)


class TopologySpreadConstraint(KubernetesObject):
    """TopologySpreadConstraint specifies how to spread matching pods among the given topology."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["max_skew", "topology_key", "when_unsatisfiable"]

    label_selector: meta.LabelSelector
    """ LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain. """
    match_label_keys: list[str]
    """ 
    MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.
    
    This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).
     """
    max_skew: int
    """ MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |  P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed. """
    min_domains: int
    """ 
    MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.
    
    For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.
     """
    node_affinity_policy: str
    """ 
    NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.
    
    If this value is nil, the behavior is equivalent to the Honor policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.
     """
    node_taints_policy: str
    """ 
    NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.
    
    If this value is nil, the behavior is equivalent to the Ignore policy. This is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature flag.
     """
    topology_key: str
    """ TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It's a required field. """
    when_unsatisfiable: str
    """ 
    WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location,
      but giving higher precedence to topologies that would help reduce the
      skew.
    A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.
     """

    def __init__(
        self,
        label_selector: meta.LabelSelector = None,
        match_label_keys: list[str] = None,
        max_skew: int = None,
        min_domains: int = None,
        node_affinity_policy: str = None,
        node_taints_policy: str = None,
        topology_key: str = None,
        when_unsatisfiable: str = None,
    ):
        super().__init__(
            label_selector=label_selector,
            match_label_keys=match_label_keys,
            max_skew=max_skew,
            min_domains=min_domains,
            node_affinity_policy=node_affinity_policy,
            node_taints_policy=node_taints_policy,
            topology_key=topology_key,
            when_unsatisfiable=when_unsatisfiable,
        )


class SecretProjection(KubernetesObject):
    """
    Adapts a secret into a projected volume.

    The contents of the target Secret's Data field will be presented in a projected volume as files using the keys in the Data field as the file names. Note that this is identical to a secret volume source without the default mode.
    """

    __slots__ = ()

    _api_version_ = "v1"

    items: list[KeyToPath]
    """ items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """
    name: str
    """ Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    optional: bool
    """ optional field specify whether the Secret or its key must be defined """

    def __init__(self, items: list[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(items=items, name=name, optional=optional)


class ServiceAccountTokenProjection(KubernetesObject):
    """ServiceAccountTokenProjection represents a projected service account token volume. This projection can be used to insert a service account token into the pods runtime filesystem for use against APIs (Kubernetes API Server or otherwise)."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    audience: str
    """ audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver. """
    expiration_seconds: int
    """ expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes. """
    path: str
    """ path is the path relative to the mount point of the file to project the token into. """

    def __init__(self, audience: str = None, expiration_seconds: int = None, path: str = None):
        super().__init__(audience=audience, expiration_seconds=expiration_seconds, path=path)


class VolumeProjection(KubernetesObject):
    """Projection that may be projected along with other supported volume types"""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "downward_api": "downwardAPI",
    }
    _revfield_names_ = {
        "downwardAPI": "downward_api",
    }

    cluster_trust_bundle: ClusterTrustBundleProjection
    """ 
    ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.
    
    Alpha, gated by the ClusterTrustBundleProjection feature gate.
    
    ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.
    
    Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.
     """
    config_map: ConfigMapProjection
    """ configMap information about the configMap data to project """
    downward_api: DownwardAPIProjection
    """ downwardAPI information about the downwardAPI data to project """
    secret: SecretProjection
    """ secret information about the secret data to project """
    service_account_token: ServiceAccountTokenProjection
    """ serviceAccountToken is information about the serviceAccountToken data to project """

    def __init__(
        self,
        cluster_trust_bundle: ClusterTrustBundleProjection = None,
        config_map: ConfigMapProjection = None,
        downward_api: DownwardAPIProjection = None,
        secret: SecretProjection = None,
        service_account_token: ServiceAccountTokenProjection = None,
    ):
        super().__init__(
            cluster_trust_bundle=cluster_trust_bundle,
            config_map=config_map,
            downward_api=downward_api,
            secret=secret,
            service_account_token=service_account_token,
        )


class ProjectedVolumeSource(KubernetesObject):
    """Represents a projected volume source"""

    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    """ defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """
    sources: list[VolumeProjection]
    """ sources is the list of volume projections """

    def __init__(self, default_mode: int = None, sources: list[VolumeProjection] = None):
        super().__init__(default_mode=default_mode, sources=sources)


class RBDVolumeSource(KubernetesObject):
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership management and SELinux relabeling."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "monitors"]

    fs_type: str
    """ fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd """
    image: str
    """ image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    keyring: str
    """ keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    monitors: list[str]
    """ monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    pool: str
    """ pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    read_only: bool
    """ readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    secret_ref: LocalObjectReference
    """ secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """
    user: str
    """ user is the rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it """

    def __init__(
        self,
        fs_type: str = None,
        image: str = None,
        keyring: str = None,
        monitors: list[str] = None,
        pool: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        user: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            image=image,
            keyring=keyring,
            monitors=monitors,
            pool=pool,
            read_only=read_only,
            secret_ref=secret_ref,
            user=user,
        )


class ScaleIOVolumeSource(KubernetesObject):
    """ScaleIOVolumeSource represents a persistent ScaleIO volume"""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["gateway", "secret_ref", "system"]

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs". """
    gateway: str
    """ gateway is the host address of the ScaleIO API Gateway. """
    protection_domain: str
    """ protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. """
    read_only: bool
    """ readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_ref: LocalObjectReference
    """ secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. """
    ssl_enabled: bool
    """ sslEnabled Flag enable/disable SSL communication with Gateway, default false """
    storage_mode: str
    """ storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. """
    storage_pool: str
    """ storagePool is the ScaleIO Storage Pool associated with the protection domain. """
    system: str
    """ system is the name of the storage system as configured in ScaleIO. """
    volume_name: str
    """ volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. """

    def __init__(
        self,
        fs_type: str = None,
        gateway: str = None,
        protection_domain: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        ssl_enabled: bool = None,
        storage_mode: str = None,
        storage_pool: str = None,
        system: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            gateway=gateway,
            protection_domain=protection_domain,
            read_only=read_only,
            secret_ref=secret_ref,
            ssl_enabled=ssl_enabled,
            storage_mode=storage_mode,
            storage_pool=storage_pool,
            system=system,
            volume_name=volume_name,
        )


class SecretVolumeSource(KubernetesObject):
    """
    Adapts a Secret into a volume.

    The contents of the target Secret's Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.
    """

    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    """ defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. """
    items: list[KeyToPath]
    """ items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. """
    optional: bool
    """ optional field specify whether the Secret or its keys must be defined """
    secret_name: str
    """ secretName is the name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret """

    def __init__(self, default_mode: int = None, items: list[KeyToPath] = None, optional: bool = None, secret_name: str = None):
        super().__init__(default_mode=default_mode, items=items, optional=optional, secret_name=secret_name)


class StorageOSVolumeSource(KubernetesObject):
    """Represents a StorageOS persistent volume resource."""

    __slots__ = ()

    _api_version_ = "v1"

    fs_type: str
    """ fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. """
    read_only: bool
    """ readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. """
    secret_ref: LocalObjectReference
    """ secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted. """
    volume_name: str
    """ volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace. """
    volume_namespace: str
    """ volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created. """

    def __init__(
        self,
        fs_type: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        volume_name: str = None,
        volume_namespace: str = None,
    ):
        super().__init__(
            fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_name=volume_name, volume_namespace=volume_namespace
        )


class Volume(KubernetesObject):
    """Volume represents a named volume in a pod that may be accessed by any container in the pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    _field_names_ = {
        "downward_api": "downwardAPI",
        "scale_io": "scaleIO",
    }
    _revfield_names_ = {
        "downwardAPI": "downward_api",
        "scaleIO": "scale_io",
    }

    aws_elastic_block_store: AWSElasticBlockStoreVolumeSource
    """ awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore """
    azure_disk: AzureDiskVolumeSource
    """ azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. """
    azure_file: AzureFileVolumeSource
    """ azureFile represents an Azure File Service mount on the host and bind mount to the pod. """
    cephfs: CephFSVolumeSource
    """ cephFS represents a Ceph FS mount on the host that shares a pod's lifetime """
    cinder: CinderVolumeSource
    """ cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md """
    config_map: ConfigMapVolumeSource
    """ configMap represents a configMap that should populate this volume """
    csi: CSIVolumeSource
    """ csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature). """
    downward_api: DownwardAPIVolumeSource
    """ downwardAPI represents downward API about the pod that should populate this volume """
    empty_dir: EmptyDirVolumeSource
    """ emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir """
    ephemeral: EphemeralVolumeSource
    """ 
    ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.
    
    Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity
       tracking are needed,
    c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through
       a PersistentVolumeClaim (see EphemeralVolumeSource for more
       information on the connection between this volume type
       and PersistentVolumeClaim).
    
    Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.
    
    Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.
    
    A pod can use both types of ephemeral volumes and persistent volumes at the same time.
     """
    fc: FCVolumeSource
    """ fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod. """
    flex_volume: FlexVolumeSource
    """ flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. """
    flocker: FlockerVolumeSource
    """ flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running """
    gce_persistent_disk: GCEPersistentDiskVolumeSource
    """ gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk """
    git_repo: GitRepoVolumeSource
    """ gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container. """
    glusterfs: GlusterfsVolumeSource
    """ glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md """
    host_path: HostPathVolumeSource
    """ hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath """
    iscsi: ISCSIVolumeSource
    """ iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md """
    name: str
    """ name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """
    nfs: NFSVolumeSource
    """ nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs """
    persistent_volume_claim: PersistentVolumeClaimVolumeSource
    """ persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims """
    photon_persistent_disk: PhotonPersistentDiskVolumeSource
    """ photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine """
    portworx_volume: PortworxVolumeSource
    """ portworxVolume represents a portworx volume attached and mounted on kubelets host machine """
    projected: ProjectedVolumeSource
    """ projected items for all in one resources secrets, configmaps, and downward API """
    quobyte: QuobyteVolumeSource
    """ quobyte represents a Quobyte mount on the host that shares a pod's lifetime """
    rbd: RBDVolumeSource
    """ rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md """
    scale_io: ScaleIOVolumeSource
    """ scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. """
    secret: SecretVolumeSource
    """ secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret """
    storageos: StorageOSVolumeSource
    """ storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. """
    vsphere_volume: VsphereVirtualDiskVolumeSource
    """ vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine """

    def __init__(
        self,
        aws_elastic_block_store: AWSElasticBlockStoreVolumeSource = None,
        azure_disk: AzureDiskVolumeSource = None,
        azure_file: AzureFileVolumeSource = None,
        cephfs: CephFSVolumeSource = None,
        cinder: CinderVolumeSource = None,
        config_map: ConfigMapVolumeSource = None,
        csi: CSIVolumeSource = None,
        downward_api: DownwardAPIVolumeSource = None,
        empty_dir: EmptyDirVolumeSource = None,
        ephemeral: EphemeralVolumeSource = None,
        fc: FCVolumeSource = None,
        flex_volume: FlexVolumeSource = None,
        flocker: FlockerVolumeSource = None,
        gce_persistent_disk: GCEPersistentDiskVolumeSource = None,
        git_repo: GitRepoVolumeSource = None,
        glusterfs: GlusterfsVolumeSource = None,
        host_path: HostPathVolumeSource = None,
        iscsi: ISCSIVolumeSource = None,
        name: str = None,
        nfs: NFSVolumeSource = None,
        persistent_volume_claim: PersistentVolumeClaimVolumeSource = None,
        photon_persistent_disk: PhotonPersistentDiskVolumeSource = None,
        portworx_volume: PortworxVolumeSource = None,
        projected: ProjectedVolumeSource = None,
        quobyte: QuobyteVolumeSource = None,
        rbd: RBDVolumeSource = None,
        scale_io: ScaleIOVolumeSource = None,
        secret: SecretVolumeSource = None,
        storageos: StorageOSVolumeSource = None,
        vsphere_volume: VsphereVirtualDiskVolumeSource = None,
    ):
        super().__init__(
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            cephfs=cephfs,
            cinder=cinder,
            config_map=config_map,
            csi=csi,
            downward_api=downward_api,
            empty_dir=empty_dir,
            ephemeral=ephemeral,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            git_repo=git_repo,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            name=name,
            nfs=nfs,
            persistent_volume_claim=persistent_volume_claim,
            photon_persistent_disk=photon_persistent_disk,
            portworx_volume=portworx_volume,
            projected=projected,
            quobyte=quobyte,
            rbd=rbd,
            scale_io=scale_io,
            secret=secret,
            storageos=storageos,
            vsphere_volume=vsphere_volume,
        )


class PodSpec(KubernetesObject):
    """PodSpec is a description of a pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["containers"]

    _field_names_ = {
        "host_ipc": "hostIPC",
        "host_pid": "hostPID",
        "set_hostname_as_fqdn": "setHostnameAsFQDN",
    }
    _revfield_names_ = {
        "hostIPC": "host_ipc",
        "hostPID": "host_pid",
        "setHostnameAsFQDN": "set_hostname_as_fqdn",
    }

    active_deadline_seconds: int
    """ Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer. """
    affinity: Affinity
    """ If specified, the pod's scheduling constraints """
    automount_service_account_token: bool
    """ AutomountServiceAccountToken indicates whether a service account token should be automatically mounted. """
    containers: list[Container]
    """ List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. """
    dns_config: PodDNSConfig
    """ Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy. """
    dns_policy: str
    """ Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'. """
    enable_service_links: bool
    """ EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true. """
    ephemeral_containers: list[EphemeralContainer]
    """ List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. """
    host_aliases: list[HostAlias]
    """ HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. """
    host_ipc: bool
    """ Use the host's ipc namespace. Optional: Default to false. """
    host_network: bool
    """ Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false. """
    host_pid: bool
    """ Use the host's pid namespace. Optional: Default to false. """
    host_users: bool
    """ Use the host's user namespace. Optional: Default to true. If set to true or not present, the pod will be run in the host user namespace, useful for when the pod needs a feature only available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When set to false, a new userns is created for the pod. Setting false is useful for mitigating container breakout vulnerabilities even allowing users to run their containers as root without actually having root privileges on the host. This field is alpha-level and is only honored by servers that enable the UserNamespacesSupport feature. """
    hostname: str
    """ Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value. """
    image_pull_secrets: list[LocalObjectReference]
    """ ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod """
    init_containers: list[Container]
    """ List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ """
    node_name: str
    """ NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements. """
    node_selector: dict[str, str]
    """ NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ """
    os: PodOS
    """ 
    Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.
    
    If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions
    
    If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.containers[*].securityContext.appArmorProfile - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup
     """
    overhead: dict[str, Quantity]
    """ Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md """
    preemption_policy: str
    """ PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. """
    priority: int
    """ The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. """
    priority_class_name: str
    """ If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default. """
    readiness_gates: list[PodReadinessGate]
    """ If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates """
    resource_claims: list[PodResourceClaim]
    """ 
    ResourceClaims defines which ResourceClaims must be allocated and reserved before the Pod is allowed to start. The resources will be made available to those containers which consume them by name.
    
    This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.
    
    This field is immutable.
     """
    restart_policy: str
    """ Restart policy for all containers within the pod. One of Always, OnFailure, Never. In some contexts, only a subset of those values may be permitted. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy """
    runtime_class_name: str
    """ RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class """
    scheduler_name: str
    """ If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler. """
    scheduling_gates: list[PodSchedulingGate]
    """ 
    SchedulingGates is an opaque list of values that if specified will block scheduling the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the scheduler will not attempt to schedule the pod.
    
    SchedulingGates can only be set at pod creation time, and be removed only afterwards.
     """
    security_context: PodSecurityContext
    """ SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field. """
    service_account: str
    """ DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead. """
    service_account_name: str
    """ ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ """
    set_hostname_as_fqdn: bool
    """ If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false. """
    share_process_namespace: bool
    """ Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. """
    subdomain: str
    """ If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all. """
    termination_grace_period_seconds: int
    """ Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds. """
    tolerations: list[Toleration]
    """ If specified, the pod's tolerations. """
    topology_spread_constraints: list[TopologySpreadConstraint]
    """ TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed. """
    volumes: list[Volume]
    """ List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes """

    def __init__(
        self,
        active_deadline_seconds: int = None,
        affinity: Affinity = None,
        automount_service_account_token: bool = None,
        containers: list[Container] = None,
        dns_config: PodDNSConfig = None,
        dns_policy: str = None,
        enable_service_links: bool = None,
        ephemeral_containers: list[EphemeralContainer] = None,
        host_aliases: list[HostAlias] = None,
        host_ipc: bool = None,
        host_network: bool = None,
        host_pid: bool = None,
        host_users: bool = None,
        hostname: str = None,
        image_pull_secrets: list[LocalObjectReference] = None,
        init_containers: list[Container] = None,
        node_name: str = None,
        node_selector: dict[str, str] = None,
        os: PodOS = None,
        overhead: dict[str, Quantity] = None,
        preemption_policy: str = None,
        priority: int = None,
        priority_class_name: str = None,
        readiness_gates: list[PodReadinessGate] = None,
        resource_claims: list[PodResourceClaim] = None,
        restart_policy: str = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        scheduling_gates: list[PodSchedulingGate] = None,
        security_context: PodSecurityContext = None,
        service_account: str = None,
        service_account_name: str = None,
        set_hostname_as_fqdn: bool = None,
        share_process_namespace: bool = None,
        subdomain: str = None,
        termination_grace_period_seconds: int = None,
        tolerations: list[Toleration] = None,
        topology_spread_constraints: list[TopologySpreadConstraint] = None,
        volumes: list[Volume] = None,
    ):
        super().__init__(
            active_deadline_seconds=active_deadline_seconds,
            affinity=affinity,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns_config=dns_config,
            dns_policy=dns_policy,
            enable_service_links=enable_service_links,
            ephemeral_containers=ephemeral_containers,
            host_aliases=host_aliases,
            host_ipc=host_ipc,
            host_network=host_network,
            host_pid=host_pid,
            host_users=host_users,
            hostname=hostname,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            node_name=node_name,
            node_selector=node_selector,
            os=os,
            overhead=overhead,
            preemption_policy=preemption_policy,
            priority=priority,
            priority_class_name=priority_class_name,
            readiness_gates=readiness_gates,
            resource_claims=resource_claims,
            restart_policy=restart_policy,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            scheduling_gates=scheduling_gates,
            security_context=security_context,
            service_account=service_account,
            service_account_name=service_account_name,
            set_hostname_as_fqdn=set_hostname_as_fqdn,
            share_process_namespace=share_process_namespace,
            subdomain=subdomain,
            termination_grace_period_seconds=termination_grace_period_seconds,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            volumes=volumes,
        )


class Pod(KubernetesApiResource):
    """Pod is a collection of containers that can run on a host. This resource is created by clients and scheduled onto hosts."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Pod"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: PodSpec
    """ Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PodCondition(KubernetesObject):
    """PodCondition contains details for the current condition of this pod."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_probe_time: meta.Time
    """ Last time we probed the condition. """
    last_transition_time: meta.Time
    """ Last time the condition transitioned from one status to another. """
    message: str
    """ Human-readable message indicating details about last transition. """
    reason: str
    """ Unique, one-word, CamelCase reason for the condition's last transition. """
    status: str
    """ Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """
    type: str
    """ Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """

    def __init__(
        self,
        last_probe_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_probe_time=last_probe_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class PodIP(KubernetesObject):
    """PodIP represents a single IP address allocated to the pod."""

    __slots__ = ()

    _api_version_ = "v1"

    ip: str
    """ IP is the IP address assigned to the pod """

    def __init__(self, ip: str = None):
        super().__init__(ip=ip)


class PodResourceClaimStatus(KubernetesObject):
    """PodResourceClaimStatus is stored in the PodStatus for each PodResourceClaim which references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    """ Name uniquely identifies this resource claim inside the pod. This must match the name of an entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL. """
    resource_claim_name: str
    """ ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. It this is unset, then generating a ResourceClaim was not necessary. The pod.spec.resourceClaims entry can be ignored in this case. """

    def __init__(self, name: str = None, resource_claim_name: str = None):
        super().__init__(name=name, resource_claim_name=resource_claim_name)


class PodStatus(KubernetesObject):
    """PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "host_ip": "hostIP",
        "host_ips": "hostIPs",
        "pod_ip": "podIP",
        "pod_ips": "podIPs",
    }
    _revfield_names_ = {
        "hostIP": "host_ip",
        "hostIPs": "host_ips",
        "podIP": "pod_ip",
        "podIPs": "pod_ips",
    }

    conditions: list[PodCondition]
    """ Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions """
    container_statuses: list[ContainerStatus]
    """ The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status """
    ephemeral_container_statuses: list[ContainerStatus]
    """ Status for any ephemeral containers that have run in this pod. """
    host_ip: str
    """ hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod """
    host_ips: list[HostIP]
    """ hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod. """
    init_container_statuses: list[ContainerStatus]
    """ The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status """
    message: str
    """ A human readable message indicating details about why the pod is in this condition. """
    nominated_node_name: str
    """ nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled. """
    phase: str
    """ 
    The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:
    
    Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.
    
    More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase
     """
    pod_ip: str
    """ podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated. """
    pod_ips: list[PodIP]
    """ podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet. """
    qos_class: str
    """ The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes """
    reason: str
    """ A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted' """
    resize: str
    """ Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to "Proposed" """
    resource_claim_statuses: list[PodResourceClaimStatus]
    """ Status of resource claims. """
    start_time: meta.Time
    """ RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod. """

    def __init__(
        self,
        conditions: list[PodCondition] = None,
        container_statuses: list[ContainerStatus] = None,
        ephemeral_container_statuses: list[ContainerStatus] = None,
        host_ip: str = None,
        host_ips: list[HostIP] = None,
        init_container_statuses: list[ContainerStatus] = None,
        message: str = None,
        nominated_node_name: str = None,
        phase: str = None,
        pod_ip: str = None,
        pod_ips: list[PodIP] = None,
        qos_class: str = None,
        reason: str = None,
        resize: str = None,
        resource_claim_statuses: list[PodResourceClaimStatus] = None,
        start_time: meta.Time = None,
    ):
        super().__init__(
            conditions=conditions,
            container_statuses=container_statuses,
            ephemeral_container_statuses=ephemeral_container_statuses,
            host_ip=host_ip,
            host_ips=host_ips,
            init_container_statuses=init_container_statuses,
            message=message,
            nominated_node_name=nominated_node_name,
            phase=phase,
            pod_ip=pod_ip,
            pod_ips=pod_ips,
            qos_class=qos_class,
            reason=reason,
            resize=resize,
            resource_claim_statuses=resource_claim_statuses,
            start_time=start_time,
        )


class PodTemplateSpec(KubernetesObject):
    """PodTemplateSpec describes the data a pod should have when created from a template"""

    __slots__ = ()

    _api_version_ = "v1"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: PodSpec
    """ Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, metadata: meta.ObjectMeta = None, spec: PodSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class PodTemplate(KubernetesApiResource):
    """PodTemplate describes a template for creating copies of a predefined pod."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PodTemplate"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    template: PodTemplateSpec
    """ Template defines the pods that will be created from this pod template. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, template: PodTemplateSpec = None):
        super().__init__(name, namespace, metadata=metadata, template=template)


RawExtension: t.TypeAlias = dict[str, t.Any]
""" 
RawExtension is used to hold extensions in external versions.

To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.

// Internal package:

	type MyAPIObject struct {
		runtime.TypeMeta `json:",inline"`
		MyPlugin runtime.Object `json:"myPlugin"`
	}

	type PluginA struct {
		AOption string `json:"aOption"`
	}

// External package:

	type MyAPIObject struct {
		runtime.TypeMeta `json:",inline"`
		MyPlugin runtime.RawExtension `json:"myPlugin"`
	}

	type PluginA struct {
		AOption string `json:"aOption"`
	}

// On the wire, the JSON will look something like this:

	{
		"kind":"MyAPIObject",
		"apiVersion":"v1",
		"myPlugin": {
			"kind":"PluginA",
			"aOption":"foo",
		},
	}

So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package's DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)
 """


class ReplicationControllerSpec(KubernetesObject):
    """ReplicationControllerSpec is the specification of a replication controller."""

    __slots__ = ()

    _api_version_ = "v1"

    min_ready_seconds: int
    """ Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """
    replicas: int
    """ Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller """
    selector: dict[str, str]
    """ Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """
    template: PodTemplateSpec
    """ Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """

    def __init__(
        self, min_ready_seconds: int = None, replicas: int = None, selector: dict[str, str] = None, template: PodTemplateSpec = None
    ):
        super().__init__(min_ready_seconds=min_ready_seconds, replicas=replicas, selector=selector, template=template)


class ReplicationController(KubernetesApiResource):
    """ReplicationController represents the configuration of a replication controller."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ReplicationController"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: ReplicationControllerSpec
    """ Spec defines the specification of the desired behavior of the replication controller. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ReplicationControllerSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ReplicationControllerCondition(KubernetesObject):
    """ReplicationControllerCondition describes the state of a replication controller at a certain point."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ The last time the condition transitioned from one status to another. """
    message: str
    """ A human readable message indicating details about the transition. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of replication controller condition. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class ReplicationControllerStatus(KubernetesObject):
    """ReplicationControllerStatus represents the current status of a replication controller."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["replicas"]

    available_replicas: int
    """ The number of available replicas (ready for at least minReadySeconds) for this replication controller. """
    conditions: list[ReplicationControllerCondition]
    """ Represents the latest available observations of a replication controller's current state. """
    fully_labeled_replicas: int
    """ The number of pods that have labels matching the labels of the pod template of the replication controller. """
    observed_generation: int
    """ ObservedGeneration reflects the generation of the most recently observed replication controller. """
    ready_replicas: int
    """ The number of ready replicas for this replication controller. """
    replicas: int
    """ Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller """

    def __init__(
        self,
        available_replicas: int = None,
        conditions: list[ReplicationControllerCondition] = None,
        fully_labeled_replicas: int = None,
        observed_generation: int = None,
        ready_replicas: int = None,
        replicas: int = None,
    ):
        super().__init__(
            available_replicas=available_replicas,
            conditions=conditions,
            fully_labeled_replicas=fully_labeled_replicas,
            observed_generation=observed_generation,
            ready_replicas=ready_replicas,
            replicas=replicas,
        )


class ScopedResourceSelectorRequirement(KubernetesObject):
    """A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["operator", "scope_name"]

    operator: str
    """ Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. """
    scope_name: str
    """ The name of the scope that the selector applies to. """
    values: list[str]
    """ An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. """

    def __init__(self, operator: str = None, scope_name: str = None, values: list[str] = None):
        super().__init__(operator=operator, scope_name=scope_name, values=values)


class ScopeSelector(KubernetesObject):
    """A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements."""

    __slots__ = ()

    _api_version_ = "v1"

    match_expressions: list[ScopedResourceSelectorRequirement]
    """ A list of scope selector requirements by scope of the resources. """

    def __init__(self, match_expressions: list[ScopedResourceSelectorRequirement] = None):
        super().__init__(match_expressions=match_expressions)


class ResourceQuotaSpec(KubernetesObject):
    """ResourceQuotaSpec defines the desired hard limits to enforce for Quota."""

    __slots__ = ()

    _api_version_ = "v1"

    hard: dict[str, Quantity]
    """ hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """
    scope_selector: ScopeSelector
    """ scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. """
    scopes: list[str]
    """ A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. """

    def __init__(self, hard: dict[str, Quantity] = None, scope_selector: ScopeSelector = None, scopes: list[str] = None):
        super().__init__(hard=hard, scope_selector=scope_selector, scopes=scopes)


class ResourceQuota(KubernetesApiResource):
    """ResourceQuota sets aggregate quota restrictions enforced per namespace"""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ResourceQuota"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: ResourceQuotaSpec
    """ Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceQuotaSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceQuotaStatus(KubernetesObject):
    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    __slots__ = ()

    _api_version_ = "v1"

    hard: dict[str, Quantity]
    """ Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ """
    used: dict[str, Quantity]
    """ Used is the current observed total usage of the resource in the namespace. """

    def __init__(self, hard: dict[str, Quantity] = None, used: dict[str, Quantity] = None):
        super().__init__(hard=hard, used=used)


class Secret(KubernetesApiResource):
    """Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Secret"
    _scope_ = "namespace"

    data: dict[str, Base64]
    """ Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4 """
    immutable: bool
    """ Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    string_data: dict[str, str]
    """ stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. """
    type: str
    """ Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        data: dict[str, Base64] = None,
        immutable: bool = None,
        metadata: meta.ObjectMeta = None,
        string_data: dict[str, str] = None,
        type: str = None,
    ):
        super().__init__(name, namespace, data=data, immutable=immutable, metadata=metadata, string_data=string_data, type=type)


class ServicePort(KubernetesObject):
    """ServicePort contains information on service's port."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    app_protocol: str
    """ 
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:
    
    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).
    
    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455
    
    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
     """
    name: str
    """ The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. When considering the endpoints for a Service, this must match the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service. """
    node_port: int
    """ The port on each node on which this service is exposed when type is NodePort or LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if this Service requires one.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type from NodePort to ClusterIP). More info: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport """
    port: int
    """ The port that will be exposed by this service. """
    protocol: str
    """ The IP protocol for this port. Supports "TCP", "UDP", and "SCTP". Default is TCP. """
    target_port: IntOrString
    """ Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service """

    def __init__(
        self,
        app_protocol: str = None,
        name: str = None,
        node_port: int = None,
        port: int = None,
        protocol: str = None,
        target_port: IntOrString = None,
    ):
        super().__init__(app_protocol=app_protocol, name=name, node_port=node_port, port=port, protocol=protocol, target_port=target_port)


class SessionAffinityConfig(KubernetesObject):
    """SessionAffinityConfig represents the configurations of session affinity."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "client_ip": "clientIP",
    }
    _revfield_names_ = {
        "clientIP": "client_ip",
    }

    client_ip: ClientIPConfig
    """ clientIP contains the configurations of Client IP based session affinity. """

    def __init__(self, client_ip: ClientIPConfig = None):
        super().__init__(client_ip=client_ip)


class ServiceSpec(KubernetesObject):
    """ServiceSpec describes the attributes that a user creates on a service."""

    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "cluster_ip": "clusterIP",
        "cluster_ips": "clusterIPs",
        "external_ips": "externalIPs",
        "load_balancer_ip": "loadBalancerIP",
    }
    _revfield_names_ = {
        "clusterIP": "cluster_ip",
        "clusterIPs": "cluster_ips",
        "externalIPs": "external_ips",
        "loadBalancerIP": "load_balancer_ip",
    }

    allocate_load_balancer_node_ports: bool
    """ allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is "true". It may be set to "false" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type. """
    cluster_ip: str
    """ clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address. Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """
    cluster_ips: list[str]
    """ 
    ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address.  Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.
    
    This field may hold a maximum of two entries (dual-stack IPs, in either order). These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies
     """
    external_ips: list[str]
    """ externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system. """
    external_name: str
    """ externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be "ExternalName". """
    external_traffic_policy: str
    """ externalTrafficPolicy describes how nodes distribute service traffic they receive on one of the Service's "externally-facing" addresses (NodePorts, ExternalIPs, and LoadBalancer IPs). If set to "Local", the proxy will configure the service in a way that assumes that external load balancers will take care of balancing the service traffic between nodes, and so each node will deliver traffic only to the node-local endpoints of the service, without masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be dropped.) The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). Note that traffic sent to an External IP or LoadBalancer IP from within the cluster will always get "Cluster" semantics, but clients sending to a NodePort from within the cluster may need to take traffic policy into account when picking a node. """
    health_check_node_port: int
    """ healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type). This field cannot be updated once set. """
    internal_traffic_policy: str
    """ InternalTrafficPolicy describes how nodes distribute service traffic they receive on the ClusterIP. If set to "Local", the proxy will assume that pods only want to talk to endpoints of the service on the same node as the pod, dropping the traffic if there are no local endpoints. The default value, "Cluster", uses the standard behavior of routing to all endpoints evenly (possibly modified by topology and other features). """
    ip_families: list[str]
    """ 
    IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service. Valid values are "IPv4" and "IPv6".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to "headless" services. This field will be wiped when updating a Service to type ExternalName.
    
    This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field.
     """
    ip_family_policy: str
    """ IPFamilyPolicy represents the dual-stack-ness requested or required by this Service. If there is no value provided, then this field will be set to SingleStack. Services can be "SingleStack" (a single IP family), "PreferDualStack" (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or "RequireDualStack" (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field. This field will be wiped when updating a service to type ExternalName. """
    load_balancer_class: str
    """ loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. "internal-vip" or "example.com/internal-vip". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type. """
    load_balancer_ip: str
    """ Only applies to Service Type: LoadBalancer. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature. Deprecated: This field was under-specified and its meaning varies across implementations. Using it is non-portable and it may not support dual-stack. Users are encouraged to use implementation-specific annotations when available. """
    load_balancer_source_ranges: list[str]
    """ If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/ """
    ports: list[ServicePort]
    """ The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """
    publish_not_ready_addresses: bool
    """ publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered "ready" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior. """
    selector: dict[str, str]
    """ Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/ """
    session_affinity: str
    """ Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies """
    session_affinity_config: SessionAffinityConfig
    """ sessionAffinityConfig contains the configurations of session affinity. """
    traffic_distribution: str
    """ TrafficDistribution offers a way to express preferences for how traffic is distributed to Service endpoints. Implementations can use this field as a hint, but are not required to guarantee strict adherence. If the field is not set, the implementation will apply its default routing strategy. If set to "PreferClose", implementations should prioritize endpoints that are topologically close (e.g., same zone). This is an alpha field and requires enabling ServiceTrafficDistribution feature. """
    type: str
    """ type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. "ExternalName" aliases this service to the specified externalName. Several other fields do not apply to ExternalName services. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types """

    def __init__(
        self,
        allocate_load_balancer_node_ports: bool = None,
        cluster_ip: str = None,
        cluster_ips: list[str] = None,
        external_ips: list[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        internal_traffic_policy: str = None,
        ip_families: list[str] = None,
        ip_family_policy: str = None,
        load_balancer_class: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: list[str] = None,
        ports: list[ServicePort] = None,
        publish_not_ready_addresses: bool = None,
        selector: dict[str, str] = None,
        session_affinity: str = None,
        session_affinity_config: SessionAffinityConfig = None,
        traffic_distribution: str = None,
        type: str = None,
    ):
        super().__init__(
            allocate_load_balancer_node_ports=allocate_load_balancer_node_ports,
            cluster_ip=cluster_ip,
            cluster_ips=cluster_ips,
            external_ips=external_ips,
            external_name=external_name,
            external_traffic_policy=external_traffic_policy,
            health_check_node_port=health_check_node_port,
            internal_traffic_policy=internal_traffic_policy,
            ip_families=ip_families,
            ip_family_policy=ip_family_policy,
            load_balancer_class=load_balancer_class,
            load_balancer_ip=load_balancer_ip,
            load_balancer_source_ranges=load_balancer_source_ranges,
            ports=ports,
            publish_not_ready_addresses=publish_not_ready_addresses,
            selector=selector,
            session_affinity=session_affinity,
            session_affinity_config=session_affinity_config,
            traffic_distribution=traffic_distribution,
            type=type,
        )


class Service(KubernetesApiResource):
    """Service is a named abstraction of software service (for example, mysql) consisting of local port (for example 3306) that the proxy listens on, and the selector that determines which pods will answer requests sent through the proxy."""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Service"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: ServiceSpec
    """ Spec defines the behavior of a service. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ServiceSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ServiceAccount(KubernetesApiResource):
    """ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral systems, for an identity * a principal that can be authenticated and authorized * a set of secrets"""

    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ServiceAccount"
    _scope_ = "namespace"

    automount_service_account_token: bool
    """ AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level. """
    image_pull_secrets: list[LocalObjectReference]
    """ ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    secrets: list[ObjectReference]
    """ Secrets is a list of the secrets in the same namespace that pods running using this ServiceAccount are allowed to use. Pods are only limited to this list if this service account has a "kubernetes.io/enforce-mountable-secrets" annotation set to "true". This field should not be used to find auto-generated service account token secrets for use outside of pods. Instead, tokens can be requested directly using the TokenRequest API, or service account token secrets can be manually created. More info: https://kubernetes.io/docs/concepts/configuration/secret """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        automount_service_account_token: bool = None,
        image_pull_secrets: list[LocalObjectReference] = None,
        metadata: meta.ObjectMeta = None,
        secrets: list[ObjectReference] = None,
    ):
        super().__init__(
            name,
            namespace,
            automount_service_account_token=automount_service_account_token,
            image_pull_secrets=image_pull_secrets,
            metadata=metadata,
            secrets=secrets,
        )


class ServiceStatus(KubernetesObject):
    """ServiceStatus represents the current status of a service."""

    __slots__ = ()

    _api_version_ = "v1"

    conditions: list[meta.Condition]
    """ Current service state """
    load_balancer: LoadBalancerStatus
    """ LoadBalancer contains the current status of the load-balancer, if one is present. """

    def __init__(self, conditions: list[meta.Condition] = None, load_balancer: LoadBalancerStatus = None):
        super().__init__(conditions=conditions, load_balancer=load_balancer)


class TopologySelectorLabelRequirement(KubernetesObject):
    """A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future."""

    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "values"]

    key: str
    """ The label key that the selector applies to. """
    values: list[str]
    """ An array of string values. One value must match the label to be selected. Each entry in Values is ORed. """

    def __init__(self, key: str = None, values: list[str] = None):
        super().__init__(key=key, values=values)


class TopologySelectorTerm(KubernetesObject):
    """A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future."""

    __slots__ = ()

    _api_version_ = "v1"

    match_label_expressions: list[TopologySelectorLabelRequirement]
    """ A list of topology selector requirements by labels. """

    def __init__(self, match_label_expressions: list[TopologySelectorLabelRequirement] = None):
        super().__init__(match_label_expressions=match_label_expressions)
