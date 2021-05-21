from typing import Dict, List

from .. import KubernetesApiResource, KubernetesObject
from .. import core, meta, networking


class AWS(KubernetesObject):
    __slots__ = ()

    labels: Dict[str, str]
    region: str
    security_groups_ids: List[str]
    security_groups_names: List[str]

    def __init__(
        self,
        labels: Dict[str, str] = None,
        region: str = None,
        security_groups_ids: List[str] = None,
        security_groups_names: List[str] = None,
    ):
        super().__init__(labels=labels, region=region, security_groups_ids=security_groups_ids, security_groups_names=security_groups_names)


class AddressMatcherToPort(KubernetesObject):
    __slots__ = ()

    _required_ = ["port", "protocol"]

    name: str
    port: str
    protocol: str

    def __init__(self, name: str = None, port: str = None, protocol: str = None):
        super().__init__(name=name, port=port, protocol=protocol)


class AddressMatcher(KubernetesObject):
    __slots__ = ()

    _required_ = ["ip", "to_ports"]

    ip: str
    to_ports: List[AddressMatcherToPort]

    def __init__(self, ip: str = None, to_ports: List[AddressMatcherToPort] = None):
        super().__init__(ip=ip, to_ports=to_ports)


class Addresse(KubernetesObject):
    __slots__ = ()

    ip: str
    type: str

    def __init__(self, ip: str = None, type: str = None):
        super().__init__(ip=ip, type=type)


class AlibabaCloud(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "availability_zone": "availability-zone",
        "cidr_block": "cidr-block",
        "instance_type": "instance-type",
        "security_group_tags": "security-group-tags",
        "security_groups": "security-groups",
        "vpc_id": "vpc-id",
        "vswitch_tags": "vswitch-tags",
    }
    _revfield_names_ = {
        "availability-zone": "availability_zone",
        "cidr-block": "cidr_block",
        "instance-type": "instance_type",
        "security-group-tags": "security_group_tags",
        "security-groups": "security_groups",
        "vpc-id": "vpc_id",
        "vswitch-tags": "vswitch_tags",
    }

    availability_zone: str
    cidr_block: str
    instance_type: str
    security_group_tags: Dict[str, str]
    security_groups: List[str]
    vpc_id: str
    vswitch_tags: Dict[str, str]
    vswitches: List[str]

    def __init__(
        self,
        availability_zone: str = None,
        cidr_block: str = None,
        instance_type: str = None,
        security_group_tags: Dict[str, str] = None,
        security_groups: List[str] = None,
        vpc_id: str = None,
        vswitch_tags: Dict[str, str] = None,
        vswitches: List[str] = None,
    ):
        super().__init__(
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            instance_type=instance_type,
            security_group_tags=security_group_tags,
            security_groups=security_groups,
            vpc_id=vpc_id,
            vswitch_tags=vswitch_tags,
            vswitches=vswitches,
        )


class Azure(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "interface_name": "interface-name",
    }
    _revfield_names_ = {
        "interface-name": "interface_name",
    }

    interface_name: str

    def __init__(self, interface_name: str = None):
        super().__init__(interface_name=interface_name)


class ToFQDN(KubernetesObject):
    __slots__ = ()

    match_name: str
    match_pattern: str

    def __init__(self, match_name: str = None, match_pattern: str = None):
        super().__init__(match_name=match_name, match_pattern=match_pattern)


class ToGroup(KubernetesObject):
    __slots__ = ()

    aws: AWS

    def __init__(self, aws: AWS = None):
        super().__init__(aws=aws)


