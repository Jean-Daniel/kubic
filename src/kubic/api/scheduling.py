from kubic import KubernetesApiResource
from . import meta



class PriorityClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "scheduling.k8s.io/v1"
    _api_group_ = "scheduling.k8s.io"
    _kind_ = "PriorityClass"
    _scope_ = "cluster"

    _required_ = ["value"]

    description: str
    global_default: bool
    metadata: meta.ObjectMeta
    preemption_policy: str
    value: int

    def __init__(self, name: str, description: str = None, global_default: bool = None, metadata: meta.ObjectMeta = None, preemption_policy: str = None, value: int = None):
        super().__init__(name, "", description=description, global_default=global_default, metadata=metadata, preemption_policy=preemption_policy, value=value)


class PriorityClassList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "scheduling.k8s.io/v1"
    _api_group_ = "scheduling.k8s.io"
    _kind_ = "PriorityClassList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PriorityClass]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PriorityClass] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


