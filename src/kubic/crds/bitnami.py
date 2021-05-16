from typing import Dict

from .. import KubernetesApiResource, KubernetesObject
from .. import core, meta


class Template(KubernetesObject):
    __slots__ = ()

    data: Dict[str, str]
    metadata: meta.ObjectMeta
    type: str

    def __init__(self, data: Dict[str, str] = None, metadata: meta.ObjectMeta = None, type: str = None):
        super().__init__(data=data, metadata=metadata, type=type)


class SealedSecretSpec(KubernetesObject):
    __slots__ = ()

    encrypted_data: Dict[str, core.Base64]
    template: Template

    def __init__(self, encrypted_data: Dict[str, core.Base64] = None, template: Template = None):
        super().__init__(encrypted_data=encrypted_data, template=template)


class SealedSecret(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "bitnami.com/v1alpha1"
    _kind_ = "SealedSecret"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: SealedSecretSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: SealedSecretSpec = None):
        super().__init__("bitnami.com/v1alpha1", "SealedSecret", name, namespace, metadata=metadata, spec=spec)
