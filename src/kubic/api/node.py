from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class Overhead(KubernetesObject):
    """Overhead structure represents the resource overhead associated with running a pod."""

    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"

    pod_fixed: dict[str, core.Quantity]
    """ podFixed represents the fixed resource overhead associated with running a pod. """

    def __init__(self, pod_fixed: dict[str, core.Quantity] = None):
        super().__init__(pod_fixed=pod_fixed)


class Scheduling(KubernetesObject):
    """Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass."""

    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"

    node_selector: dict[str, str]
    """ nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission. """
    tolerations: list[core.Toleration]
    """ tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass. """

    def __init__(self, node_selector: dict[str, str] = None, tolerations: list[core.Toleration] = None):
        super().__init__(node_selector=node_selector, tolerations=tolerations)


class RuntimeClass(KubernetesApiResource):
    """RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod.  For more details, see https://kubernetes.io/docs/concepts/containers/runtime-class/"""

    __slots__ = ()

    _api_version_ = "node.k8s.io/v1"
    _api_group_ = "node.k8s.io"
    _kind_ = "RuntimeClass"
    _scope_ = "cluster"

    _required_ = ["handler"]

    handler: str
    """ handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable. """
    metadata: meta.ObjectMeta
    """ More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    overhead: Overhead
    """
    overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see
     https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
    """
    scheduling: Scheduling
    """ scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes. """

    def __init__(
        self, name: str, handler: str = None, metadata: meta.ObjectMeta = None, overhead: Overhead = None, scheduling: Scheduling = None
    ):
        super().__init__(name, "", handler=handler, metadata=metadata, overhead=overhead, scheduling=scheduling)
