from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class BoundObjectReference(KubernetesObject):
    """BoundObjectReference is a reference to an object that a token is bound to."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    api_version: str
    """ API version of the referent. """
    kind: str
    """ Kind of the referent. Valid kinds are 'Pod' and 'Secret'. """
    name: str
    """ Name of the referent. """
    uid: str
    """ UID of the referent. """

    def __init__(self, api_version: str = None, kind: str = None, name: str = None, uid: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name, uid=uid)


class SelfSubjectReview(KubernetesApiResource):
    """SelfSubjectReview contains the user information that the kube-apiserver has about the user making this request. When using impersonation, users will receive the user info of the user being impersonated.  If impersonation or request header authentication is used, any extra keys will have their case ignored and returned as lowercase."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"
    _api_group_ = "authentication.k8s.io"
    _kind_ = "SelfSubjectReview"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, namespace, metadata=metadata)


class UserInfo(KubernetesObject):
    """UserInfo holds the information about the user needed to implement the user.Info interface."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    extra: dict[str, list[str]]
    """ Any additional information provided by the authenticator. """
    groups: list[str]
    """ The names of groups this user is a part of. """
    uid: str
    """ A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. """
    username: str
    """ The name that uniquely identifies this user among all active users. """

    def __init__(self, extra: dict[str, list[str]] = None, groups: list[str] = None, uid: str = None, username: str = None):
        super().__init__(extra=extra, groups=groups, uid=uid, username=username)


class SelfSubjectReviewStatus(KubernetesObject):
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    user_info: UserInfo
    """ User attributes of the user making this request. """

    def __init__(self, user_info: UserInfo = None):
        super().__init__(user_info=user_info)


class TokenRequestSpec(KubernetesObject):
    """TokenRequestSpec contains client provided parameters of a token request."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    _required_ = ["audiences"]

    audiences: list[str]
    """ Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. """
    bound_object_ref: BoundObjectReference
    """ BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation. """
    expiration_seconds: int
    """ ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response. """

    def __init__(self, audiences: list[str] = None, bound_object_ref: BoundObjectReference = None, expiration_seconds: int = None):
        super().__init__(audiences=audiences, bound_object_ref=bound_object_ref, expiration_seconds=expiration_seconds)


class TokenRequest(KubernetesApiResource):
    """TokenRequest requests a token for a given service account."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"
    _api_group_ = "authentication.k8s.io"
    _kind_ = "TokenRequest"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: TokenRequestSpec
    """ Spec holds information about the request being evaluated """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: TokenRequestSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class TokenRequestStatus(KubernetesObject):
    """TokenRequestStatus is the result of a token request."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    _required_ = ["expiration_timestamp", "token"]

    expiration_timestamp: meta.Time
    """ ExpirationTimestamp is the time of expiration of the returned token. """
    token: str
    """ Token is the opaque bearer token. """

    def __init__(self, expiration_timestamp: meta.Time = None, token: str = None):
        super().__init__(expiration_timestamp=expiration_timestamp, token=token)


class TokenReviewSpec(KubernetesObject):
    """TokenReviewSpec is a description of the token authentication request."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    audiences: list[str]
    """ Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. """
    token: str
    """ Token is the opaque bearer token. """

    def __init__(self, audiences: list[str] = None, token: str = None):
        super().__init__(audiences=audiences, token=token)


class TokenReview(KubernetesApiResource):
    """TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"
    _api_group_ = "authentication.k8s.io"
    _kind_ = "TokenReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: TokenReviewSpec
    """ Spec holds information about the request being evaluated """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: TokenReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class TokenReviewStatus(KubernetesObject):
    """TokenReviewStatus is the result of the token authentication request."""

    __slots__ = ()

    _api_version_ = "authentication.k8s.io/v1"

    audiences: list[str]
    """ Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server. """
    authenticated: bool
    """ Authenticated indicates that the token was associated with a known user. """
    error: str
    """ Error indicates that the token couldn't be checked """
    user: UserInfo
    """ User is the UserInfo associated with the provided token. """

    def __init__(self, audiences: list[str] = None, authenticated: bool = None, error: str = None, user: UserInfo = None):
        super().__init__(audiences=audiences, authenticated=authenticated, error=error, user=user)
