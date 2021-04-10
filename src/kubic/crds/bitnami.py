from typing import Any, Dict

from .. import KubernetesApiResource
from .. import meta


class SealedSecret(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "bitnami.com/v1alpha1"
    _kind_ = "SealedSecret"

    metadata: meta.ObjectMeta
    spec: Dict[str, Any]

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: Dict[str, Any] = None):
        super().__init__("bitnami.com/v1alpha1", "SealedSecret", name, namespace, metadata=metadata, spec=spec)
