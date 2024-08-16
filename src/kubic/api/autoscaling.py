from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class MetricTarget(KubernetesObject):
    """MetricTarget defines the target value, average value, or average utilization of a specific metric"""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["type"]

    average_utilization: int
    """ averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type """
    average_value: core.Quantity
    """ averageValue is the target value of the average of the metric across all relevant pods (as a quantity) """
    type: str
    """ type represents whether the metric type is Utilization, Value, or AverageValue """
    value: core.Quantity
    """ value is the target value of the metric (as a quantity). """

    def __init__(self, average_utilization: int = None, average_value: core.Quantity = None, type: str = None, value: core.Quantity = None):
        super().__init__(average_utilization=average_utilization, average_value=average_value, type=type, value=value)


class ContainerResourceMetricSource(KubernetesObject):
    """ContainerResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["container", "name", "target"]

    container: str
    """ container is the name of the container in the pods of the scaling target """
    name: str
    """ name is the name of the resource in question. """
    target: MetricTarget
    """ target specifies the target value for the given metric """

    def __init__(self, container: str = None, name: str = None, target: MetricTarget = None):
        super().__init__(container=container, name=name, target=target)


class MetricValueStatus(KubernetesObject):
    """MetricValueStatus holds the current value for a metric"""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    average_utilization: int
    """ currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. """
    average_value: core.Quantity
    """ averageValue is the current value of the average of the metric across all relevant pods (as a quantity) """
    value: core.Quantity
    """ value is the current value of the metric (as a quantity). """

    def __init__(self, average_utilization: int = None, average_value: core.Quantity = None, value: core.Quantity = None):
        super().__init__(average_utilization=average_utilization, average_value=average_value, value=value)


class ContainerResourceMetricStatus(KubernetesObject):
    """ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing a single container in each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["container", "current", "name"]

    container: str
    """ container is the name of the container in the pods of the scaling target """
    current: MetricValueStatus
    """ current contains the current value for the given metric """
    name: str
    """ name is the name of the resource in question. """

    def __init__(self, container: str = None, current: MetricValueStatus = None, name: str = None):
        super().__init__(container=container, current=current, name=name)


class CrossVersionObjectReference(KubernetesObject):
    """CrossVersionObjectReference contains enough information to let you identify the referred resource."""

    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    _required_ = ["kind", "name"]

    api_version: str
    """ apiVersion is the API version of the referent """
    kind: str
    """ kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds """
    name: str
    """ name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names """

    def __init__(self, api_version: str = None, kind: str = None, name: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name)


class MetricIdentifier(KubernetesObject):
    """MetricIdentifier defines the name and optionally selector for a metric"""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["name"]

    name: str
    """ name is the name of the given metric """
    selector: meta.LabelSelector
    """ selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics. """

    def __init__(self, name: str = None, selector: meta.LabelSelector = None):
        super().__init__(name=name, selector=selector)


class ExternalMetricSource(KubernetesObject):
    """ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["metric", "target"]

    metric: MetricIdentifier
    """ metric identifies the target metric by name and selector """
    target: MetricTarget
    """ target specifies the target value for the given metric """

    def __init__(self, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(metric=metric, target=target)


class ExternalMetricStatus(KubernetesObject):
    """ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "metric"]

    current: MetricValueStatus
    """ current contains the current value for the given metric """
    metric: MetricIdentifier
    """ metric identifies the target metric by name and selector """

    def __init__(self, current: MetricValueStatus = None, metric: MetricIdentifier = None):
        super().__init__(current=current, metric=metric)


class HPAScalingPolicy(KubernetesObject):
    """HPAScalingPolicy is a single policy which must hold true for a specified past interval."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["period_seconds", "type", "value"]

    period_seconds: int
    """ periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). """
    type: str
    """ type is used to specify the scaling policy. """
    value: int
    """ value contains the amount of change which is permitted by the policy. It must be greater than zero """

    def __init__(self, period_seconds: int = None, type: str = None, value: int = None):
        super().__init__(period_seconds=period_seconds, type=type, value=value)


class HPAScalingRules(KubernetesObject):
    """HPAScalingRules configures the scaling behavior for one direction. These Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    policies: list[HPAScalingPolicy]
    """ policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid """
    select_policy: str
    """ selectPolicy is used to specify which policy should be used. If not set, the default value Max is used. """
    stabilization_window_seconds: int
    """ stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). """

    def __init__(self, policies: list[HPAScalingPolicy] = None, select_policy: str = None, stabilization_window_seconds: int = None):
        super().__init__(policies=policies, select_policy=select_policy, stabilization_window_seconds=stabilization_window_seconds)


