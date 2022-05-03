from typing import Dict, List

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

    for_zones: List[ForZone]

    def __init__(self, for_zones: List[ForZone] = None):
        super().__init__(for_zones=for_zones)


class Endpoint(KubernetesObject):
    __slots__ = ()

    _api_version_ = "discovery.k8s.io/v1"

    _required_ = ["addresses"]

    addresses: List[str]
    conditions: EndpointConditions
    deprecated_topology: Dict[str, str]
    hints: EndpointHints
    hostname: str
    node_name: str
    target_ref: core.ObjectReference
    zone: str

    def __init__(
        self,
        addresses: List[str] = None,
        conditions: EndpointConditions = None,
        deprecated_topology: Dict[str, str] = None,
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
    _kind_ = "EndpointSlice"
    _scope_ = "namespace"

    _required_ = ["address_type", "endpoints"]

    address_type: str
    endpoints: List[Endpoint]
    metadata: meta.ObjectMeta
    ports: List[EndpointPort]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        address_type: str = None,
        endpoints: List[Endpoint] = None,
        metadata: meta.ObjectMeta = None,
        ports: List[EndpointPort] = None,
    ):
        super().__init__(
            "discovery.k8s.io/v1",
            "EndpointSlice",
            name,
            namespace,
            address_type=address_type,
            endpoints=endpoints,
            metadata=metadata,
            ports=ports,
        )
