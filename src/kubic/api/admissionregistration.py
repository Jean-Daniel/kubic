from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class AuditAnnotation(KubernetesObject):
    """AuditAnnotation describes how to produce an audit annotation for an API request."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["key", "value_expression"]

    key: str
    """
    key specifies the audit annotation key. The audit annotation keys of a ValidatingAdmissionPolicy must be unique. The key must be a qualified name ([A-Za-z0-9][-A-Za-z0-9_.]*) no more than 63 bytes in length.
    
    The key is combined with the resource name of the ValidatingAdmissionPolicy to construct an audit annotation key: "{ValidatingAdmissionPolicy name}/{key}".
    
    If an admission webhook uses the same resource name as this ValidatingAdmissionPolicy and the same audit annotation key, the annotation key will be identical. In this case, the first annotation written with the key will be included in the audit event and all subsequent annotations with the same key will be discarded.
    
    Required.
    """
    value_expression: str
    """
    valueExpression represents the expression which is evaluated by CEL to produce an audit annotation value. The expression must evaluate to either a string or null value. If the expression evaluates to a string, the audit annotation is included with the string value. If the expression evaluates to null or empty string the audit annotation will be omitted. The valueExpression may be no longer than 5kb in length. If the result of the valueExpression is more than 10kb in length, it will be truncated to 10kb.
    
    If multiple ValidatingAdmissionPolicyBinding resources match an API request, then the valueExpression will be evaluated for each binding. All unique values produced by the valueExpressions will be joined together in a comma-separated list.
    
    Required.
    """

    def __init__(self, key: str = None, value_expression: str = None):
        super().__init__(key=key, value_expression=value_expression)


class ExpressionWarning(KubernetesObject):
    """ExpressionWarning is a warning information that targets a specific expression."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["field_ref", "warning"]

    field_ref: str
    """ The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is "spec.validations[0].expression" """
    warning: str
    """ The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler. """

    def __init__(self, field_ref: str = None, warning: str = None):
        super().__init__(field_ref=field_ref, warning=warning)


