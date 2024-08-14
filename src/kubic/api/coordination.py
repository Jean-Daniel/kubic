from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class LeaseSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"

    acquire_time: meta.MicroTime
    holder_identity: str
    lease_duration_seconds: int
    lease_transitions: int
    preferred_holder: str
    renew_time: meta.MicroTime
    strategy: str

    def __init__(
        self,
        acquire_time: meta.MicroTime = None,
        holder_identity: str = None,
        lease_duration_seconds: int = None,
        lease_transitions: int = None,
        preferred_holder: str = None,
        renew_time: meta.MicroTime = None,
        strategy: str = None,
    ):
        super().__init__(
            acquire_time=acquire_time,
            holder_identity=holder_identity,
            lease_duration_seconds=lease_duration_seconds,
            lease_transitions=lease_transitions,
            preferred_holder=preferred_holder,
            renew_time=renew_time,
            strategy=strategy,
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


class LeaseCandidateSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1alpha1"

    _required_ = ["lease_name", "preferred_strategies"]

    binary_version: str
    emulation_version: str
    lease_name: str
    ping_time: meta.MicroTime
    preferred_strategies: list[str]
    renew_time: meta.MicroTime

    def __init__(
        self,
        binary_version: str = None,
        emulation_version: str = None,
        lease_name: str = None,
        ping_time: meta.MicroTime = None,
        preferred_strategies: list[str] = None,
        renew_time: meta.MicroTime = None,
    ):
        super().__init__(
            binary_version=binary_version,
            emulation_version=emulation_version,
            lease_name=lease_name,
            ping_time=ping_time,
            preferred_strategies=preferred_strategies,
            renew_time=renew_time,
        )


class LeaseCandidate(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1alpha1"
    _api_group_ = "coordination.k8s.io"
    _kind_ = "LeaseCandidate"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: LeaseCandidateSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: LeaseCandidateSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
