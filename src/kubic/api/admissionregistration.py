from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class AuditAnnotation(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    _required_ = ["key", "value_expression"]

    key: str
    value_expression: str

    def __init__(self, key: str = None, value_expression: str = None):
        super().__init__(key=key, value_expression=value_expression)


class ExpressionWarning(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    _required_ = ["field_ref", "warning"]

    field_ref: str
    warning: str

    def __init__(self, field_ref: str = None, warning: str = None):
        super().__init__(field_ref=field_ref, warning=warning)


class MatchCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["expression", "name"]

    expression: str
    name: str

    def __init__(self, expression: str = None, name: str = None):
        super().__init__(expression=expression, name=name)


class NamedRuleWithOperations(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    api_groups: list[str]
    api_versions: list[str]
    operations: list[str]
    resource_names: list[str]
    resources: list[str]
    scope: str

    def __init__(
        self,
        api_groups: list[str] = None,
        api_versions: list[str] = None,
        operations: list[str] = None,
        resource_names: list[str] = None,
        resources: list[str] = None,
        scope: str = None,
    ):
        super().__init__(
            api_groups=api_groups,
            api_versions=api_versions,
            operations=operations,
            resource_names=resource_names,
            resources=resources,
            scope=scope,
        )


class MatchResources(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    exclude_resource_rules: list[NamedRuleWithOperations]
    match_policy: str
    namespace_selector: meta.LabelSelector
    object_selector: meta.LabelSelector
    resource_rules: list[NamedRuleWithOperations]

    def __init__(
        self,
        exclude_resource_rules: list[NamedRuleWithOperations] = None,
        match_policy: str = None,
        namespace_selector: meta.LabelSelector = None,
        object_selector: meta.LabelSelector = None,
        resource_rules: list[NamedRuleWithOperations] = None,
    ):
        super().__init__(
            exclude_resource_rules=exclude_resource_rules,
            match_policy=match_policy,
            namespace_selector=namespace_selector,
            object_selector=object_selector,
            resource_rules=resource_rules,
        )


class ServiceReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["name", "namespace"]

    name: str
    namespace: str
    path: str
    port: int

    def __init__(self, name: str = None, namespace: str = None, path: str = None, port: int = None):
        super().__init__(name=name, namespace=namespace, path=path, port=port)


class WebhookClientConfig(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    ca_bundle: core.Base64
    service: ServiceReference
    url: str

    def __init__(self, ca_bundle: core.Base64 = None, service: ServiceReference = None, url: str = None):
        super().__init__(ca_bundle=ca_bundle, service=service, url=url)


class RuleWithOperations(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    api_groups: list[str]
    api_versions: list[str]
    operations: list[str]
    resources: list[str]
    scope: str

    def __init__(
        self,
        api_groups: list[str] = None,
        api_versions: list[str] = None,
        operations: list[str] = None,
        resources: list[str] = None,
        scope: str = None,
    ):
        super().__init__(api_groups=api_groups, api_versions=api_versions, operations=operations, resources=resources, scope=scope)


class MutatingWebhook(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: list[str]
    client_config: WebhookClientConfig
    failure_policy: str
    match_conditions: list[MatchCondition]
    match_policy: str
    name: str
    namespace_selector: meta.LabelSelector
    object_selector: meta.LabelSelector
    reinvocation_policy: str
    rules: list[RuleWithOperations]
    side_effects: str
    timeout_seconds: int

    def __init__(
        self,
        admission_review_versions: list[str] = None,
        client_config: WebhookClientConfig = None,
        failure_policy: str = None,
        match_conditions: list[MatchCondition] = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: meta.LabelSelector = None,
        object_selector: meta.LabelSelector = None,
        reinvocation_policy: str = None,
        rules: list[RuleWithOperations] = None,
        side_effects: str = None,
        timeout_seconds: int = None,
    ):
        super().__init__(
            admission_review_versions=admission_review_versions,
            client_config=client_config,
            failure_policy=failure_policy,
            match_conditions=match_conditions,
            match_policy=match_policy,
            name=name,
            namespace_selector=namespace_selector,
            object_selector=object_selector,
            reinvocation_policy=reinvocation_policy,
            rules=rules,
            side_effects=side_effects,
            timeout_seconds=timeout_seconds,
        )


class MutatingWebhookConfiguration(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "MutatingWebhookConfiguration"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    webhooks: list[MutatingWebhook]

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, webhooks: list[MutatingWebhook] = None):
        super().__init__(name, "", metadata=metadata, webhooks=webhooks)


class MutatingWebhookConfigurationList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "MutatingWebhookConfigurationList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[MutatingWebhookConfiguration]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[MutatingWebhookConfiguration] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ParamKind(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    api_version: str
    kind: str

    def __init__(self, api_version: str = None, kind: str = None):
        super().__init__(api_version=api_version, kind=kind)


class ParamRef(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    name: str
    namespace: str

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class TypeChecking(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    expression_warnings: list[ExpressionWarning]

    def __init__(self, expression_warnings: list[ExpressionWarning] = None):
        super().__init__(expression_warnings=expression_warnings)


class Validation(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    _required_ = ["expression"]

    expression: str
    message: str
    message_expression: str
    reason: str

    def __init__(self, expression: str = None, message: str = None, message_expression: str = None, reason: str = None):
        super().__init__(expression=expression, message=message, message_expression=message_expression, reason=reason)


class ValidatingAdmissionPolicySpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    audit_annotations: list[AuditAnnotation]
    failure_policy: str
    match_conditions: list[MatchCondition]
    match_constraints: MatchResources
    param_kind: ParamKind
    validations: list[Validation]

    def __init__(
        self,
        audit_annotations: list[AuditAnnotation] = None,
        failure_policy: str = None,
        match_conditions: list[MatchCondition] = None,
        match_constraints: MatchResources = None,
        param_kind: ParamKind = None,
        validations: list[Validation] = None,
    ):
        super().__init__(
            audit_annotations=audit_annotations,
            failure_policy=failure_policy,
            match_conditions=match_conditions,
            match_constraints=match_constraints,
            param_kind=param_kind,
            validations=validations,
        )


class ValidatingAdmissionPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingAdmissionPolicy"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ValidatingAdmissionPolicySpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ValidatingAdmissionPolicySpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ValidatingAdmissionPolicyBindingSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    match_resources: MatchResources
    param_ref: ParamRef
    policy_name: str
    validation_actions: list[str]

    def __init__(
        self,
        match_resources: MatchResources = None,
        param_ref: ParamRef = None,
        policy_name: str = None,
        validation_actions: list[str] = None,
    ):
        super().__init__(
            match_resources=match_resources, param_ref=param_ref, policy_name=policy_name, validation_actions=validation_actions
        )


class ValidatingAdmissionPolicyBinding(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingAdmissionPolicyBinding"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ValidatingAdmissionPolicyBindingSpec

    def __init__(
        self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ValidatingAdmissionPolicyBindingSpec = None
    ):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ValidatingAdmissionPolicyBindingList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingAdmissionPolicyBindingList"
    _scope_ = "namespace"

    items: list[ValidatingAdmissionPolicyBinding]
    metadata: meta.ListMeta

    def __init__(
        self, name: str, namespace: str = None, items: list[ValidatingAdmissionPolicyBinding] = None, metadata: meta.ListMeta = None
    ):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ValidatingAdmissionPolicyList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingAdmissionPolicyList"
    _scope_ = "namespace"

    items: list[ValidatingAdmissionPolicy]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ValidatingAdmissionPolicy] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ValidatingAdmissionPolicyStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1alpha1"

    conditions: list[meta.Condition]
    observed_generation: int
    type_checking: TypeChecking

    def __init__(self, conditions: list[meta.Condition] = None, observed_generation: int = None, type_checking: TypeChecking = None):
        super().__init__(conditions=conditions, observed_generation=observed_generation, type_checking=type_checking)


class ValidatingWebhook(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: list[str]
    client_config: WebhookClientConfig
    failure_policy: str
    match_conditions: list[MatchCondition]
    match_policy: str
    name: str
    namespace_selector: meta.LabelSelector
    object_selector: meta.LabelSelector
    rules: list[RuleWithOperations]
    side_effects: str
    timeout_seconds: int

    def __init__(
        self,
        admission_review_versions: list[str] = None,
        client_config: WebhookClientConfig = None,
        failure_policy: str = None,
        match_conditions: list[MatchCondition] = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: meta.LabelSelector = None,
        object_selector: meta.LabelSelector = None,
        rules: list[RuleWithOperations] = None,
        side_effects: str = None,
        timeout_seconds: int = None,
    ):
        super().__init__(
            admission_review_versions=admission_review_versions,
            client_config=client_config,
            failure_policy=failure_policy,
            match_conditions=match_conditions,
            match_policy=match_policy,
            name=name,
            namespace_selector=namespace_selector,
            object_selector=object_selector,
            rules=rules,
            side_effects=side_effects,
            timeout_seconds=timeout_seconds,
        )


class ValidatingWebhookConfiguration(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingWebhookConfiguration"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    webhooks: list[ValidatingWebhook]

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, webhooks: list[ValidatingWebhook] = None):
        super().__init__(name, "", metadata=metadata, webhooks=webhooks)


class ValidatingWebhookConfigurationList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingWebhookConfigurationList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ValidatingWebhookConfiguration]
    metadata: meta.ListMeta

    def __init__(
        self, name: str, namespace: str = None, items: list[ValidatingWebhookConfiguration] = None, metadata: meta.ListMeta = None
    ):
        super().__init__(name, namespace, items=items, metadata=metadata)
