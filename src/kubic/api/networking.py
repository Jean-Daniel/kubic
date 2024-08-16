from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class ServiceBackendPort(KubernetesObject):
    """ServiceBackendPort is the service port being referenced."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    name: str
    """ name is the name of the port on the Service. This is a mutually exclusive setting with "Number". """
    number: int
    """ number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with "Name". """

    def __init__(self, name: str = None, number: int = None):
        super().__init__(name=name, number=number)


class IngressServiceBackend(KubernetesObject):
    """IngressServiceBackend references a Kubernetes Service as a Backend."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["name"]

    name: str
    """ name is the referenced service. The service must exist in the same namespace as the Ingress object. """
    port: ServiceBackendPort
    """ port of the referenced service. A port name or port number is required for a IngressServiceBackend. """

    def __init__(self, name: str = None, port: ServiceBackendPort = None):
        super().__init__(name=name, port=port)


class IngressBackend(KubernetesObject):
    """IngressBackend describes all endpoints for a given service and port."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    resource: core.TypedLocalObjectReference
    """ resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with "Service". """
    service: IngressServiceBackend
    """ service references a service as a backend. This is a mutually exclusive setting with "Resource". """

    def __init__(self, resource: core.TypedLocalObjectReference = None, service: IngressServiceBackend = None):
        super().__init__(resource=resource, service=service)


class HTTPIngressPath(KubernetesObject):
    """HTTPIngressPath associates a path with a backend. Incoming urls matching the path are forwarded to the backend."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["backend", "path_type"]

    backend: IngressBackend
    """ backend defines the referenced service endpoint to which the traffic will be forwarded to. """
    path: str
    """ path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". """
    path_type: str
    """ 
    pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is
      done on a path element by element basis. A path element refers is the
      list of labels in the path split by the '/' separator. A request is a
      match for path p if every p is an element-wise prefix of p of the
      request path. Note that if the last element of the path is a substring
      of the last element in request path, it is not a match (e.g. /foo/bar
      matches /foo/bar/baz, but does not match /foo/barbaz).
    * ImplementationSpecific: Interpretation of the Path matching is up to
      the IngressClass. Implementations can treat this as a separate PathType
      or treat it identically to Prefix or Exact path types.
    Implementations are required to support all path types.
     """

    def __init__(self, backend: IngressBackend = None, path: str = None, path_type: str = None):
        super().__init__(backend=backend, path=path, path_type=path_type)


class HTTPIngressRuleValue(KubernetesObject):
    """HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["paths"]

    paths: list[HTTPIngressPath]
    """ paths is a collection of paths that map requests to backends. """

    def __init__(self, paths: list[HTTPIngressPath] = None):
        super().__init__(paths=paths)


class ParentReference(KubernetesObject):
    """ParentReference describes a reference to a parent object."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"

    _required_ = ["name", "resource"]

    group: str
    """ Group is the group of the object being referenced. """
    name: str
    """ Name is the name of the object being referenced. """
    namespace: str
    """ Namespace is the namespace of the object being referenced. """
    resource: str
    """ Resource is the resource of the object being referenced. """

    def __init__(self, group: str = None, name: str = None, namespace: str = None, resource: str = None):
        super().__init__(group=group, name=name, namespace=namespace, resource=resource)


class IPAddressSpec(KubernetesObject):
    """IPAddressSpec describe the attributes in an IP Address."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"

    _required_ = ["parent_ref"]

    parent_ref: ParentReference
    """ ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object. """

    def __init__(self, parent_ref: ParentReference = None):
        super().__init__(parent_ref=parent_ref)


class IPAddress(KubernetesApiResource):
    """IPAddress represents a single IP of a single IP Family. The object is designed to be used by APIs that operate on IP addresses. The object is used by the Service core API for allocation of IP addresses. An IP address can be represented in different formats, to guarantee the uniqueness of the IP, the name of the object is the IP address in canonical format, four decimal digits separated by dots suppressing leading zeros for IPv4 and the representation defined by RFC 5952 for IPv6. Valid: 192.168.1.5 or 2001:db8::1 or 2001:db8:aaaa:bbbb:cccc:dddd:eeee:1 Invalid: 10.01.2.3 or 2001:db8:0:0:0::1"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "IPAddress"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: IPAddressSpec
    """ spec is the desired state of the IPAddress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: IPAddressSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class IPBlock(KubernetesObject):
    """IPBlock describes a particular CIDR (Ex. "192.168.1.0/24","2001:db8::/64") that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should not be included within this rule."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["cidr"]

    _revfield_names_ = {
        "except": "except_",
    }

    cidr: str
    """ cidr is a string representing the IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" """
    except_: list[str]
    """ except is a slice of CIDRs that should not be included within an IPBlock Valid examples are "192.168.1.0/24" or "2001:db8::/64" Except values will be rejected if they are outside the cidr range """

    def __init__(self, cidr: str = None, except_: list[str] = None):
        super().__init__(cidr=cidr, except_=except_)


