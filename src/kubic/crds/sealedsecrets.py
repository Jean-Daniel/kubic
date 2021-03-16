from typing import Any, Dict

from .. import api
from ..base import KubernetesApiResource


class SealedSecret(KubernetesApiResource):
    __slots__ = ()

    _group_ = "bitnami.com"

    metadata: api.ObjectMeta
    spec: Dict[str, Any]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: api.ObjectMeta = None,
        spec: Dict[str, Any] = None,
    ):
        super().__init__(
            "bitnami.com/v1alpha1",
            "SealedSecret",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )
