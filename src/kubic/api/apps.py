from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class ControllerRevision(KubernetesApiResource):
    """ControllerRevision implements an immutable snapshot of state data. Clients are responsible for serializing and deserializing the objects that contain their internal state. Once a ControllerRevision has been successfully created, it can not be updated. The API Server will fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this object is beta. However, it may be subject to name and representation changes in future releases, and clients should not depend on its stability. It is primarily for internal use by controllers."""

    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "ControllerRevision"
    _scope_ = "namespace"

    _required_ = ["revision"]

    data: core.RawExtension
    """ Data is the serialized representation of the state. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    revision: int
    """ Revision indicates the revision of the state represented by Data. """

    def __init__(
        self, name: str, namespace: str = None, data: core.RawExtension = None, metadata: meta.ObjectMeta = None, revision: int = None
    ):
        super().__init__(name, namespace, data=data, metadata=metadata, revision=revision)


class RollingUpdateDaemonSet(KubernetesObject):
    """Spec to control the desired behavior of daemon set rolling update."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    max_surge: core.IntOrString
    """ The maximum number of nodes with an existing available DaemonSet pod that can have an updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is evicted, or is drained) an updated pod is immediatedly created on that node without considering surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset on any given node can double if the readiness check fails, and so resource intensive daemonsets should take into account that they may cause evictions during disruption. """
    max_unavailable: core.IntOrString
    """ The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update. """

    def __init__(self, max_surge: core.IntOrString = None, max_unavailable: core.IntOrString = None):
        super().__init__(max_surge=max_surge, max_unavailable=max_unavailable)


