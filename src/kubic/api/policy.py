from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class Eviction(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "policy/v1"
    _api_group_ = "policy"
    _kind_ = "Eviction"
    _scope_ = "namespace"

    delete_options: meta.DeleteOptions
    metadata: meta.ObjectMeta

    def __init__(self, name: str, namespace: str = None, delete_options: meta.DeleteOptions = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, namespace, delete_options=delete_options, metadata=metadata)


class PodDisruptionBudgetSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1"

    max_unavailable: core.IntOrString
    min_available: core.IntOrString
    selector: meta.LabelSelector

    def __init__(
        self, max_unavailable: core.IntOrString = None, min_available: core.IntOrString = None, selector: meta.LabelSelector = None
    ):
        super().__init__(max_unavailable=max_unavailable, min_available=min_available, selector=selector)


class PodDisruptionBudget(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "policy/v1"
    _api_group_ = "policy"
    _kind_ = "PodDisruptionBudget"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PodDisruptionBudgetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodDisruptionBudgetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PodDisruptionBudgetList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "policy/v1"
    _api_group_ = "policy"
    _kind_ = "PodDisruptionBudgetList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PodDisruptionBudget]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PodDisruptionBudget] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class PodDisruptionBudgetStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1"

    _required_ = ["current_healthy", "desired_healthy", "disruptions_allowed", "expected_pods"]

    conditions: list[meta.Condition]
    current_healthy: int
    desired_healthy: int
    disrupted_pods: dict[str, meta.Time]
    disruptions_allowed: int
    expected_pods: int
    observed_generation: int

    def __init__(
        self,
        conditions: list[meta.Condition] = None,
        current_healthy: int = None,
        desired_healthy: int = None,
        disrupted_pods: dict[str, meta.Time] = None,
        disruptions_allowed: int = None,
        expected_pods: int = None,
        observed_generation: int = None,
    ):
        super().__init__(
            conditions=conditions,
            current_healthy=current_healthy,
            desired_healthy=desired_healthy,
            disrupted_pods=disrupted_pods,
            disruptions_allowed=disruptions_allowed,
            expected_pods=expected_pods,
            observed_generation=observed_generation,
        )
