from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class Eviction(KubernetesApiResource):
    """Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod.  A request to cause such an eviction is created by POSTing to .../pods/<pod name>/evictions."""

    __slots__ = ()

    _api_version_ = "policy/v1"
    _api_group_ = "policy"
    _kind_ = "Eviction"
    _scope_ = "namespace"

    delete_options: meta.DeleteOptions
    """ DeleteOptions may be provided """
    metadata: meta.ObjectMeta
    """ ObjectMeta describes the pod that is being evicted. """

    def __init__(self, name: str, namespace: str = None, delete_options: meta.DeleteOptions = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, namespace, delete_options=delete_options, metadata=metadata)


class PodDisruptionBudgetSpec(KubernetesObject):
    """PodDisruptionBudgetSpec is a description of a PodDisruptionBudget."""

    __slots__ = ()

    _api_version_ = "policy/v1"

    max_unavailable: core.IntOrString
    """ An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable". """
    min_available: core.IntOrString
    """ An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%". """
    selector: meta.LabelSelector
    """ Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace. """
    unhealthy_pod_eviction_policy: str
    """ 
    UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".
    
    Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.
    
    IfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.
    
    AlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.
    
    Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.
    
    This field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default).
     """

    def __init__(
        self,
        max_unavailable: core.IntOrString = None,
        min_available: core.IntOrString = None,
        selector: meta.LabelSelector = None,
        unhealthy_pod_eviction_policy: str = None,
    ):
        super().__init__(
            max_unavailable=max_unavailable,
            min_available=min_available,
            selector=selector,
            unhealthy_pod_eviction_policy=unhealthy_pod_eviction_policy,
        )


class PodDisruptionBudget(KubernetesApiResource):
    """PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods"""

    __slots__ = ()

    _api_version_ = "policy/v1"
    _api_group_ = "policy"
    _kind_ = "PodDisruptionBudget"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: PodDisruptionBudgetSpec
    """ Specification of the desired behavior of the PodDisruptionBudget. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodDisruptionBudgetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PodDisruptionBudgetStatus(KubernetesObject):
    """PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may trail the actual state of a system."""

    __slots__ = ()

    _api_version_ = "policy/v1"

    _required_ = ["current_healthy", "desired_healthy", "disruptions_allowed", "expected_pods"]

    conditions: list[meta.Condition]
    """ 
    Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute
                  the number of allowed disruptions. Therefore no disruptions are
                  allowed and the status of the condition will be False.
    - InsufficientPods: The number of pods are either at or below the number
                        required by the PodDisruptionBudget. No disruptions are
                        allowed and the status of the condition will be False.
    - SufficientPods: There are more pods than required by the PodDisruptionBudget.
                      The condition will be True, and the number of allowed
                      disruptions are provided by the disruptionsAllowed property.
     """
    current_healthy: int
    """ current number of healthy pods """
    desired_healthy: int
    """ minimum desired number of healthy pods """
    disrupted_pods: dict[str, meta.Time]
    """ DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions. """
    disruptions_allowed: int
    """ Number of pod disruptions that are currently allowed. """
    expected_pods: int
    """ total number of pods counted by this disruption budget """
    observed_generation: int
    """ Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation. """

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
