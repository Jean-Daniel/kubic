from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


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


class ValidatingWebhook(KubernetesObject):
    __slots__ = ()

    _api_version_ = "admissionregistration.k8s.io/v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: list[str]
    client_config: WebhookClientConfig
    failure_policy: str
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
