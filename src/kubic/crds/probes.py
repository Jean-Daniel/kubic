from typing import Dict, List

from .. import api
from ..base import KubernetesObject, KubernetesApiResource


class Prober(KubernetesObject):
    __slots__ = ()

    path: str
    scheme: str
    url: str

    _required_ = ["url"]

    def __init__(self, path: str = None, scheme: str = None, url: str = None):
        super().__init__(path=path, scheme=scheme, url=url)


class NamespaceSelector(KubernetesObject):
    __slots__ = ()

    any: bool
    match_names: List[str]

    def __init__(self, any: bool = None, match_names: List[str] = None):
        super().__init__(any=any, match_names=match_names)


class RelabelingConfig(KubernetesObject):
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


class MatchExpression(KubernetesObject):
    __slots__ = ()

    key: str
    operator: str
    values: List[str]

    _required_ = ["key", "operator"]

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


class Ingress(KubernetesObject):
    __slots__ = ()

    namespace_selector: NamespaceSelector
    relabeling_configs: List[RelabelingConfig]
    selector: Selector

    def __init__(
        self,
        namespace_selector: NamespaceSelector = None,
        relabeling_configs: List[RelabelingConfig] = None,
        selector: Selector = None,
    ):
        super().__init__(
            namespace_selector=namespace_selector,
            relabeling_configs=relabeling_configs,
            selector=selector,
        )


class StaticConfig(KubernetesObject):
    __slots__ = ()

    labels: Dict[str, str]
    static: List[str]

    def __init__(self, labels: Dict[str, str] = None, static: List[str] = None):
        super().__init__(labels=labels, static=static)


class Target(KubernetesObject):
    __slots__ = ()

    ingress: Ingress
    static_config: StaticConfig

    def __init__(self, ingress: Ingress = None, static_config: StaticConfig = None):
        super().__init__(ingress=ingress, static_config=static_config)


class ProbeSpec(KubernetesObject):
    __slots__ = ()

    interval: str
    job_name: str
    module: str
    prober: Prober
    scrape_timeout: str
    targets: Target

    def __init__(
        self,
        interval: str = None,
        job_name: str = None,
        module: str = None,
        prober: Prober = None,
        scrape_timeout: str = None,
        targets: Target = None,
    ):
        super().__init__(
            interval=interval,
            job_name=job_name,
            module=module,
            prober=prober,
            scrape_timeout=scrape_timeout,
            targets=targets,
        )


class Probe(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"

    metadata: api.ObjectMeta
    spec: ProbeSpec

    _required_ = ["spec"]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: api.ObjectMeta = None,
        spec: ProbeSpec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "Probe",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )
