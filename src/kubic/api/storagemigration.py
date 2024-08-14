from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class GroupVersionResource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    group: str
    resource: str
    version: str

    def __init__(self, group: str = None, resource: str = None, version: str = None):
        super().__init__(group=group, resource=resource, version=version)


class MigrationCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    _required_ = ["status", "type"]

    last_update_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(self, last_update_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None):
        super().__init__(last_update_time=last_update_time, message=message, reason=reason, status=status, type=type)


class StorageVersionMigrationSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    _required_ = ["resource"]

    continue_token: str
    resource: GroupVersionResource

    def __init__(self, continue_token: str = None, resource: GroupVersionResource = None):
        super().__init__(continue_token=continue_token, resource=resource)


class StorageVersionMigration(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"
    _api_group_ = "storagemigration.k8s.io"
    _kind_ = "StorageVersionMigration"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: StorageVersionMigrationSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StorageVersionMigrationSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class StorageVersionMigrationStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    conditions: list[MigrationCondition]
    resource_version: str

    def __init__(self, conditions: list[MigrationCondition] = None, resource_version: str = None):
        super().__init__(conditions=conditions, resource_version=resource_version)
