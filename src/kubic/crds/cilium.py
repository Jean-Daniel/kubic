from typing import Any, Dict, List

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
        super().__init__(
            labels=labels,
            region=region,
            security_groups_ids=security_groups_ids,
            security_groups_names=security_groups_names,
        )


class Adding(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "dest_port": "dest-port",
        "identity_labels": "identity-labels",
    }
    _revfield_names_ = {
        "dest-port": "dest_port",
        "identity-labels": "identity_labels",
    }

    dest_port: int
    identity: int
    identity_labels: Dict[str, str]
    protocol: int

    def __init__(
        self,
        dest_port: int = None,
        identity: int = None,
        identity_labels: Dict[str, str] = None,
        protocol: int = None,
    ):
        super().__init__(
            dest_port=dest_port,
            identity=identity,
            identity_labels=identity_labels,
            protocol=protocol,
        )


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


class Addressing(KubernetesObject):
    __slots__ = ()

    ipv4: str
    ipv6: str

    def __init__(self, ipv4: str = None, ipv6: str = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6)


class Allowed(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "dest_port": "dest-port",
        "identity_labels": "identity-labels",
    }
    _revfield_names_ = {
        "dest-port": "dest_port",
        "identity-labels": "identity_labels",
    }

    dest_port: int
    identity: int
    identity_labels: Dict[str, str]
    protocol: int

    def __init__(
        self,
        dest_port: int = None,
        identity: int = None,
        identity_labels: Dict[str, str] = None,
        protocol: int = None,
    ):
        super().__init__(
            dest_port=dest_port,
            identity=identity,
            identity_labels=identity_labels,
            protocol=protocol,
        )


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

    def __init__(
        self,
        mismatch: str = None,
        name: str = None,
        secret: Secret = None,
        value: str = None,
    ):
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

    def __init__(
        self,
        k8s_service: K8sService = None,
        k8s_service_selector: K8sServiceSelector = None,
    ):
        super().__init__(
            k8s_service=k8s_service, k8s_service_selector=k8s_service_selector
        )


class CiliumClusterwideNetworkPolicySpecEgress(KubernetesObject):
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
    to_cidr_set: List[networking.IPBlock]
    to_endpoints: List[meta.LabelSelector]
    to_entities: List[str]
    to_fqd_ns: List[ToFQDN]
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
        to_fqd_ns: List[ToFQDN] = None,
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


class CiliumClusterwideNetworkPolicySpecIngress(KubernetesObject):
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
    ingress: List[CiliumClusterwideNetworkPolicySpecIngress]
    ingress_deny: List[IngressDeny]
    labels: List[Label]
    node_selector: meta.LabelSelector

    def __init__(
        self,
        description: str = None,
        egress: List[CiliumClusterwideNetworkPolicySpecEgress] = None,
        egress_deny: List[EgressDeny] = None,
        endpoint_selector: meta.LabelSelector = None,
        ingress: List[CiliumClusterwideNetworkPolicySpecIngress] = None,
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


class DerivativePolicie(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    enforcing: bool
    error: str
    last_updated: meta.Time
    local_policy_revision: int
    ok: bool

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        enforcing: bool = None,
        error: str = None,
        last_updated: meta.Time = None,
        local_policy_revision: int = None,
        ok: bool = None,
    ):
        super().__init__(
            annotations=annotations,
            enforcing=enforcing,
            error=error,
            last_updated=last_updated,
            local_policy_revision=local_policy_revision,
            ok=ok,
        )


class Node(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    enforcing: bool
    error: str
    last_updated: meta.Time
    local_policy_revision: int
    ok: bool

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        enforcing: bool = None,
        error: str = None,
        last_updated: meta.Time = None,
        local_policy_revision: int = None,
        ok: bool = None,
    ):
        super().__init__(
            annotations=annotations,
            enforcing=enforcing,
            error=error,
            last_updated=last_updated,
            local_policy_revision=local_policy_revision,
            ok=ok,
        )


class CiliumClusterwideNetworkPolicyStatus(KubernetesObject):
    __slots__ = ()

    derivative_policies: Dict[str, DerivativePolicie]
    nodes: Dict[str, Node]

    def __init__(
        self,
        derivative_policies: Dict[str, DerivativePolicie] = None,
        nodes: Dict[str, Node] = None,
    ):
        super().__init__(derivative_policies=derivative_policies, nodes=nodes)


class CiliumClusterwideNetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumClusterwideNetworkPolicySpec
    specs: List[CiliumClusterwideNetworkPolicySpec]
    status: CiliumClusterwideNetworkPolicyStatus

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        spec: CiliumClusterwideNetworkPolicySpec = None,
        specs: List[CiliumClusterwideNetworkPolicySpec] = None,
        status: CiliumClusterwideNetworkPolicyStatus = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumClusterwideNetworkPolicy",
            name,
            "",
            metadata=metadata,
            spec=spec,
            specs=specs,
            status=status,
        )


