from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class LeaseSpec(KubernetesObject):
    """LeaseSpec is a specification of a Lease."""

    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1"

    acquire_time: meta.MicroTime
    """ acquireTime is a time when the current lease was acquired. """
    holder_identity: str
    """ holderIdentity contains the identity of the holder of a current lease. If Coordinated Leader Election is used, the holder identity must be equal to the elected LeaseCandidate.metadata.name field. """
    lease_duration_seconds: int
    """ leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measured against the time of last observed renewTime. """
    lease_transitions: int
    """ leaseTransitions is the number of transitions of a lease between holders. """
    preferred_holder: str
    """ PreferredHolder signals to a lease holder that the lease has a more optimal holder and should be given up. This field can only be set if Strategy is also set. """
    renew_time: meta.MicroTime
    """ renewTime is a time when the current holder of a lease has last updated the lease. """
    strategy: str
    """ Strategy indicates the strategy for picking the leader for coordinated leader election. If the field is not specified, there is no active coordination for this lease. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled. """

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


class LeaseCandidateSpec(KubernetesObject):
    """LeaseCandidateSpec is a specification of a Lease."""

    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1alpha2"

    _required_ = ["binary_version", "lease_name", "strategy"]

    binary_version: str
    """ BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required. """
    emulation_version: str
    """ EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is "OldestEmulationVersion" """
    lease_name: str
    """ LeaseName is the name of the lease for which this candidate is contending. This field is immutable. """
    ping_time: meta.MicroTime
    """ PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime. """
    renew_time: meta.MicroTime
    """ RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates. """
    strategy: str
    """ Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved. """

    def __init__(
        self,
        binary_version: str = None,
        emulation_version: str = None,
        lease_name: str = None,
        ping_time: meta.MicroTime = None,
        renew_time: meta.MicroTime = None,
        strategy: str = None,
    ):
        super().__init__(
            binary_version=binary_version,
            emulation_version=emulation_version,
            lease_name=lease_name,
            ping_time=ping_time,
            renew_time=renew_time,
            strategy=strategy,
        )


class LeaseCandidate(KubernetesApiResource):
    """LeaseCandidate defines a candidate for a Lease object. Candidates are created such that coordinated leader election will pick the best leader from the list of candidates."""

    __slots__ = ()

    _api_version_ = "coordination.k8s.io/v1alpha2"
    _api_group_ = "coordination.k8s.io"
    _kind_ = "LeaseCandidate"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: LeaseCandidateSpec
    """ spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: LeaseCandidateSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
