from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class BoundObjectReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    api_version: str
    kind: str
    name: str
    uid: str

    def __init__(self, api_version: str = None, kind: str = None, name: str = None, uid: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name, uid=uid)


class SelfSubjectReview(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"
    _api_group_ = "authentication.k8s.io"
    _kind_ = "SelfSubjectReview"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, namespace, metadata=metadata)


class UserInfo(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    extra: dict[str, list[str]]
    groups: list[str]
    uid: str
    username: str

    def __init__(self, extra: dict[str, list[str]] = None, groups: list[str] = None, uid: str = None, username: str = None):
        super().__init__(extra=extra, groups=groups, uid=uid, username=username)


class SelfSubjectReviewStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    user_info: UserInfo

    def __init__(self, user_info: UserInfo = None):
        super().__init__(user_info=user_info)


class TokenRequestSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    _required_ = ["audiences"]

    audiences: list[str]
    bound_object_ref: BoundObjectReference
    expiration_seconds: int

    def __init__(self, audiences: list[str] = None, bound_object_ref: BoundObjectReference = None, expiration_seconds: int = None):
        super().__init__(audiences=audiences, bound_object_ref=bound_object_ref, expiration_seconds=expiration_seconds)


class TokenRequest(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"
    _api_group_ = "authentication.k8s.io"
    _kind_ = "TokenRequest"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: TokenRequestSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: TokenRequestSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class TokenRequestStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    _required_ = ["expiration_timestamp", "token"]

    expiration_timestamp: meta.Time
    token: str

    def __init__(self, expiration_timestamp: meta.Time = None, token: str = None):
        super().__init__(expiration_timestamp=expiration_timestamp, token=token)


class TokenReviewSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    audiences: list[str]
    token: str

    def __init__(self, audiences: list[str] = None, token: str = None):
        super().__init__(audiences=audiences, token=token)


class TokenReview(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"
    _api_group_ = "authentication.k8s.io"
    _kind_ = "TokenReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: TokenReviewSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: TokenReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class TokenReviewStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    audiences: list[str]
    authenticated: bool
    error: str
    user: UserInfo

    def __init__(self, audiences: list[str] = None, authenticated: bool = None, error: str = None, user: UserInfo = None):
        super().__init__(audiences=audiences, authenticated=authenticated, error=error, user=user)
