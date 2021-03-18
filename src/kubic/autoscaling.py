from . import KubernetesApiResource, KubernetesObject
from . import meta


class CrossVersionObjectReference(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v1"

    _required_ = ["kind", "name"]

    api_version: str
    kind: str
    name: str

    def __init__(self, api_version: str = None, kind: str = None, name: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name)


class HorizontalPodAutoscalerSpec(KubernetesObject):
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v1"

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
    __slots__ = ()

    _group_ = "autoscaling"
    _version_ = "v1"

    metadata: meta.ObjectMeta
    spec: HorizontalPodAutoscalerSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: HorizontalPodAutoscalerSpec = None,
    ):
        super().__init__(
            "autoscaling/v1",
            "HorizontalPodAutoscaler",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )
