from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class ClusterCIDRSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"

    _required_ = ["per_node_host_bits"]

    ipv4: str
    ipv6: str
    node_selector: core.NodeSelector
    per_node_host_bits: int

    def __init__(self, ipv4: str = None, ipv6: str = None, node_selector: core.NodeSelector = None, per_node_host_bits: int = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6, node_selector=node_selector, per_node_host_bits=per_node_host_bits)


class ClusterCIDR(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "ClusterCIDR"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ClusterCIDRSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ClusterCIDRSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ClusterCIDRList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "ClusterCIDRList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ClusterCIDR]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ClusterCIDR] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ServiceBackendPort(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    name: str
    number: int

    def __init__(self, name: str = None, number: int = None):
        super().__init__(name=name, number=number)


class IngressServiceBackend(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["name"]

    name: str
    port: ServiceBackendPort

    def __init__(self, name: str = None, port: ServiceBackendPort = None):
        super().__init__(name=name, port=port)


class IngressBackend(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    resource: core.TypedLocalObjectReference
    service: IngressServiceBackend

    def __init__(self, resource: core.TypedLocalObjectReference = None, service: IngressServiceBackend = None):
        super().__init__(resource=resource, service=service)


class HTTPIngressPath(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["backend", "path_type"]

    backend: IngressBackend
    path: str
    path_type: str

    def __init__(self, backend: IngressBackend = None, path: str = None, path_type: str = None):
        super().__init__(backend=backend, path=path, path_type=path_type)


class HTTPIngressRuleValue(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["paths"]

    paths: list[HTTPIngressPath]

    def __init__(self, paths: list[HTTPIngressPath] = None):
        super().__init__(paths=paths)


class IPBlock(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["cidr"]

    _revfield_names_ = {
        "except": "except_",
    }

    cidr: str
    except_: list[str]

    def __init__(self, cidr: str = None, except_: list[str] = None):
        super().__init__(cidr=cidr, except_=except_)


class IngressRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    host: str
    http: HTTPIngressRuleValue

    def __init__(self, host: str = None, http: HTTPIngressRuleValue = None):
        super().__init__(host=host, http=http)


class IngressTLS(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    hosts: list[str]
    secret_name: str

    def __init__(self, hosts: list[str] = None, secret_name: str = None):
        super().__init__(hosts=hosts, secret_name=secret_name)


class IngressSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    default_backend: IngressBackend
    ingress_class_name: str
    rules: list[IngressRule]
    tls: list[IngressTLS]

    def __init__(
        self,
        default_backend: IngressBackend = None,
        ingress_class_name: str = None,
        rules: list[IngressRule] = None,
        tls: list[IngressTLS] = None,
    ):
        super().__init__(default_backend=default_backend, ingress_class_name=ingress_class_name, rules=rules, tls=tls)


class Ingress(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "Ingress"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: IngressSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: IngressSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class IngressClassParametersReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["kind", "name"]

    api_group: str
    kind: str
    name: str
    namespace: str
    scope: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None, scope: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace, scope=scope)


class IngressClassSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    controller: str
    parameters: IngressClassParametersReference

    def __init__(self, controller: str = None, parameters: IngressClassParametersReference = None):
        super().__init__(controller=controller, parameters=parameters)


class IngressClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "IngressClass"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: IngressClassSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: IngressClassSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class IngressClassList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "IngressClassList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[IngressClass]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[IngressClass] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class IngressList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "IngressList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Ingress]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Ingress] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class IngressStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    load_balancer: core.LoadBalancerStatus

    def __init__(self, load_balancer: core.LoadBalancerStatus = None):
        super().__init__(load_balancer=load_balancer)


class NetworkPolicyPort(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    end_port: int
    port: core.IntOrString
    protocol: str

    def __init__(self, end_port: int = None, port: core.IntOrString = None, protocol: str = None):
        super().__init__(end_port=end_port, port=port, protocol=protocol)


class NetworkPolicyPeer(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    ip_block: IPBlock
    namespace_selector: meta.LabelSelector
    pod_selector: meta.LabelSelector

    def __init__(self, ip_block: IPBlock = None, namespace_selector: meta.LabelSelector = None, pod_selector: meta.LabelSelector = None):
        super().__init__(ip_block=ip_block, namespace_selector=namespace_selector, pod_selector=pod_selector)


class NetworkPolicyEgressRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    ports: list[NetworkPolicyPort]
    to: list[NetworkPolicyPeer]

    def __init__(self, ports: list[NetworkPolicyPort] = None, to: list[NetworkPolicyPeer] = None):
        super().__init__(ports=ports, to=to)


class NetworkPolicyIngressRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _revfield_names_ = {
        "from": "from_",
    }

    from_: list[NetworkPolicyPeer]
    ports: list[NetworkPolicyPort]

    def __init__(self, from_: list[NetworkPolicyPeer] = None, ports: list[NetworkPolicyPort] = None):
        super().__init__(from_=from_, ports=ports)


class NetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["pod_selector"]

    egress: list[NetworkPolicyEgressRule]
    ingress: list[NetworkPolicyIngressRule]
    pod_selector: meta.LabelSelector
    policy_types: list[str]

    def __init__(
        self,
        egress: list[NetworkPolicyEgressRule] = None,
        ingress: list[NetworkPolicyIngressRule] = None,
        pod_selector: meta.LabelSelector = None,
        policy_types: list[str] = None,
    ):
        super().__init__(egress=egress, ingress=ingress, pod_selector=pod_selector, policy_types=policy_types)


class NetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "NetworkPolicy"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: NetworkPolicySpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: NetworkPolicySpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class NetworkPolicyList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "NetworkPolicyList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[NetworkPolicy]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[NetworkPolicy] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class NetworkPolicyStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    conditions: list[meta.Condition]

    def __init__(self, conditions: list[meta.Condition] = None):
        super().__init__(conditions=conditions)
