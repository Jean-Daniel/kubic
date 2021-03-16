from typing import Any, Dict, List

from .. import api
from ..base import KubernetesObject, KubernetesApiResource


class UpdatePolicy(KubernetesObject):
    __slots__ = ()

    update_mode: str

    def __init__(self, update_mode: str = None):
        super().__init__(update_mode=update_mode)


class ResourcePolicy(KubernetesObject):
    __slots__ = ()

    container_policies: List[Dict[str, Any]]

    def __init__(self, container_policies: List[Dict[str, Any]] = None):
        super().__init__(container_policies=container_policies)


class VerticalPodAutoscalerSpec(KubernetesObject):
    __slots__ = ()

    resource_policy: ResourcePolicy
    target_ref: api.CrossVersionObjectReference
    update_policy: UpdatePolicy

    def __init__(
        self,
        resource_policy: ResourcePolicy = None,
        target_ref: api.CrossVersionObjectReference = None,
        update_policy: UpdatePolicy = None,
    ):
        super().__init__(
            resource_policy=resource_policy,
            target_ref=target_ref,
            update_policy=update_policy,
        )


class VerticalPodAutoscaler(KubernetesApiResource):
    __slots__ = ()

    _group_ = "autoscaling.k8s.io"

    metadata: api.ObjectMeta
    spec: VerticalPodAutoscalerSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: api.ObjectMeta = None,
        spec: VerticalPodAutoscalerSpec = None,
    ):
        super().__init__(
            "autoscaling.k8s.io/v1beta2",
            "VerticalPodAutoscaler",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )
