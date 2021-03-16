from typing import Dict, List, Union

from .. import api
from ..base import KubernetesObject, KubernetesApiResource

IntOrString = Union[int, str]


class Rule(KubernetesObject):
    __slots__ = ()
    _revfield_names_ = {
        "for": "for_",
    }

    alert: str
    annotations: Dict[str, str]
    expr: IntOrString
    for_: str
    labels: Dict[str, str]
    record: str

    _required_ = ["expr"]

    def __init__(
        self,
        alert: str = None,
        annotations: Dict[str, str] = None,
        expr: IntOrString = None,
        for_: str = None,
        labels: Dict[str, str] = None,
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
    _field_names_ = {
        "partial_response_strategy": "partial_response_strategy",
    }

    interval: str
    name: str
    partial_response_strategy: str
    rules: List[Rule]

    _required_ = ["name", "rules"]

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


class PrometheusRuleSpec(KubernetesObject):
    __slots__ = ()

    groups: List[Group]

    def __init__(self, groups: List[Group] = None):
        super().__init__(groups=groups)


class PrometheusRule(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"

    metadata: api.ObjectMeta
    spec: PrometheusRuleSpec

    _required_ = ["spec"]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: api.ObjectMeta = None,
        spec: PrometheusRuleSpec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "PrometheusRule",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )
