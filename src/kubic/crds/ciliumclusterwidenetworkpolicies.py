from typing import Dict, List

from .. import api
from ..base import KubernetesObject, KubernetesApiResource


class ToCIDRSet(KubernetesObject):
    __slots__ = ()
    _revfield_names_ = {
        "except": "except_",
    }

    cidr: str
    except_: List[str]

    _required_ = ["cidr"]

    def __init__(self, cidr: str = None, except_: List[str] = None):
        super().__init__(cidr=cidr, except_=except_)


class MatchExpression(KubernetesObject):
    __slots__ = ()

    key: str
    operator: str
    values: List[str]

    _required_ = ["key", "operator"]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class ToEndpoint(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class ToFQDN(KubernetesObject):
    __slots__ = ()

    match_name: str
    match_pattern: str

    def __init__(self, match_name: str = None, match_pattern: str = None):
        super().__init__(match_name=match_name, match_pattern=match_pattern)


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
        super().__init__(
            labels=labels,
            region=region,
            security_groups_ids=security_groups_ids,
            security_groups_names=security_groups_names,
        )


class ToGroup(KubernetesObject):
    __slots__ = ()

    aws: AWS

    def __init__(self, aws: AWS = None):
        super().__init__(aws=aws)


class Secret(KubernetesObject):
    __slots__ = ()

    name: str
    namespace: str

    _required_ = ["name"]

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class OriginatingTLS(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["secret"]

    def __init__(
        self,
        certificate: str = None,
        private_key: str = None,
        secret: Secret = None,
        trusted_ca: str = None,
    ):
        super().__init__(
            certificate=certificate,
            private_key=private_key,
            secret=secret,
            trusted_ca=trusted_ca,
        )


class Port(KubernetesObject):
    __slots__ = ()

    port: str
    protocol: str

    _required_ = ["port"]

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

    mismatch: str
    name: str
    secret: Secret
    value: str

    _required_ = ["name"]

    def __init__(
        self,
        mismatch: str = None,
        name: str = None,
        secret: Secret = None,
        value: str = None,
    ):
        super().__init__(mismatch=mismatch, name=name, secret=secret, value=value)


IDNHostname = str


class Http(KubernetesObject):
    __slots__ = ()

    header_matches: List[HeaderMatche]
    headers: List[str]
    host: IDNHostname
    method: str
    path: str

    def __init__(
        self,
        header_matches: List[HeaderMatche] = None,
        headers: List[str] = None,
        host: IDNHostname = None,
        method: str = None,
        path: str = None,
    ):
        super().__init__(
            header_matches=header_matches,
            headers=headers,
            host=host,
            method=method,
            path=path,
        )


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

    def __init__(
        self,
        api_key: str = None,
        api_version: str = None,
        client_id: str = None,
        role: str = None,
        topic: str = None,
    ):
        super().__init__(
            api_key=api_key,
            api_version=api_version,
            client_id=client_id,
            role=role,
            topic=topic,
        )


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

    _required_ = ["secret"]

    def __init__(
        self,
        certificate: str = None,
        private_key: str = None,
        secret: Secret = None,
        trusted_ca: str = None,
    ):
        super().__init__(
            certificate=certificate,
            private_key=private_key,
            secret=secret,
            trusted_ca=trusted_ca,
        )


class ToRequire(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class K8sService(KubernetesObject):
    __slots__ = ()

    namespace: str
    service_name: str

    def __init__(self, namespace: str = None, service_name: str = None):
        super().__init__(namespace=namespace, service_name=service_name)


class Selector(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class K8sServiceSelector(KubernetesObject):
    __slots__ = ()

    namespace: str
    selector: Selector

    _required_ = ["selector"]

    def __init__(self, namespace: str = None, selector: Selector = None):
        super().__init__(namespace=namespace, selector=selector)


class ToService(KubernetesObject):
    __slots__ = ()

    k8s_service: K8sService
    k8s_service_selector: K8sServiceSelector

    def __init__(
        self,
        k8s_service: K8sService = None,
        k8s_service_selector: K8sServiceSelector = None,
    ):
        super().__init__(
            k8s_service=k8s_service, k8s_service_selector=k8s_service_selector
        )


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
        self,
        originating_tls: OriginatingTLS = None,
        ports: List[Port] = None,
        rules: Rule = None,
        terminating_tls: TerminatingTLS = None,
    ):
        super().__init__(
            originating_tls=originating_tls,
            ports=ports,
            rules=rules,
            terminating_tls=terminating_tls,
        )


class Egress(KubernetesObject):
    __slots__ = ()
    _field_names_ = {
        "to_cidr": "toCIDR",
        "to_cidr_set": "toCIDRSet",
        "to_fqd_ns": "toFQDNs",
    }
    _revfield_names_ = {
        "toCIDR": "to_cidr",
        "toCIDRSet": "to_cidr_set",
        "toFQDNs": "to_fqd_ns",
    }

    to_cidr: List[str]
    to_cidr_set: List[ToCIDRSet]
    to_endpoints: List[ToEndpoint]
    to_entities: List[str]
    to_fqd_ns: List[ToFQDN]
    to_groups: List[ToGroup]
    to_ports: List[EgressToPort]
    to_requires: List[ToRequire]
    to_services: List[ToService]

    def __init__(
        self,
        to_cidr: List[str] = None,
        to_cidr_set: List[ToCIDRSet] = None,
        to_endpoints: List[ToEndpoint] = None,
        to_entities: List[str] = None,
        to_fqd_ns: List[ToFQDN] = None,
        to_groups: List[ToGroup] = None,
        to_ports: List[EgressToPort] = None,
        to_requires: List[ToRequire] = None,
        to_services: List[ToService] = None,
    ):
        super().__init__(
            to_cidr=to_cidr,
            to_cidr_set=to_cidr_set,
            to_endpoints=to_endpoints,
            to_entities=to_entities,
            to_fqd_ns=to_fqd_ns,
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
    to_cidr_set: List[ToCIDRSet]
    to_endpoints: List[ToEndpoint]
    to_entities: List[str]
    to_groups: List[ToGroup]
    to_ports: List[EgressDenyToPort]
    to_requires: List[ToRequire]
    to_services: List[ToService]

    def __init__(
        self,
        to_cidr: List[str] = None,
        to_cidr_set: List[ToCIDRSet] = None,
        to_endpoints: List[ToEndpoint] = None,
        to_entities: List[str] = None,
        to_groups: List[ToGroup] = None,
        to_ports: List[EgressDenyToPort] = None,
        to_requires: List[ToRequire] = None,
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


class EndpointSelector(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class FromCIDRSet(KubernetesObject):
    __slots__ = ()
    _revfield_names_ = {
        "except": "except_",
    }

    cidr: str
    except_: List[str]

    _required_ = ["cidr"]

    def __init__(self, cidr: str = None, except_: List[str] = None):
        super().__init__(cidr=cidr, except_=except_)


class FromEndpoint(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class FromRequire(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


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
        self,
        originating_tls: OriginatingTLS = None,
        ports: List[Port] = None,
        rules: Rule = None,
        terminating_tls: TerminatingTLS = None,
    ):
        super().__init__(
            originating_tls=originating_tls,
            ports=ports,
            rules=rules,
            terminating_tls=terminating_tls,
        )


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
    from_cidr_set: List[FromCIDRSet]
    from_endpoints: List[FromEndpoint]
    from_entities: List[str]
    from_requires: List[FromRequire]
    to_ports: List[IngressToPort]

    def __init__(
        self,
        from_cidr: List[str] = None,
        from_cidr_set: List[FromCIDRSet] = None,
        from_endpoints: List[FromEndpoint] = None,
        from_entities: List[str] = None,
        from_requires: List[FromRequire] = None,
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
    from_cidr_set: List[FromCIDRSet]
    from_endpoints: List[FromEndpoint]
    from_entities: List[str]
    from_requires: List[FromRequire]
    to_ports: List[IngressDenyToPort]

    def __init__(
        self,
        from_cidr: List[str] = None,
        from_cidr_set: List[FromCIDRSet] = None,
        from_endpoints: List[FromEndpoint] = None,
        from_entities: List[str] = None,
        from_requires: List[FromRequire] = None,
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

    key: str
    source: str
    value: str

    _required_ = ["key"]

    def __init__(self, key: str = None, source: str = None, value: str = None):
        super().__init__(key=key, source=source, value=value)


class NodeSelector(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[MatchExpression] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class CiliumClusterwideNetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    description: str
    egress: List[Egress]
    egress_deny: List[EgressDeny]
    endpoint_selector: EndpointSelector
    ingress: List[Ingress]
    ingress_deny: List[IngressDeny]
    labels: List[Label]
    node_selector: NodeSelector

    def __init__(
        self,
        description: str = None,
        egress: List[Egress] = None,
        egress_deny: List[EgressDeny] = None,
        endpoint_selector: EndpointSelector = None,
        ingress: List[Ingress] = None,
        ingress_deny: List[IngressDeny] = None,
        labels: List[Label] = None,
        node_selector: NodeSelector = None,
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

    _group_ = "cilium.io"

    metadata: api.ObjectMeta
    spec: CiliumClusterwideNetworkPolicySpec
    specs: List[CiliumClusterwideNetworkPolicySpec]

    _required_ = ["metadata"]

    def __init__(
        self,
        name: str,
        metadata: api.ObjectMeta = None,
        spec: CiliumClusterwideNetworkPolicySpec = None,
        specs: List[CiliumClusterwideNetworkPolicySpec] = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumClusterwideNetworkPolicy",
            name,
            "",
            metadata=metadata,
            spec=spec,
            specs=specs,
        )
