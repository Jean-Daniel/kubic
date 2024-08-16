from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class GroupVersionResource(KubernetesObject):
    """The names of the group, the version, and the resource."""

    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    group: str
    """ The name of the group. """
    resource: str
    """ The name of the resource. """
    version: str
    """ The name of the version. """

    def __init__(self, group: str = None, resource: str = None, version: str = None):
        super().__init__(group=group, resource=resource, version=version)


class MigrationCondition(KubernetesObject):
    """Describes the state of a migration at a certain point."""

    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    _required_ = ["status", "type"]

    last_update_time: meta.Time
    """ The last time this condition was updated. """
    message: str
    """ A human readable message indicating details about the transition. """
    reason: str
    """ The reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of the condition. """

    def __init__(self, last_update_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None):
        super().__init__(last_update_time=last_update_time, message=message, reason=reason, status=status, type=type)


class StorageVersionMigrationSpec(KubernetesObject):
    """Spec of the storage version migration."""

    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    _required_ = ["resource"]

    continue_token: str
    """ The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration. """
    resource: GroupVersionResource
    """ The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable. """

    def __init__(self, continue_token: str = None, resource: GroupVersionResource = None):
        super().__init__(continue_token=continue_token, resource=resource)


class StorageVersionMigration(KubernetesApiResource):
    """StorageVersionMigration represents a migration of stored data to the latest storage version."""

    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"
    _api_group_ = "storagemigration.k8s.io"
    _kind_ = "StorageVersionMigration"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: StorageVersionMigrationSpec
    """ Specification of the migration. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: StorageVersionMigrationSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class StorageVersionMigrationStatus(KubernetesObject):
    """Status of the storage version migration."""

    __slots__ = ()

    _api_version_ = "storagemigration.k8s.io/v1alpha1"

    conditions: list[MigrationCondition]
    """ The latest available observations of the migration's current state. """
    resource_version: str
    """ ResourceVersion to compare with the GC cache for performing the migration. This is the current resource version of given group, version and resource when kube-controller-manager first observes this StorageVersionMigration resource. """

    def __init__(self, conditions: list[MigrationCondition] = None, resource_version: str = None):
        super().__init__(conditions=conditions, resource_version=resource_version)
