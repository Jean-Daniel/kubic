import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from ..api import meta


class Addresse(KubernetesObject):
    __slots__ = ()

    _required_ = ["value"]

    type: str
    value: str

    def __init__(self, type: str = None, value: str = None):
        super().__init__(type=type, value=value)


class Kind(KubernetesObject):
    __slots__ = ()

    _required_ = ["kind"]

    group: str
    kind: str

    def __init__(self, group: str = None, kind: str = None):
        super().__init__(group=group, kind=kind)


class Namespace(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "from": "from_",
    }

    from_: str
    selector: meta.LabelSelector

    def __init__(self, from_: str = None, selector: meta.LabelSelector = None):
        super().__init__(from_=from_, selector=selector)


class AllowedRoute(KubernetesObject):
    __slots__ = ()

    kinds: t.List[Kind]
    namespaces: Namespace

    def __init__(self, kinds: t.List[Kind] = None, namespaces: Namespace = None):
        super().__init__(kinds=kinds, namespaces=namespaces)


class CertificateRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    group: str
    kind: str
    name: str
    namespace: str

    def __init__(self, group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(group=group, kind=kind, name=name, namespace=namespace)


class ExtensionRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["group", "kind", "name"]

    group: str
    kind: str
    name: str

    def __init__(self, group: str = None, kind: str = None, name: str = None):
        super().__init__(group=group, kind=kind, name=name)


class RequestHeader(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "value"]

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class RequestHeaderModifier(KubernetesObject):
    __slots__ = ()

    add: t.List[RequestHeader]
    remove: t.List[str]
    set: t.List[RequestHeader]

    def __init__(self, add: t.List[RequestHeader] = None, remove: t.List[str] = None, set: t.List[RequestHeader] = None):
        super().__init__(add=add, remove=remove, set=set)


class RequestMirrorBackendRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    group: str
    kind: str
    name: str
    namespace: str
    port: int

    def __init__(self, group: str = None, kind: str = None, name: str = None, namespace: str = None, port: int = None):
        super().__init__(group=group, kind=kind, name=name, namespace=namespace, port=port)


class RequestMirror(KubernetesObject):
    __slots__ = ()

    _required_ = ["backend_ref"]

    backend_ref: RequestMirrorBackendRef

    def __init__(self, backend_ref: RequestMirrorBackendRef = None):
        super().__init__(backend_ref=backend_ref)


class RequestRedirect(KubernetesObject):
    __slots__ = ()

    hostname: str
    port: int
    scheme: str
    status_code: int

    def __init__(self, hostname: str = None, port: int = None, scheme: str = None, status_code: int = None):
        super().__init__(hostname=hostname, port=port, scheme=scheme, status_code=status_code)


class Filter(KubernetesObject):
    __slots__ = ()

    _required_ = ["type"]

    extension_ref: ExtensionRef
    request_header_modifier: RequestHeaderModifier
    request_mirror: RequestMirror
    request_redirect: RequestRedirect
    type: str

    def __init__(
        self,
        extension_ref: ExtensionRef = None,
        request_header_modifier: RequestHeaderModifier = None,
        request_mirror: RequestMirror = None,
        request_redirect: RequestRedirect = None,
        type: str = None,
    ):
        super().__init__(
            extension_ref=extension_ref,
            request_header_modifier=request_header_modifier,
            request_mirror=request_mirror,
            request_redirect=request_redirect,
            type=type,
        )


class TLS(KubernetesObject):
    __slots__ = ()

    certificate_refs: t.List[CertificateRef]
    mode: str
    options: t.Dict[str, str]

    def __init__(self, certificate_refs: t.List[CertificateRef] = None, mode: str = None, options: t.Dict[str, str] = None):
        super().__init__(certificate_refs=certificate_refs, mode=mode, options=options)


class Listener(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "port", "protocol"]

    allowed_routes: AllowedRoute
    hostname: str
    name: str
    port: int
    protocol: str
    tls: TLS

    def __init__(
        self,
        allowed_routes: AllowedRoute = None,
        hostname: str = None,
        name: str = None,
        port: int = None,
        protocol: str = None,
        tls: TLS = None,
    ):
        super().__init__(allowed_routes=allowed_routes, hostname=hostname, name=name, port=port, protocol=protocol, tls=tls)


class GatewaySpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["gateway_class_name", "listeners"]

    addresses: t.List[Addresse]
    gateway_class_name: str
    listeners: t.List[Listener]

    def __init__(self, addresses: t.List[Addresse] = None, gateway_class_name: str = None, listeners: t.List[Listener] = None):
        super().__init__(addresses=addresses, gateway_class_name=gateway_class_name, listeners=listeners)


class Gateway(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "gateway.networking.k8s.io/v1beta1"
    _kind_ = "Gateway"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: GatewaySpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: GatewaySpec = None):
        super().__init__("gateway.networking.k8s.io/v1beta1", "Gateway", name, namespace, metadata=metadata, spec=spec)


class ParametersRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["group", "kind", "name"]

    group: str
    kind: str
    name: str
    namespace: str

    def __init__(self, group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(group=group, kind=kind, name=name, namespace=namespace)


class GatewayClassSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["controller_name"]

    controller_name: str
    description: str
    parameters_ref: ParametersRef

    def __init__(self, controller_name: str = None, description: str = None, parameters_ref: ParametersRef = None):
        super().__init__(controller_name=controller_name, description=description, parameters_ref=parameters_ref)


class GatewayClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "gateway.networking.k8s.io/v1beta1"
    _kind_ = "GatewayClass"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: GatewayClassSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: GatewayClassSpec = None):
        super().__init__("gateway.networking.k8s.io/v1beta1", "GatewayClass", name, "", metadata=metadata, spec=spec)


class ParentRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    group: str
    kind: str
    name: str
    namespace: str
    section_name: str

    def __init__(self, group: str = None, kind: str = None, name: str = None, namespace: str = None, section_name: str = None):
        super().__init__(group=group, kind=kind, name=name, namespace=namespace, section_name=section_name)


class RuleBackendRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    filters: t.List[Filter]
    group: str
    kind: str
    name: str
    namespace: str
    port: int
    weight: int

    def __init__(
        self,
        filters: t.List[Filter] = None,
        group: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        port: int = None,
        weight: int = None,
    ):
        super().__init__(filters=filters, group=group, kind=kind, name=name, namespace=namespace, port=port, weight=weight)


class Header(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "value"]

    name: str
    type: str
    value: str

    def __init__(self, name: str = None, type: str = None, value: str = None):
        super().__init__(name=name, type=type, value=value)


class Path(KubernetesObject):
    __slots__ = ()

    type: str
    value: str

    def __init__(self, type: str = None, value: str = None):
        super().__init__(type=type, value=value)


class QueryParam(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "value"]

    name: str
    type: str
    value: str

    def __init__(self, name: str = None, type: str = None, value: str = None):
        super().__init__(name=name, type=type, value=value)


class Match(KubernetesObject):
    __slots__ = ()

    headers: t.List[Header]
    method: str
    path: Path
    query_params: t.List[QueryParam]

    def __init__(self, headers: t.List[Header] = None, method: str = None, path: Path = None, query_params: t.List[QueryParam] = None):
        super().__init__(headers=headers, method=method, path=path, query_params=query_params)


class Rule(KubernetesObject):
    __slots__ = ()

    backend_refs: t.List[RuleBackendRef]
    filters: t.List[Filter]
    matches: t.List[Match]

    def __init__(self, backend_refs: t.List[RuleBackendRef] = None, filters: t.List[Filter] = None, matches: t.List[Match] = None):
        super().__init__(backend_refs=backend_refs, filters=filters, matches=matches)


class HTTPRouteSpec(KubernetesObject):
    __slots__ = ()

    hostnames: t.List[str]
    parent_refs: t.List[ParentRef]
    rules: t.List[Rule]

    def __init__(self, hostnames: t.List[str] = None, parent_refs: t.List[ParentRef] = None, rules: t.List[Rule] = None):
        super().__init__(hostnames=hostnames, parent_refs=parent_refs, rules=rules)


class HTTPRoute(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "gateway.networking.k8s.io/v1beta1"
    _kind_ = "HTTPRoute"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: HTTPRouteSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: HTTPRouteSpec = None):
        super().__init__("gateway.networking.k8s.io/v1beta1", "HTTPRoute", name, namespace, metadata=metadata, spec=spec)
