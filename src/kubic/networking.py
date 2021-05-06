from typing import List

from . import KubernetesApiResource, KubernetesObject
from . import core, meta


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

    _required_ = ["backend"]

    backend: IngressBackend
    path: str
    path_type: str

    def __init__(self, backend: IngressBackend = None, path: str = None, path_type: str = None):
        super().__init__(backend=backend, path=path, path_type=path_type)


class HTTPIngressRuleValue(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["paths"]

    paths: List[HTTPIngressPath]

    def __init__(self, paths: List[HTTPIngressPath] = None):
        super().__init__(paths=paths)


class IPBlock(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["cidr"]

    _revfield_names_ = {
        "except": "except_",
    }

    cidr: str
    except_: List[str]

    def __init__(self, cidr: str = None, except_: List[str] = None):
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

    hosts: List[str]
    secret_name: str

    def __init__(self, hosts: List[str] = None, secret_name: str = None):
        super().__init__(hosts=hosts, secret_name=secret_name)


class IngressSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    default_backend: IngressBackend
    ingress_class_name: str
    rules: List[IngressRule]
    tls: List[IngressTLS]

    def __init__(
        self,
        default_backend: IngressBackend = None,
        ingress_class_name: str = None,
        rules: List[IngressRule] = None,
        tls: List[IngressTLS] = None,
    ):
        super().__init__(default_backend=default_backend, ingress_class_name=ingress_class_name, rules=rules, tls=tls)


class Ingress(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _kind_ = "Ingress"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: IngressSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: IngressSpec = None):
        super().__init__("networking.k8s.io/v1", "Ingress", name, namespace, metadata=metadata, spec=spec)


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
    _kind_ = "IngressClass"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: IngressClassSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: IngressClassSpec = None):
        super().__init__("networking.k8s.io/v1", "IngressClass", name, "", metadata=metadata, spec=spec)


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

    ports: List[NetworkPolicyPort]
    to: List[NetworkPolicyPeer]

    def __init__(self, ports: List[NetworkPolicyPort] = None, to: List[NetworkPolicyPeer] = None):
        super().__init__(ports=ports, to=to)


class NetworkPolicyIngressRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _revfield_names_ = {
        "from": "from_",
    }

    from_: List[NetworkPolicyPeer]
    ports: List[NetworkPolicyPort]

    def __init__(self, from_: List[NetworkPolicyPeer] = None, ports: List[NetworkPolicyPort] = None):
        super().__init__(from_=from_, ports=ports)


class NetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["pod_selector"]

    egress: List[NetworkPolicyEgressRule]
    ingress: List[NetworkPolicyIngressRule]
    pod_selector: meta.LabelSelector
    policy_types: List[str]

    def __init__(
        self,
        egress: List[NetworkPolicyEgressRule] = None,
        ingress: List[NetworkPolicyIngressRule] = None,
        pod_selector: meta.LabelSelector = None,
        policy_types: List[str] = None,
    ):
        super().__init__(egress=egress, ingress=ingress, pod_selector=pod_selector, policy_types=policy_types)


class NetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _kind_ = "NetworkPolicy"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: NetworkPolicySpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: NetworkPolicySpec = None):
        super().__init__("networking.k8s.io/v1", "NetworkPolicy", name, namespace, metadata=metadata, spec=spec)
