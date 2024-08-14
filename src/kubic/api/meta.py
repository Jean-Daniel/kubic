import typing as t

from kubic import KubernetesApiResource, KubernetesObject


class GroupVersionForDiscovery(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _required_ = ["group_version", "version"]

    group_version: str
    version: str

    def __init__(self, group_version: str = None, version: str = None):
        super().__init__(group_version=group_version, version=version)


class ServerAddressByClientCIDR(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _required_ = ["client_cidr", "server_address"]

    _field_names_ = {
        "client_cidr": "clientCIDR",
    }
    _revfield_names_ = {
        "clientCIDR": "client_cidr",
    }

    client_cidr: str
    server_address: str

    def __init__(self, client_cidr: str = None, server_address: str = None):
        super().__init__(client_cidr=client_cidr, server_address=server_address)


class APIGroup(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "APIGroup"
    _scope_ = "namespace"

    _required_ = ["group_name", "versions"]

    _field_names_ = {
        "group_name": "name",
        "server_address_by_client_cidrs": "serverAddressByClientCIDRs",
    }
    _revfield_names_ = {
        "name": "group_name",
        "serverAddressByClientCIDRs": "server_address_by_client_cidrs",
    }

    group_name: str
    preferred_version: GroupVersionForDiscovery
    server_address_by_client_cidrs: list[ServerAddressByClientCIDR]
    versions: list[GroupVersionForDiscovery]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        group_name: str = None,
        preferred_version: GroupVersionForDiscovery = None,
        server_address_by_client_cidrs: list[ServerAddressByClientCIDR] = None,
        versions: list[GroupVersionForDiscovery] = None,
    ):
        super().__init__(
            name,
            namespace,
            group_name=group_name,
            preferred_version=preferred_version,
            server_address_by_client_cidrs=server_address_by_client_cidrs,
            versions=versions,
        )


class APIGroupList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "APIGroupList"
    _scope_ = "namespace"

    _required_ = ["groups"]

    groups: list[APIGroup]

    def __init__(self, name: str, namespace: str = None, groups: list[APIGroup] = None):
        super().__init__(name, namespace, groups=groups)


class APIResource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _required_ = ["kind", "name", "namespaced", "singular_name", "verbs"]

    categories: list[str]
    group: str
    kind: str
    name: str
    namespaced: bool
    short_names: list[str]
    singular_name: str
    storage_version_hash: str
    verbs: list[str]
    version: str

    def __init__(
        self,
        categories: list[str] = None,
        group: str = None,
        kind: str = None,
        name: str = None,
        namespaced: bool = None,
        short_names: list[str] = None,
        singular_name: str = None,
        storage_version_hash: str = None,
        verbs: list[str] = None,
        version: str = None,
    ):
        super().__init__(
            categories=categories,
            group=group,
            kind=kind,
            name=name,
            namespaced=namespaced,
            short_names=short_names,
            singular_name=singular_name,
            storage_version_hash=storage_version_hash,
            verbs=verbs,
            version=version,
        )


class APIResourceList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "APIResourceList"
    _scope_ = "namespace"

    _required_ = ["group_version", "resources"]

    group_version: str
    resources: list[APIResource]

    def __init__(self, name: str, namespace: str = None, group_version: str = None, resources: list[APIResource] = None):
        super().__init__(name, namespace, group_version=group_version, resources=resources)


class APIVersions(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "APIVersions"
    _scope_ = "namespace"

    _required_ = ["server_address_by_client_cidrs", "versions"]

    _field_names_ = {
        "server_address_by_client_cidrs": "serverAddressByClientCIDRs",
    }
    _revfield_names_ = {
        "serverAddressByClientCIDRs": "server_address_by_client_cidrs",
    }

    server_address_by_client_cidrs: list[ServerAddressByClientCIDR]
    versions: list[str]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        server_address_by_client_cidrs: list[ServerAddressByClientCIDR] = None,
        versions: list[str] = None,
    ):
        super().__init__(name, namespace, server_address_by_client_cidrs=server_address_by_client_cidrs, versions=versions)


Time: t.TypeAlias = str


class Condition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _required_ = ["last_transition_time", "message", "reason", "status", "type"]

    last_transition_time: Time
    message: str
    observed_generation: int
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_transition_time: Time = None,
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


class Preconditions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    resource_version: str
    uid: str

    def __init__(self, resource_version: str = None, uid: str = None):
        super().__init__(resource_version=resource_version, uid=uid)


class DeleteOptions(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "DeleteOptions"
    _scope_ = "namespace"

    dry_run: list[str]
    grace_period_seconds: int
    orphan_dependents: bool
    preconditions: Preconditions
    propagation_policy: str

    def __init__(
        self,
        name: str,
        namespace: str = None,
        dry_run: list[str] = None,
        grace_period_seconds: int = None,
        orphan_dependents: bool = None,
        preconditions: Preconditions = None,
        propagation_policy: str = None,
    ):
        super().__init__(
            name,
            namespace,
            dry_run=dry_run,
            grace_period_seconds=grace_period_seconds,
            orphan_dependents=orphan_dependents,
            preconditions=preconditions,
            propagation_policy=propagation_policy,
        )


class FieldSelectorRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: list[str]

    def __init__(self, key: str = None, operator: str = None, values: list[str] = None):
        super().__init__(key=key, operator=operator, values=values)


FieldsV1: t.TypeAlias = dict[str, t.Any]


class LabelSelectorRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: list[str]

    def __init__(self, key: str = None, operator: str = None, values: list[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class LabelSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    match_expressions: list[LabelSelectorRequirement]
    match_labels: dict[str, str]

    def __init__(self, match_expressions: list[LabelSelectorRequirement] = None, match_labels: dict[str, str] = None):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class ListMeta(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    _revfield_names_ = {
        "continue": "continue_",
    }

    continue_: str
    remaining_item_count: int
    resource_version: str
    self_link: str

    def __init__(self, continue_: str = None, remaining_item_count: int = None, resource_version: str = None, self_link: str = None):
        super().__init__(
            continue_=continue_, remaining_item_count=remaining_item_count, resource_version=resource_version, self_link=self_link
        )


class ManagedFieldsEntry(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    api_version: str
    fields_type: str
    fields_v1: FieldsV1
    manager: str
    operation: str
    subresource: str
    time: Time

    def __init__(
        self,
        api_version: str = None,
        fields_type: str = None,
        fields_v1: FieldsV1 = None,
        manager: str = None,
        operation: str = None,
        subresource: str = None,
        time: Time = None,
    ):
        super().__init__(
            api_version=api_version,
            fields_type=fields_type,
            fields_v1=fields_v1,
            manager=manager,
            operation=operation,
            subresource=subresource,
            time=time,
        )


MicroTime: t.TypeAlias = Time


class OwnerReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

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

    _api_version_ = "meta/v1"

    annotations: dict[str, str]
    creation_timestamp: Time
    deletion_grace_period_seconds: int
    deletion_timestamp: Time
    finalizers: list[str]
    generate_name: str
    generation: int
    labels: dict[str, str]
    name: str
    namespace: str
    owner_references: list[OwnerReference]
    resource_version: str
    self_link: str
    uid: str

    def __init__(
        self,
        annotations: dict[str, str] = None,
        creation_timestamp: Time = None,
        deletion_grace_period_seconds: int = None,
        deletion_timestamp: Time = None,
        finalizers: list[str] = None,
        generate_name: str = None,
        generation: int = None,
        labels: dict[str, str] = None,
        name: str = None,
        namespace: str = None,
        owner_references: list[OwnerReference] = None,
        resource_version: str = None,
        self_link: str = None,
        uid: str = None,
    ):
        super().__init__(
            annotations=annotations,
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


Patch: t.TypeAlias = dict[str, t.Any]


class StatusCause(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    field: str
    message: str
    reason: str

    def __init__(self, field: str = None, message: str = None, reason: str = None):
        super().__init__(field=field, message=message, reason=reason)


class StatusDetails(KubernetesObject):
    __slots__ = ()

    _api_version_ = "meta/v1"

    causes: list[StatusCause]
    group: str
    kind: str
    name: str
    retry_after_seconds: int
    uid: str

    def __init__(
        self,
        causes: list[StatusCause] = None,
        group: str = None,
        kind: str = None,
        name: str = None,
        retry_after_seconds: int = None,
        uid: str = None,
    ):
        super().__init__(causes=causes, group=group, kind=kind, name=name, retry_after_seconds=retry_after_seconds, uid=uid)


class Status(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "Status"
    _scope_ = "namespace"

    code: int
    details: StatusDetails
    message: str
    metadata: ListMeta
    reason: str

    def __init__(
        self,
        name: str,
        namespace: str = None,
        code: int = None,
        details: StatusDetails = None,
        message: str = None,
        metadata: ListMeta = None,
        reason: str = None,
    ):
        super().__init__(name, namespace, code=code, details=details, message=message, metadata=metadata, reason=reason)


class WatchEvent(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "meta/v1"
    _api_group_ = "meta"
    _kind_ = "WatchEvent"
    _scope_ = "namespace"

    _required_ = ["object", "type"]

    object: dict[str, t.Any]
    type: str

    def __init__(self, name: str, namespace: str = None, object: dict[str, t.Any] = None, type: str = None):
        super().__init__(name, namespace, object=object, type=type)
