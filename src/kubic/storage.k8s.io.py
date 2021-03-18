from typing import Dict, List

from . import KubernetesApiResource
from . import core, meta


class StorageClass(KubernetesApiResource):
    __slots__ = ()

    _group_ = "storage.k8s.io"
    _version_ = "v1"

    _required_ = ["provisioner"]

    allow_volume_expansion: bool
    allowed_topologies: List[core.TopologySelectorTerm]
    metadata: meta.ObjectMeta
    mount_options: List[str]
    parameters: Dict[str]
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
        parameters: Dict[str] = None,
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
