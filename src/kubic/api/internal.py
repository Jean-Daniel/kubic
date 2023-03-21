import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from . import meta



class ServerStorageVersion(KubernetesObject):
    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"

    _field_names_ = {
        "api_server_id": "apiServerID",
    }
    _revfield_names_ = {
        "apiServerID": "api_server_id",
    }

    api_server_id: str
    decodable_versions: list[str]
    encoding_version: str

    def __init__(self, api_server_id: str = None, decodable_versions: list[str] = None, encoding_version: str = None):
        super().__init__(api_server_id=api_server_id, decodable_versions=decodable_versions, encoding_version=encoding_version)


StorageVersionSpec: t.TypeAlias = dict[str, t.Any]


class StorageVersion(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"
    _api_group_ = "internal.apiserver.k8s.io"
    _kind_ = "StorageVersion"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: StorageVersionSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StorageVersionSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class StorageVersionCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"

    _required_ = ["reason", "status", "type"]

    last_transition_time: meta.Time
    message: str
    observed_generation: int
    reason: str
    status: str
    type: str

    def __init__(self, last_transition_time: meta.Time = None, message: str = None, observed_generation: int = None, reason: str = None, status: str = None, type: str = None):
        super().__init__(last_transition_time=last_transition_time, message=message, observed_generation=observed_generation, reason=reason, status=status, type=type)


class StorageVersionList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"
    _api_group_ = "internal.apiserver.k8s.io"
    _kind_ = "StorageVersionList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[StorageVersion]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[StorageVersion] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class StorageVersionStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"

    common_encoding_version: str
    conditions: list[StorageVersionCondition]
    storage_versions: list[ServerStorageVersion]

    def __init__(self, common_encoding_version: str = None, conditions: list[StorageVersionCondition] = None, storage_versions: list[ServerStorageVersion] = None):
        super().__init__(common_encoding_version=common_encoding_version, conditions=conditions, storage_versions=storage_versions)


