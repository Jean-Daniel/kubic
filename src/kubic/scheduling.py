from . import KubernetesApiResource
from . import meta


class PriorityClass(KubernetesApiResource):
    __slots__ = ()

    _kind_ = "PriorityClass"
    _group_ = "scheduling.k8s.io"
    _version_ = "v1"

    _required_ = ["value"]

    description: str
    global_default: bool
    metadata: meta.ObjectMeta
    preemption_policy: str
    value: int

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
            "scheduling.k8s.io/v1",
            "PriorityClass",
            name,
            "",
            description=description,
            global_default=global_default,
            metadata=metadata,
            preemption_policy=preemption_policy,
            value=value,
        )