class IngressRule(KubernetesObject):
    """IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    host: str
    """ 
    host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to
       the IP in the Spec of the parent Ingress.
    2. The `:` delimiter is not respected because ports are not allowed.
    	  Currently the port of an Ingress is implicitly :80 for http and
    	  :443 for https.
    Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
    
    host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If host is precise, the request matches this rule if the http host header is equal to Host. 2. If host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule.
     """
    http: HTTPIngressRuleValue

    def __init__(self, host: str = None, http: HTTPIngressRuleValue = None):
        super().__init__(host=host, http=http)


class IngressTLS(KubernetesObject):
    """IngressTLS describes the transport layer security associated with an ingress."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    hosts: list[str]
    """ hosts is a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. """
    secret_name: str
    """ secretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the "Host" header is used for routing. """

    def __init__(self, hosts: list[str] = None, secret_name: str = None):
        super().__init__(hosts=hosts, secret_name=secret_name)


class IngressSpec(KubernetesObject):
    """IngressSpec describes the Ingress the user wishes to exist."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    default_backend: IngressBackend
    """ defaultBackend is the backend that should handle requests that don't match any rule. If Rules are not specified, DefaultBackend must be specified. If DefaultBackend is not set, the handling of requests that do not match any of the rules will be up to the Ingress controller. """
    ingress_class_name: str
    """ ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -> IngressClass -> Ingress resource). Although the `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present. """
    rules: list[IngressRule]
    """ rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend. """
    tls: list[IngressTLS]
    """ tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI. """

    def __init__(
        self,
        default_backend: IngressBackend = None,
        ingress_class_name: str = None,
        rules: list[IngressRule] = None,
        tls: list[IngressTLS] = None,
    ):
        super().__init__(default_backend=default_backend, ingress_class_name=ingress_class_name, rules=rules, tls=tls)


class Ingress(KubernetesApiResource):
    """Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "Ingress"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: IngressSpec
    """ spec is the desired state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: IngressSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class IngressClassParametersReference(KubernetesObject):
    """IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["kind", "name"]

    api_group: str
    """ apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. """
    kind: str
    """ kind is the type of resource being referenced. """
    name: str
    """ name is the name of resource being referenced. """
    namespace: str
    """ namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster". """
    scope: str
    """ scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace". """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None, scope: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace, scope=scope)


class IngressClassSpec(KubernetesObject):
    """IngressClassSpec provides information about the class of an Ingress."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    controller: str
    """ controller refers to the name of the controller that should handle this class. This allows for different "flavors" that are controlled by the same controller. For example, you may have different parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. "acme.io/ingress-controller". This field is immutable. """
    parameters: IngressClassParametersReference
    """ parameters is a link to a custom resource containing additional configuration for the controller. This is optional if the controller does not require extra parameters. """

    def __init__(self, controller: str = None, parameters: IngressClassParametersReference = None):
        super().__init__(controller=controller, parameters=parameters)


class IngressClass(KubernetesApiResource):
    """IngressClass represents the class of the Ingress, referenced by the Ingress Spec. The `ingressclass.kubernetes.io/is-default-class` annotation can be used to indicate that an IngressClass should be considered default. When a single IngressClass resource has this annotation set to true, new Ingress resources without a class specified will be assigned this default class."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "IngressClass"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: IngressClassSpec
    """ spec is the desired state of the IngressClass. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: IngressClassSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class IngressPortStatus(KubernetesObject):
    """IngressPortStatus represents the error condition of a service port"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["port", "protocol"]

    error: str
    """ 
    error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use
      CamelCase names
    - cloud provider specific error values must have names that comply with the
      format foo.example.com/CamelCase.
     """
    port: int
    """ port is the port number of the ingress port. """
    protocol: str
    """ protocol is the protocol of the ingress port. The supported values are: "TCP", "UDP", "SCTP" """

    def __init__(self, error: str = None, port: int = None, protocol: str = None):
        super().__init__(error=error, port=port, protocol=protocol)


class IngressLoadBalancerIngress(KubernetesObject):
    """IngressLoadBalancerIngress represents the status of a load-balancer ingress point."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    hostname: str
    """ hostname is set for load-balancer ingress points that are DNS based. """
    ip: str
    """ ip is set for load-balancer ingress points that are IP based. """
    ports: list[IngressPortStatus]
    """ ports provides information about the ports exposed by this LoadBalancer. """

    def __init__(self, hostname: str = None, ip: str = None, ports: list[IngressPortStatus] = None):
        super().__init__(hostname=hostname, ip=ip, ports=ports)


class IngressLoadBalancerStatus(KubernetesObject):
    """IngressLoadBalancerStatus represents the status of a load-balancer."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    ingress: list[IngressLoadBalancerIngress]
    """ ingress is a list containing ingress points for the load-balancer. """

    def __init__(self, ingress: list[IngressLoadBalancerIngress] = None):
        super().__init__(ingress=ingress)


