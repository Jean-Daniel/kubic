from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta



class ServiceReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    name: str
    namespace: str
    port: int

    def __init__(self, name: str = None, namespace: str = None, port: int = None):
        super().__init__(name=name, namespace=namespace, port=port)


class APIServiceSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    _required_ = ["group_priority_minimum", "version_priority"]

    _field_names_ = {
        "insecure_skip_tls_verify": "insecureSkipTLSVerify",
    }
    _revfield_names_ = {
        "insecureSkipTLSVerify": "insecure_skip_tls_verify",
    }

    ca_bundle: core.Base64
    group: str
    group_priority_minimum: int
    insecure_skip_tls_verify: bool
    service: ServiceReference
    version: str
    version_priority: int

    def __init__(self, ca_bundle: core.Base64 = None, group: str = None, group_priority_minimum: int = None, insecure_skip_tls_verify: bool = None, service: ServiceReference = None, version: str = None, version_priority: int = None):
        super().__init__(ca_bundle=ca_bundle, group=group, group_priority_minimum=group_priority_minimum, insecure_skip_tls_verify=insecure_skip_tls_verify, service=service, version=version, version_priority=version_priority)


class APIService(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"
    _api_group_ = "apiregistration.k8s.io"
    _kind_ = "APIService"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: APIServiceSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: APIServiceSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class APIServiceCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class APIServiceList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"
    _api_group_ = "apiregistration.k8s.io"
    _kind_ = "APIServiceList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[APIService]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[APIService] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class APIServiceStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    conditions: list[APIServiceCondition]

    def __init__(self, conditions: list[APIServiceCondition] = None):
        super().__init__(conditions=conditions)