class Secret(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    name: str
    namespace: str

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class OriginatingTLS(KubernetesObject):
    __slots__ = ()

    _required_ = ["secret"]

    _field_names_ = {
        "trusted_ca": "trustedCA",
    }
    _revfield_names_ = {
        "trustedCA": "trusted_ca",
    }

    certificate: str
    private_key: str
    secret: Secret
    trusted_ca: str

    def __init__(self, certificate: str = None, private_key: str = None, secret: Secret = None, trusted_ca: str = None):
        super().__init__(certificate=certificate, private_key=private_key, secret=secret, trusted_ca=trusted_ca)


class Port(KubernetesObject):
    __slots__ = ()

    _required_ = ["port"]

    port: str
    protocol: str

    def __init__(self, port: str = None, protocol: str = None):
        super().__init__(port=port, protocol=protocol)


class DNS(KubernetesObject):
    __slots__ = ()

    match_name: str
    match_pattern: str

    def __init__(self, match_name: str = None, match_pattern: str = None):
        super().__init__(match_name=match_name, match_pattern=match_pattern)


class HeaderMatche(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    mismatch: str
    name: str
    secret: Secret
    value: str

    def __init__(self, mismatch: str = None, name: str = None, secret: Secret = None, value: str = None):
        super().__init__(mismatch=mismatch, name=name, secret=secret, value=value)


class Http(KubernetesObject):
    __slots__ = ()

    header_matches: List[HeaderMatche]
    headers: List[str]
    host: core.IDNHostname
    method: str
    path: str

    def __init__(
        self,
        header_matches: List[HeaderMatche] = None,
        headers: List[str] = None,
        host: core.IDNHostname = None,
        method: str = None,
        path: str = None,
    ):
        super().__init__(header_matches=header_matches, headers=headers, host=host, method=method, path=path)


class Kafka(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "client_id": "clientID",
    }
    _revfield_names_ = {
        "clientID": "client_id",
    }

    api_key: str
    api_version: str
    client_id: str
    role: str
    topic: str

    def __init__(self, api_key: str = None, api_version: str = None, client_id: str = None, role: str = None, topic: str = None):
        super().__init__(api_key=api_key, api_version=api_version, client_id=client_id, role=role, topic=topic)


class Rule(KubernetesObject):
    __slots__ = ()

    dns: List[DNS]
    http: List[Http]
    kafka: List[Kafka]
    l7: List[Dict[str, str]]
    l7proto: str

    def __init__(
        self,
        dns: List[DNS] = None,
        http: List[Http] = None,
        kafka: List[Kafka] = None,
        l7: List[Dict[str, str]] = None,
        l7proto: str = None,
    ):
        super().__init__(dns=dns, http=http, kafka=kafka, l7=l7, l7proto=l7proto)


class TerminatingTLS(KubernetesObject):
    __slots__ = ()

    _required_ = ["secret"]

    _field_names_ = {
        "trusted_ca": "trustedCA",
    }
    _revfield_names_ = {
        "trustedCA": "trusted_ca",
    }

    certificate: str
    private_key: str
    secret: Secret
    trusted_ca: str

    def __init__(self, certificate: str = None, private_key: str = None, secret: Secret = None, trusted_ca: str = None):
        super().__init__(certificate=certificate, private_key=private_key, secret=secret, trusted_ca=trusted_ca)


class EgressToPort(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "originating_tls": "originatingTLS",
        "terminating_tls": "terminatingTLS",
    }
    _revfield_names_ = {
        "originatingTLS": "originating_tls",
        "terminatingTLS": "terminating_tls",
    }

    originating_tls: OriginatingTLS
    ports: List[Port]
    rules: Rule
    terminating_tls: TerminatingTLS

    def __init__(
        self, originating_tls: OriginatingTLS = None, ports: List[Port] = None, rules: Rule = None, terminating_tls: TerminatingTLS = None
    ):
        super().__init__(originating_tls=originating_tls, ports=ports, rules=rules, terminating_tls=terminating_tls)


class K8sService(KubernetesObject):
    __slots__ = ()

    namespace: str
    service_name: str

    def __init__(self, namespace: str = None, service_name: str = None):
        super().__init__(namespace=namespace, service_name=service_name)


class K8sServiceSelector(KubernetesObject):
    __slots__ = ()

    _required_ = ["selector"]

    namespace: str
    selector: meta.LabelSelector

    def __init__(self, namespace: str = None, selector: meta.LabelSelector = None):
        super().__init__(namespace=namespace, selector=selector)


class ToService(KubernetesObject):
    __slots__ = ()

    k8s_service: K8sService
    k8s_service_selector: K8sServiceSelector

    def __init__(self, k8s_service: K8sService = None, k8s_service_selector: K8sServiceSelector = None):
        super().__init__(k8s_service=k8s_service, k8s_service_selector=k8s_service_selector)


class CiliumClusterwideNetworkPolicySpecEgress(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "to_cidr": "toCIDR",
        "to_cidr_set": "toCIDRSet",
        "to_fqdns": "toFQDNs",
    }
    _revfield_names_ = {
        "toCIDR": "to_cidr",
        "toCIDRSet": "to_cidr_set",
        "toFQDNs": "to_fqdns",
    }

    to_cidr: List[str]
    to_cidr_set: List[networking.IPBlock]
    to_endpoints: List[meta.LabelSelector]
    to_entities: List[str]
    to_fqdns: List[ToFQDN]
    to_groups: List[ToGroup]
    to_ports: List[EgressToPort]
    to_requires: List[meta.LabelSelector]
    to_services: List[ToService]

    def __init__(
        self,
        to_cidr: List[str] = None,
        to_cidr_set: List[networking.IPBlock] = None,
        to_endpoints: List[meta.LabelSelector] = None,
        to_entities: List[str] = None,
        to_fqdns: List[ToFQDN] = None,
        to_groups: List[ToGroup] = None,
        to_ports: List[EgressToPort] = None,
        to_requires: List[meta.LabelSelector] = None,
        to_services: List[ToService] = None,
    ):
        super().__init__(
            to_cidr=to_cidr,
            to_cidr_set=to_cidr_set,
            to_endpoints=to_endpoints,
            to_entities=to_entities,
            to_fqdns=to_fqdns,
            to_groups=to_groups,
            to_ports=to_ports,
            to_requires=to_requires,
            to_services=to_services,
        )


class EgressDenyToPort(KubernetesObject):
    __slots__ = ()

    ports: List[Port]

    def __init__(self, ports: List[Port] = None):
        super().__init__(ports=ports)


class EgressDeny(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "to_cidr": "toCIDR",
        "to_cidr_set": "toCIDRSet",
    }
    _revfield_names_ = {
        "toCIDR": "to_cidr",
        "toCIDRSet": "to_cidr_set",
    }

    to_cidr: List[str]
    to_cidr_set: List[networking.IPBlock]
    to_endpoints: List[meta.LabelSelector]
    to_entities: List[str]
    to_groups: List[ToGroup]
    to_ports: List[EgressDenyToPort]
    to_requires: List[meta.LabelSelector]
    to_services: List[ToService]

    def __init__(
        self,
        to_cidr: List[str] = None,
        to_cidr_set: List[networking.IPBlock] = None,
        to_endpoints: List[meta.LabelSelector] = None,
        to_entities: List[str] = None,
        to_groups: List[ToGroup] = None,
        to_ports: List[EgressDenyToPort] = None,
        to_requires: List[meta.LabelSelector] = None,
        to_services: List[ToService] = None,
    ):
        super().__init__(
            to_cidr=to_cidr,
            to_cidr_set=to_cidr_set,
            to_endpoints=to_endpoints,
            to_entities=to_entities,
            to_groups=to_groups,
            to_ports=to_ports,
            to_requires=to_requires,
            to_services=to_services,
        )


class IngressToPort(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "originating_tls": "originatingTLS",
        "terminating_tls": "terminatingTLS",
    }
    _revfield_names_ = {
        "originatingTLS": "originating_tls",
        "terminatingTLS": "terminating_tls",
    }

    originating_tls: OriginatingTLS
    ports: List[Port]
    rules: Rule
    terminating_tls: TerminatingTLS

    def __init__(
        self, originating_tls: OriginatingTLS = None, ports: List[Port] = None, rules: Rule = None, terminating_tls: TerminatingTLS = None
    ):
        super().__init__(originating_tls=originating_tls, ports=ports, rules=rules, terminating_tls=terminating_tls)


class Ingress(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "from_cidr": "fromCIDR",
        "from_cidr_set": "fromCIDRSet",
    }
    _revfield_names_ = {
        "fromCIDR": "from_cidr",
        "fromCIDRSet": "from_cidr_set",
    }

    from_cidr: List[str]
    from_cidr_set: List[networking.IPBlock]
    from_endpoints: List[meta.LabelSelector]
    from_entities: List[str]
    from_requires: List[meta.LabelSelector]
    to_ports: List[IngressToPort]

    def __init__(
        self,
        from_cidr: List[str] = None,
        from_cidr_set: List[networking.IPBlock] = None,
        from_endpoints: List[meta.LabelSelector] = None,
        from_entities: List[str] = None,
        from_requires: List[meta.LabelSelector] = None,
        to_ports: List[IngressToPort] = None,
    ):
        super().__init__(
            from_cidr=from_cidr,
            from_cidr_set=from_cidr_set,
            from_endpoints=from_endpoints,
            from_entities=from_entities,
            from_requires=from_requires,
            to_ports=to_ports,
        )


class IngressDenyToPort(KubernetesObject):
    __slots__ = ()

    ports: List[Port]

    def __init__(self, ports: List[Port] = None):
        super().__init__(ports=ports)


class IngressDeny(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "from_cidr": "fromCIDR",
        "from_cidr_set": "fromCIDRSet",
    }
    _revfield_names_ = {
        "fromCIDR": "from_cidr",
        "fromCIDRSet": "from_cidr_set",
    }

    from_cidr: List[str]
    from_cidr_set: List[networking.IPBlock]
    from_endpoints: List[meta.LabelSelector]
    from_entities: List[str]
    from_requires: List[meta.LabelSelector]
    to_ports: List[IngressDenyToPort]

    def __init__(
        self,
        from_cidr: List[str] = None,
        from_cidr_set: List[networking.IPBlock] = None,
        from_endpoints: List[meta.LabelSelector] = None,
        from_entities: List[str] = None,
        from_requires: List[meta.LabelSelector] = None,
        to_ports: List[IngressDenyToPort] = None,
    ):
        super().__init__(
            from_cidr=from_cidr,
            from_cidr_set=from_cidr_set,
            from_endpoints=from_endpoints,
            from_entities=from_entities,
            from_requires=from_requires,
            to_ports=to_ports,
        )


class Label(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    source: str
    value: str

    def __init__(self, key: str = None, source: str = None, value: str = None):
        super().__init__(key=key, source=source, value=value)


class CiliumClusterwideNetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    description: str
    egress: List[CiliumClusterwideNetworkPolicySpecEgress]
    egress_deny: List[EgressDeny]
    endpoint_selector: meta.LabelSelector
    ingress: List[Ingress]
    ingress_deny: List[IngressDeny]
    labels: List[Label]
    node_selector: meta.LabelSelector

    def __init__(
        self,
        description: str = None,
        egress: List[CiliumClusterwideNetworkPolicySpecEgress] = None,
        egress_deny: List[EgressDeny] = None,
        endpoint_selector: meta.LabelSelector = None,
        ingress: List[Ingress] = None,
        ingress_deny: List[IngressDeny] = None,
        labels: List[Label] = None,
        node_selector: meta.LabelSelector = None,
    ):
        super().__init__(
            description=description,
            egress=egress,
            egress_deny=egress_deny,
            endpoint_selector=endpoint_selector,
            ingress=ingress,
            ingress_deny=ingress_deny,
            labels=labels,
            node_selector=node_selector,
        )


class CiliumClusterwideNetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumClusterwideNetworkPolicy"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumClusterwideNetworkPolicySpec
    specs: List[CiliumClusterwideNetworkPolicySpec]

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        spec: CiliumClusterwideNetworkPolicySpec = None,
        specs: List[CiliumClusterwideNetworkPolicySpec] = None,
    ):
        super().__init__("cilium.io/v2", "CiliumClusterwideNetworkPolicy", name, "", metadata=metadata, spec=spec, specs=specs)


class CiliumEgressNATPolicySpecEgress(KubernetesObject):
    __slots__ = ()

    namespace_selector: meta.LabelSelector
    pod_selector: meta.LabelSelector

    def __init__(self, namespace_selector: meta.LabelSelector = None, pod_selector: meta.LabelSelector = None):
        super().__init__(namespace_selector=namespace_selector, pod_selector=pod_selector)


class CiliumEgressNATPolicySpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["destination_cidrs", "egress", "egress_source_ip"]

    _field_names_ = {
        "destination_cidrs": "destinationCIDRs",
        "egress_source_ip": "egressSourceIP",
    }
    _revfield_names_ = {
        "destinationCIDRs": "destination_cidrs",
        "egressSourceIP": "egress_source_ip",
    }

    destination_cidrs: List[str]
    egress: List[CiliumEgressNATPolicySpecEgress]
    egress_source_ip: str

    def __init__(
        self, destination_cidrs: List[str] = None, egress: List[CiliumEgressNATPolicySpecEgress] = None, egress_source_ip: str = None
    ):
        super().__init__(destination_cidrs=destination_cidrs, egress=egress, egress_source_ip=egress_source_ip)


class CiliumEgressNATPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _kind_ = "CiliumEgressNATPolicy"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumEgressNATPolicySpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumEgressNATPolicySpec = None):
        super().__init__("cilium.io/v2alpha1", "CiliumEgressNATPolicy", name, "", metadata=metadata, spec=spec)


class CiliumEndpoint(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumEndpoint"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None):
        super().__init__("cilium.io/v2", "CiliumEndpoint", name, namespace, metadata=metadata)


class CiliumExternalWorkloadSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "ipv4_alloc_cidr": "ipv4-alloc-cidr",
        "ipv6_alloc_cidr": "ipv6-alloc-cidr",
    }
    _revfield_names_ = {
        "ipv4-alloc-cidr": "ipv4_alloc_cidr",
        "ipv6-alloc-cidr": "ipv6_alloc_cidr",
    }

    ipv4_alloc_cidr: str
    ipv6_alloc_cidr: str

    def __init__(self, ipv4_alloc_cidr: str = None, ipv6_alloc_cidr: str = None):
        super().__init__(ipv4_alloc_cidr=ipv4_alloc_cidr, ipv6_alloc_cidr=ipv6_alloc_cidr)


class CiliumExternalWorkload(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumExternalWorkload"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumExternalWorkloadSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumExternalWorkloadSpec = None):
        super().__init__("cilium.io/v2", "CiliumExternalWorkload", name, "", metadata=metadata, spec=spec)


class CiliumIdentity(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumIdentity"
    _scope_ = "cluster"

    _required_ = ["metadata", "security_labels"]

    _field_names_ = {
        "security_labels": "security-labels",
    }
    _revfield_names_ = {
        "security-labels": "security_labels",
    }

    metadata: meta.ObjectMeta
    security_labels: Dict[str, str]

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, security_labels: Dict[str, str] = None):
        super().__init__("cilium.io/v2", "CiliumIdentity", name, "", metadata=metadata, security_labels=security_labels)


class RedirectBackendToPort(KubernetesObject):
    __slots__ = ()

    _required_ = ["port", "protocol"]

    name: str
    port: str
    protocol: str

    def __init__(self, name: str = None, port: str = None, protocol: str = None):
        super().__init__(name=name, port=port, protocol=protocol)


class RedirectBackend(KubernetesObject):
    __slots__ = ()

    _required_ = ["local_endpoint_selector", "to_ports"]

    local_endpoint_selector: meta.LabelSelector
    to_ports: List[RedirectBackendToPort]

    def __init__(self, local_endpoint_selector: meta.LabelSelector = None, to_ports: List[RedirectBackendToPort] = None):
        super().__init__(local_endpoint_selector=local_endpoint_selector, to_ports=to_ports)


class ServiceMatcherToPort(KubernetesObject):
    __slots__ = ()

    _required_ = ["port", "protocol"]

    name: str
    port: str
    protocol: str

    def __init__(self, name: str = None, port: str = None, protocol: str = None):
        super().__init__(name=name, port=port, protocol=protocol)


class ServiceMatcher(KubernetesObject):
    __slots__ = ()

    _required_ = ["namespace", "service_name"]

    namespace: str
    service_name: str
    to_ports: List[ServiceMatcherToPort]

    def __init__(self, namespace: str = None, service_name: str = None, to_ports: List[ServiceMatcherToPort] = None):
        super().__init__(namespace=namespace, service_name=service_name, to_ports=to_ports)


class RedirectFrontend(KubernetesObject):
    __slots__ = ()

    address_matcher: AddressMatcher
    service_matcher: ServiceMatcher

    def __init__(self, address_matcher: AddressMatcher = None, service_matcher: ServiceMatcher = None):
        super().__init__(address_matcher=address_matcher, service_matcher=service_matcher)


class CiliumLocalRedirectPolicySpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["redirect_backend", "redirect_frontend"]

    description: str
    redirect_backend: RedirectBackend
    redirect_frontend: RedirectFrontend

    def __init__(self, description: str = None, redirect_backend: RedirectBackend = None, redirect_frontend: RedirectFrontend = None):
        super().__init__(description=description, redirect_backend=redirect_backend, redirect_frontend=redirect_frontend)


class CiliumLocalRedirectPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumLocalRedirectPolicy"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumLocalRedirectPolicySpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CiliumLocalRedirectPolicySpec = None):
        super().__init__("cilium.io/v2", "CiliumLocalRedirectPolicy", name, namespace, metadata=metadata, spec=spec)


class CiliumNetworkPolicySpecEgress(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "to_cidr": "toCIDR",
        "to_cidr_set": "toCIDRSet",
        "to_fqdns": "toFQDNs",
    }
    _revfield_names_ = {
        "toCIDR": "to_cidr",
        "toCIDRSet": "to_cidr_set",
        "toFQDNs": "to_fqdns",
    }

    to_cidr: List[str]
    to_cidr_set: List[networking.IPBlock]
    to_endpoints: List[meta.LabelSelector]
    to_entities: List[str]
    to_fqdns: List[ToFQDN]
    to_groups: List[ToGroup]
    to_ports: List[EgressToPort]
    to_requires: List[meta.LabelSelector]
    to_services: List[ToService]

    def __init__(
        self,
        to_cidr: List[str] = None,
        to_cidr_set: List[networking.IPBlock] = None,
        to_endpoints: List[meta.LabelSelector] = None,
        to_entities: List[str] = None,
        to_fqdns: List[ToFQDN] = None,
        to_groups: List[ToGroup] = None,
        to_ports: List[EgressToPort] = None,
        to_requires: List[meta.LabelSelector] = None,
        to_services: List[ToService] = None,
    ):
        super().__init__(
            to_cidr=to_cidr,
            to_cidr_set=to_cidr_set,
            to_endpoints=to_endpoints,
            to_entities=to_entities,
            to_fqdns=to_fqdns,
            to_groups=to_groups,
            to_ports=to_ports,
            to_requires=to_requires,
            to_services=to_services,
        )


class CiliumNetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    description: str
    egress: List[CiliumNetworkPolicySpecEgress]
    egress_deny: List[EgressDeny]
    endpoint_selector: meta.LabelSelector
    ingress: List[Ingress]
    ingress_deny: List[IngressDeny]
    labels: List[Label]
    node_selector: meta.LabelSelector

    def __init__(
        self,
        description: str = None,
        egress: List[CiliumNetworkPolicySpecEgress] = None,
        egress_deny: List[EgressDeny] = None,
        endpoint_selector: meta.LabelSelector = None,
        ingress: List[Ingress] = None,
        ingress_deny: List[IngressDeny] = None,
        labels: List[Label] = None,
        node_selector: meta.LabelSelector = None,
    ):
        super().__init__(
            description=description,
            egress=egress,
            egress_deny=egress_deny,
            endpoint_selector=endpoint_selector,
            ingress=ingress,
            ingress_deny=ingress_deny,
            labels=labels,
            node_selector=node_selector,
        )


class CiliumNetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumNetworkPolicy"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumNetworkPolicySpec
    specs: List[CiliumNetworkPolicySpec]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: CiliumNetworkPolicySpec = None,
        specs: List[CiliumNetworkPolicySpec] = None,
    ):
        super().__init__("cilium.io/v2", "CiliumNetworkPolicy", name, namespace, metadata=metadata, spec=spec, specs=specs)


class Encryption(KubernetesObject):
    __slots__ = ()

    key: int

    def __init__(self, key: int = None):
        super().__init__(key=key)


class ENI(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "availability_zone": "availability-zone",
        "delete_on_termination": "delete-on-termination",
        "first_interface_index": "first-interface-index",
        "instance_id": "instance-id",
        "instance_type": "instance-type",
        "max_above_watermark": "max-above-watermark",
        "min_allocate": "min-allocate",
        "pre_allocate": "pre-allocate",
        "security_group_tags": "security-group-tags",
        "security_groups": "security-groups",
        "subnet_tags": "subnet-tags",
        "vpc_id": "vpc-id",
    }
    _revfield_names_ = {
        "availability-zone": "availability_zone",
        "delete-on-termination": "delete_on_termination",
        "first-interface-index": "first_interface_index",
        "instance-id": "instance_id",
        "instance-type": "instance_type",
        "max-above-watermark": "max_above_watermark",
        "min-allocate": "min_allocate",
        "pre-allocate": "pre_allocate",
        "security-group-tags": "security_group_tags",
        "security-groups": "security_groups",
        "subnet-tags": "subnet_tags",
        "vpc-id": "vpc_id",
    }

    availability_zone: str
    delete_on_termination: bool
    first_interface_index: int
    instance_id: str
    instance_type: str
    max_above_watermark: int
    min_allocate: int
    pre_allocate: int
    security_group_tags: Dict[str, str]
    security_groups: List[str]
    subnet_tags: Dict[str, str]
    vpc_id: str

    def __init__(
        self,
        availability_zone: str = None,
        delete_on_termination: bool = None,
        first_interface_index: int = None,
        instance_id: str = None,
        instance_type: str = None,
        max_above_watermark: int = None,
        min_allocate: int = None,
        pre_allocate: int = None,
        security_group_tags: Dict[str, str] = None,
        security_groups: List[str] = None,
        subnet_tags: Dict[str, str] = None,
        vpc_id: str = None,
    ):
        super().__init__(
            availability_zone=availability_zone,
            delete_on_termination=delete_on_termination,
            first_interface_index=first_interface_index,
            instance_id=instance_id,
            instance_type=instance_type,
            max_above_watermark=max_above_watermark,
            min_allocate=min_allocate,
            pre_allocate=pre_allocate,
            security_group_tags=security_group_tags,
            security_groups=security_groups,
            subnet_tags=subnet_tags,
            vpc_id=vpc_id,
        )


class Health(KubernetesObject):
    __slots__ = ()

    ipv4: str
    ipv6: str

    def __init__(self, ipv4: str = None, ipv6: str = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6)


class Pool(KubernetesObject):
    __slots__ = ()

    owner: str
    resource: str

    def __init__(self, owner: str = None, resource: str = None):
        super().__init__(owner=owner, resource=resource)


class IPAM(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "max_above_watermark": "max-above-watermark",
        "max_allocate": "max-allocate",
        "min_allocate": "min-allocate",
        "pod_cidrs": "podCIDRs",
        "pre_allocate": "pre-allocate",
    }
    _revfield_names_ = {
        "max-above-watermark": "max_above_watermark",
        "max-allocate": "max_allocate",
        "min-allocate": "min_allocate",
        "podCIDRs": "pod_cidrs",
        "pre-allocate": "pre_allocate",
    }

    max_above_watermark: int
    max_allocate: int
    min_allocate: int
    pod_cidrs: List[str]
    pool: Dict[str, Pool]
    pre_allocate: int

    def __init__(
        self,
        max_above_watermark: int = None,
        max_allocate: int = None,
        min_allocate: int = None,
        pod_cidrs: List[str] = None,
        pool: Dict[str, Pool] = None,
        pre_allocate: int = None,
    ):
        super().__init__(
            max_above_watermark=max_above_watermark,
            max_allocate=max_allocate,
            min_allocate=min_allocate,
            pod_cidrs=pod_cidrs,
            pool=pool,
            pre_allocate=pre_allocate,
        )


class CiliumNodeSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "alibaba_cloud": "alibaba-cloud",
        "instance_id": "instance-id",
    }
    _revfield_names_ = {
        "alibaba-cloud": "alibaba_cloud",
        "instance-id": "instance_id",
    }

    addresses: List[Addresse]
    alibaba_cloud: AlibabaCloud
    azure: Azure
    encryption: Encryption
    eni: ENI
    health: Health
    instance_id: str
    ipam: IPAM
    nodeidentity: int

    def __init__(
        self,
        addresses: List[Addresse] = None,
        alibaba_cloud: AlibabaCloud = None,
        azure: Azure = None,
        encryption: Encryption = None,
        eni: ENI = None,
        health: Health = None,
        instance_id: str = None,
        ipam: IPAM = None,
        nodeidentity: int = None,
    ):
        super().__init__(
            addresses=addresses,
            alibaba_cloud=alibaba_cloud,
            azure=azure,
            encryption=encryption,
            eni=eni,
            health=health,
            instance_id=instance_id,
            ipam=ipam,
            nodeidentity=nodeidentity,
        )


class CiliumNode(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _kind_ = "CiliumNode"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumNodeSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumNodeSpec = None):
        super().__init__("cilium.io/v2", "CiliumNode", name, "", metadata=metadata, spec=spec)
