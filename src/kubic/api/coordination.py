from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class LeaseSpec(KubernetesObject):
    """LeaseSpec is a specification of a Lease."""

    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"

    acquire_time: meta.MicroTime
    """ acquireTime is a time when the current lease was acquired. """
    holder_identity: str
    """ holderIdentity contains the identity of the holder of a current lease. """
    lease_duration_seconds: int
    """ leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime. """
    lease_transitions: int
    """ leaseTransitions is the number of transitions of a lease between holders. """
    renew_time: meta.MicroTime
    """ renewTime is a time when the current holder of a lease has last updated the lease. """

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
    """Lease defines a lease concept."""

    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"
    _api_group_ = "coordination.k8s.io"
    _kind_ = "Lease"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: LeaseSpec
    """ spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: LeaseSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
