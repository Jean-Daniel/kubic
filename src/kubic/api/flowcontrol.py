from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class FlowDistinguisherMethod(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["type"]

    type: str

    def __init__(self, type: str = None):
        super().__init__(type=type)


class PriorityLevelConfigurationReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class NonResourcePolicyRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["non_resource_urls", "verbs"]

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


class ResourcePolicyRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["api_groups", "resources", "verbs"]

    api_groups: list[str]
    cluster_scope: bool
    namespaces: list[str]
    resources: list[str]
    verbs: list[str]

    def __init__(
        self,
        api_groups: list[str] = None,
        cluster_scope: bool = None,
        namespaces: list[str] = None,
        resources: list[str] = None,
        verbs: list[str] = None,
    ):
        super().__init__(api_groups=api_groups, cluster_scope=cluster_scope, namespaces=namespaces, resources=resources, verbs=verbs)


class GroupSubject(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class ServiceAccountSubject(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["name", "namespace"]

    name: str
    namespace: str

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class UserSubject(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class Subject(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["kind"]

    group: GroupSubject
    kind: str
    service_account: ServiceAccountSubject
    user: UserSubject

    def __init__(
        self, group: GroupSubject = None, kind: str = None, service_account: ServiceAccountSubject = None, user: UserSubject = None
    ):
        super().__init__(group=group, kind=kind, service_account=service_account, user=user)


class PolicyRulesWithSubjects(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["subjects"]

    non_resource_rules: list[NonResourcePolicyRule]
    resource_rules: list[ResourcePolicyRule]
    subjects: list[Subject]

    def __init__(
        self,
        non_resource_rules: list[NonResourcePolicyRule] = None,
        resource_rules: list[ResourcePolicyRule] = None,
        subjects: list[Subject] = None,
    ):
        super().__init__(non_resource_rules=non_resource_rules, resource_rules=resource_rules, subjects=subjects)


class FlowSchemaSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["priority_level_configuration"]

    distinguisher_method: FlowDistinguisherMethod
    matching_precedence: int
    priority_level_configuration: PriorityLevelConfigurationReference
    rules: list[PolicyRulesWithSubjects]

    def __init__(
        self,
        distinguisher_method: FlowDistinguisherMethod = None,
        matching_precedence: int = None,
        priority_level_configuration: PriorityLevelConfigurationReference = None,
        rules: list[PolicyRulesWithSubjects] = None,
    ):
        super().__init__(
            distinguisher_method=distinguisher_method,
            matching_precedence=matching_precedence,
            priority_level_configuration=priority_level_configuration,
            rules=rules,
        )


class FlowSchema(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"
    _api_group_ = "flowcontrol.apiserver.k8s.io"
    _kind_ = "FlowSchema"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: FlowSchemaSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: FlowSchemaSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class FlowSchemaCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class FlowSchemaList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"
    _api_group_ = "flowcontrol.apiserver.k8s.io"
    _kind_ = "FlowSchemaList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[FlowSchema]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[FlowSchema] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class FlowSchemaStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    conditions: list[FlowSchemaCondition]

    def __init__(self, conditions: list[FlowSchemaCondition] = None):
        super().__init__(conditions=conditions)


class QueuingConfiguration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    hand_size: int
    queue_length_limit: int
    queues: int

    def __init__(self, hand_size: int = None, queue_length_limit: int = None, queues: int = None):
        super().__init__(hand_size=hand_size, queue_length_limit=queue_length_limit, queues=queues)


class LimitResponse(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["type"]

    queuing: QueuingConfiguration
    type: str

    def __init__(self, queuing: QueuingConfiguration = None, type: str = None):
        super().__init__(queuing=queuing, type=type)


class LimitedPriorityLevelConfiguration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    assured_concurrency_shares: int
    borrowing_limit_percent: int
    lendable_percent: int
    limit_response: LimitResponse

    def __init__(
        self,
        assured_concurrency_shares: int = None,
        borrowing_limit_percent: int = None,
        lendable_percent: int = None,
        limit_response: LimitResponse = None,
    ):
        super().__init__(
            assured_concurrency_shares=assured_concurrency_shares,
            borrowing_limit_percent=borrowing_limit_percent,
            lendable_percent=lendable_percent,
            limit_response=limit_response,
        )


class PriorityLevelConfigurationSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    _required_ = ["type"]

    limited: LimitedPriorityLevelConfiguration
    type: str

    def __init__(self, limited: LimitedPriorityLevelConfiguration = None, type: str = None):
        super().__init__(limited=limited, type=type)


class PriorityLevelConfiguration(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"
    _api_group_ = "flowcontrol.apiserver.k8s.io"
    _kind_ = "PriorityLevelConfiguration"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: PriorityLevelConfigurationSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: PriorityLevelConfigurationSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class PriorityLevelConfigurationCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class PriorityLevelConfigurationList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"
    _api_group_ = "flowcontrol.apiserver.k8s.io"
    _kind_ = "PriorityLevelConfigurationList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PriorityLevelConfiguration]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PriorityLevelConfiguration] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class PriorityLevelConfigurationStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1beta2"

    conditions: list[PriorityLevelConfigurationCondition]

    def __init__(self, conditions: list[PriorityLevelConfigurationCondition] = None):
        super().__init__(conditions=conditions)
