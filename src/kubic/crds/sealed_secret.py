from typing import Any, Dict

from .. import KubernetesObject, KubernetesApiResource
from .. import meta


class SealedSecret(KubernetesApiResource):
    __slots__ = ()

    _group_ = "bitnami.com"
    _version_ = "v1alpha1"

    metadata: meta.ObjectMeta
    spec: Dict[Any]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: Dict[Any] = None,
    ):
        super().__init__(
            "bitnami.com/v1alpha1",
            "SealedSecret",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


New = SealedSecret