class HorizontalPodAutoscalerSpec(KubernetesObject):
    """specification of a horizontal pod autoscaler."""

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
    """ maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas. """
    min_replicas: int
    """ minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. """
    scale_target_ref: CrossVersionObjectReference
    """ reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource. """
    target_cpu_utilization_percentage: int
    """ targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used. """

    def __init__(
        self,
        max_replicas: int = None,
        min_replicas: int = None,
        scale_target_ref: CrossVersionObjectReference = None,
        target_cpu_utilization_percentage: int = None,
    ):
        super().__init__(
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            scale_target_ref=scale_target_ref,
            target_cpu_utilization_percentage=target_cpu_utilization_percentage,
        )


class HorizontalPodAutoscaler(KubernetesApiResource):
    """configuration of a horizontal pod autoscaler."""

    __slots__ = ()

    _api_version_ = "autoscaling/v1"
    _api_group_ = "autoscaling"
    _kind_ = "HorizontalPodAutoscaler"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: HorizontalPodAutoscalerSpec
    """ spec defines the behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: HorizontalPodAutoscalerSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class HorizontalPodAutoscalerBehavior(KubernetesObject):
    """HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively)."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    scale_down: HPAScalingRules
    """ scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used). """
    scale_up: HPAScalingRules
    """
    scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:
      * increase no more than 4 pods per 60 seconds
      * double the number of pods per 60 seconds
    No stabilization is used.
    """

    def __init__(self, scale_down: HPAScalingRules = None, scale_up: HPAScalingRules = None):
        super().__init__(scale_down=scale_down, scale_up=scale_up)


class HorizontalPodAutoscalerCondition(KubernetesObject):
    """HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ lastTransitionTime is the last time the condition transitioned from one status to another """
    message: str
    """ message is a human-readable explanation containing details about the transition """
    reason: str
    """ reason is the reason for the condition's last transition. """
    status: str
    """ status is the status of the condition (True, False, Unknown) """
    type: str
    """ type describes the current condition """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class HorizontalPodAutoscalerStatus(KubernetesObject):
    """current status of a horizontal pod autoscaler"""

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
    """ currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU. """
    current_replicas: int
    """ currentReplicas is the current number of replicas of pods managed by this autoscaler. """
    desired_replicas: int
    """ desiredReplicas is the  desired number of replicas of pods managed by this autoscaler. """
    last_scale_time: meta.Time
    """ lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed. """
    observed_generation: int
    """ observedGeneration is the most recent generation observed by this autoscaler. """

    def __init__(
        self,
        current_cpu_utilization_percentage: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
        last_scale_time: meta.Time = None,
        observed_generation: int = None,
    ):
        super().__init__(
            current_cpu_utilization_percentage=current_cpu_utilization_percentage,
            current_replicas=current_replicas,
            desired_replicas=desired_replicas,
            last_scale_time=last_scale_time,
            observed_generation=observed_generation,
        )


class ObjectMetricSource(KubernetesObject):
    """ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object)."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["described_object", "metric", "target"]

    described_object: CrossVersionObjectReference
    """ describedObject specifies the descriptions of a object,such as kind,name apiVersion """
    metric: MetricIdentifier
    """ metric identifies the target metric by name and selector """
    target: MetricTarget
    """ target specifies the target value for the given metric """

    def __init__(self, described_object: CrossVersionObjectReference = None, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(described_object=described_object, metric=metric, target=target)


class PodsMetricSource(KubernetesObject):
    """PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["metric", "target"]

    metric: MetricIdentifier
    """ metric identifies the target metric by name and selector """
    target: MetricTarget
    """ target specifies the target value for the given metric """

    def __init__(self, metric: MetricIdentifier = None, target: MetricTarget = None):
        super().__init__(metric=metric, target=target)


