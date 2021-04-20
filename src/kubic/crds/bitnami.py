from typing import Dict

from .. import KubernetesApiResource, KubernetesObject
from .. import core, meta


class Metadata(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    labels: Dict[str, str]

    def __init__(self, annotations: Dict[str, str] = None, labels: Dict[str, str] = None):
        super().__init__(annotations=annotations, labels=labels)


class Template(KubernetesObject):
    __slots__ = ()

    metadata: Metadata
    type: str

    def __init__(self, metadata: Metadata = None, type: str = None):
        super().__init__(metadata=metadata, type=type)


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

    metadata: meta.ObjectMeta
    spec: SealedSecretSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: SealedSecretSpec = None):
        super().__init__("bitnami.com/v1alpha1", "SealedSecret", name, namespace, metadata=metadata, spec=spec)
