from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class ControllerRevision(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "ControllerRevision"
    _scope_ = "namespace"

    _required_ = ["revision"]

    data: core.RawExtension
    metadata: meta.ObjectMeta
    revision: int

    def __init__(
        self, name: str, namespace: str = None, data: core.RawExtension = None, metadata: meta.ObjectMeta = None, revision: int = None
    ):
        super().__init__(name, namespace, data=data, metadata=metadata, revision=revision)


class ControllerRevisionList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "ControllerRevisionList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ControllerRevision]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ControllerRevision] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


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
    _api_group_ = "apps"
    _kind_ = "DaemonSet"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: DaemonSetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DaemonSetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class DaemonSetCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class DaemonSetList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "DaemonSetList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[DaemonSet]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[DaemonSet] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class DaemonSetStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["current_number_scheduled", "desired_number_scheduled", "number_misscheduled", "number_ready"]

    collision_count: int
    conditions: list[DaemonSetCondition]
    current_number_scheduled: int
    desired_number_scheduled: int
    number_available: int
    number_misscheduled: int
    number_ready: int
    number_unavailable: int
    observed_generation: int
    updated_number_scheduled: int

    def __init__(
        self,
        collision_count: int = None,
        conditions: list[DaemonSetCondition] = None,
        current_number_scheduled: int = None,
        desired_number_scheduled: int = None,
        number_available: int = None,
        number_misscheduled: int = None,
        number_ready: int = None,
        number_unavailable: int = None,
        observed_generation: int = None,
        updated_number_scheduled: int = None,
    ):
        super().__init__(
            collision_count=collision_count,
            conditions=conditions,
            current_number_scheduled=current_number_scheduled,
            desired_number_scheduled=desired_number_scheduled,
            number_available=number_available,
            number_misscheduled=number_misscheduled,
            number_ready=number_ready,
            number_unavailable=number_unavailable,
            observed_generation=observed_generation,
            updated_number_scheduled=updated_number_scheduled,
        )


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
    _api_group_ = "apps"
    _kind_ = "Deployment"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: DeploymentSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DeploymentSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class DeploymentCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    last_update_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_transition_time: meta.Time = None,
        last_update_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_transition_time=last_transition_time,
            last_update_time=last_update_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class DeploymentList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "DeploymentList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Deployment]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Deployment] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class DeploymentStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    available_replicas: int
    collision_count: int
    conditions: list[DeploymentCondition]
    observed_generation: int
    ready_replicas: int
    replicas: int
    unavailable_replicas: int
    updated_replicas: int

    def __init__(
        self,
        available_replicas: int = None,
        collision_count: int = None,
        conditions: list[DeploymentCondition] = None,
        observed_generation: int = None,
        ready_replicas: int = None,
        replicas: int = None,
        unavailable_replicas: int = None,
        updated_replicas: int = None,
    ):
        super().__init__(
            available_replicas=available_replicas,
            collision_count=collision_count,
            conditions=conditions,
            observed_generation=observed_generation,
            ready_replicas=ready_replicas,
            replicas=replicas,
            unavailable_replicas=unavailable_replicas,
            updated_replicas=updated_replicas,
        )


class ReplicaSetSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector"]

    min_ready_seconds: int
    replicas: int
    selector: meta.LabelSelector
    template: core.PodTemplateSpec

    def __init__(
        self,
        min_ready_seconds: int = None,
        replicas: int = None,
        selector: meta.LabelSelector = None,
        template: core.PodTemplateSpec = None,
    ):
        super().__init__(min_ready_seconds=min_ready_seconds, replicas=replicas, selector=selector, template=template)


class ReplicaSet(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "ReplicaSet"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ReplicaSetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ReplicaSetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ReplicaSetCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class ReplicaSetList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "ReplicaSetList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ReplicaSet]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ReplicaSet] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ReplicaSetStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["replicas"]

    available_replicas: int
    conditions: list[ReplicaSetCondition]
    fully_labeled_replicas: int
    observed_generation: int
    ready_replicas: int
    replicas: int

    def __init__(
        self,
        available_replicas: int = None,
        conditions: list[ReplicaSetCondition] = None,
        fully_labeled_replicas: int = None,
        observed_generation: int = None,
        ready_replicas: int = None,
        replicas: int = None,
    ):
        super().__init__(
            available_replicas=available_replicas,
            conditions=conditions,
            fully_labeled_replicas=fully_labeled_replicas,
            observed_generation=observed_generation,
            ready_replicas=ready_replicas,
            replicas=replicas,
        )


class RollingUpdateStatefulSetStrategy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    max_unavailable: core.IntOrString
    partition: int

    def __init__(self, max_unavailable: core.IntOrString = None, partition: int = None):
        super().__init__(max_unavailable=max_unavailable, partition=partition)


class StatefulSetOrdinals(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    start: int

    def __init__(self, start: int = None):
        super().__init__(start=start)


class StatefulSetPersistentVolumeClaimRetentionPolicy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    when_deleted: str
    when_scaled: str

    def __init__(self, when_deleted: str = None, when_scaled: str = None):
        super().__init__(when_deleted=when_deleted, when_scaled=when_scaled)


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

    min_ready_seconds: int
    ordinals: StatefulSetOrdinals
    persistent_volume_claim_retention_policy: StatefulSetPersistentVolumeClaimRetentionPolicy
    pod_management_policy: str
    replicas: int
    revision_history_limit: int
    selector: meta.LabelSelector
    service_name: str
    template: core.PodTemplateSpec
    update_strategy: StatefulSetUpdateStrategy
    volume_claim_templates: list[core.PersistentVolumeClaim]

    def __init__(
        self,
        min_ready_seconds: int = None,
        ordinals: StatefulSetOrdinals = None,
        persistent_volume_claim_retention_policy: StatefulSetPersistentVolumeClaimRetentionPolicy = None,
        pod_management_policy: str = None,
        replicas: int = None,
        revision_history_limit: int = None,
        selector: meta.LabelSelector = None,
        service_name: str = None,
        template: core.PodTemplateSpec = None,
        update_strategy: StatefulSetUpdateStrategy = None,
        volume_claim_templates: list[core.PersistentVolumeClaim] = None,
    ):
        super().__init__(
            min_ready_seconds=min_ready_seconds,
            ordinals=ordinals,
            persistent_volume_claim_retention_policy=persistent_volume_claim_retention_policy,
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
    _api_group_ = "apps"
    _kind_ = "StatefulSet"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: StatefulSetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StatefulSetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class StatefulSetCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class StatefulSetList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "StatefulSetList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[StatefulSet]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[StatefulSet] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class StatefulSetStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["replicas"]

    available_replicas: int
    collision_count: int
    conditions: list[StatefulSetCondition]
    current_replicas: int
    current_revision: str
    observed_generation: int
    ready_replicas: int
    replicas: int
    update_revision: str
    updated_replicas: int

    def __init__(
        self,
        available_replicas: int = None,
        collision_count: int = None,
        conditions: list[StatefulSetCondition] = None,
        current_replicas: int = None,
        current_revision: str = None,
        observed_generation: int = None,
        ready_replicas: int = None,
        replicas: int = None,
        update_revision: str = None,
        updated_replicas: int = None,
    ):
        super().__init__(
            available_replicas=available_replicas,
            collision_count=collision_count,
            conditions=conditions,
            current_replicas=current_replicas,
            current_revision=current_revision,
            observed_generation=observed_generation,
            ready_replicas=ready_replicas,
            replicas=replicas,
            update_revision=update_revision,
            updated_replicas=updated_replicas,
        )