class DaemonSetUpdateStrategy(KubernetesObject):
    """DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    rolling_update: RollingUpdateDaemonSet
    """ Rolling update config params. Present only if type = "RollingUpdate". """
    type: str
    """ Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate. """

    def __init__(self, rolling_update: RollingUpdateDaemonSet = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class DaemonSetSpec(KubernetesObject):
    """DaemonSetSpec is the specification of a daemon set."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector", "template"]

    min_ready_seconds: int
    """ The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready). """
    revision_history_limit: int
    """ The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """
    selector: meta.LabelSelector
    """ A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """
    template: core.PodTemplateSpec
    """ An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """
    update_strategy: DaemonSetUpdateStrategy
    """ An update strategy to replace existing DaemonSet pods with new pods. """

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
    """DaemonSet represents the configuration of a daemon set."""

    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "DaemonSet"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: DaemonSetSpec
    """ The desired behavior of this daemon set. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DaemonSetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class DaemonSetCondition(KubernetesObject):
    """DaemonSetCondition describes the state of a DaemonSet at a certain point."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ Last time the condition transitioned from one status to another. """
    message: str
    """ A human readable message indicating details about the transition. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of DaemonSet condition. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class DaemonSetStatus(KubernetesObject):
    """DaemonSetStatus represents the current status of a daemon set."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["current_number_scheduled", "desired_number_scheduled", "number_misscheduled", "number_ready"]

    collision_count: int
    """ Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. """
    conditions: list[DaemonSetCondition]
    """ Represents the latest available observations of a DaemonSet's current state. """
    current_number_scheduled: int
    """ The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """
    desired_number_scheduled: int
    """ The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """
    number_available: int
    """ The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) """
    number_misscheduled: int
    """ The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ """
    number_ready: int
    """ numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition. """
    number_unavailable: int
    """ The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) """
    observed_generation: int
    """ The most recent generation observed by the daemon set controller. """
    updated_number_scheduled: int
    """ The total number of nodes that are running updated daemon pod """

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
    """Spec to control the desired behavior of rolling update."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    max_surge: core.IntOrString
    """ The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. """
    max_unavailable: core.IntOrString
    """ The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. """

    def __init__(self, max_surge: core.IntOrString = None, max_unavailable: core.IntOrString = None):
        super().__init__(max_surge=max_surge, max_unavailable=max_unavailable)


class DeploymentStrategy(KubernetesObject):
    """DeploymentStrategy describes how to replace existing pods with new ones."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    rolling_update: RollingUpdateDeployment
    """ Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate. """
    type: str
    """ Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate. """

    def __init__(self, rolling_update: RollingUpdateDeployment = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class DeploymentSpec(KubernetesObject):
    """DeploymentSpec is the specification of the desired behavior of the Deployment."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector", "template"]

    min_ready_seconds: int
    """ Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """
    paused: bool
    """ Indicates that the deployment is paused. """
    progress_deadline_seconds: int
    """ The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. """
    replicas: int
    """ Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. """
    revision_history_limit: int
    """ The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. """
    selector: meta.LabelSelector
    """ Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels. """
    strategy: DeploymentStrategy
    """ The deployment strategy to use to replace existing pods with new ones. """
    template: core.PodTemplateSpec
    """ Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always". """

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
    """Deployment enables declarative updates for Pods and ReplicaSets."""

    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "Deployment"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: DeploymentSpec
    """ Specification of the desired behavior of the Deployment. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DeploymentSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class DeploymentCondition(KubernetesObject):
    """DeploymentCondition describes the state of a deployment at a certain point."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ Last time the condition transitioned from one status to another. """
    last_update_time: meta.Time
    """ The last time this condition was updated. """
    message: str
    """ A human readable message indicating details about the transition. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of deployment condition. """

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


class DeploymentStatus(KubernetesObject):
    """DeploymentStatus is the most recently observed status of the Deployment."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    available_replicas: int
    """ Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. """
    collision_count: int
    """ Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet. """
    conditions: list[DeploymentCondition]
    """ Represents the latest available observations of a deployment's current state. """
    observed_generation: int
    """ The generation observed by the deployment controller. """
    ready_replicas: int
    """ readyReplicas is the number of pods targeted by this Deployment with a Ready Condition. """
    replicas: int
    """ Total number of non-terminated pods targeted by this deployment (their labels match the selector). """
    unavailable_replicas: int
    """ Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created. """
    updated_replicas: int
    """ Total number of non-terminated pods targeted by this deployment that have the desired template spec. """

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
    """ReplicaSetSpec is the specification of a ReplicaSet."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector"]

    min_ready_seconds: int
    """ Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """
    replicas: int
    """ Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller """
    selector: meta.LabelSelector
    """ Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """
    template: core.PodTemplateSpec
    """ Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template """

    def __init__(
        self,
        min_ready_seconds: int = None,
        replicas: int = None,
        selector: meta.LabelSelector = None,
        template: core.PodTemplateSpec = None,
    ):
        super().__init__(min_ready_seconds=min_ready_seconds, replicas=replicas, selector=selector, template=template)


class ReplicaSet(KubernetesApiResource):
    """ReplicaSet ensures that a specified number of pod replicas are running at any given time."""

    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "ReplicaSet"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: ReplicaSetSpec
    """ Spec defines the specification of the desired behavior of the ReplicaSet. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ReplicaSetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ReplicaSetCondition(KubernetesObject):
    """ReplicaSetCondition describes the state of a replica set at a certain point."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ The last time the condition transitioned from one status to another. """
    message: str
    """ A human readable message indicating details about the transition. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of replica set condition. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class ReplicaSetStatus(KubernetesObject):
    """ReplicaSetStatus represents the current status of a ReplicaSet."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["replicas"]

    available_replicas: int
    """ The number of available replicas (ready for at least minReadySeconds) for this replica set. """
    conditions: list[ReplicaSetCondition]
    """ Represents the latest available observations of a replica set's current state. """
    fully_labeled_replicas: int
    """ The number of pods that have labels matching the labels of the pod template of the replicaset. """
    observed_generation: int
    """ ObservedGeneration reflects the generation of the most recently observed ReplicaSet. """
    ready_replicas: int
    """ readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition. """
    replicas: int
    """ Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller """

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
    """RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    max_unavailable: core.IntOrString
    """ The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable. """
    partition: int
    """ Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0. """

    def __init__(self, max_unavailable: core.IntOrString = None, partition: int = None):
        super().__init__(max_unavailable=max_unavailable, partition=partition)


class StatefulSetOrdinals(KubernetesObject):
    """StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    start: int
    """
    start is the number representing the first replica's index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range:
      [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas).
    If unset, defaults to 0. Replica indices will be in the range:
      [0, .spec.replicas).
    """

    def __init__(self, start: int = None):
        super().__init__(start=start)


class StatefulSetPersistentVolumeClaimRetentionPolicy(KubernetesObject):
    """StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    when_deleted: str
    """ WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted. """
    when_scaled: str
    """ WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted. """

    def __init__(self, when_deleted: str = None, when_scaled: str = None):
        super().__init__(when_deleted=when_deleted, when_scaled=when_scaled)


class StatefulSetUpdateStrategy(KubernetesObject):
    """StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    rolling_update: RollingUpdateStatefulSetStrategy
    """ RollingUpdate is used to communicate parameters when Type is RollingUpdateStatefulSetStrategyType. """
    type: str
    """ Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. """

    def __init__(self, rolling_update: RollingUpdateStatefulSetStrategy = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class StatefulSetSpec(KubernetesObject):
    """A StatefulSetSpec is the specification of a StatefulSet."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["selector", "service_name", "template"]

    min_ready_seconds: int
    """ Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) """
    ordinals: StatefulSetOrdinals
    """ ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals behavior assigns a "0" index to the first replica and increments the index by one for each additional replica requested. Using the ordinals field requires the StatefulSetStartOrdinal feature gate to be enabled, which is beta. """
    persistent_volume_claim_retention_policy: StatefulSetPersistentVolumeClaimRetentionPolicy
    """ persistentVolumeClaimRetentionPolicy describes the lifecycle of persistent volume claims created from volumeClaimTemplates. By default, all persistent volume claims are created as needed and retained until manually deleted. This policy allows the lifecycle to be altered, for example by deleting persistent volume claims when their stateful set is deleted, or when their pod is scaled down. This requires the StatefulSetAutoDeletePVC feature gate to be enabled, which is alpha.  +optional """
    pod_management_policy: str
    """ podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once. """
    replicas: int
    """ replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1. """
    revision_history_limit: int
    """ revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10. """
    selector: meta.LabelSelector
    """ selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """
    service_name: str
    """ serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller. """
    template: core.PodTemplateSpec
    """ template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always". """
    update_strategy: StatefulSetUpdateStrategy
    """ updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. """
    volume_claim_templates: list[core.PersistentVolumeClaim]
    """ volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name. """

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
    """
    StatefulSet represents a set of pods with consistent identities. Identities are defined as:
      - Network: A single stable DNS and hostname.
      - Storage: As many VolumeClaims as requested.

    The StatefulSet guarantees that a given network identity will always map to the same storage identity.
    """

    __slots__ = ()

    _api_version_ = "apps/v1"
    _api_group_ = "apps"
    _kind_ = "StatefulSet"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: StatefulSetSpec
    """ Spec defines the desired identities of pods in this set. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StatefulSetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class StatefulSetCondition(KubernetesObject):
    """StatefulSetCondition describes the state of a statefulset at a certain point."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ Last time the condition transitioned from one status to another. """
    message: str
    """ A human readable message indicating details about the transition. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of statefulset condition. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class StatefulSetStatus(KubernetesObject):
    """StatefulSetStatus represents the current state of a StatefulSet."""

    __slots__ = ()

    _api_version_ = "apps/v1"

    _required_ = ["replicas"]

    available_replicas: int
    """ Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset. """
    collision_count: int
    """ collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. """
    conditions: list[StatefulSetCondition]
    """ Represents the latest available observations of a statefulset's current state. """
    current_replicas: int
    """ currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision. """
    current_revision: str
    """ currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas). """
    observed_generation: int
    """ observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server. """
    ready_replicas: int
    """ readyReplicas is the number of pods created for this StatefulSet with a Ready Condition. """
    replicas: int
    """ replicas is the number of Pods created by the StatefulSet controller. """
    update_revision: str
    """ updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas) """
    updated_replicas: int
    """ updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision. """

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
