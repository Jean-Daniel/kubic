from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class ExemptPriorityLevelConfiguration(KubernetesObject):
    """ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt requests. In the mandatory exempt configuration object the values in the fields here can be modified by authorized users, unlike the rest of the `spec`."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    lendable_percent: int
    """ 
    `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.
    
    LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )
     """
    nominal_concurrency_shares: int
    """ 
    `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally reserved for this priority level. This DOES NOT limit the dispatching from this priority level but affects the other priority levels through the borrowing mechanism. The server's concurrency limit (ServerCL) is divided among all the priority levels in proportion to their NCS values:
    
    NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)
    
    Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of zero.
     """

    def __init__(self, lendable_percent: int = None, nominal_concurrency_shares: int = None):
        super().__init__(lendable_percent=lendable_percent, nominal_concurrency_shares=nominal_concurrency_shares)


class FlowDistinguisherMethod(KubernetesObject):
    """FlowDistinguisherMethod specifies the method of a flow distinguisher."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["type"]

    type: str
    """ `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required. """

    def __init__(self, type: str = None):
        super().__init__(type=type)


class PriorityLevelConfigurationReference(KubernetesObject):
    """PriorityLevelConfigurationReference contains information that points to the "request-priority" being used."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["name"]

    name: str
    """ `name` is the name of the priority level configuration being referenced Required. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class NonResourcePolicyRule(KubernetesObject):
    """NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["non_resource_urls", "verbs"]

    _field_names_ = {
        "non_resource_urls": "nonResourceURLs",
    }
    _revfield_names_ = {
        "nonResourceURLs": "non_resource_urls",
    }

    non_resource_urls: list[str]
    """ 
    `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:
      - "/healthz" is legal
      - "/hea*" is illegal
      - "/hea" is legal but matches nothing
      - "/hea/*" also matches nothing
      - "/healthz/*" matches all per-component health checks.
    "*" matches all non-resource urls. if it is present, it must be the only entry. Required.
     """
    verbs: list[str]
    """ `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required. """

    def __init__(self, non_resource_urls: list[str] = None, verbs: list[str] = None):
        super().__init__(non_resource_urls=non_resource_urls, verbs=verbs)


class ResourcePolicyRule(KubernetesObject):
    """ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request's namespace."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["api_groups", "resources", "verbs"]

    api_groups: list[str]
    """ `apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required. """
    cluster_scope: bool
    """ `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list. """
    namespaces: list[str]
    """ `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "*".  Note that "*" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true. """
    resources: list[str]
    """ `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ "services", "nodes/status" ].  This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required. """
    verbs: list[str]
    """ `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required. """

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
    """GroupSubject holds detailed information for group-kind subject."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["name"]

    name: str
    """ name is the user group that matches, or "*" to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class ServiceAccountSubject(KubernetesObject):
    """ServiceAccountSubject holds detailed information for service-account-kind subject."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["name", "namespace"]

    name: str
    """ `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required. """
    namespace: str
    """ `namespace` is the namespace of matching ServiceAccount objects. Required. """

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class UserSubject(KubernetesObject):
    """UserSubject holds detailed information for user-kind subject."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["name"]

    name: str
    """ `name` is the username that matches, or "*" to match all usernames. Required. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class Subject(KubernetesObject):
    """Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["kind"]

    group: GroupSubject
    """ `group` matches based on user group name. """
    kind: str
    """ `kind` indicates which one of the other fields is non-empty. Required """
    service_account: ServiceAccountSubject
    """ `serviceAccount` matches ServiceAccounts. """
    user: UserSubject
    """ `user` matches based on username. """

    def __init__(
        self, group: GroupSubject = None, kind: str = None, service_account: ServiceAccountSubject = None, user: UserSubject = None
    ):
        super().__init__(group=group, kind=kind, service_account=service_account, user=user)


class PolicyRulesWithSubjects(KubernetesObject):
    """PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["subjects"]

    non_resource_rules: list[NonResourcePolicyRule]
    """ `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. """
    resource_rules: list[ResourcePolicyRule]
    """ `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty. """
    subjects: list[Subject]
    """ subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. """

    def __init__(
        self,
        non_resource_rules: list[NonResourcePolicyRule] = None,
        resource_rules: list[ResourcePolicyRule] = None,
        subjects: list[Subject] = None,
    ):
        super().__init__(non_resource_rules=non_resource_rules, resource_rules=resource_rules, subjects=subjects)


class FlowSchemaSpec(KubernetesObject):
    """FlowSchemaSpec describes how the FlowSchema's specification looks like."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["priority_level_configuration"]

    distinguisher_method: FlowDistinguisherMethod
    """ `distinguisherMethod` defines how to compute the flow distinguisher for requests that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be the empty string. """
    matching_precedence: int
    """ `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. """
    priority_level_configuration: PriorityLevelConfigurationReference
    """ `priorityLevelConfiguration` should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required. """
    rules: list[PolicyRulesWithSubjects]
    """ `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. """

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
    """FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher"."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"
    _api_group_ = "flowcontrol.apiserver.k8s.io"
    _kind_ = "FlowSchema"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: FlowSchemaSpec
    """ `spec` is the specification of the desired behavior of a FlowSchema. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: FlowSchemaSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class FlowSchemaCondition(KubernetesObject):
    """FlowSchemaCondition describes conditions for a FlowSchema."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    last_transition_time: meta.Time
    """ `lastTransitionTime` is the last time the condition transitioned from one status to another. """
    message: str
    """ `message` is a human-readable message indicating details about last transition. """
    reason: str
    """ `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """
    status: str
    """ `status` is the status of the condition. Can be True, False, Unknown. Required. """
    type: str
    """ `type` is the type of the condition. Required. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class FlowSchemaStatus(KubernetesObject):
    """FlowSchemaStatus represents the current state of a FlowSchema."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    conditions: list[FlowSchemaCondition]
    """ `conditions` is a list of the current states of FlowSchema. """

    def __init__(self, conditions: list[FlowSchemaCondition] = None):
        super().__init__(conditions=conditions)


class QueuingConfiguration(KubernetesObject):
    """QueuingConfiguration holds the configuration parameters for queuing"""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    hand_size: int
    """ `handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8. """
    queue_length_limit: int
    """ `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50. """
    queues: int
    """ `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64. """

    def __init__(self, hand_size: int = None, queue_length_limit: int = None, queues: int = None):
        super().__init__(hand_size=hand_size, queue_length_limit=queue_length_limit, queues=queues)


class LimitResponse(KubernetesObject):
    """LimitResponse defines how to handle requests that can not be executed right now."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["type"]

    queuing: QueuingConfiguration
    """ `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`. """
    type: str
    """ `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required. """

    def __init__(self, queuing: QueuingConfiguration = None, type: str = None):
        super().__init__(queuing=queuing, type=type)


class LimitedPriorityLevelConfiguration(KubernetesObject):
    """
    LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:
      - How are requests for this priority level limited?
      - What should be done with requests that exceed the limit?
    """

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    borrowing_limit_percent: int
    """ 
    `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.
    
    BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )
    
    The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite.
     """
    lendable_percent: int
    """ 
    `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.
    
    LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )
     """
    limit_response: LimitResponse
    """ `limitResponse` indicates what to do with requests that can not be executed right now """
    nominal_concurrency_shares: int
    """ 
    `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:
    
    NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)
    
    Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level.
    
    If not specified, this field defaults to a value of 30.
    
    Setting this field to zero supports the construction of a "jail" for this priority level that is used to hold some request(s)
     """

    def __init__(
        self,
        borrowing_limit_percent: int = None,
        lendable_percent: int = None,
        limit_response: LimitResponse = None,
        nominal_concurrency_shares: int = None,
    ):
        super().__init__(
            borrowing_limit_percent=borrowing_limit_percent,
            lendable_percent=lendable_percent,
            limit_response=limit_response,
            nominal_concurrency_shares=nominal_concurrency_shares,
        )


class PriorityLevelConfigurationSpec(KubernetesObject):
    """PriorityLevelConfigurationSpec specifies the configuration of a priority level."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    _required_ = ["type"]

    exempt: ExemptPriorityLevelConfiguration
    """ `exempt` specifies how requests are handled for an exempt priority level. This field MUST be empty if `type` is `"Limited"`. This field MAY be non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then the default values for `ExemptPriorityLevelConfiguration` apply. """
    limited: LimitedPriorityLevelConfiguration
    """ `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`. """
    type: str
    """ `type` indicates whether this priority level is subject to limitation on request execution.  A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `"Limited"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required. """

    def __init__(
        self, exempt: ExemptPriorityLevelConfiguration = None, limited: LimitedPriorityLevelConfiguration = None, type: str = None
    ):
        super().__init__(exempt=exempt, limited=limited, type=type)


class PriorityLevelConfiguration(KubernetesApiResource):
    """PriorityLevelConfiguration represents the configuration of a priority level."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"
    _api_group_ = "flowcontrol.apiserver.k8s.io"
    _kind_ = "PriorityLevelConfiguration"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: PriorityLevelConfigurationSpec
    """ `spec` is the specification of the desired behavior of a "request-priority". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: PriorityLevelConfigurationSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class PriorityLevelConfigurationCondition(KubernetesObject):
    """PriorityLevelConfigurationCondition defines the condition of priority level."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    last_transition_time: meta.Time
    """ `lastTransitionTime` is the last time the condition transitioned from one status to another. """
    message: str
    """ `message` is a human-readable message indicating details about last transition. """
    reason: str
    """ `reason` is a unique, one-word, CamelCase reason for the condition's last transition. """
    status: str
    """ `status` is the status of the condition. Can be True, False, Unknown. Required. """
    type: str
    """ `type` is the type of the condition. Required. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class PriorityLevelConfigurationStatus(KubernetesObject):
    """PriorityLevelConfigurationStatus represents the current state of a "request-priority"."""

    __slots__ = ()

    _api_version_ = "flowcontrol.apiserver.k8s.io/v1"

    conditions: list[PriorityLevelConfigurationCondition]
    """ `conditions` is the current state of "request-priority". """

    def __init__(self, conditions: list[PriorityLevelConfigurationCondition] = None):
        super().__init__(conditions=conditions)
