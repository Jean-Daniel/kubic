from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class CertificateSigningRequestSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"

    _required_ = ["request", "signer_name"]

    expiration_seconds: int
    extra: dict[str, list[str]]
    groups: list[str]
    request: core.Base64
    signer_name: str
    uid: str
    usages: list[str]
    username: str

    def __init__(
        self,
        expiration_seconds: int = None,
        extra: dict[str, list[str]] = None,
        groups: list[str] = None,
        request: core.Base64 = None,
        signer_name: str = None,
        uid: str = None,
        usages: list[str] = None,
        username: str = None,
    ):
        super().__init__(
            expiration_seconds=expiration_seconds,
            extra=extra,
            groups=groups,
            request=request,
            signer_name=signer_name,
            uid=uid,
            usages=usages,
            username=username,
        )


class CertificateSigningRequest(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"
    _api_group_ = "certificates.k8s.io"
    _kind_ = "CertificateSigningRequest"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CertificateSigningRequestSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CertificateSigningRequestSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CertificateSigningRequestCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    last_update_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_transition_time: meta.Time = None,
        last_update_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_transition_time=last_transition_time,
            last_update_time=last_update_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class CertificateSigningRequestStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1"

    certificate: core.Base64
    conditions: list[CertificateSigningRequestCondition]

    def __init__(self, certificate: core.Base64 = None, conditions: list[CertificateSigningRequestCondition] = None):
        super().__init__(certificate=certificate, conditions=conditions)


class ClusterTrustBundleSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1alpha1"

    _required_ = ["trust_bundle"]

    signer_name: str
    trust_bundle: str

    def __init__(self, signer_name: str = None, trust_bundle: str = None):
        super().__init__(signer_name=signer_name, trust_bundle=trust_bundle)


class ClusterTrustBundle(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "certificates.k8s.io/v1alpha1"
    _api_group_ = "certificates.k8s.io"
    _kind_ = "ClusterTrustBundle"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ClusterTrustBundleSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ClusterTrustBundleSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
