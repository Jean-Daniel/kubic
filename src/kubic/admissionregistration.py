from typing import List

from . import KubernetesApiResource, KubernetesObject
from . import core, meta


class ServiceReference(KubernetesObject):
    __slots__ = ()

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    _required_ = ["name", "namespace"]

    name: str
    namespace: str
    path: str
    port: int

    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        path: str = None,
        port: int = None,
    ):
        super().__init__(name=name, namespace=namespace, path=path, port=port)


class WebhookClientConfig(KubernetesObject):
    __slots__ = ()

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    ca_bundle: core.Base64
    service: ServiceReference
    url: str

    def __init__(
        self,
        ca_bundle: core.Base64 = None,
        service: ServiceReference = None,
        url: str = None,
    ):
        super().__init__(ca_bundle=ca_bundle, service=service, url=url)


class RuleWithOperations(KubernetesObject):
    __slots__ = ()

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    api_groups: List[str]
    api_versions: List[str]
    operations: List[str]
    resources: List[str]
    scope: str

    def __init__(
        self,
        api_groups: List[str] = None,
        api_versions: List[str] = None,
        operations: List[str] = None,
        resources: List[str] = None,
        scope: str = None,
    ):
        super().__init__(
            api_groups=api_groups,
            api_versions=api_versions,
            operations=operations,
            resources=resources,
            scope=scope,
        )


class MutatingWebhook(KubernetesObject):
    __slots__ = ()

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: List[str]
    client_config: WebhookClientConfig
    failure_policy: str
    match_policy: str
    name: str
    namespace_selector: meta.LabelSelector
    object_selector: meta.LabelSelector
    reinvocation_policy: str
    rules: List[RuleWithOperations]
    side_effects: str
    timeout_seconds: int

    def __init__(
        self,
        admission_review_versions: List[str] = None,
        client_config: WebhookClientConfig = None,
        failure_policy: str = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: meta.LabelSelector = None,
        object_selector: meta.LabelSelector = None,
        reinvocation_policy: str = None,
        rules: List[RuleWithOperations] = None,
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

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    metadata: meta.ObjectMeta
    webhooks: List[MutatingWebhook]

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        webhooks: List[MutatingWebhook] = None,
    ):
        super().__init__(
            "admissionregistration.k8s.io/v1",
            "MutatingWebhookConfiguration",
            name,
            "",
            metadata=metadata,
            webhooks=webhooks,
        )


class ValidatingWebhook(KubernetesObject):
    __slots__ = ()

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    admission_review_versions: List[str]
    client_config: WebhookClientConfig
    failure_policy: str
    match_policy: str
    name: str
    namespace_selector: meta.LabelSelector
    object_selector: meta.LabelSelector
    rules: List[RuleWithOperations]
    side_effects: str
    timeout_seconds: int

    def __init__(
        self,
        admission_review_versions: List[str] = None,
        client_config: WebhookClientConfig = None,
        failure_policy: str = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: meta.LabelSelector = None,
        object_selector: meta.LabelSelector = None,
        rules: List[RuleWithOperations] = None,
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

    _group_ = "admissionregistration.k8s.io"
    _version_ = "v1"

    metadata: meta.ObjectMeta
    webhooks: List[ValidatingWebhook]

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        webhooks: List[ValidatingWebhook] = None,
    ):
        super().__init__(
            "admissionregistration.k8s.io/v1",
            "ValidatingWebhookConfiguration",
            name,
            "",
            metadata=metadata,
            webhooks=webhooks,
        )