class Configuration(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "error_retry": "error-retry",
        "error_retry_base": "error-retry-base",
    }
    _revfield_names_ = {
        "error-retry": "error_retry",
        "error-retry-base": "error_retry_base",
    }

    error_retry: bool
    error_retry_base: int
    interval: int

    def __init__(
        self,
        error_retry: bool = None,
        error_retry_base: int = None,
        interval: int = None,
    ):
        super().__init__(
            error_retry=error_retry,
            error_retry_base=error_retry_base,
            interval=interval,
        )


class ControllerStatus(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "consecutive_failure_count": "consecutive-failure-count",
        "failure_count": "failure-count",
        "last_failure_msg": "last-failure-msg",
        "last_failure_timestamp": "last-failure-timestamp",
        "last_success_timestamp": "last-success-timestamp",
        "success_count": "success-count",
    }
    _revfield_names_ = {
        "consecutive-failure-count": "consecutive_failure_count",
        "failure-count": "failure_count",
        "last-failure-msg": "last_failure_msg",
        "last-failure-timestamp": "last_failure_timestamp",
        "last-success-timestamp": "last_success_timestamp",
        "success-count": "success_count",
    }

    consecutive_failure_count: int
    failure_count: int
    last_failure_msg: str
    last_failure_timestamp: str
    last_success_timestamp: str
    success_count: int

    def __init__(
        self,
        consecutive_failure_count: int = None,
        failure_count: int = None,
        last_failure_msg: str = None,
        last_failure_timestamp: str = None,
        last_success_timestamp: str = None,
        success_count: int = None,
    ):
        super().__init__(
            consecutive_failure_count=consecutive_failure_count,
            failure_count=failure_count,
            last_failure_msg=last_failure_msg,
            last_failure_timestamp=last_failure_timestamp,
            last_success_timestamp=last_success_timestamp,
            success_count=success_count,
        )


class Controller(KubernetesObject):
    __slots__ = ()

    configuration: Configuration
    name: str
    status: ControllerStatus
    uuid: str

    def __init__(
        self,
        configuration: Configuration = None,
        name: str = None,
        status: ControllerStatus = None,
        uuid: str = None,
    ):
        super().__init__(
            configuration=configuration, name=name, status=status, uuid=uuid
        )


class Encryption(KubernetesObject):
    __slots__ = ()

    key: int

    def __init__(self, key: int = None):
        super().__init__(key=key)


class ExternalIdentifier(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "container_id": "container-id",
        "container_name": "container-name",
        "docker_endpoint_id": "docker-endpoint-id",
        "docker_network_id": "docker-network-id",
        "k8s_namespace": "k8s-namespace",
        "k8s_pod_name": "k8s-pod-name",
        "pod_name": "pod-name",
    }
    _revfield_names_ = {
        "container-id": "container_id",
        "container-name": "container_name",
        "docker-endpoint-id": "docker_endpoint_id",
        "docker-network-id": "docker_network_id",
        "k8s-namespace": "k8s_namespace",
        "k8s-pod-name": "k8s_pod_name",
        "pod-name": "pod_name",
    }

    container_id: str
    container_name: str
    docker_endpoint_id: str
    docker_network_id: str
    k8s_namespace: str
    k8s_pod_name: str
    pod_name: str

    def __init__(
        self,
        container_id: str = None,
        container_name: str = None,
        docker_endpoint_id: str = None,
        docker_network_id: str = None,
        k8s_namespace: str = None,
        k8s_pod_name: str = None,
        pod_name: str = None,
    ):
        super().__init__(
            container_id=container_id,
            container_name=container_name,
            docker_endpoint_id=docker_endpoint_id,
            docker_network_id=docker_network_id,
            k8s_namespace=k8s_namespace,
            k8s_pod_name=k8s_pod_name,
            pod_name=pod_name,
        )


