from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class EndpointConditions(KubernetesObject):
    """EndpointConditions represents the current condition of an endpoint."""

    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    ready: bool
    """ ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag. """
    serving: bool
    """ serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. """
    terminating: bool
    """ terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. """

    def __init__(self, ready: bool = None, serving: bool = None, terminating: bool = None):
        super().__init__(ready=ready, serving=serving, terminating=terminating)


class ForZone(KubernetesObject):
    """ForZone provides information about which zones should consume this endpoint."""

    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    _required_ = ["name"]

    name: str
    """ name represents the name of the zone. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class EndpointHints(KubernetesObject):
    """EndpointHints provides hints describing how an endpoint should be consumed."""

    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    for_zones: list[ForZone]
    """ forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. """

    def __init__(self, for_zones: list[ForZone] = None):
        super().__init__(for_zones=for_zones)


class Endpoint(KubernetesObject):
    """Endpoint represents a single logical "backend" implementing a service."""

    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    _required_ = ["addresses"]

    addresses: list[str]
    """ addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267 """
    conditions: EndpointConditions
    """ conditions contains information about the current status of the endpoint. """
    deprecated_topology: dict[str, str]
    """ deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead. """
    hints: EndpointHints
    """ hints contains information associated with how an endpoint should be consumed. """
    hostname: str
    """ hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation. """
    node_name: str
    """ nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. """
    target_ref: core.ObjectReference
    """ targetRef is a reference to a Kubernetes object that represents this endpoint. """
    zone: str
    """ zone is the name of the Zone this endpoint exists in. """

    def __init__(
        self,
        addresses: list[str] = None,
        conditions: EndpointConditions = None,
        deprecated_topology: dict[str, str] = None,
        hints: EndpointHints = None,
        hostname: str = None,
        node_name: str = None,
        target_ref: core.ObjectReference = None,
        zone: str = None,
    ):
        super().__init__(
            addresses=addresses,
            conditions=conditions,
            deprecated_topology=deprecated_topology,
            hints=hints,
            hostname=hostname,
            node_name=node_name,
            target_ref=target_ref,
            zone=zone,
        )


class EndpointPort(KubernetesObject):
    """EndpointPort represents a Port used by an EndpointSlice"""

    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    app_protocol: str
    """
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:
    
    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).
    
    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455
    
    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
    """
    name: str
    """ name represents the name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is derived from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string. """
    port: int
    """ port represents the port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer. """
    protocol: str
    """ protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. """

    def __init__(self, app_protocol: str = None, name: str = None, port: int = None, protocol: str = None):
        super().__init__(app_protocol=app_protocol, name=name, port=port, protocol=protocol)


class EndpointSlice(KubernetesApiResource):
    """EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints."""

    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"
    _api_group_ = "discovery.k8s.io"
    _kind_ = "EndpointSlice"
    _scope_ = "namespace"

    _required_ = ["address_type", "endpoints"]

    address_type: str
    """ addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name. """
    endpoints: list[Endpoint]
    """ endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. """
    ports: list[EndpointPort]
    """ ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports. """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        address_type: str = None,
        endpoints: list[Endpoint] = None,
        metadata: meta.ObjectMeta = None,
        ports: list[EndpointPort] = None,
    ):
        super().__init__(name, namespace, address_type=address_type, endpoints=endpoints, metadata=metadata, ports=ports)
