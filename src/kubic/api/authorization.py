from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class NonResourceAttributes(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    path: str
    verb: str

    def __init__(self, path: str = None, verb: str = None):
        super().__init__(path=path, verb=verb)


class ResourceAttributes(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    group: str
    name: str
    namespace: str
    resource: str
    subresource: str
    verb: str
    version: str

    def __init__(
        self,
        group: str = None,
        name: str = None,
        namespace: str = None,
        resource: str = None,
        subresource: str = None,
        verb: str = None,
        version: str = None,
    ):
        super().__init__(
            group=group, name=name, namespace=namespace, resource=resource, subresource=subresource, verb=verb, version=version
        )


class SubjectAccessReviewSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    extra: dict[str, list[str]]
    groups: list[str]
    non_resource_attributes: NonResourceAttributes
    resource_attributes: ResourceAttributes
    uid: str
    user: str

    def __init__(
        self,
        extra: dict[str, list[str]] = None,
        groups: list[str] = None,
        non_resource_attributes: NonResourceAttributes = None,
        resource_attributes: ResourceAttributes = None,
        uid: str = None,
        user: str = None,
    ):
        super().__init__(
            extra=extra,
            groups=groups,
            non_resource_attributes=non_resource_attributes,
            resource_attributes=resource_attributes,
            uid=uid,
            user=user,
        )


class LocalSubjectAccessReview(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "LocalSubjectAccessReview"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: SubjectAccessReviewSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: SubjectAccessReviewSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class NonResourceRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["verbs"]

    _field_names_ = {
        "non_resource_urls": "nonResourceURLs",
    }
    _revfield_names_ = {
        "nonResourceURLs": "non_resource_urls",
    }

    non_resource_urls: list[str]
    verbs: list[str]

    def __init__(self, non_resource_urls: list[str] = None, verbs: list[str] = None):
        super().__init__(non_resource_urls=non_resource_urls, verbs=verbs)


class ResourceRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["verbs"]

    api_groups: list[str]
    resource_names: list[str]
    resources: list[str]
    verbs: list[str]

    def __init__(
        self, api_groups: list[str] = None, resource_names: list[str] = None, resources: list[str] = None, verbs: list[str] = None
    ):
        super().__init__(api_groups=api_groups, resource_names=resource_names, resources=resources, verbs=verbs)


class SelfSubjectAccessReviewSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    non_resource_attributes: NonResourceAttributes
    resource_attributes: ResourceAttributes

    def __init__(self, non_resource_attributes: NonResourceAttributes = None, resource_attributes: ResourceAttributes = None):
        super().__init__(non_resource_attributes=non_resource_attributes, resource_attributes=resource_attributes)


class SelfSubjectAccessReview(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "SelfSubjectAccessReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: SelfSubjectAccessReviewSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: SelfSubjectAccessReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class SelfSubjectRulesReviewSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    namespace: str

    def __init__(self, namespace: str = None):
        super().__init__(namespace=namespace)


class SelfSubjectRulesReview(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "SelfSubjectRulesReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: SelfSubjectRulesReviewSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: SelfSubjectRulesReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class SubjectAccessReview(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "SubjectAccessReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: SubjectAccessReviewSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: SubjectAccessReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class SubjectAccessReviewStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["allowed"]

    allowed: bool
    denied: bool
    evaluation_error: str
    reason: str

    def __init__(self, allowed: bool = None, denied: bool = None, evaluation_error: str = None, reason: str = None):
        super().__init__(allowed=allowed, denied=denied, evaluation_error=evaluation_error, reason=reason)


class SubjectRulesReviewStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["incomplete", "non_resource_rules", "resource_rules"]

    evaluation_error: str
    incomplete: bool
    non_resource_rules: list[NonResourceRule]
    resource_rules: list[ResourceRule]

    def __init__(
        self,
        evaluation_error: str = None,
        incomplete: bool = None,
        non_resource_rules: list[NonResourceRule] = None,
        resource_rules: list[ResourceRule] = None,
    ):
        super().__init__(
            evaluation_error=evaluation_error, incomplete=incomplete, non_resource_rules=non_resource_rules, resource_rules=resource_rules
        )
