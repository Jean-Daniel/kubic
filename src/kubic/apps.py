from typing import List

from . import KubernetesApiResource, KubernetesObject
from . import core, meta


class RollingUpdateDaemonSet(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    max_surge: core.IntOrString
    max_unavailable: core.IntOrString

    def __init__(self, max_surge: core.IntOrString = None, max_unavailable: core.IntOrString = None):
        super().__init__(max_surge=max_surge, max_unavailable=max_unavailable)


class DaemonSetUpdateStrategy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    rolling_update: RollingUpdateDaemonSet
    type: str

    def __init__(self, rolling_update: RollingUpdateDaemonSet = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class DaemonSetSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector", "template"]

    min_ready_seconds: int
    revision_history_limit: int
    selector: meta.LabelSelector
    template: core.PodTemplateSpec
    update_strategy: DaemonSetUpdateStrategy

    def __init__(
        self,
        min_ready_seconds: int = None,
        revision_history_limit: int = None,
        selector: meta.LabelSelector = None,
        template: core.PodTemplateSpec = None,
        update_strategy: DaemonSetUpdateStrategy = None,
    ):
        super().__init__(
            min_ready_seconds=min_ready_seconds,
            revision_history_limit=revision_history_limit,
            selector=selector,
            template=template,
            update_strategy=update_strategy,
        )


class DaemonSet(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _kind_ = "DaemonSet"

    metadata: meta.ObjectMeta
    spec: DaemonSetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DaemonSetSpec = None):
        super().__init__("apps/v1", "DaemonSet", name, namespace, metadata=metadata, spec=spec)


class RollingUpdateDeployment(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    max_surge: core.IntOrString
    max_unavailable: core.IntOrString

    def __init__(self, max_surge: core.IntOrString = None, max_unavailable: core.IntOrString = None):
        super().__init__(max_surge=max_surge, max_unavailable=max_unavailable)


class DeploymentStrategy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    rolling_update: RollingUpdateDeployment
    type: str

    def __init__(self, rolling_update: RollingUpdateDeployment = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class DeploymentSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector", "template"]

    min_ready_seconds: int
    paused: bool
    progress_deadline_seconds: int
    replicas: int
    revision_history_limit: int
    selector: meta.LabelSelector
    strategy: DeploymentStrategy
    template: core.PodTemplateSpec

    def __init__(
        self,
        min_ready_seconds: int = None,
        paused: bool = None,
        progress_deadline_seconds: int = None,
        replicas: int = None,
        revision_history_limit: int = None,
        selector: meta.LabelSelector = None,
        strategy: DeploymentStrategy = None,
        template: core.PodTemplateSpec = None,
    ):
        super().__init__(
            min_ready_seconds=min_ready_seconds,
            paused=paused,
            progress_deadline_seconds=progress_deadline_seconds,
            replicas=replicas,
            revision_history_limit=revision_history_limit,
            selector=selector,
            strategy=strategy,
            template=template,
        )


class Deployment(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _kind_ = "Deployment"

    metadata: meta.ObjectMeta
    spec: DeploymentSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DeploymentSpec = None):
        super().__init__("apps/v1", "Deployment", name, namespace, metadata=metadata, spec=spec)


class RollingUpdateStatefulSetStrategy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    partition: int

    def __init__(self, partition: int = None):
        super().__init__(partition=partition)


class StatefulSetUpdateStrategy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    rolling_update: RollingUpdateStatefulSetStrategy
    type: str

    def __init__(self, rolling_update: RollingUpdateStatefulSetStrategy = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class StatefulSetSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector", "service_name", "template"]

    pod_management_policy: str
    replicas: int
    revision_history_limit: int
    selector: meta.LabelSelector
    service_name: str
    template: core.PodTemplateSpec
    update_strategy: StatefulSetUpdateStrategy
    volume_claim_templates: List[core.PersistentVolumeClaim]

    def __init__(
        self,
        pod_management_policy: str = None,
        replicas: int = None,
        revision_history_limit: int = None,
        selector: meta.LabelSelector = None,
        service_name: str = None,
        template: core.PodTemplateSpec = None,
        update_strategy: StatefulSetUpdateStrategy = None,
        volume_claim_templates: List[core.PersistentVolumeClaim] = None,
    ):
        super().__init__(
            pod_management_policy=pod_management_policy,
            replicas=replicas,
            revision_history_limit=revision_history_limit,
            selector=selector,
            service_name=service_name,
            template=template,
            update_strategy=update_strategy,
            volume_claim_templates=volume_claim_templates,
        )


class StatefulSet(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _kind_ = "StatefulSet"

    metadata: meta.ObjectMeta
    spec: StatefulSetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StatefulSetSpec = None):
        super().__init__("apps/v1", "StatefulSet", name, namespace, metadata=metadata, spec=spec)