class MatchCondition(KubernetesObject):
    """MatchCondition represents a condition which must by fulfilled for a request to be sent to a webhook."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["expression", "name"]

    expression: str
    """
    Expression represents the expression which will be evaluated by CEL. Must evaluate to bool. CEL expressions have access to the contents of the AdmissionRequest and Authorizer, organized into CEL variables:
    
    'object' - The object from the incoming request. The value is null for DELETE requests. 'oldObject' - The existing object. The value is null for CREATE requests. 'request' - Attributes of the admission request(/pkg/apis/admission/types.go#AdmissionRequest). 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request.
      See https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
    'authorizer.requestResource' - A CEL ResourceCheck constructed from the 'authorizer' and configured with the
      request resource.
    Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/
    
    Required.
    """
    name: str
    """
    Name is an identifier for this match condition, used for strategic merging of MatchConditions, as well as providing an identifier for logging purposes. A good name should be descriptive of the associated expression. Name must be a qualified name consisting of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName',  or 'my.name',  or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional DNS subdomain prefix and '/' (e.g. 'example.com/MyName')
    
    Required.
    """

    def __init__(self, expression: str = None, name: str = None):
        super().__init__(expression=expression, name=name)


class NamedRuleWithOperations(KubernetesObject):
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    api_groups: list[str]
    """ APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required. """
    api_versions: list[str]
    """ APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required. """
    operations: list[str]
    """ Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required. """
    resource_names: list[str]
    """ ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. """
    resources: list[str]
    """
    Resources is a list of resources this rule applies to.
    
    For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.
    
    If wildcard is present, the validation rule will ensure resources do not overlap with each other.
    
    Depending on the enclosing object, subresources might not be allowed. Required.
    """
    scope: str
    """ scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*". """

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
    """MatchResources decides whether to run the admission control policy on an object based on whether it meets the match criteria. The exclude rules take precedence over include rules (if a resource matches both, it is excluded)"""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    exclude_resource_rules: list[NamedRuleWithOperations]
    """ ExcludeResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over include rules (if a resource matches both, it is excluded) """
    match_policy: str
    """
    matchPolicy defines how the "MatchResources" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".
    
    - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the ValidatingAdmissionPolicy.
    
    - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.
    
    Defaults to "Equivalent"
    """
    namespace_selector: meta.LabelSelector
    """
    NamespaceSelector decides whether to run the admission control policy on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the policy.
    
    For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {
      "matchExpressions": [
        {
          "key": "runlevel",
          "operator": "NotIn",
          "values": [
            "0",
            "1"
          ]
        }
      ]
    }
    
    If instead you want to only run the policy on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {
      "matchExpressions": [
        {
          "key": "environment",
          "operator": "In",
          "values": [
            "prod",
            "staging"
          ]
        }
      ]
    }
    
    See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.
    
    Default to the empty LabelSelector, which matches everything.
    """
    object_selector: meta.LabelSelector
    """ ObjectSelector decides whether to run the validation based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the cel validation, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. """
    resource_rules: list[NamedRuleWithOperations]
    """ ResourceRules describes what operations on what resources/subresources the ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule. """

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
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["name", "namespace"]

    name: str
    """ `name` is the name of the service. Required """
    namespace: str
    """ `namespace` is the namespace of the service. Required """
    path: str
    """ `path` is an optional URL path which will be sent in any request to this service. """
    port: int
    """ If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive). """

    def __init__(self, name: str = None, namespace: str = None, path: str = None, port: int = None):
        super().__init__(name=name, namespace=namespace, path=path, port=port)


class WebhookClientConfig(KubernetesObject):
    """WebhookClientConfig contains the information to make a TLS connection with the webhook"""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    ca_bundle: core.Base64
    """ `caBundle` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. """
    service: ServiceReference
    """
    `service` is a reference to the service for this webhook. Either `service` or `url` must be specified.
    
    If the webhook is running within the cluster, then you should use `service`.
    """
    url: str
    """
    `url` gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.
    
    The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.
    
    Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.
    
    The scheme must be "https"; the URL must begin with "https://".
    
    A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.
    
    Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.
    """

    def __init__(self, ca_bundle: core.Base64 = None, service: ServiceReference = None, url: str = None):
        super().__init__(ca_bundle=ca_bundle, service=service, url=url)


class RuleWithOperations(KubernetesObject):
    """RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    api_groups: list[str]
    """ APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required. """
    api_versions: list[str]
    """ APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required. """
    operations: list[str]
    """ Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required. """
    resources: list[str]
    """
    Resources is a list of resources this rule applies to.
    
    For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.
    
    If wildcard is present, the validation rule will ensure resources do not overlap with each other.
    
    Depending on the enclosing object, subresources might not be allowed. Required.
    """
    scope: str
    """ scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*". """

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
    """MutatingWebhook describes an admission webhook and the resources and operations it applies to."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: list[str]
    """ AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. """
    client_config: WebhookClientConfig
    """ ClientConfig defines how to communicate with the hook. Required """
    failure_policy: str
    """ FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. """
    match_conditions: list[MatchCondition]
    """
    MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.
    
    The exact matching logic is (in order):
      1. If ANY matchCondition evaluates to FALSE, the webhook is skipped.
      2. If ALL matchConditions evaluate to TRUE, the webhook is called.
      3. If any matchCondition evaluates to an error (but none are FALSE):
         - If failurePolicy=Fail, reject the request
         - If failurePolicy=Ignore, the error is ignored and the webhook is skipped
    """
    match_policy: str
    """
    matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".
    
    - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.
    
    - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.
    
    Defaults to "Equivalent"
    """
    name: str
    """ The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. """
    namespace_selector: meta.LabelSelector
    """
    NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.
    
    For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {
      "matchExpressions": [
        {
          "key": "runlevel",
          "operator": "NotIn",
          "values": [
            "0",
            "1"
          ]
        }
      ]
    }
    
    If instead you want to only run the webhook on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {
      "matchExpressions": [
        {
          "key": "environment",
          "operator": "In",
          "values": [
            "prod",
            "staging"
          ]
        }
      ]
    }
    
    See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.
    
    Default to the empty LabelSelector, which matches everything.
    """
    object_selector: meta.LabelSelector
    """ ObjectSelector decides whether to run the webhook based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the webhook, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. """
    reinvocation_policy: str
    """
    reinvocationPolicy indicates whether this webhook should be called multiple times as part of a single admission evaluation. Allowed values are "Never" and "IfNeeded".
    
    Never: the webhook will not be called more than once in a single admission evaluation.
    
    IfNeeded: the webhook will be called at least one additional time as part of the admission evaluation if the object being admitted is modified by other admission plugins after the initial webhook call. Webhooks that specify this option *must* be idempotent, able to process objects they previously admitted. Note: * the number of additional invocations is not guaranteed to be exactly one. * if additional invocations result in further modifications to the object, webhooks are not guaranteed to be invoked again. * webhooks that use this option may be reordered to minimize the number of additional invocations. * to validate an object after all mutations are guaranteed complete, use a validating admission webhook instead.
    
    Defaults to "Never".
    """
    rules: list[RuleWithOperations]
    """ Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects. """
    side_effects: str
    """ SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. """
    timeout_seconds: int
    """ TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. """

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
    """MutatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and may change the object."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "MutatingWebhookConfiguration"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """
    webhooks: list[MutatingWebhook]
    """ Webhooks is a list of webhooks and the affected resources and operations. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, webhooks: list[MutatingWebhook] = None):
        super().__init__(name, "", metadata=metadata, webhooks=webhooks)


class ParamKind(KubernetesObject):
    """ParamKind is a tuple of Group Kind and Version."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    api_version: str
    """ APIVersion is the API group version the resources belong to. In format of "group/version". Required. """
    kind: str
    """ Kind is the API kind the resources belong to. Required. """

    def __init__(self, api_version: str = None, kind: str = None):
        super().__init__(api_version=api_version, kind=kind)


class ParamRef(KubernetesObject):
    """ParamRef describes how to locate the params to be used as input to expressions of rules applied by a policy binding."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    name: str
    """
    name is the name of the resource being referenced.
    
    One of `name` or `selector` must be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset.
    
    A single parameter used for all admission requests can be configured by setting the `name` field, leaving `selector` blank, and setting namespace if `paramKind` is namespace-scoped.
    """
    namespace: str
    """
    namespace is the namespace of the referenced resource. Allows limiting the search for params to a specific namespace. Applies to both `name` and `selector` fields.
    
    A per-namespace parameter may be used by specifying a namespace-scoped `paramKind` in the policy and leaving this field empty.
    
    - If `paramKind` is cluster-scoped, this field MUST be unset. Setting this field results in a configuration error.
    
    - If `paramKind` is namespace-scoped, the namespace of the object being evaluated for admission will be used when this field is left unset. Take care that if this is left empty the binding must not match any cluster-scoped resources, which will result in an error.
    """
    parameter_not_found_action: str
    """
    `parameterNotFoundAction` controls the behavior of the binding when the resource exists, and name or selector is valid, but there are no parameters matched by the binding. If the value is set to `Allow`, then no matched parameters will be treated as successful validation by the binding. If set to `Deny`, then no matched parameters will be subject to the `failurePolicy` of the policy.
    
    Allowed values are `Allow` or `Deny`
    
    Required
    """
    selector: meta.LabelSelector
    """
    selector can be used to match multiple param objects based on their labels. Supply selector: {} to match all resources of the ParamKind.
    
    If multiple params are found, they are all evaluated with the policy expressions and the results are ANDed together.
    
    One of `name` or `selector` must be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset.
    """

    def __init__(
        self, name: str = None, namespace: str = None, parameter_not_found_action: str = None, selector: meta.LabelSelector = None
    ):
        super().__init__(name=name, namespace=namespace, parameter_not_found_action=parameter_not_found_action, selector=selector)


class TypeChecking(KubernetesObject):
    """TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy"""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    expression_warnings: list[ExpressionWarning]
    """ The type checking warnings for each expression. """

    def __init__(self, expression_warnings: list[ExpressionWarning] = None):
        super().__init__(expression_warnings=expression_warnings)


class Validation(KubernetesObject):
    """Validation specifies the CEL expression which is used to apply the validation."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["expression"]

    expression: str
    """
    Expression represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec CEL expressions have access to the contents of the API request/response, organized into CEL variables as well as some other useful variables:
    
    - 'object' - The object from the incoming request. The value is null for DELETE requests. - 'oldObject' - The existing object. The value is null for CREATE requests. - 'request' - Attributes of the API request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - Parameter resource referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind. - 'namespaceObject' - The namespace object that the incoming object belongs to. The value is null for cluster-scoped resources. - 'variables' - Map of composited variables, from its name to its lazily evaluated value.
      For example, a variable named 'foo' can be accessed as 'variables.foo'.
    - 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal (user or service account) of the request.
      See https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz
    - 'authorizer.requestResource' - A CEL ResourceCheck constructed from the 'authorizer' and configured with the
      request resource.
    
    The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object. No other metadata properties are accessible.
    
    Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:
    	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if",
    	  "import", "let", "loop", "package", "namespace", "return".
    Examples:
      - Expression accessing a property named "namespace": {"Expression": "object.__namespace__ > 0"}
      - Expression accessing a property named "x-prop": {"Expression": "object.x__dash__prop > 0"}
      - Expression accessing a property named "redact__d": {"Expression": "object.redact__underscores__d > 0"}
    
    Equality on arrays with list type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:
      - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and
        non-intersecting elements in `Y` are appended, retaining their partial order.
      - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values
        are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with
        non-intersecting keys are appended, retaining their partial order.
    Required.
    """
    message: str
    """ Message represents the message displayed when validation fails. The message is required if the Expression contains line breaks. The message must not contain line breaks. If unset, the message is "failed rule: {Rule}". e.g. "must be a URL with the host matching spec.host" If the Expression contains line breaks. Message is required. The message must not contain line breaks. If unset, the message is "failed Expression: {Expression}". """
    message_expression: str
    """ messageExpression declares a CEL expression that evaluates to the validation failure message that is returned when this rule fails. Since messageExpression is used as a failure message, it must evaluate to a string. If both message and messageExpression are present on a validation, then messageExpression will be used if validation fails. If messageExpression results in a runtime error, the runtime error is logged, and the validation failure message is produced as if the messageExpression field were unset. If messageExpression evaluates to an empty string, a string with only spaces, or a string that contains line breaks, then the validation failure message will also be produced as if the messageExpression field were unset, and the fact that messageExpression produced an empty string/string with only spaces/string with line breaks will be logged. messageExpression has access to all the same variables as the `expression` except for 'authorizer' and 'authorizer.requestResource'. Example: "object.x must be less than max ("+string(params.max)+")" """
    reason: str
    """ Reason represents a machine-readable description of why this validation failed. If this is the first validation in the list to fail, this reason, as well as the corresponding HTTP response code, are used in the HTTP response to the client. The currently supported reasons are: "Unauthorized", "Forbidden", "Invalid", "RequestEntityTooLarge". If not set, StatusReasonInvalid is used in the response to the client. """

    def __init__(self, expression: str = None, message: str = None, message_expression: str = None, reason: str = None):
        super().__init__(expression=expression, message=message, message_expression=message_expression, reason=reason)


class Variable(KubernetesObject):
    """Variable is the definition of a variable that is used for composition. A variable is defined as a named expression."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["expression", "name"]

    expression: str
    """ Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation. """
    name: str
    """ Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through `variables` For example, if name is "foo", the variable will be available as `variables.foo` """

    def __init__(self, expression: str = None, name: str = None):
        super().__init__(expression=expression, name=name)


class ValidatingAdmissionPolicySpec(KubernetesObject):
    """ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    audit_annotations: list[AuditAnnotation]
    """ auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required. """
    failure_policy: str
    """
    failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.
    
    A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.
    
    failurePolicy does not define how validations that evaluate to false are handled.
    
    When failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how failures are enforced.
    
    Allowed values are Ignore or Fail. Defaults to Fail.
    """
    match_conditions: list[MatchCondition]
    """
    MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.
    
    If a parameter object is provided, it can be accessed via the `params` handle in the same manner as validation expressions.
    
    The exact matching logic is (in order):
      1. If ANY matchCondition evaluates to FALSE, the policy is skipped.
      2. If ALL matchConditions evaluate to TRUE, the policy is evaluated.
      3. If any matchCondition evaluates to an error (but none are FALSE):
         - If failurePolicy=Fail, reject the request
         - If failurePolicy=Ignore, the policy is skipped
    """
    match_constraints: MatchResources
    """ MatchConstraints specifies what resources this policy is designed to validate. The AdmissionPolicy cares about a request if it matches _all_ Constraints. However, in order to prevent clusters from being put into an unstable state that cannot be recovered from via the API ValidatingAdmissionPolicy cannot match ValidatingAdmissionPolicy and ValidatingAdmissionPolicyBinding. Required. """
    param_kind: ParamKind
    """ ParamKind specifies the kind of resources used to parameterize this policy. If absent, there are no parameters for this policy and the param CEL variable will not be provided to validation expressions. If ParamKind refers to a non-existent kind, this policy definition is mis-configured and the FailurePolicy is applied. If paramKind is specified but paramRef is unset in ValidatingAdmissionPolicyBinding, the params variable will be null. """
    validations: list[Validation]
    """ Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required. """
    variables: list[Variable]
    """
    Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under `variables` in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.
    
    The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic.
    """

    def __init__(
        self,
        audit_annotations: list[AuditAnnotation] = None,
        failure_policy: str = None,
        match_conditions: list[MatchCondition] = None,
        match_constraints: MatchResources = None,
        param_kind: ParamKind = None,
        validations: list[Validation] = None,
        variables: list[Variable] = None,
    ):
        super().__init__(
            audit_annotations=audit_annotations,
            failure_policy=failure_policy,
            match_conditions=match_conditions,
            match_constraints=match_constraints,
            param_kind=param_kind,
            validations=validations,
            variables=variables,
        )


class ValidatingAdmissionPolicy(KubernetesApiResource):
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or rejects an object without changing it."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingAdmissionPolicy"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """
    spec: ValidatingAdmissionPolicySpec
    """ Specification of the desired behavior of the ValidatingAdmissionPolicy. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ValidatingAdmissionPolicySpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ValidatingAdmissionPolicyBindingSpec(KubernetesObject):
    """ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    match_resources: MatchResources
    """ MatchResources declares what resources match this binding and will be validated by it. Note that this is intersected with the policy's matchConstraints, so only requests that are matched by the policy can be selected by this. If this is unset, all resources matched by the policy are validated by this binding When resourceRules is unset, it does not constrain resource matching. If a resource is matched by the other fields of this object, it will be validated. Note that this is differs from ValidatingAdmissionPolicy matchConstraints, where resourceRules are required. """
    param_ref: ParamRef
    """ paramRef specifies the parameter resource used to configure the admission control policy. It should point to a resource of the type specified in ParamKind of the bound ValidatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the ValidatingAdmissionPolicy applied. If the policy does not specify a ParamKind then this field is ignored, and the rules are evaluated without a param. """
    policy_name: str
    """ PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. """
    validation_actions: list[str]
    """
    validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.
    
    Failures defined by the ValidatingAdmissionPolicy's FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.
    
    validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.
    
    The supported actions values are:
    
    "Deny" specifies that a validation failure results in a denied request.
    
    "Warn" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.
    
    "Audit" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: `"validation.policy.admission.k8s.io/validation_failure": "[{"message": "Invalid value", {"policy": "policy.example.com", {"binding": "policybinding.example.com", {"expressionIndex": "1", {"validationActions": ["Audit"]}]"`
    
    Clients should expect to handle additional values by ignoring any values not recognized.
    
    "Deny" and "Warn" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.
    
    Required.
    """

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
    """
    ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

    For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.

    The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.
    """

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingAdmissionPolicyBinding"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """
    spec: ValidatingAdmissionPolicyBindingSpec
    """ Specification of the desired behavior of the ValidatingAdmissionPolicyBinding. """

    def __init__(
        self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ValidatingAdmissionPolicyBindingSpec = None
    ):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ValidatingAdmissionPolicyStatus(KubernetesObject):
    """ValidatingAdmissionPolicyStatus represents the status of an admission validation policy."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    conditions: list[meta.Condition]
    """ The conditions represent the latest available observations of a policy's current state. """
    observed_generation: int
    """ The generation observed by the controller. """
    type_checking: TypeChecking
    """ The results of type checking for each expression. Presence of this field indicates the completion of the type checking. """

    def __init__(self, conditions: list[meta.Condition] = None, observed_generation: int = None, type_checking: TypeChecking = None):
        super().__init__(conditions=conditions, observed_generation=observed_generation, type_checking=type_checking)


class ValidatingWebhook(KubernetesObject):
    """ValidatingWebhook describes an admission webhook and the resources and operations it applies to."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: list[str]
    """ AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. """
    client_config: WebhookClientConfig
    """ ClientConfig defines how to communicate with the hook. Required """
    failure_policy: str
    """ FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. """
    match_conditions: list[MatchCondition]
    """
    MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.
    
    The exact matching logic is (in order):
      1. If ANY matchCondition evaluates to FALSE, the webhook is skipped.
      2. If ALL matchConditions evaluate to TRUE, the webhook is called.
      3. If any matchCondition evaluates to an error (but none are FALSE):
         - If failurePolicy=Fail, reject the request
         - If failurePolicy=Ignore, the error is ignored and the webhook is skipped
    """
    match_policy: str
    """
    matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".
    
    - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.
    
    - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.
    
    Defaults to "Equivalent"
    """
    name: str
    """ The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. """
    namespace_selector: meta.LabelSelector
    """
    NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.
    
    For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {
      "matchExpressions": [
        {
          "key": "runlevel",
          "operator": "NotIn",
          "values": [
            "0",
            "1"
          ]
        }
      ]
    }
    
    If instead you want to only run the webhook on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {
      "matchExpressions": [
        {
          "key": "environment",
          "operator": "In",
          "values": [
            "prod",
            "staging"
          ]
        }
      ]
    }
    
    See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels for more examples of label selectors.
    
    Default to the empty LabelSelector, which matches everything.
    """
    object_selector: meta.LabelSelector
    """ ObjectSelector decides whether to run the webhook based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the webhook, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything. """
    rules: list[RuleWithOperations]
    """ Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects. """
    side_effects: str
    """ SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. """
    timeout_seconds: int
    """ TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. """

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
    """ValidatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and object without changing it."""

    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"
    _api_group_ = "admissionregistration.k8s.io"
    _kind_ = "ValidatingWebhookConfiguration"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """
    webhooks: list[ValidatingWebhook]
    """ Webhooks is a list of webhooks and the affected resources and operations. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, webhooks: list[ValidatingWebhook] = None):
        super().__init__(name, "", metadata=metadata, webhooks=webhooks)