class StatusHealth(KubernetesObject):
    __slots__ = ()

    bpf: str
    connected: bool
    overall_health: str
    policy: str

    def __init__(
        self,
        bpf: str = None,
        connected: bool = None,
        overall_health: str = None,
        policy: str = None,
    ):
        super().__init__(
            bpf=bpf, connected=connected, overall_health=overall_health, policy=policy
        )


class Identity(KubernetesObject):
    __slots__ = ()

    id: int
    labels: List[str]

    def __init__(self, id: int = None, labels: List[str] = None):
        super().__init__(id=id, labels=labels)


class LOG(KubernetesObject):
    __slots__ = ()

    code: str
    message: str
    state: str
    timestamp: str

    def __init__(
        self,
        code: str = None,
        message: str = None,
        state: str = None,
        timestamp: str = None,
    ):
        super().__init__(code=code, message=message, state=state, timestamp=timestamp)


class NamedPort(KubernetesObject):
    __slots__ = ()

    name: str
    port: int
    protocol: str

    def __init__(self, name: str = None, port: int = None, protocol: str = None):
        super().__init__(name=name, port=port, protocol=protocol)


class Networking(KubernetesObject):
    __slots__ = ()

    _required_ = ["addressing"]

    addressing: List[Addressing]
    node: str

    def __init__(self, addressing: List[Addressing] = None, node: str = None):
        super().__init__(addressing=addressing, node=node)


class Denied(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "dest_port": "dest-port",
        "identity_labels": "identity-labels",
    }
    _revfield_names_ = {
        "dest-port": "dest_port",
        "identity-labels": "identity_labels",
    }

    dest_port: int
    identity: int
    identity_labels: Dict[str, str]
    protocol: int

    def __init__(
        self,
        dest_port: int = None,
        identity: int = None,
        identity_labels: Dict[str, str] = None,
        protocol: int = None,
    ):
        super().__init__(
            dest_port=dest_port,
            identity=identity,
            identity_labels=identity_labels,
            protocol=protocol,
        )


class Removing(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "dest_port": "dest-port",
        "identity_labels": "identity-labels",
    }
    _revfield_names_ = {
        "dest-port": "dest_port",
        "identity-labels": "identity_labels",
    }

    dest_port: int
    identity: int
    identity_labels: Dict[str, str]
    protocol: int

    def __init__(
        self,
        dest_port: int = None,
        identity: int = None,
        identity_labels: Dict[str, str] = None,
        protocol: int = None,
    ):
        super().__init__(
            dest_port=dest_port,
            identity=identity,
            identity_labels=identity_labels,
            protocol=protocol,
        )


class PolicyEgress(KubernetesObject):
    __slots__ = ()

    _required_ = ["enforcing"]

    adding: List[Adding]
    allowed: List[Allowed]
    denied: List[Denied]
    enforcing: bool
    removing: List[Removing]

    def __init__(
        self,
        adding: List[Adding] = None,
        allowed: List[Allowed] = None,
        denied: List[Denied] = None,
        enforcing: bool = None,
        removing: List[Removing] = None,
    ):
        super().__init__(
            adding=adding,
            allowed=allowed,
            denied=denied,
            enforcing=enforcing,
            removing=removing,
        )


class PolicyIngress(KubernetesObject):
    __slots__ = ()

    _required_ = ["enforcing"]

    adding: List[Adding]
    allowed: List[Allowed]
    denied: List[Denied]
    enforcing: bool
    removing: List[Removing]

    def __init__(
        self,
        adding: List[Adding] = None,
        allowed: List[Allowed] = None,
        denied: List[Denied] = None,
        enforcing: bool = None,
        removing: List[Removing] = None,
    ):
        super().__init__(
            adding=adding,
            allowed=allowed,
            denied=denied,
            enforcing=enforcing,
            removing=removing,
        )


class Policy(KubernetesObject):
    __slots__ = ()

    egress: PolicyEgress
    ingress: PolicyIngress

    def __init__(self, egress: PolicyEgress = None, ingress: PolicyIngress = None):
        super().__init__(egress=egress, ingress=ingress)


