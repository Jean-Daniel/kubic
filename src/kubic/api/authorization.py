from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class NonResourceAttributes(KubernetesObject):
    """NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface"""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    path: str
    """ Path is the URL path of the request """
    verb: str
    """ Verb is the standard HTTP verb """

    def __init__(self, path: str = None, verb: str = None):
        super().__init__(path=path, verb=verb)


class ResourceAttributes(KubernetesObject):
    """ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface"""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    group: str
    """ Group is the API Group of the Resource.  "*" means all. """
    name: str
    """ Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all. """
    namespace: str
    """ Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview """
    resource: str
    """ Resource is one of the existing resource types.  "*" means all. """
    subresource: str
    """ Subresource is one of the existing resource types.  "" means none. """
    verb: str
    """ Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all. """
    version: str
    """ Version is the API Version of the Resource.  "*" means all. """

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
    """SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set"""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    extra: dict[str, list[str]]
    """ Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. """
    groups: list[str]
    """ Groups is the groups you're testing for. """
    non_resource_attributes: NonResourceAttributes
    """ NonResourceAttributes describes information for a non-resource access request """
    resource_attributes: ResourceAttributes
    """ ResourceAuthorizationAttributes describes information for a resource access request """
    uid: str
    """ UID information about the requesting user. """
    user: str
    """ User is the user you're testing for. If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups """

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
    """LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking."""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "LocalSubjectAccessReview"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: SubjectAccessReviewSpec
    """ Spec holds information about the request being evaluated.  spec.namespace must be equal to the namespace you made the request against.  If empty, it is defaulted. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: SubjectAccessReviewSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class NonResourceRule(KubernetesObject):
    """NonResourceRule holds information that describes a rule for the non-resource"""

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
    """ NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all. """
    verbs: list[str]
    """ Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all. """

    def __init__(self, non_resource_urls: list[str] = None, verbs: list[str] = None):
        super().__init__(non_resource_urls=non_resource_urls, verbs=verbs)


class ResourceRule(KubernetesObject):
    """ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete."""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["verbs"]

    api_groups: list[str]
    """ APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all. """
    resource_names: list[str]
    """ ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all. """
    resources: list[str]
    """
    Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.
     "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups.
    """
    verbs: list[str]
    """ Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all. """

    def __init__(
        self, api_groups: list[str] = None, resource_names: list[str] = None, resources: list[str] = None, verbs: list[str] = None
    ):
        super().__init__(api_groups=api_groups, resource_names=resource_names, resources=resources, verbs=verbs)


class SelfSubjectAccessReviewSpec(KubernetesObject):
    """SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set"""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    non_resource_attributes: NonResourceAttributes
    """ NonResourceAttributes describes information for a non-resource access request """
    resource_attributes: ResourceAttributes
    """ ResourceAuthorizationAttributes describes information for a resource access request """

    def __init__(self, non_resource_attributes: NonResourceAttributes = None, resource_attributes: ResourceAttributes = None):
        super().__init__(non_resource_attributes=non_resource_attributes, resource_attributes=resource_attributes)


class SelfSubjectAccessReview(KubernetesApiResource):
    """SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means "in all namespaces".  Self is a special case, because users should always be able to check whether they can perform an action"""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "SelfSubjectAccessReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: SelfSubjectAccessReviewSpec
    """ Spec holds information about the request being evaluated.  user and groups must be empty """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: SelfSubjectAccessReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class SelfSubjectRulesReviewSpec(KubernetesObject):
    """SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview."""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    namespace: str
    """ Namespace to evaluate rules for. Required. """

    def __init__(self, namespace: str = None):
        super().__init__(namespace=namespace)


class SelfSubjectRulesReview(KubernetesApiResource):
    """SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server's authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server."""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "SelfSubjectRulesReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: SelfSubjectRulesReviewSpec
    """ Spec holds information about the request being evaluated. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: SelfSubjectRulesReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class SubjectAccessReview(KubernetesApiResource):
    """SubjectAccessReview checks whether or not a user or group can perform an action."""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"
    _api_group_ = "authorization.k8s.io"
    _kind_ = "SubjectAccessReview"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: SubjectAccessReviewSpec
    """ Spec holds information about the request being evaluated """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: SubjectAccessReviewSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class SubjectAccessReviewStatus(KubernetesObject):
    """SubjectAccessReviewStatus"""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["allowed"]

    allowed: bool
    """ Allowed is required. True if the action would be allowed, false otherwise. """
    denied: bool
    """ Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. """
    evaluation_error: str
    """ EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. """
    reason: str
    """ Reason is optional.  It indicates why a request was allowed or denied. """

    def __init__(self, allowed: bool = None, denied: bool = None, evaluation_error: str = None, reason: str = None):
        super().__init__(allowed=allowed, denied=denied, evaluation_error=evaluation_error, reason=reason)


class SubjectRulesReviewStatus(KubernetesObject):
    """SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete."""

    __slots__ = ()

    _api_version_ = "authorization.k8s.io/v1"

    _required_ = ["incomplete", "non_resource_rules", "resource_rules"]

    evaluation_error: str
    """ EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. """
    incomplete: bool
    """ Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation. """
    non_resource_rules: list[NonResourceRule]
    """ NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """
    resource_rules: list[ResourceRule]
    """ ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete. """

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
