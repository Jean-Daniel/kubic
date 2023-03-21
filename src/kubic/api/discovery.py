from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class EndpointConditions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    ready: bool
    serving: bool
    terminating: bool

    def __init__(self, ready: bool = None, serving: bool = None, terminating: bool = None):
        super().__init__(ready=ready, serving=serving, terminating=terminating)


class ForZone(KubernetesObject):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class EndpointHints(KubernetesObject):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    for_zones: list[ForZone]

    def __init__(self, for_zones: list[ForZone] = None):
        super().__init__(for_zones=for_zones)


class Endpoint(KubernetesObject):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    _required_ = ["addresses"]

    addresses: list[str]
    conditions: EndpointConditions
    deprecated_topology: dict[str, str]
    hints: EndpointHints
    hostname: str
    node_name: str
    target_ref: core.ObjectReference
    zone: str

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
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    app_protocol: str
    name: str
    port: int
    protocol: str

    def __init__(self, app_protocol: str = None, name: str = None, port: int = None, protocol: str = None):
        super().__init__(app_protocol=app_protocol, name=name, port=port, protocol=protocol)


class EndpointSlice(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"
    _api_group_ = "discovery.k8s.io"
    _kind_ = "EndpointSlice"
    _scope_ = "namespace"

    _required_ = ["address_type", "endpoints"]

    address_type: str
    endpoints: list[Endpoint]
    metadata: meta.ObjectMeta
    ports: list[EndpointPort]

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


class EndpointSliceList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"
    _api_group_ = "discovery.k8s.io"
    _kind_ = "EndpointSliceList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[EndpointSlice]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[EndpointSlice] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)
