from kubic import KubernetesApiResource
from . import meta


class PriorityClass(KubernetesApiResource):
    """PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer."""

    __slots__ = ()

    _api_version_ = "scheduling.k8s.io/v1"
    _api_group_ = "scheduling.k8s.io"
    _kind_ = "PriorityClass"
    _scope_ = "cluster"

    _required_ = ["value"]

    description: str
    """ description is an arbitrary string that usually provides guidelines on when this priority class should be used. """
    global_default: bool
    """ globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    preemption_policy: str
    """ preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. """
    value: int
    """ value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec. """

    def __init__(
        self,
        name: str,
        description: str = None,
        global_default: bool = None,
        metadata: meta.ObjectMeta = None,
        preemption_policy: str = None,
        value: int = None,
    ):
        super().__init__(
            name,
            "",
            description=description,
            global_default=global_default,
            metadata=metadata,
            preemption_policy=preemption_policy,
            value=value,
        )