class CiliumEndpointStatus(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "external_identifiers": "external-identifiers",
        "named_ports": "named-ports",
        "visibility_policy_status": "visibility-policy-status",
    }
    _revfield_names_ = {
        "external-identifiers": "external_identifiers",
        "named-ports": "named_ports",
        "visibility-policy-status": "visibility_policy_status",
    }

    controllers: List[Controller]
    encryption: Encryption
    external_identifiers: ExternalIdentifier
    health: StatusHealth
    id: int
    identity: Identity
    log: List[LOG]
    named_ports: List[NamedPort]
    networking: Networking
    policy: Policy
    state: str
    visibility_policy_status: str

    def __init__(
        self,
        controllers: List[Controller] = None,
        encryption: Encryption = None,
        external_identifiers: ExternalIdentifier = None,
        health: StatusHealth = None,
        id: int = None,
        identity: Identity = None,
        log: List[LOG] = None,
        named_ports: List[NamedPort] = None,
        networking: Networking = None,
        policy: Policy = None,
        state: str = None,
        visibility_policy_status: str = None,
    ):
        super().__init__(
            controllers=controllers,
            encryption=encryption,
            external_identifiers=external_identifiers,
            health=health,
            id=id,
            identity=identity,
            log=log,
            named_ports=named_ports,
            networking=networking,
            policy=policy,
            state=state,
            visibility_policy_status=visibility_policy_status,
        )


class CiliumEndpoint(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    status: CiliumEndpointStatus

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        status: CiliumEndpointStatus = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumEndpoint",
            name,
            namespace,
            metadata=metadata,
            status=status,
        )


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
        super().__init__(
            ipv4_alloc_cidr=ipv4_alloc_cidr, ipv6_alloc_cidr=ipv6_alloc_cidr
        )


class CiliumExternalWorkloadStatus(KubernetesObject):
    __slots__ = ()

    id: int
    ip: str

    def __init__(self, id: int = None, ip: str = None):
        super().__init__(id=id, ip=ip)


class CiliumExternalWorkload(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumExternalWorkloadSpec
    status: CiliumExternalWorkloadStatus

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        spec: CiliumExternalWorkloadSpec = None,
        status: CiliumExternalWorkloadStatus = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumExternalWorkload",
            name,
            "",
            metadata=metadata,
            spec=spec,
            status=status,
        )


class CiliumIdentity(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata", "security_labels"]

    _field_names_ = {
        "security_labels": "security-labels",
    }
    _revfield_names_ = {
        "security-labels": "security_labels",
    }

    metadata: meta.ObjectMeta
    security_labels: Dict[str, str]

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        security_labels: Dict[str, str] = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumIdentity",
            name,
            "",
            metadata=metadata,
            security_labels=security_labels,
        )


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

    def __init__(
        self,
        local_endpoint_selector: meta.LabelSelector = None,
        to_ports: List[RedirectBackendToPort] = None,
    ):
        super().__init__(
            local_endpoint_selector=local_endpoint_selector, to_ports=to_ports
        )


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

    def __init__(
        self,
        namespace: str = None,
        service_name: str = None,
        to_ports: List[ServiceMatcherToPort] = None,
    ):
        super().__init__(
            namespace=namespace, service_name=service_name, to_ports=to_ports
        )


class RedirectFrontend(KubernetesObject):
    __slots__ = ()

    address_matcher: AddressMatcher
    service_matcher: ServiceMatcher

    def __init__(
        self,
        address_matcher: AddressMatcher = None,
        service_matcher: ServiceMatcher = None,
    ):
        super().__init__(
            address_matcher=address_matcher, service_matcher=service_matcher
        )


class CiliumLocalRedirectPolicySpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["redirect_backend", "redirect_frontend"]

    description: str
    redirect_backend: RedirectBackend
    redirect_frontend: RedirectFrontend

    def __init__(
        self,
        description: str = None,
        redirect_backend: RedirectBackend = None,
        redirect_frontend: RedirectFrontend = None,
    ):
        super().__init__(
            description=description,
            redirect_backend=redirect_backend,
            redirect_frontend=redirect_frontend,
        )


