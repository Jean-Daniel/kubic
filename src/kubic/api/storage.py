from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta



class TokenRequest(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    _required_ = ["audience"]

    audience: str
    expiration_seconds: int

    def __init__(self, audience: str = None, expiration_seconds: int = None):
        super().__init__(audience=audience, expiration_seconds=expiration_seconds)


class CSIDriverSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    attach_required: bool
    fs_group_policy: str
    pod_info_on_mount: bool
    requires_republish: bool
    se_linux_mount: bool
    storage_capacity: bool
    token_requests: list[TokenRequest]
    volume_lifecycle_modes: list[str]

    def __init__(self, attach_required: bool = None, fs_group_policy: str = None, pod_info_on_mount: bool = None, requires_republish: bool = None, se_linux_mount: bool = None, storage_capacity: bool = None, token_requests: list[TokenRequest] = None, volume_lifecycle_modes: list[str] = None):
        super().__init__(attach_required=attach_required, fs_group_policy=fs_group_policy, pod_info_on_mount=pod_info_on_mount, requires_republish=requires_republish, se_linux_mount=se_linux_mount, storage_capacity=storage_capacity, token_requests=token_requests, volume_lifecycle_modes=volume_lifecycle_modes)


class CSIDriver(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "CSIDriver"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CSIDriverSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CSIDriverSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CSIDriverList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "CSIDriverList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[CSIDriver]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[CSIDriver] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class VolumeNodeResources(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    count: int

    def __init__(self, count: int = None):
        super().__init__(count=count)


class CSINodeDriver(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    _required_ = ["name", "node_id"]

    _field_names_ = {
        "node_id": "nodeID",
    }
    _revfield_names_ = {
        "nodeID": "node_id",
    }

    allocatable: VolumeNodeResources
    name: str
    node_id: str
    topology_keys: list[str]

    def __init__(self, allocatable: VolumeNodeResources = None, name: str = None, node_id: str = None, topology_keys: list[str] = None):
        super().__init__(allocatable=allocatable, name=name, node_id=node_id, topology_keys=topology_keys)


class CSINodeSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    _required_ = ["drivers"]

    drivers: list[CSINodeDriver]

    def __init__(self, drivers: list[CSINodeDriver] = None):
        super().__init__(drivers=drivers)


class CSINode(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "CSINode"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CSINodeSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CSINodeSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CSINodeList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "CSINodeList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[CSINode]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[CSINode] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class CSIStorageCapacity(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "CSIStorageCapacity"
    _scope_ = "namespace"

    _required_ = ["storage_class_name"]

    capacity: core.Quantity
    maximum_volume_size: core.Quantity
    metadata: meta.ObjectMeta
    node_topology: meta.LabelSelector
    storage_class_name: str

    def __init__(self, name: str, namespace: str = None, capacity: core.Quantity = None, maximum_volume_size: core.Quantity = None, metadata: meta.ObjectMeta = None, node_topology: meta.LabelSelector = None, storage_class_name: str = None):
        super().__init__(name, namespace, capacity=capacity, maximum_volume_size=maximum_volume_size, metadata=metadata, node_topology=node_topology, storage_class_name=storage_class_name)


class CSIStorageCapacityList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "CSIStorageCapacityList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[CSIStorageCapacity]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[CSIStorageCapacity] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class StorageClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "StorageClass"
    _scope_ = "cluster"

    _required_ = ["provisioner"]

    allow_volume_expansion: bool
    allowed_topologies: list[core.TopologySelectorTerm]
    metadata: meta.ObjectMeta
    mount_options: list[str]
    parameters: dict[str, str]
    provisioner: str
    reclaim_policy: str
    volume_binding_mode: str

    def __init__(self, name: str, allow_volume_expansion: bool = None, allowed_topologies: list[core.TopologySelectorTerm] = None, metadata: meta.ObjectMeta = None, mount_options: list[str] = None, parameters: dict[str, str] = None, provisioner: str = None, reclaim_policy: str = None, volume_binding_mode: str = None):
        super().__init__(name, "", allow_volume_expansion=allow_volume_expansion, allowed_topologies=allowed_topologies, metadata=metadata, mount_options=mount_options, parameters=parameters, provisioner=provisioner, reclaim_policy=reclaim_policy, volume_binding_mode=volume_binding_mode)


class StorageClassList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "StorageClassList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[StorageClass]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[StorageClass] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class VolumeAttachmentSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    inline_volume_spec: core.PersistentVolumeSpec
    persistent_volume_name: str

    def __init__(self, inline_volume_spec: core.PersistentVolumeSpec = None, persistent_volume_name: str = None):
        super().__init__(inline_volume_spec=inline_volume_spec, persistent_volume_name=persistent_volume_name)


class VolumeAttachmentSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    _required_ = ["attacher", "node_name", "source"]

    attacher: str
    node_name: str
    source: VolumeAttachmentSource

    def __init__(self, attacher: str = None, node_name: str = None, source: VolumeAttachmentSource = None):
        super().__init__(attacher=attacher, node_name=node_name, source=source)


class VolumeAttachment(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "VolumeAttachment"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VolumeAttachmentSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: VolumeAttachmentSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class VolumeAttachmentList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _api_group_ = "storage.k8s.io"
    _kind_ = "VolumeAttachmentList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[VolumeAttachment]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[VolumeAttachment] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class VolumeError(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    message: str
    time: meta.Time

    def __init__(self, message: str = None, time: meta.Time = None):
        super().__init__(message=message, time=time)


class VolumeAttachmentStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"

    _required_ = ["attached"]

    attach_error: VolumeError
    attached: bool
    attachment_metadata: dict[str, str]
    detach_error: VolumeError

    def __init__(self, attach_error: VolumeError = None, attached: bool = None, attachment_metadata: dict[str, str] = None, detach_error: VolumeError = None):
        super().__init__(attach_error=attach_error, attached=attached, attachment_metadata=attachment_metadata, detach_error=detach_error)


