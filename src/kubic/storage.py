from typing import Dict, List

from . import KubernetesApiResource, KubernetesObject
from . import core, meta


class StorageClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storage.k8s.io/v1"
    _kind_ = "StorageClass"
    _scope_ = "cluster"

    _required_ = ["provisioner"]

    allow_volume_expansion: bool
    allowed_topologies: List[core.TopologySelectorTerm]
    metadata: meta.ObjectMeta
    mount_options: List[str]
    parameters: Dict[str, str]
    provisioner: str
    reclaim_policy: str
    volume_binding_mode: str

    def __init__(
        self,
        name: str,
        allow_volume_expansion: bool = None,
        allowed_topologies: List[core.TopologySelectorTerm] = None,
        metadata: meta.ObjectMeta = None,
        mount_options: List[str] = None,
        parameters: Dict[str, str] = None,
        provisioner: str = None,
        reclaim_policy: str = None,
        volume_binding_mode: str = None,
    ):
        super().__init__(
            "storage.k8s.io/v1",
            "StorageClass",
            name,
            "",
            allow_volume_expansion=allow_volume_expansion,
            allowed_topologies=allowed_topologies,
            metadata=metadata,
            mount_options=mount_options,
            parameters=parameters,
            provisioner=provisioner,
            reclaim_policy=reclaim_policy,
            volume_binding_mode=volume_binding_mode,
        )


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
    _kind_ = "VolumeAttachment"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VolumeAttachmentSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: VolumeAttachmentSpec = None):
        super().__init__("storage.k8s.io/v1", "VolumeAttachment", name, "", metadata=metadata, spec=spec)
