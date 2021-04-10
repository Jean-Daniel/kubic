from typing import Dict, List

from . import KubernetesObject


class LabelSelectorRequirement(KubernetesObject):
    __slots__ = ()

    _group_ = "meta"
    _version_ = "v1"

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: List[str]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class LabelSelector(KubernetesObject):
    __slots__ = ()

    _group_ = "meta"
    _version_ = "v1"

    match_expressions: List[LabelSelectorRequirement]
    match_labels: Dict[str, str]

    def __init__(self, match_expressions: List[LabelSelectorRequirement] = None, match_labels: Dict[str, str] = None):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


Time = str


class OwnerReference(KubernetesObject):
    __slots__ = ()

    _group_ = "meta"
    _version_ = "v1"

    _required_ = ["api_version", "kind", "name", "uid"]

    api_version: str
    block_owner_deletion: bool
    controller: bool
    kind: str
    name: str
    uid: str

    def __init__(
        self,
        api_version: str = None,
        block_owner_deletion: bool = None,
        controller: bool = None,
        kind: str = None,
        name: str = None,
        uid: str = None,
    ):
        super().__init__(
            api_version=api_version, block_owner_deletion=block_owner_deletion, controller=controller, kind=kind, name=name, uid=uid
        )


class ObjectMeta(KubernetesObject):
    __slots__ = ()

    _group_ = "meta"
    _version_ = "v1"

    annotations: Dict[str, str]
    cluster_name: str
    creation_timestamp: Time
    deletion_grace_period_seconds: int
    deletion_timestamp: Time
    finalizers: List[str]
    generate_name: str
    generation: int
    labels: Dict[str, str]
    name: str
    namespace: str
    owner_references: List[OwnerReference]
    resource_version: str
    self_link: str
    uid: str

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        cluster_name: str = None,
        creation_timestamp: Time = None,
        deletion_grace_period_seconds: int = None,
        deletion_timestamp: Time = None,
        finalizers: List[str] = None,
        generate_name: str = None,
        generation: int = None,
        labels: Dict[str, str] = None,
        name: str = None,
        namespace: str = None,
        owner_references: List[OwnerReference] = None,
        resource_version: str = None,
        self_link: str = None,
        uid: str = None,
    ):
        super().__init__(
            annotations=annotations,
            cluster_name=cluster_name,
            creation_timestamp=creation_timestamp,
            deletion_grace_period_seconds=deletion_grace_period_seconds,
            deletion_timestamp=deletion_timestamp,
            finalizers=finalizers,
            generate_name=generate_name,
            generation=generation,
            labels=labels,
            name=name,
            namespace=namespace,
            owner_references=owner_references,
            resource_version=resource_version,
            self_link=self_link,
            uid=uid,
        )
