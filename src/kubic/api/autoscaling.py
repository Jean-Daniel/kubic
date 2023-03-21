from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta



class MetricTarget(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["type"]

    average_utilization: int
    average_value: core.Quantity
    type: str
    value: core.Quantity

    def __init__(self, average_utilization: int = None, average_value: core.Quantity = None, type: str = None, value: core.Quantity = None):
        super().__init__(average_utilization=average_utilization, average_value=average_value, type=type, value=value)


class ContainerResourceMetricSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["container", "name", "target"]

    container: str
    name: str
    target: MetricTarget

    def __init__(self, container: str = None, name: str = None, target: MetricTarget = None):
        super().__init__(container=container, name=name, target=target)


class MetricValueStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    average_utilization: int
    average_value: core.Quantity
    value: core.Quantity

    def __init__(self, average_utilization: int = None, average_value: core.Quantity = None, value: core.Quantity = None):
        super().__init__(average_utilization=average_utilization, average_value=average_value, value=value)


class ContainerResourceMetricStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["container", "current", "name"]

    container: str
    current: MetricValueStatus
    name: str

    def __init__(self, container: str = None, current: MetricValueStatus = None, name: str = None):
        super().__init__(container=container, current=current, name=name)


class CrossVersionObjectReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    _required_ = ["kind", "name"]

    api_version: str
    kind: str
    name: str

    def __init__(self, api_version: str = None, kind: str = None, name: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name)


class MetricIdentifier(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["name"]

    name: str
    selector: meta.LabelSelector

    def __init__(self, name: str = None, selector: meta.LabelSelector = None):
        super().__init__(name=name, selector=selector)


class ExternalMetricSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["metric", "target"]

    metric: MetricIdentifier
    target: MetricTarget

    def __init__(self, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(metric=metric, target=target)


class ExternalMetricStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "metric"]

    current: MetricValueStatus
    metric: MetricIdentifier

    def __init__(self, current: MetricValueStatus = None, metric: MetricIdentifier = None):
        super().__init__(current=current, metric=metric)


class HPAScalingPolicy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["period_seconds", "type", "value"]

    period_seconds: int
    type: str
    value: int

    def __init__(self, period_seconds: int = None, type: str = None, value: int = None):
        super().__init__(period_seconds=period_seconds, type=type, value=value)


class HPAScalingRules(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    policies: list[HPAScalingPolicy]
    select_policy: str
    stabilization_window_seconds: int

    def __init__(self, policies: list[HPAScalingPolicy] = None, select_policy: str = None, stabilization_window_seconds: int = None):
        super().__init__(policies=policies, select_policy=select_policy, stabilization_window_seconds=stabilization_window_seconds)


class HorizontalPodAutoscalerSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    _required_ = ["max_replicas", "scale_target_ref"]

    _field_names_ = {
        "target_cpu_utilization_percentage": "targetCPUUtilizationPercentage",
    }
    _revfield_names_ = {
        "targetCPUUtilizationPercentage": "target_cpu_utilization_percentage",
    }

    max_replicas: int
    min_replicas: int
    scale_target_ref: CrossVersionObjectReference
    target_cpu_utilization_percentage: int

    def __init__(self, max_replicas: int = None, min_replicas: int = None, scale_target_ref: CrossVersionObjectReference = None, target_cpu_utilization_percentage: int = None):
        super().__init__(max_replicas=max_replicas, min_replicas=min_replicas, scale_target_ref=scale_target_ref, target_cpu_utilization_percentage=target_cpu_utilization_percentage)


class HorizontalPodAutoscaler(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"
    _api_group_ = "autoscaling"
    _kind_ = "HorizontalPodAutoscaler"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: HorizontalPodAutoscalerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: HorizontalPodAutoscalerSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class HorizontalPodAutoscalerBehavior(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    scale_down: HPAScalingRules
    scale_up: HPAScalingRules

    def __init__(self, scale_down: HPAScalingRules = None, scale_up: HPAScalingRules = None):
        super().__init__(scale_down=scale_down, scale_up=scale_up)


class HorizontalPodAutoscalerCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class HorizontalPodAutoscalerList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"
    _api_group_ = "autoscaling"
    _kind_ = "HorizontalPodAutoscalerList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[HorizontalPodAutoscaler]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[HorizontalPodAutoscaler] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class HorizontalPodAutoscalerStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    _required_ = ["current_replicas", "desired_replicas"]

    _field_names_ = {
        "current_cpu_utilization_percentage": "currentCPUUtilizationPercentage",
    }
    _revfield_names_ = {
        "currentCPUUtilizationPercentage": "current_cpu_utilization_percentage",
    }

    current_cpu_utilization_percentage: int
    current_replicas: int
    desired_replicas: int
    last_scale_time: meta.Time
    observed_generation: int

    def __init__(self, current_cpu_utilization_percentage: int = None, current_replicas: int = None, desired_replicas: int = None, last_scale_time: meta.Time = None, observed_generation: int = None):
        super().__init__(current_cpu_utilization_percentage=current_cpu_utilization_percentage, current_replicas=current_replicas, desired_replicas=desired_replicas, last_scale_time=last_scale_time, observed_generation=observed_generation)


class ObjectMetricSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["described_object", "metric", "target"]

    described_object: CrossVersionObjectReference
    metric: MetricIdentifier
    target: MetricTarget

    def __init__(self, described_object: CrossVersionObjectReference = None, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(described_object=described_object, metric=metric, target=target)


class PodsMetricSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["metric", "target"]

    metric: MetricIdentifier
    target: MetricTarget

    def __init__(self, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(metric=metric, target=target)


class ResourceMetricSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["name", "target"]

    name: str
    target: MetricTarget

    def __init__(self, name: str = None, target: MetricTarget = None):
        super().__init__(name=name, target=target)


class MetricSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["type"]

    container_resource: ContainerResourceMetricSource
    external: ExternalMetricSource
    object: ObjectMetricSource
    pods: PodsMetricSource
    resource: ResourceMetricSource
    type: str

    def __init__(self, container_resource: ContainerResourceMetricSource = None, external: ExternalMetricSource = None, object: ObjectMetricSource = None, pods: PodsMetricSource = None, resource: ResourceMetricSource = None, type: str = None):
        super().__init__(container_resource=container_resource, external=external, object=object, pods=pods, resource=resource, type=type)


class ObjectMetricStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "described_object", "metric"]

    current: MetricValueStatus
    described_object: CrossVersionObjectReference
    metric: MetricIdentifier

    def __init__(self, current: MetricValueStatus = None, described_object: CrossVersionObjectReference = None, metric: MetricIdentifier = None):
        super().__init__(current=current, described_object=described_object, metric=metric)


class PodsMetricStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "metric"]

    current: MetricValueStatus
    metric: MetricIdentifier

    def __init__(self, current: MetricValueStatus = None, metric: MetricIdentifier = None):
        super().__init__(current=current, metric=metric)


class ResourceMetricStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "name"]

    current: MetricValueStatus
    name: str

    def __init__(self, current: MetricValueStatus = None, name: str = None):
        super().__init__(current=current, name=name)


class MetricStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["type"]

    container_resource: ContainerResourceMetricStatus
    external: ExternalMetricStatus
    object: ObjectMetricStatus
    pods: PodsMetricStatus
    resource: ResourceMetricStatus
    type: str

    def __init__(self, container_resource: ContainerResourceMetricStatus = None, external: ExternalMetricStatus = None, object: ObjectMetricStatus = None, pods: PodsMetricStatus = None, resource: ResourceMetricStatus = None, type: str = None):
        super().__init__(container_resource=container_resource, external=external, object=object, pods=pods, resource=resource, type=type)


class ScaleSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    replicas: int

    def __init__(self, replicas: int = None):
        super().__init__(replicas=replicas)


class Scale(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"
    _api_group_ = "autoscaling"
    _kind_ = "Scale"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ScaleSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ScaleSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ScaleStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    _required_ = ["replicas"]

    replicas: int
    selector: str

    def __init__(self, replicas: int = None, selector: str = None):
        super().__init__(replicas=replicas, selector=selector)


