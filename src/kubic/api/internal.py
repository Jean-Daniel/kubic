import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class ServerStorageVersion(KubernetesObject):
    """An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend."""

    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"

    _field_names_ = {
        "api_server_id": "apiServerID",
    }
    _revfield_names_ = {
        "apiServerID": "api_server_id",
    }

    api_server_id: str
    """ The ID of the reporting API server. """
    decodable_versions: list[str]
    """ The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. """
    encoding_version: str
    """ The API server encodes the object to this version when persisting it in the backend (e.g., etcd). """
    served_versions: list[str]
    """ The API server can serve these versions. DecodableVersions must include all ServedVersions. """

    def __init__(
        self,
        api_server_id: str = None,
        decodable_versions: list[str] = None,
        encoding_version: str = None,
        served_versions: list[str] = None,
    ):
        super().__init__(
            api_server_id=api_server_id,
            decodable_versions=decodable_versions,
            encoding_version=encoding_version,
            served_versions=served_versions,
        )


StorageVersionSpec: t.TypeAlias = dict[str, t.Any]
""" StorageVersionSpec is an empty spec. """


class StorageVersion(KubernetesApiResource):
    """Storage version of a specific resource."""

    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"
    _api_group_ = "internal.apiserver.k8s.io"
    _kind_ = "StorageVersion"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ The name is <group>.<resource>. """
    spec: StorageVersionSpec
    """ Spec is an empty spec. It is here to comply with Kubernetes API style. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StorageVersionSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class StorageVersionCondition(KubernetesObject):
    """Describes the state of the storageVersion at a certain point."""

    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"

    _required_ = ["message", "reason", "status", "type"]

    last_transition_time: meta.Time
    """ Last time the condition transitioned from one status to another. """
    message: str
    """ A human readable message indicating details about the transition. """
    observed_generation: int
    """ If set, this represents the .metadata.generation that the condition was set based upon. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of the condition. """

    def __init__(
        self,
        last_transition_time: meta.Time = None,
        message: str = None,
        observed_generation: int = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_transition_time=last_transition_time,
            message=message,
            observed_generation=observed_generation,
            reason=reason,
            status=status,
            type=type,
        )


class StorageVersionStatus(KubernetesObject):
    """API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend."""

    __slots__ = ()

    _api_version_ = "internal.apiserver.k8s.io/v1alpha1"

    common_encoding_version: str
    """ If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. """
    conditions: list[StorageVersionCondition]
    """ The latest available observations of the storageVersion's state. """
    storage_versions: list[ServerStorageVersion]
    """ The reported versions per API server instance. """

    def __init__(
        self,
        common_encoding_version: str = None,
        conditions: list[StorageVersionCondition] = None,
        storage_versions: list[ServerStorageVersion] = None,
    ):
        super().__init__(common_encoding_version=common_encoding_version, conditions=conditions, storage_versions=storage_versions)
