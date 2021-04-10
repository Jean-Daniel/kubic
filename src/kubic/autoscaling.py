from typing import List

from . import KubernetesApiResource, KubernetesObject
from . import core, meta


class MetricTarget(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["type"]

    average_utilization: int
    average_value: core.Quantity
    type: str
    value: core.Quantity

    def __init__(self, average_utilization: int = None, average_value: core.Quantity = None, type: str = None, value: core.Quantity = None):
        super().__init__(average_utilization=average_utilization, average_value=average_value, type=type, value=value)


class ContainerResourceMetricSource(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["container", "name", "target"]

    container: str
    name: str
    target: MetricTarget

    def __init__(self, container: str = None, name: str = None, target: MetricTarget = None):
        super().__init__(container=container, name=name, target=target)


class CrossVersionObjectReference(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["kind", "name"]

    api_version: str
    kind: str
    name: str

    def __init__(self, api_version: str = None, kind: str = None, name: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name)


class MetricIdentifier(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["name"]

    name: str
    selector: meta.LabelSelector

    def __init__(self, name: str = None, selector: meta.LabelSelector = None):
        super().__init__(name=name, selector=selector)


class ExternalMetricSource(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["metric", "target"]

    metric: MetricIdentifier
    target: MetricTarget

    def __init__(self, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(metric=metric, target=target)


class HPAScalingPolicy(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["period_seconds", "type", "value"]

    period_seconds: int
    type: str
    value: int

    def __init__(self, period_seconds: int = None, type: str = None, value: int = None):
        super().__init__(period_seconds=period_seconds, type=type, value=value)


class HPAScalingRules(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    policies: List[HPAScalingPolicy]
    select_policy: str
    stabilization_window_seconds: int

    def __init__(self, policies: List[HPAScalingPolicy] = None, select_policy: str = None, stabilization_window_seconds: int = None):
        super().__init__(policies=policies, select_policy=select_policy, stabilization_window_seconds=stabilization_window_seconds)


class HorizontalPodAutoscalerBehavior(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    scale_down: HPAScalingRules
    scale_up: HPAScalingRules

    def __init__(self, scale_down: HPAScalingRules = None, scale_up: HPAScalingRules = None):
        super().__init__(scale_down=scale_down, scale_up=scale_up)


class ObjectMetricSource(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["described_object", "metric", "target"]

    described_object: CrossVersionObjectReference
    metric: MetricIdentifier
    target: MetricTarget

    def __init__(self, described_object: CrossVersionObjectReference = None, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(described_object=described_object, metric=metric, target=target)


class PodsMetricSource(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["metric", "target"]

    metric: MetricIdentifier
    target: MetricTarget

    def __init__(self, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(metric=metric, target=target)


class ResourceMetricSource(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["name", "target"]

    name: str
    target: MetricTarget

    def __init__(self, name: str = None, target: MetricTarget = None):
        super().__init__(name=name, target=target)


class MetricSpec(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["type"]

    container_resource: ContainerResourceMetricSource
    external: ExternalMetricSource
    object: ObjectMetricSource
    pods: PodsMetricSource
    resource: ResourceMetricSource
    type: str

    def __init__(
        self,
        container_resource: ContainerResourceMetricSource = None,
        external: ExternalMetricSource = None,
        object: ObjectMetricSource = None,
        pods: PodsMetricSource = None,
        resource: ResourceMetricSource = None,
        type: str = None,
    ):
        super().__init__(container_resource=container_resource, external=external, object=object, pods=pods, resource=resource, type=type)


class HorizontalPodAutoscalerSpec(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v2beta2"

    _required_ = ["max_replicas", "scale_target_ref"]

    behavior: HorizontalPodAutoscalerBehavior
    max_replicas: int
    metrics: List[MetricSpec]
    min_replicas: int
    scale_target_ref: CrossVersionObjectReference

    def __init__(
        self,
        behavior: HorizontalPodAutoscalerBehavior = None,
        max_replicas: int = None,
        metrics: List[MetricSpec] = None,
        min_replicas: int = None,
        scale_target_ref: CrossVersionObjectReference = None,
    ):
        super().__init__(
            behavior=behavior, max_replicas=max_replicas, metrics=metrics, min_replicas=min_replicas, scale_target_ref=scale_target_ref
        )


class HorizontalPodAutoscaler(KubernetesApiResource):
    __slots__ = ()

    _kind_ = "HorizontalPodAutoscaler"
    _group_ = "autoscaling"
    _version_ = "v2beta2"

    metadata: meta.ObjectMeta
    spec: HorizontalPodAutoscalerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: HorizontalPodAutoscalerSpec = None):
        super().__init__("autoscaling/v2beta2", "HorizontalPodAutoscaler", name, namespace, metadata=metadata, spec=spec)