class ResourceMetricSource(KubernetesObject):
    """ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.  Only one "target" type should be set."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["name", "target"]

    name: str
    """ name is the name of the resource in question. """
    target: MetricTarget
    """ target specifies the target value for the given metric """

    def __init__(self, name: str = None, target: MetricTarget = None):
        super().__init__(name=name, target=target)


class MetricSpec(KubernetesObject):
    """MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once)."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["type"]

    container_resource: ContainerResourceMetricSource
    """ containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag. """
    external: ExternalMetricSource
    """ external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """
    object: ObjectMetricSource
    """ object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """
    pods: PodsMetricSource
    """ pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """
    resource: ResourceMetricSource
    """ resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """
    type: str
    """ type is the type of metric source.  It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """

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


class ObjectMetricStatus(KubernetesObject):
    """ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object)."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "described_object", "metric"]

    current: MetricValueStatus
    """ current contains the current value for the given metric """
    described_object: CrossVersionObjectReference
    """ DescribedObject specifies the descriptions of a object,such as kind,name apiVersion """
    metric: MetricIdentifier
    """ metric identifies the target metric by name and selector """

    def __init__(
        self, current: MetricValueStatus = None, described_object: CrossVersionObjectReference = None, metric: MetricIdentifier = None
    ):
        super().__init__(current=current, described_object=described_object, metric=metric)


class PodsMetricStatus(KubernetesObject):
    """PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second)."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "metric"]

    current: MetricValueStatus
    """ current contains the current value for the given metric """
    metric: MetricIdentifier
    """ metric identifies the target metric by name and selector """

    def __init__(self, current: MetricValueStatus = None, metric: MetricIdentifier = None):
        super().__init__(current=current, metric=metric)


class ResourceMetricStatus(KubernetesObject):
    """ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["current", "name"]

    current: MetricValueStatus
    """ current contains the current value for the given metric """
    name: str
    """ name is the name of the resource in question. """

    def __init__(self, current: MetricValueStatus = None, name: str = None):
        super().__init__(current=current, name=name)


class MetricStatus(KubernetesObject):
    """MetricStatus describes the last-read state of a single metric."""

    __slots__ = ()

    _api_version_ = "autoscaling/v2"

    _required_ = ["type"]

    container_resource: ContainerResourceMetricStatus
    """ container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """
    external: ExternalMetricStatus
    """ external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). """
    object: ObjectMetricStatus
    """ object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object). """
    pods: PodsMetricStatus
    """ pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value. """
    resource: ResourceMetricStatus
    """ resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. """
    type: str
    """ type is the type of metric source.  It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled """

    def __init__(
        self,
        container_resource: ContainerResourceMetricStatus = None,
        external: ExternalMetricStatus = None,
        object: ObjectMetricStatus = None,
        pods: PodsMetricStatus = None,
        resource: ResourceMetricStatus = None,
        type: str = None,
    ):
        super().__init__(container_resource=container_resource, external=external, object=object, pods=pods, resource=resource, type=type)


class ScaleSpec(KubernetesObject):
    """ScaleSpec describes the attributes of a scale subresource."""

    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    replicas: int
    """ replicas is the desired number of instances for the scaled object. """

    def __init__(self, replicas: int = None):
        super().__init__(replicas=replicas)


class Scale(KubernetesApiResource):
    """Scale represents a scaling request for a resource."""

    __slots__ = ()

    _api_version_ = "autoscaling/v1"
    _api_group_ = "autoscaling"
    _kind_ = "Scale"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata. """
    spec: ScaleSpec
    """ spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ScaleSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ScaleStatus(KubernetesObject):
    """ScaleStatus represents the current status of a scale subresource."""

    __slots__ = ()

    _api_version_ = "autoscaling/v1"

    _required_ = ["replicas"]

    replicas: int
    """ replicas is the actual number of observed instances of the scaled object. """
    selector: str
    """ selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ """

    def __init__(self, replicas: int = None, selector: str = None):
        super().__init__(replicas=replicas, selector=selector)
