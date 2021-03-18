from typing import Dict, List

from .. import KubernetesObject, KubernetesApiResource
from .. import core, meta


class Rule(KubernetesObject):
    __slots__ = ()

    _required_ = ["expr"]

    _revfield_names_ = {
        "for": "for_",
    }

    alert: str
    annotations: Dict[str]
    expr: core.IntOrString
    for_: str
    labels: Dict[str]
    record: str

    def __init__(
        self,
        alert: str = None,
        annotations: Dict[str] = None,
        expr: core.IntOrString = None,
        for_: str = None,
        labels: Dict[str] = None,
        record: str = None,
    ):
        super().__init__(
            alert=alert,
            annotations=annotations,
            expr=expr,
            for_=for_,
            labels=labels,
            record=record,
        )


class Group(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "rules"]

    _field_names_ = {
        "partial_response_strategy": "partial_response_strategy",
    }

    interval: str
    name: str
    partial_response_strategy: str
    rules: List[Rule]

    def __init__(
        self,
        interval: str = None,
        name: str = None,
        partial_response_strategy: str = None,
        rules: List[Rule] = None,
    ):
        super().__init__(
            interval=interval,
            name=name,
            partial_response_strategy=partial_response_strategy,
            rules=rules,
        )


class Spec(KubernetesObject):
    __slots__ = ()

    groups: List[Group]

    def __init__(self, groups: List[Group] = None):
        super().__init__(groups=groups)


class PrometheusRule(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: Spec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: Spec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "PrometheusRule",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


New = PrometheusRule