class IngressStatus(KubernetesObject):
    """IngressStatus describe the current state of the Ingress."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    load_balancer: IngressLoadBalancerStatus
    """ loadBalancer contains the current status of the load-balancer. """

    def __init__(self, load_balancer: IngressLoadBalancerStatus = None):
        super().__init__(load_balancer=load_balancer)


class NetworkPolicyPort(KubernetesObject):
    """NetworkPolicyPort describes a port to allow traffic on"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    end_port: int
    """ endPort indicates that the range of ports from port to endPort if set, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port. """
    port: core.IntOrString
    """ port represents the port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. """
    protocol: str
    """ protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. """

    def __init__(self, end_port: int = None, port: core.IntOrString = None, protocol: str = None):
        super().__init__(end_port=end_port, port=port, protocol=protocol)


class NetworkPolicyPeer(KubernetesObject):
    """NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    ip_block: IPBlock
    """ ipBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be. """
    namespace_selector: meta.LabelSelector
    """ 
    namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.
    
    If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector.
     """
    pod_selector: meta.LabelSelector
    """ 
    podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.
    
    If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy's own namespace.
     """

    def __init__(self, ip_block: IPBlock = None, namespace_selector: meta.LabelSelector = None, pod_selector: meta.LabelSelector = None):
        super().__init__(ip_block=ip_block, namespace_selector=namespace_selector, pod_selector=pod_selector)


class NetworkPolicyEgressRule(KubernetesObject):
    """NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and to. This type is beta-level in 1.8"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    ports: list[NetworkPolicyPort]
    """ ports is a list of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """
    to: list[NetworkPolicyPeer]
    """ to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list. """

    def __init__(self, ports: list[NetworkPolicyPort] = None, to: list[NetworkPolicyPeer] = None):
        super().__init__(ports=ports, to=to)


class NetworkPolicyIngressRule(KubernetesObject):
    """NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _revfield_names_ = {
        "from": "from_",
    }

    from_: list[NetworkPolicyPeer]
    """ from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list. """
    ports: list[NetworkPolicyPort]
    """ ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. """

    def __init__(self, from_: list[NetworkPolicyPeer] = None, ports: list[NetworkPolicyPort] = None):
        super().__init__(from_=from_, ports=ports)


class NetworkPolicySpec(KubernetesObject):
    """NetworkPolicySpec provides the specification of a NetworkPolicy"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"

    _required_ = ["pod_selector"]

    egress: list[NetworkPolicyEgressRule]
    """ egress is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8 """
    ingress: list[NetworkPolicyIngressRule]
    """ ingress is a list of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default) """
    pod_selector: meta.LabelSelector
    """ podSelector selects the pods to which this NetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace. """
    policy_types: list[str]
    """ policyTypes is a list of rule types that the NetworkPolicy relates to. Valid options are ["Ingress"], ["Egress"], or ["Ingress", "Egress"]. If this field is not specified, it will default based on the existence of ingress or egress rules; policies that contain an egress section are assumed to affect egress, and all policies (whether or not they contain an ingress section) are assumed to affect ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8 """

    def __init__(
        self,
        egress: list[NetworkPolicyEgressRule] = None,
        ingress: list[NetworkPolicyIngressRule] = None,
        pod_selector: meta.LabelSelector = None,
        policy_types: list[str] = None,
    ):
        super().__init__(egress=egress, ingress=ingress, pod_selector=pod_selector, policy_types=policy_types)


class NetworkPolicy(KubernetesApiResource):
    """NetworkPolicy describes what network traffic is allowed for a set of Pods"""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "NetworkPolicy"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: NetworkPolicySpec
    """ spec represents the specification of the desired behavior for this NetworkPolicy. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: NetworkPolicySpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ServiceCIDRSpec(KubernetesObject):
    """ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"

    cidrs: list[str]
    """ CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable. """

    def __init__(self, cidrs: list[str] = None):
        super().__init__(cidrs=cidrs)


class ServiceCIDR(KubernetesApiResource):
    """ServiceCIDR defines a range of IP addresses using CIDR format (e.g. 192.168.0.0/24 or 2001:db2::/64). This range is used to allocate ClusterIPs to Service objects."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"
    _api_group_ = "networking.k8s.io"
    _kind_ = "ServiceCIDR"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: ServiceCIDRSpec
    """ spec is the desired state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ServiceCIDRSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ServiceCIDRStatus(KubernetesObject):
    """ServiceCIDRStatus describes the current state of the ServiceCIDR."""

    __slots__ = ()

    _api_version_ = "networking.k8s.io/v1alpha1"

    conditions: list[meta.Condition]
    """ conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state """

    def __init__(self, conditions: list[meta.Condition] = None):
        super().__init__(conditions=conditions)
