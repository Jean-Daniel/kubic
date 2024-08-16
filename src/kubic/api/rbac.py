from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class AggregationRule(KubernetesObject):
    """AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole"""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    cluster_role_selectors: list[meta.LabelSelector]
    """ ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added """

    def __init__(self, cluster_role_selectors: list[meta.LabelSelector] = None):
        super().__init__(cluster_role_selectors=cluster_role_selectors)


class PolicyRule(KubernetesObject):
    """PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to."""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    _required_ = ["verbs"]

    _field_names_ = {
        "non_resource_urls": "nonResourceURLs",
    }
    _revfield_names_ = {
        "nonResourceURLs": "non_resource_urls",
    }

    api_groups: list[str]
    """ APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups. """
    non_resource_urls: list[str]
    """ NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both. """
    resource_names: list[str]
    """ ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. """
    resources: list[str]
    """ Resources is a list of resources this rule applies to. '*' represents all resources. """
    verbs: list[str]
    """ Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*' represents all verbs. """

    def __init__(
        self,
        api_groups: list[str] = None,
        non_resource_urls: list[str] = None,
        resource_names: list[str] = None,
        resources: list[str] = None,
        verbs: list[str] = None,
    ):
        super().__init__(
            api_groups=api_groups, non_resource_urls=non_resource_urls, resource_names=resource_names, resources=resources, verbs=verbs
        )


class ClusterRole(KubernetesApiResource):
    """ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding."""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "ClusterRole"
    _scope_ = "cluster"

    aggregation_rule: AggregationRule
    """ AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. """
    rules: list[PolicyRule]
    """ Rules holds all the PolicyRules for this ClusterRole """

    def __init__(
        self, name: str, aggregation_rule: AggregationRule = None, metadata: meta.ObjectMeta = None, rules: list[PolicyRule] = None
    ):
        super().__init__(name, "", aggregation_rule=aggregation_rule, metadata=metadata, rules=rules)


class RoleRef(KubernetesObject):
    """RoleRef contains information that points to the role being used"""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    _required_ = ["api_group", "kind", "name"]

    api_group: str
    """ APIGroup is the group for the resource being referenced """
    kind: str
    """ Kind is the type of resource being referenced """
    name: str
    """ Name is the name of resource being referenced """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class Subject(KubernetesObject):
    """Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names."""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    _required_ = ["kind", "name"]

    api_group: str
    """ APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects. """
    kind: str
    """ Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error. """
    name: str
    """ Name of the object being referenced. """
    namespace: str
    """ Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error. """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace)


class ClusterRoleBinding(KubernetesApiResource):
    """ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in the global namespace, and adds who information via Subject."""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "ClusterRoleBinding"
    _scope_ = "cluster"

    _required_ = ["role_ref"]

    metadata: meta.ObjectMeta
    """ Standard object's metadata. """
    role_ref: RoleRef
    """ RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable. """
    subjects: list[Subject]
    """ Subjects holds references to the objects the role applies to. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, role_ref: RoleRef = None, subjects: list[Subject] = None):
        super().__init__(name, "", metadata=metadata, role_ref=role_ref, subjects=subjects)


class Role(KubernetesApiResource):
    """Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding."""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "Role"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. """
    rules: list[PolicyRule]
    """ Rules holds all the PolicyRules for this Role """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, rules: list[PolicyRule] = None):
        super().__init__(name, namespace, metadata=metadata, rules=rules)


class RoleBinding(KubernetesApiResource):
    """RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace."""

    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "RoleBinding"
    _scope_ = "namespace"

    _required_ = ["role_ref"]

    metadata: meta.ObjectMeta
    """ Standard object's metadata. """
    role_ref: RoleRef
    """ RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable. """
    subjects: list[Subject]
    """ Subjects holds references to the objects the role applies to. """

    def __init__(
        self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, role_ref: RoleRef = None, subjects: list[Subject] = None
    ):
        super().__init__(name, namespace, metadata=metadata, role_ref=role_ref, subjects=subjects)