class CiliumLocalRedirectPolicyStatus(KubernetesObject):
    __slots__ = ()

    ok: Dict[str, Any]

    def __init__(self, ok: Dict[str, Any] = None):
        super().__init__(ok=ok)


class CiliumLocalRedirectPolicy(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumLocalRedirectPolicySpec
    status: CiliumLocalRedirectPolicyStatus

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: CiliumLocalRedirectPolicySpec = None,
        status: CiliumLocalRedirectPolicyStatus = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumLocalRedirectPolicy",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
            status=status,
        )


class CiliumNetworkPolicySpecEgress(KubernetesObject):
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
    to_cidr_set: List[networking.IPBlock]
    to_endpoints: List[meta.LabelSelector]
    to_entities: List[str]
    to_fqd_ns: List[ToFQDN]
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
        to_fqd_ns: List[ToFQDN] = None,
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
            to_fqd_ns=to_fqd_ns,
            to_groups=to_groups,
            to_ports=to_ports,
            to_requires=to_requires,
            to_services=to_services,
        )


class CiliumNetworkPolicySpecIngress(KubernetesObject):
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


class CiliumNetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    description: str
    egress: List[CiliumNetworkPolicySpecEgress]
    egress_deny: List[EgressDeny]
    endpoint_selector: meta.LabelSelector
    ingress: List[CiliumNetworkPolicySpecIngress]
    ingress_deny: List[IngressDeny]
    labels: List[Label]
    node_selector: meta.LabelSelector

    def __init__(
        self,
        description: str = None,
        egress: List[CiliumNetworkPolicySpecEgress] = None,
        egress_deny: List[EgressDeny] = None,
        endpoint_selector: meta.LabelSelector = None,
        ingress: List[CiliumNetworkPolicySpecIngress] = None,
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


class CiliumNetworkPolicyStatus(KubernetesObject):
    __slots__ = ()

    derivative_policies: Dict[str, DerivativePolicie]
    nodes: Dict[str, Node]

    def __init__(
        self,
        derivative_policies: Dict[str, DerivativePolicie] = None,
        nodes: Dict[str, Node] = None,
    ):
        super().__init__(derivative_policies=derivative_policies, nodes=nodes)


class CiliumNetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumNetworkPolicySpec
    specs: List[CiliumNetworkPolicySpec]
    status: CiliumNetworkPolicyStatus

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: CiliumNetworkPolicySpec = None,
        specs: List[CiliumNetworkPolicySpec] = None,
        status: CiliumNetworkPolicyStatus = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumNetworkPolicy",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
            specs=specs,
            status=status,
        )


class CiliumNodeSpecAddresse(KubernetesObject):
    __slots__ = ()

    ip: str
    type: str

    def __init__(self, ip: str = None, type: str = None):
        super().__init__(ip=ip, type=type)


class CiliumNodeSpecAzure(KubernetesObject):
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


class CiliumNodeSpecENI(KubernetesObject):
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


class CiliumNodeSpecHealth(KubernetesObject):
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


class CiliumNodeSpecIPAM(KubernetesObject):
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
        "instance_id": "instance-id",
    }
    _revfield_names_ = {
        "instance-id": "instance_id",
    }

    addresses: List[CiliumNodeSpecAddresse]
    azure: CiliumNodeSpecAzure
    encryption: Encryption
    eni: CiliumNodeSpecENI
    health: CiliumNodeSpecHealth
    instance_id: str
    ipam: CiliumNodeSpecIPAM
    nodeidentity: int

    def __init__(
        self,
        addresses: List[CiliumNodeSpecAddresse] = None,
        azure: CiliumNodeSpecAzure = None,
        encryption: Encryption = None,
        eni: CiliumNodeSpecENI = None,
        health: CiliumNodeSpecHealth = None,
        instance_id: str = None,
        ipam: CiliumNodeSpecIPAM = None,
        nodeidentity: int = None,
    ):
        super().__init__(
            addresses=addresses,
            azure=azure,
            encryption=encryption,
            eni=eni,
            health=health,
            instance_id=instance_id,
            ipam=ipam,
            nodeidentity=nodeidentity,
        )


class InterfaceAddresse(KubernetesObject):
    __slots__ = ()

    ip: str
    state: str
    subnet: str

    def __init__(self, ip: str = None, state: str = None, subnet: str = None):
        super().__init__(ip=ip, state=state, subnet=subnet)


