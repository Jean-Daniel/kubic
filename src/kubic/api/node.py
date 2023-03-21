from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class Overhead(KubernetesObject):
    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"

    pod_fixed: dict[str, core.Quantity]

    def __init__(self, pod_fixed: dict[str, core.Quantity] = None):
        super().__init__(pod_fixed=pod_fixed)


class Scheduling(KubernetesObject):
    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"

    node_selector: dict[str, str]
    tolerations: list[core.Toleration]

    def __init__(self, node_selector: dict[str, str] = None, tolerations: list[core.Toleration] = None):
        super().__init__(node_selector=node_selector, tolerations=tolerations)


class RuntimeClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"
    _api_group_ = "node.k8s.io"
    _kind_ = "RuntimeClass"
    _scope_ = "cluster"

    _required_ = ["handler"]

    handler: str
    metadata: meta.ObjectMeta
    overhead: Overhead
    scheduling: Scheduling

    def __init__(
        self, name: str, handler: str = None, metadata: meta.ObjectMeta = None, overhead: Overhead = None, scheduling: Scheduling = None
    ):
        super().__init__(name, "", handler=handler, metadata=metadata, overhead=overhead, scheduling=scheduling)


class RuntimeClassList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"
    _api_group_ = "node.k8s.io"
    _kind_ = "RuntimeClassList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[RuntimeClass]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[RuntimeClass] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)
