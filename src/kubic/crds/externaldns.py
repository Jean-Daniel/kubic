from typing import Dict, List

from .. import KubernetesApiResource, KubernetesObject
from .. import meta


class ProviderSpecific(KubernetesObject):
    __slots__ = ()

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class Endpoint(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "record_ttl": "recordTTL",
    }
    _revfield_names_ = {
        "recordTTL": "record_ttl",
    }

    dns_name: str
    labels: Dict[str, str]
    provider_specific: List[ProviderSpecific]
    record_ttl: int
    record_type: str
    set_identifier: str
    targets: List[str]

    def __init__(
        self,
        dns_name: str = None,
        labels: Dict[str, str] = None,
        provider_specific: List[ProviderSpecific] = None,
        record_ttl: int = None,
        record_type: str = None,
        set_identifier: str = None,
        targets: List[str] = None,
    ):
        super().__init__(
            dns_name=dns_name,
            labels=labels,
            provider_specific=provider_specific,
            record_ttl=record_ttl,
            record_type=record_type,
            set_identifier=set_identifier,
            targets=targets,
        )


class DNSEndpointSpec(KubernetesObject):
    __slots__ = ()

    endpoints: List[Endpoint]

    def __init__(self, endpoints: List[Endpoint] = None):
        super().__init__(endpoints=endpoints)


class DNSEndpoint(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "externaldns.k8s.io/v1alpha1"
    _kind_ = "DNSEndpoint"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: DNSEndpointSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DNSEndpointSpec = None):
        super().__init__("externaldns.k8s.io/v1alpha1", "DNSEndpoint", name, namespace, metadata=metadata, spec=spec)