class Interface(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "security_group": "security-group",
    }
    _revfield_names_ = {
        "security-group": "security_group",
    }

    addresses: List[InterfaceAddresse]
    id: str
    mac: str
    name: str
    security_group: str
    state: str

    def __init__(
        self,
        addresses: List[InterfaceAddresse] = None,
        id: str = None,
        mac: str = None,
        name: str = None,
        security_group: str = None,
        state: str = None,
    ):
        super().__init__(
            addresses=addresses,
            id=id,
            mac=mac,
            name=name,
            security_group=security_group,
            state=state,
        )


class StatusAzure(KubernetesObject):
    __slots__ = ()

    interfaces: List[Interface]

    def __init__(self, interfaces: List[Interface] = None):
        super().__init__(interfaces=interfaces)


class Subnet(KubernetesObject):
    __slots__ = ()

    cidr: str
    id: str

    def __init__(self, cidr: str = None, id: str = None):
        super().__init__(cidr=cidr, id=id)


class VPC(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "primary_cidr": "primary-cidr",
    }
    _revfield_names_ = {
        "primary-cidr": "primary_cidr",
    }

    cidrs: List[str]
    id: str
    primary_cidr: str

    def __init__(
        self, cidrs: List[str] = None, id: str = None, primary_cidr: str = None
    ):
        super().__init__(cidrs=cidrs, id=id, primary_cidr=primary_cidr)


class ENIStatusENI(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "availability_zone": "availability-zone",
        "security_groups": "security-groups",
    }
    _revfield_names_ = {
        "availability-zone": "availability_zone",
        "security-groups": "security_groups",
    }

    addresses: List[str]
    availability_zone: str
    description: str
    id: str
    ip: str
    mac: str
    number: int
    security_groups: List[str]
    subnet: Subnet
    vpc: VPC

    def __init__(
        self,
        addresses: List[str] = None,
        availability_zone: str = None,
        description: str = None,
        id: str = None,
        ip: str = None,
        mac: str = None,
        number: int = None,
        security_groups: List[str] = None,
        subnet: Subnet = None,
        vpc: VPC = None,
    ):
        super().__init__(
            addresses=addresses,
            availability_zone=availability_zone,
            description=description,
            id=id,
            ip=ip,
            mac=mac,
            number=number,
            security_groups=security_groups,
            subnet=subnet,
            vpc=vpc,
        )


class ENIStatus(KubernetesObject):
    __slots__ = ()

    enis: Dict[str, ENIStatusENI]

    def __init__(self, enis: Dict[str, ENIStatusENI] = None):
        super().__init__(enis=enis)


class OperatorStatus(KubernetesObject):
    __slots__ = ()

    error: str

    def __init__(self, error: str = None):
        super().__init__(error=error)


class Used(KubernetesObject):
    __slots__ = ()

    owner: str
    resource: str

    def __init__(self, owner: str = None, resource: str = None):
        super().__init__(owner=owner, resource=resource)


class StatusIPAM(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "operator_status": "operator-status",
    }
    _revfield_names_ = {
        "operator-status": "operator_status",
    }

    operator_status: OperatorStatus
    used: Dict[str, Used]

    def __init__(
        self, operator_status: OperatorStatus = None, used: Dict[str, Used] = None
    ):
        super().__init__(operator_status=operator_status, used=used)


class CiliumNodeStatus(KubernetesObject):
    __slots__ = ()

    azure: StatusAzure
    eni: ENIStatus
    ipam: StatusIPAM

    def __init__(
        self, azure: StatusAzure = None, eni: ENIStatus = None, ipam: StatusIPAM = None
    ):
        super().__init__(azure=azure, eni=eni, ipam=ipam)


class CiliumNode(KubernetesApiResource):
    __slots__ = ()

    _group_ = "cilium.io"
    _version_ = "v2"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumNodeSpec
    status: CiliumNodeStatus

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        spec: CiliumNodeSpec = None,
        status: CiliumNodeStatus = None,
    ):
        super().__init__(
            "cilium.io/v2",
            "CiliumNode",
            name,
            "",
            metadata=metadata,
            spec=spec,
            status=status,
        )
