from typing import Dict, List, Union

from ..base import KubernetesObject, KubernetesApiResource
from .. import api


class Password(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Username(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class BasicAuth(KubernetesObject):
    __slots__ = ()

    password: Password
    username: Username

    def __init__(self, password: Password = None, username: Username = None):
        super().__init__(password=password, username=username)


class BearerTokenSecret(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class MetricRelabeling(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: List[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: List[str] = None,
        target_label: str = None,
    ):
        super().__init__(
            action=action,
            modulus=modulus,
            regex=regex,
            replacement=replacement,
            separator=separator,
            source_labels=source_labels,
            target_label=target_label,
        )


class Relabeling(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: List[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: List[str] = None,
        target_label: str = None,
    ):
        super().__init__(
            action=action,
            modulus=modulus,
            regex=regex,
            replacement=replacement,
            separator=separator,
            source_labels=source_labels,
            target_label=target_label,
        )


IntOrString = Union[int, str]


class ConfigMap(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Secret(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class CA(KubernetesObject):
    __slots__ = ()

    config_map: ConfigMap
    secret: Secret

    def __init__(self, config_map: ConfigMap = None, secret: Secret = None):
        super().__init__(config_map=config_map, secret=secret)


class Cert(KubernetesObject):
    __slots__ = ()

    config_map: ConfigMap
    secret: Secret

    def __init__(self, config_map: ConfigMap = None, secret: Secret = None):
        super().__init__(config_map=config_map, secret=secret)


class KeySecret(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class TLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class Endpoint(KubernetesObject):
    __slots__ = ()

    basic_auth: BasicAuth
    bearer_token_file: str
    bearer_token_secret: BearerTokenSecret
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    metric_relabelings: List[MetricRelabeling]
    params: Dict[str, List[str]]
    path: str
    port: str
    proxy_url: str
    relabelings: List[Relabeling]
    scheme: str
    scrape_timeout: str
    target_port: IntOrString
    tls_config: TLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_file: str = None,
        bearer_token_secret: BearerTokenSecret = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        metric_relabelings: List[MetricRelabeling] = None,
        params: Dict[str, List[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabelings: List[Relabeling] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        target_port: IntOrString = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_file=bearer_token_file,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            metric_relabelings=metric_relabelings,
            params=params,
            path=path,
            port=port,
            proxy_url=proxy_url,
            relabelings=relabelings,
            scheme=scheme,
            scrape_timeout=scrape_timeout,
            target_port=target_port,
            tls_config=tls_config,
        )


class NamespaceSelector(KubernetesObject):
    __slots__ = ()

    any: bool
    match_names: List[str]

    def __init__(self, any: bool = None, match_names: List[str] = None):
        super().__init__(any=any, match_names=match_names)


class MatchExpression(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: List[str]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


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


class Spec(KubernetesObject):
    __slots__ = ()

    _required_ = ["endpoints", "selector"]

    endpoints: List[Endpoint]
    job_label: str
    namespace_selector: NamespaceSelector
    pod_target_labels: List[str]
    sample_limit: int
    selector: Selector
    target_labels: List[str]
    target_limit: int

    def __init__(
        self,
        endpoints: List[Endpoint] = None,
        job_label: str = None,
        namespace_selector: NamespaceSelector = None,
        pod_target_labels: List[str] = None,
        sample_limit: int = None,
        selector: Selector = None,
        target_labels: List[str] = None,
        target_limit: int = None,
    ):
        super().__init__(
            endpoints=endpoints,
            job_label=job_label,
            namespace_selector=namespace_selector,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
            target_labels=target_labels,
            target_limit=target_limit,
        )


class ServiceMonitor(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: api.ObjectMeta
    spec: Spec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: api.ObjectMeta = None,
        spec: Spec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "ServiceMonitor",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


New = ServiceMonitor
