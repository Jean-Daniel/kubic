from typing import List

from . import KubernetesApiResource, KubernetesObject
from . import meta


class AggregationRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"

    cluster_role_selectors: List[meta.LabelSelector]

    def __init__(self, cluster_role_selectors: List[meta.LabelSelector] = None):
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

    api_groups: List[str]
    non_resource_urls: List[str]
    resource_names: List[str]
    resources: List[str]
    verbs: List[str]

    def __init__(
        self,
        api_groups: List[str] = None,
        non_resource_urls: List[str] = None,
        resource_names: List[str] = None,
        resources: List[str] = None,
        verbs: List[str] = None,
    ):
        super().__init__(
            api_groups=api_groups, non_resource_urls=non_resource_urls, resource_names=resource_names, resources=resources, verbs=verbs
        )


class ClusterRole(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _kind_ = "ClusterRole"
    _scope_ = "cluster"

    aggregation_rule: AggregationRule
    metadata: meta.ObjectMeta
    rules: List[PolicyRule]

    def __init__(
        self, name: str, aggregation_rule: AggregationRule = None, metadata: meta.ObjectMeta = None, rules: List[PolicyRule] = None
    ):
        super().__init__(
            "rbac.authorization.k8s.io/v1", "ClusterRole", name, "", aggregation_rule=aggregation_rule, metadata=metadata, rules=rules
        )


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
    _kind_ = "ClusterRoleBinding"
    _scope_ = "cluster"

    _required_ = ["role_ref"]

    metadata: meta.ObjectMeta
    role_ref: RoleRef
    subjects: List[Subject]

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, role_ref: RoleRef = None, subjects: List[Subject] = None):
        super().__init__(
            "rbac.authorization.k8s.io/v1", "ClusterRoleBinding", name, "", metadata=metadata, role_ref=role_ref, subjects=subjects
        )


class Role(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _kind_ = "Role"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    rules: List[PolicyRule]

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, rules: List[PolicyRule] = None):
        super().__init__("rbac.authorization.k8s.io/v1", "Role", name, namespace, metadata=metadata, rules=rules)


class RoleBinding(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rbac.authorization.k8s.io/v1"
    _kind_ = "RoleBinding"
    _scope_ = "namespace"

    _required_ = ["role_ref"]

    metadata: meta.ObjectMeta
    role_ref: RoleRef
    subjects: List[Subject]

    def __init__(
        self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, role_ref: RoleRef = None, subjects: List[Subject] = None
    ):
        super().__init__(
            "rbac.authorization.k8s.io/v1", "RoleBinding", name, namespace, metadata=metadata, role_ref=role_ref, subjects=subjects
        )
