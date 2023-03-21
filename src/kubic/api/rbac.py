from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class AggregationRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    cluster_role_selectors: list[meta.LabelSelector]

    def __init__(self, cluster_role_selectors: list[meta.LabelSelector] = None):
        super().__init__(cluster_role_selectors=cluster_role_selectors)


class PolicyRule(KubernetesObject):
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
    non_resource_urls: list[str]
    resource_names: list[str]
    resources: list[str]
    verbs: list[str]

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
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "ClusterRole"
    _scope_ = "cluster"

    aggregation_rule: AggregationRule
    metadata: meta.ObjectMeta
    rules: list[PolicyRule]

    def __init__(
        self, name: str, aggregation_rule: AggregationRule = None, metadata: meta.ObjectMeta = None, rules: list[PolicyRule] = None
    ):
        super().__init__(name, "", aggregation_rule=aggregation_rule, metadata=metadata, rules=rules)


class RoleRef(KubernetesObject):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    _required_ = ["api_group", "kind", "name"]

    api_group: str
    kind: str
    name: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class Subject(KubernetesObject):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    _required_ = ["kind", "name"]

    api_group: str
    kind: str
    name: str
    namespace: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace)


class ClusterRoleBinding(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "ClusterRoleBinding"
    _scope_ = "cluster"

    _required_ = ["role_ref"]

    metadata: meta.ObjectMeta
    role_ref: RoleRef
    subjects: list[Subject]

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, role_ref: RoleRef = None, subjects: list[Subject] = None):
        super().__init__(name, "", metadata=metadata, role_ref=role_ref, subjects=subjects)


class ClusterRoleBindingList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "ClusterRoleBindingList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ClusterRoleBinding]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ClusterRoleBinding] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ClusterRoleList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "ClusterRoleList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ClusterRole]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ClusterRole] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class Role(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "Role"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    rules: list[PolicyRule]

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, rules: list[PolicyRule] = None):
        super().__init__(name, namespace, metadata=metadata, rules=rules)


class RoleBinding(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "RoleBinding"
    _scope_ = "namespace"

    _required_ = ["role_ref"]

    metadata: meta.ObjectMeta
    role_ref: RoleRef
    subjects: list[Subject]

    def __init__(
        self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, role_ref: RoleRef = None, subjects: list[Subject] = None
    ):
        super().__init__(name, namespace, metadata=metadata, role_ref=role_ref, subjects=subjects)


class RoleBindingList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "RoleBindingList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[RoleBinding]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[RoleBinding] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class RoleList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _api_group_ = "rbac.authorization.k8s.io"
    _kind_ = "RoleList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Role]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Role] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)
