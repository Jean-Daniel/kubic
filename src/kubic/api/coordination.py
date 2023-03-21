from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class LeaseSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"

    acquire_time: meta.MicroTime
    holder_identity: str
    lease_duration_seconds: int
    lease_transitions: int
    renew_time: meta.MicroTime

    def __init__(
        self,
        acquire_time: meta.MicroTime = None,
        holder_identity: str = None,
        lease_duration_seconds: int = None,
        lease_transitions: int = None,
        renew_time: meta.MicroTime = None,
    ):
        super().__init__(
            acquire_time=acquire_time,
            holder_identity=holder_identity,
            lease_duration_seconds=lease_duration_seconds,
            lease_transitions=lease_transitions,
            renew_time=renew_time,
        )


class Lease(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"
    _api_group_ = "coordination.k8s.io"
    _kind_ = "Lease"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: LeaseSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: LeaseSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class LeaseList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"
    _api_group_ = "coordination.k8s.io"
    _kind_ = "LeaseList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Lease]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Lease] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)
