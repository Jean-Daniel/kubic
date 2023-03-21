import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from . import meta


class AWSElasticBlockStoreVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    partition: int
    read_only: bool
    volume_id: str

    def __init__(self, fs_type: str = None, partition: int = None, read_only: bool = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, partition=partition, read_only=read_only, volume_id=volume_id)


class NodeSelectorRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: list[str]

    def __init__(self, key: str = None, operator: str = None, values: list[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class NodeSelectorTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    match_expressions: list[NodeSelectorRequirement]
    match_fields: list[NodeSelectorRequirement]

    def __init__(self, match_expressions: list[NodeSelectorRequirement] = None, match_fields: list[NodeSelectorRequirement] = None):
        super().__init__(match_expressions=match_expressions, match_fields=match_fields)


class PreferredSchedulingTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["preference", "weight"]

    preference: NodeSelectorTerm
    weight: int

    def __init__(self, preference: NodeSelectorTerm = None, weight: int = None):
        super().__init__(preference=preference, weight=weight)


class NodeSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["node_selector_terms"]

    node_selector_terms: list[NodeSelectorTerm]

    def __init__(self, node_selector_terms: list[NodeSelectorTerm] = None):
        super().__init__(node_selector_terms=node_selector_terms)


class NodeAffinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: list[PreferredSchedulingTerm]
    required_during_scheduling_ignored_during_execution: NodeSelector

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: list[PreferredSchedulingTerm] = None,
        required_during_scheduling_ignored_during_execution: NodeSelector = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAffinityTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["topology_key"]

    label_selector: meta.LabelSelector
    namespace_selector: meta.LabelSelector
    namespaces: list[str]
    topology_key: str

    def __init__(
        self,
        label_selector: meta.LabelSelector = None,
        namespace_selector: meta.LabelSelector = None,
        namespaces: list[str] = None,
        topology_key: str = None,
    ):
        super().__init__(
            label_selector=label_selector, namespace_selector=namespace_selector, namespaces=namespaces, topology_key=topology_key
        )


class WeightedPodAffinityTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["pod_affinity_term", "weight"]

    pod_affinity_term: PodAffinityTerm
    weight: int

    def __init__(self, pod_affinity_term: PodAffinityTerm = None, weight: int = None):
        super().__init__(pod_affinity_term=pod_affinity_term, weight=weight)


class PodAffinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm]
    required_during_scheduling_ignored_during_execution: list[PodAffinityTerm]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm] = None,
        required_during_scheduling_ignored_during_execution: list[PodAffinityTerm] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAntiAffinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm]
    required_during_scheduling_ignored_during_execution: list[PodAffinityTerm]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: list[WeightedPodAffinityTerm] = None,
        required_during_scheduling_ignored_during_execution: list[PodAffinityTerm] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class Affinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    node_affinity: NodeAffinity
    pod_affinity: PodAffinity
    pod_anti_affinity: PodAntiAffinity

    def __init__(self, node_affinity: NodeAffinity = None, pod_affinity: PodAffinity = None, pod_anti_affinity: PodAntiAffinity = None):
        super().__init__(node_affinity=node_affinity, pod_affinity=pod_affinity, pod_anti_affinity=pod_anti_affinity)


class AttachedVolume(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["device_path", "name"]

    device_path: str
    name: str

    def __init__(self, device_path: str = None, name: str = None):
        super().__init__(device_path=device_path, name=name)


class AzureDiskVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["disk_name", "disk_uri"]

    _field_names_ = {
        "disk_uri": "diskURI",
    }
    _revfield_names_ = {
        "diskURI": "disk_uri",
    }

    caching_mode: str
    disk_name: str
    disk_uri: str
    fs_type: str
    kind: str
    read_only: bool

    def __init__(
        self,
        caching_mode: str = None,
        disk_name: str = None,
        disk_uri: str = None,
        fs_type: str = None,
        kind: str = None,
        read_only: bool = None,
    ):
        super().__init__(caching_mode=caching_mode, disk_name=disk_name, disk_uri=disk_uri, fs_type=fs_type, kind=kind, read_only=read_only)


class AzureFilePersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["secret_name", "share_name"]

    read_only: bool
    secret_name: str
    secret_namespace: str
    share_name: str

    def __init__(self, read_only: bool = None, secret_name: str = None, secret_namespace: str = None, share_name: str = None):
        super().__init__(read_only=read_only, secret_name=secret_name, secret_namespace=secret_namespace, share_name=share_name)


class AzureFileVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["secret_name", "share_name"]

    read_only: bool
    secret_name: str
    share_name: str

    def __init__(self, read_only: bool = None, secret_name: str = None, share_name: str = None):
        super().__init__(read_only=read_only, secret_name=secret_name, share_name=share_name)


Base64: t.TypeAlias = str


class ObjectReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    api_version: str
    field_path: str
    kind: str
    name: str
    namespace: str
    resource_version: str
    uid: str

    def __init__(
        self,
        api_version: str = None,
        field_path: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        resource_version: str = None,
        uid: str = None,
    ):
        super().__init__(
            api_version=api_version,
            field_path=field_path,
            kind=kind,
            name=name,
            namespace=namespace,
            resource_version=resource_version,
            uid=uid,
        )


class Binding(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Binding"
    _scope_ = "namespace"

    _required_ = ["target"]

    metadata: meta.ObjectMeta
    target: ObjectReference

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, target: ObjectReference = None):
        super().__init__(name, namespace, metadata=metadata, target=target)


class SecretReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    name: str
    namespace: str

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class CSIPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver", "volume_handle"]

    controller_expand_secret_ref: SecretReference
    controller_publish_secret_ref: SecretReference
    driver: str
    fs_type: str
    node_expand_secret_ref: SecretReference
    node_publish_secret_ref: SecretReference
    node_stage_secret_ref: SecretReference
    read_only: bool
    volume_attributes: dict[str, str]
    volume_handle: str

    def __init__(
        self,
        controller_expand_secret_ref: SecretReference = None,
        controller_publish_secret_ref: SecretReference = None,
        driver: str = None,
        fs_type: str = None,
        node_expand_secret_ref: SecretReference = None,
        node_publish_secret_ref: SecretReference = None,
        node_stage_secret_ref: SecretReference = None,
        read_only: bool = None,
        volume_attributes: dict[str, str] = None,
        volume_handle: str = None,
    ):
        super().__init__(
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            driver=driver,
            fs_type=fs_type,
            node_expand_secret_ref=node_expand_secret_ref,
            node_publish_secret_ref=node_publish_secret_ref,
            node_stage_secret_ref=node_stage_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
            volume_handle=volume_handle,
        )


class LocalObjectReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class CSIVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    fs_type: str
    node_publish_secret_ref: LocalObjectReference
    read_only: bool
    volume_attributes: dict[str, str]

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        node_publish_secret_ref: LocalObjectReference = None,
        read_only: bool = None,
        volume_attributes: dict[str, str] = None,
    ):
        super().__init__(
            driver=driver,
            fs_type=fs_type,
            node_publish_secret_ref=node_publish_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
        )


class Capabilities(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    add: list[str]
    drop: list[str]

    def __init__(self, add: list[str] = None, drop: list[str] = None):
        super().__init__(add=add, drop=drop)


class CephFSPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["monitors"]

    monitors: list[str]
    path: str
    read_only: bool
    secret_file: str
    secret_ref: SecretReference
    user: str

    def __init__(
        self,
        monitors: list[str] = None,
        path: str = None,
        read_only: bool = None,
        secret_file: str = None,
        secret_ref: SecretReference = None,
        user: str = None,
    ):
        super().__init__(monitors=monitors, path=path, read_only=read_only, secret_file=secret_file, secret_ref=secret_ref, user=user)


class CephFSVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["monitors"]

    monitors: list[str]
    path: str
    read_only: bool
    secret_file: str
    secret_ref: LocalObjectReference
    user: str

    def __init__(
        self,
        monitors: list[str] = None,
        path: str = None,
        read_only: bool = None,
        secret_file: str = None,
        secret_ref: LocalObjectReference = None,
        user: str = None,
    ):
        super().__init__(monitors=monitors, path=path, read_only=read_only, secret_file=secret_file, secret_ref=secret_ref, user=user)


class CinderPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    read_only: bool
    secret_ref: SecretReference
    volume_id: str

    def __init__(self, fs_type: str = None, read_only: bool = None, secret_ref: SecretReference = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_id=volume_id)


class CinderVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    read_only: bool
    secret_ref: LocalObjectReference
    volume_id: str

    def __init__(self, fs_type: str = None, read_only: bool = None, secret_ref: LocalObjectReference = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_id=volume_id)


class ClientIPConfig(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    timeout_seconds: int

    def __init__(self, timeout_seconds: int = None):
        super().__init__(timeout_seconds=timeout_seconds)


class ComponentCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    error: str
    message: str
    status: str
    type: str

    def __init__(self, error: str = None, message: str = None, status: str = None, type: str = None):
        super().__init__(error=error, message=message, status=status, type=type)


class ComponentStatus(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ComponentStatus"
    _scope_ = "cluster"

    conditions: list[ComponentCondition]
    metadata: meta.ObjectMeta

    def __init__(self, name: str, conditions: list[ComponentCondition] = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, "", conditions=conditions, metadata=metadata)


class ComponentStatusList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ComponentStatusList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ComponentStatus]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ComponentStatus] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ConfigMap(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ConfigMap"
    _scope_ = "namespace"

    binary_data: dict[str, Base64]
    data: dict[str, str]
    immutable: bool
    metadata: meta.ObjectMeta

    def __init__(
        self,
        name: str,
        namespace: str = None,
        binary_data: dict[str, Base64] = None,
        data: dict[str, str] = None,
        immutable: bool = None,
        metadata: meta.ObjectMeta = None,
    ):
        super().__init__(name, namespace, binary_data=binary_data, data=data, immutable=immutable, metadata=metadata)


class ConfigMapEnvSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    name: str
    optional: bool

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class ConfigMapKeySelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class ConfigMapList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ConfigMapList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ConfigMap]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ConfigMap] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ConfigMapNodeConfigSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["kubelet_config_key", "name", "namespace"]

    kubelet_config_key: str
    name: str
    namespace: str
    resource_version: str
    uid: str

    def __init__(
        self, kubelet_config_key: str = None, name: str = None, namespace: str = None, resource_version: str = None, uid: str = None
    ):
        super().__init__(kubelet_config_key=kubelet_config_key, name=name, namespace=namespace, resource_version=resource_version, uid=uid)


class KeyToPath(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "path"]

    key: str
    mode: int
    path: str

    def __init__(self, key: str = None, mode: int = None, path: str = None):
        super().__init__(key=key, mode=mode, path=path)


class ConfigMapProjection(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    items: list[KeyToPath]
    name: str
    optional: bool

    def __init__(self, items: list[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(items=items, name=name, optional=optional)


class ConfigMapVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    items: list[KeyToPath]
    name: str
    optional: bool

    def __init__(self, default_mode: int = None, items: list[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(default_mode=default_mode, items=items, name=name, optional=optional)


class ObjectFieldSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["field_path"]

    api_version: str
    field_path: str

    def __init__(self, api_version: str = None, field_path: str = None):
        super().__init__(api_version=api_version, field_path=field_path)


Quantity: t.TypeAlias = str | int | float


class ResourceFieldSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["resource"]

    container_name: str
    divisor: Quantity
    resource: str

    def __init__(self, container_name: str = None, divisor: Quantity = None, resource: str = None):
        super().__init__(container_name=container_name, divisor=divisor, resource=resource)


class SecretKeySelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class EnvVarSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    config_map_key_ref: ConfigMapKeySelector
    field_ref: ObjectFieldSelector
    resource_field_ref: ResourceFieldSelector
    secret_key_ref: SecretKeySelector

    def __init__(
        self,
        config_map_key_ref: ConfigMapKeySelector = None,
        field_ref: ObjectFieldSelector = None,
        resource_field_ref: ResourceFieldSelector = None,
        secret_key_ref: SecretKeySelector = None,
    ):
        super().__init__(
            config_map_key_ref=config_map_key_ref, field_ref=field_ref, resource_field_ref=resource_field_ref, secret_key_ref=secret_key_ref
        )


class EnvVar(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str
    value: str
    value_from: EnvVarSource

    def __init__(self, name: str = None, value: str = None, value_from: EnvVarSource = None):
        super().__init__(name=name, value=value, value_from=value_from)


class SecretEnvSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    name: str
    optional: bool

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class EnvFromSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    config_map_ref: ConfigMapEnvSource
    prefix: str
    secret_ref: SecretEnvSource

    def __init__(self, config_map_ref: ConfigMapEnvSource = None, prefix: str = None, secret_ref: SecretEnvSource = None):
        super().__init__(config_map_ref=config_map_ref, prefix=prefix, secret_ref=secret_ref)


class ExecAction(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    command: list[str]

    def __init__(self, command: list[str] = None):
        super().__init__(command=command)


class HTTPHeader(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name", "value"]

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


IntOrString: t.TypeAlias = int | str


class HTTPGetAction(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    host: str
    http_headers: list[HTTPHeader]
    path: str
    port: IntOrString
    scheme: str

    def __init__(
        self, host: str = None, http_headers: list[HTTPHeader] = None, path: str = None, port: IntOrString = None, scheme: str = None
    ):
        super().__init__(host=host, http_headers=http_headers, path=path, port=port, scheme=scheme)


class TCPSocketAction(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    host: str
    port: IntOrString

    def __init__(self, host: str = None, port: IntOrString = None):
        super().__init__(host=host, port=port)


class LifecycleHandler(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    exec: ExecAction
    http_get: HTTPGetAction
    tcp_socket: TCPSocketAction

    def __init__(self, exec: ExecAction = None, http_get: HTTPGetAction = None, tcp_socket: TCPSocketAction = None):
        super().__init__(exec=exec, http_get=http_get, tcp_socket=tcp_socket)


class Lifecycle(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    post_start: LifecycleHandler
    pre_stop: LifecycleHandler

    def __init__(self, post_start: LifecycleHandler = None, pre_stop: LifecycleHandler = None):
        super().__init__(post_start=post_start, pre_stop=pre_stop)


class GRPCAction(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    port: int
    service: str

    def __init__(self, port: int = None, service: str = None):
        super().__init__(port=port, service=service)


class Probe(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    exec: ExecAction
    failure_threshold: int
    grpc: GRPCAction
    http_get: HTTPGetAction
    initial_delay_seconds: int
    period_seconds: int
    success_threshold: int
    tcp_socket: TCPSocketAction
    termination_grace_period_seconds: int
    timeout_seconds: int

    def __init__(
        self,
        exec: ExecAction = None,
        failure_threshold: int = None,
        grpc: GRPCAction = None,
        http_get: HTTPGetAction = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: TCPSocketAction = None,
        termination_grace_period_seconds: int = None,
        timeout_seconds: int = None,
    ):
        super().__init__(
            exec=exec,
            failure_threshold=failure_threshold,
            grpc=grpc,
            http_get=http_get,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            tcp_socket=tcp_socket,
            termination_grace_period_seconds=termination_grace_period_seconds,
            timeout_seconds=timeout_seconds,
        )


class ContainerPort(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["container_port"]

    _field_names_ = {
        "host_ip": "hostIP",
    }
    _revfield_names_ = {
        "hostIP": "host_ip",
    }

    container_port: int
    host_ip: str
    host_port: int
    name: str
    protocol: str

    def __init__(self, container_port: int = None, host_ip: str = None, host_port: int = None, name: str = None, protocol: str = None):
        super().__init__(container_port=container_port, host_ip=host_ip, host_port=host_port, name=name, protocol=protocol)


class ResourceRequirements(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    limits: dict[str, Quantity]
    requests: dict[str, Quantity]

    def __init__(self, limits: dict[str, Quantity] = None, requests: dict[str, Quantity] = None):
        super().__init__(limits=limits, requests=requests)


class SELinuxOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    level: str
    role: str
    type: str
    user: str

    def __init__(self, level: str = None, role: str = None, type: str = None, user: str = None):
        super().__init__(level=level, role=role, type=type, user=user)


class SeccompProfile(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["type"]

    localhost_profile: str
    type: str

    def __init__(self, localhost_profile: str = None, type: str = None):
        super().__init__(localhost_profile=localhost_profile, type=type)


class WindowsSecurityContextOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    gmsa_credential_spec: str
    gmsa_credential_spec_name: str
    host_process: bool
    run_as_user_name: str

    def __init__(
        self,
        gmsa_credential_spec: str = None,
        gmsa_credential_spec_name: str = None,
        host_process: bool = None,
        run_as_user_name: str = None,
    ):
        super().__init__(
            gmsa_credential_spec=gmsa_credential_spec,
            gmsa_credential_spec_name=gmsa_credential_spec_name,
            host_process=host_process,
            run_as_user_name=run_as_user_name,
        )


class SecurityContext(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    allow_privilege_escalation: bool
    capabilities: Capabilities
    privileged: bool
    proc_mount: str
    read_only_root_filesystem: bool
    run_as_group: int
    run_as_non_root: bool
    run_as_user: int
    se_linux_options: SELinuxOptions
    seccomp_profile: SeccompProfile
    windows_options: WindowsSecurityContextOptions

    def __init__(
        self,
        allow_privilege_escalation: bool = None,
        capabilities: Capabilities = None,
        privileged: bool = None,
        proc_mount: str = None,
        read_only_root_filesystem: bool = None,
        run_as_group: int = None,
        run_as_non_root: bool = None,
        run_as_user: int = None,
        se_linux_options: SELinuxOptions = None,
        seccomp_profile: SeccompProfile = None,
        windows_options: WindowsSecurityContextOptions = None,
    ):
        super().__init__(
            allow_privilege_escalation=allow_privilege_escalation,
            capabilities=capabilities,
            privileged=privileged,
            proc_mount=proc_mount,
            read_only_root_filesystem=read_only_root_filesystem,
            run_as_group=run_as_group,
            run_as_non_root=run_as_non_root,
            run_as_user=run_as_user,
            se_linux_options=se_linux_options,
            seccomp_profile=seccomp_profile,
            windows_options=windows_options,
        )


class VolumeDevice(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["device_path", "name"]

    device_path: str
    name: str

    def __init__(self, device_path: str = None, name: str = None):
        super().__init__(device_path=device_path, name=name)


class VolumeMount(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["mount_path", "name"]

    mount_path: str
    mount_propagation: str
    name: str
    read_only: bool
    sub_path: str
    sub_path_expr: str

    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
        sub_path_expr: str = None,
    ):
        super().__init__(
            mount_path=mount_path,
            mount_propagation=mount_propagation,
            name=name,
            read_only=read_only,
            sub_path=sub_path,
            sub_path_expr=sub_path_expr,
        )


class Container(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    args: list[str]
    command: list[str]
    env: list[EnvVar]
    env_from: list[EnvFromSource]
    image: str
    image_pull_policy: str
    lifecycle: Lifecycle
    liveness_probe: Probe
    name: str
    ports: list[ContainerPort]
    readiness_probe: Probe
    resources: ResourceRequirements
    security_context: SecurityContext
    startup_probe: Probe
    stdin: bool
    stdin_once: bool
    termination_message_path: str
    termination_message_policy: str
    tty: bool
    volume_devices: list[VolumeDevice]
    volume_mounts: list[VolumeMount]
    working_dir: str

    def __init__(
        self,
        args: list[str] = None,
        command: list[str] = None,
        env: list[EnvVar] = None,
        env_from: list[EnvFromSource] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: Probe = None,
        name: str = None,
        ports: list[ContainerPort] = None,
        readiness_probe: Probe = None,
        resources: ResourceRequirements = None,
        security_context: SecurityContext = None,
        startup_probe: Probe = None,
        stdin: bool = None,
        stdin_once: bool = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        tty: bool = None,
        volume_devices: list[VolumeDevice] = None,
        volume_mounts: list[VolumeMount] = None,
        working_dir: str = None,
    ):
        super().__init__(
            args=args,
            command=command,
            env=env,
            env_from=env_from,
            image=image,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness_probe=liveness_probe,
            name=name,
            ports=ports,
            readiness_probe=readiness_probe,
            resources=resources,
            security_context=security_context,
            startup_probe=startup_probe,
            stdin=stdin,
            stdin_once=stdin_once,
            termination_message_path=termination_message_path,
            termination_message_policy=termination_message_policy,
            tty=tty,
            volume_devices=volume_devices,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )


class ContainerImage(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    names: list[str]
    size_bytes: int

    def __init__(self, names: list[str] = None, size_bytes: int = None):
        super().__init__(names=names, size_bytes=size_bytes)


class ContainerStateRunning(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    started_at: meta.Time

    def __init__(self, started_at: meta.Time = None):
        super().__init__(started_at=started_at)


class ContainerStateTerminated(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["exit_code"]

    _field_names_ = {
        "container_id": "containerID",
    }
    _revfield_names_ = {
        "containerID": "container_id",
    }

    container_id: str
    exit_code: int
    finished_at: meta.Time
    message: str
    reason: str
    signal: int
    started_at: meta.Time

    def __init__(
        self,
        container_id: str = None,
        exit_code: int = None,
        finished_at: meta.Time = None,
        message: str = None,
        reason: str = None,
        signal: int = None,
        started_at: meta.Time = None,
    ):
        super().__init__(
            container_id=container_id,
            exit_code=exit_code,
            finished_at=finished_at,
            message=message,
            reason=reason,
            signal=signal,
            started_at=started_at,
        )


class ContainerStateWaiting(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    message: str
    reason: str

    def __init__(self, message: str = None, reason: str = None):
        super().__init__(message=message, reason=reason)


class ContainerState(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    running: ContainerStateRunning
    terminated: ContainerStateTerminated
    waiting: ContainerStateWaiting

    def __init__(
        self, running: ContainerStateRunning = None, terminated: ContainerStateTerminated = None, waiting: ContainerStateWaiting = None
    ):
        super().__init__(running=running, terminated=terminated, waiting=waiting)


class ContainerStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "image_id", "name", "ready", "restart_count"]

    _field_names_ = {
        "container_id": "containerID",
        "image_id": "imageID",
    }
    _revfield_names_ = {
        "containerID": "container_id",
        "imageID": "image_id",
    }

    container_id: str
    image: str
    image_id: str
    last_state: ContainerState
    name: str
    ready: bool
    restart_count: int
    started: bool
    state: ContainerState

    def __init__(
        self,
        container_id: str = None,
        image: str = None,
        image_id: str = None,
        last_state: ContainerState = None,
        name: str = None,
        ready: bool = None,
        restart_count: int = None,
        started: bool = None,
        state: ContainerState = None,
    ):
        super().__init__(
            container_id=container_id,
            image=image,
            image_id=image_id,
            last_state=last_state,
            name=name,
            ready=ready,
            restart_count=restart_count,
            started=started,
            state=state,
        )


class DaemonEndpoint(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    _field_names_ = {
        "port": "Port",
    }
    _revfield_names_ = {
        "Port": "port",
    }

    port: int

    def __init__(self, port: int = None):
        super().__init__(port=port)


class DownwardAPIVolumeFile(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    field_ref: ObjectFieldSelector
    mode: int
    path: str
    resource_field_ref: ResourceFieldSelector

    def __init__(
        self, field_ref: ObjectFieldSelector = None, mode: int = None, path: str = None, resource_field_ref: ResourceFieldSelector = None
    ):
        super().__init__(field_ref=field_ref, mode=mode, path=path, resource_field_ref=resource_field_ref)


class DownwardAPIProjection(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    items: list[DownwardAPIVolumeFile]

    def __init__(self, items: list[DownwardAPIVolumeFile] = None):
        super().__init__(items=items)


class DownwardAPIVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    items: list[DownwardAPIVolumeFile]

    def __init__(self, default_mode: int = None, items: list[DownwardAPIVolumeFile] = None):
        super().__init__(default_mode=default_mode, items=items)


class EmptyDirVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    medium: str
    size_limit: Quantity

    def __init__(self, medium: str = None, size_limit: Quantity = None):
        super().__init__(medium=medium, size_limit=size_limit)


class EndpointAddress(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["ip"]

    hostname: str
    ip: str
    node_name: str
    target_ref: ObjectReference

    def __init__(self, hostname: str = None, ip: str = None, node_name: str = None, target_ref: ObjectReference = None):
        super().__init__(hostname=hostname, ip=ip, node_name=node_name, target_ref=target_ref)


class EndpointPort(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    app_protocol: str
    name: str
    port: int
    protocol: str

    def __init__(self, app_protocol: str = None, name: str = None, port: int = None, protocol: str = None):
        super().__init__(app_protocol=app_protocol, name=name, port=port, protocol=protocol)


class EndpointSubset(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    addresses: list[EndpointAddress]
    not_ready_addresses: list[EndpointAddress]
    ports: list[EndpointPort]

    def __init__(
        self, addresses: list[EndpointAddress] = None, not_ready_addresses: list[EndpointAddress] = None, ports: list[EndpointPort] = None
    ):
        super().__init__(addresses=addresses, not_ready_addresses=not_ready_addresses, ports=ports)


class Endpoints(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Endpoints"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    subsets: list[EndpointSubset]

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, subsets: list[EndpointSubset] = None):
        super().__init__(name, namespace, metadata=metadata, subsets=subsets)


class EndpointsList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "EndpointsList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Endpoints]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Endpoints] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class EphemeralContainer(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    args: list[str]
    command: list[str]
    env: list[EnvVar]
    env_from: list[EnvFromSource]
    image: str
    image_pull_policy: str
    lifecycle: Lifecycle
    liveness_probe: Probe
    name: str
    ports: list[ContainerPort]
    readiness_probe: Probe
    resources: ResourceRequirements
    security_context: SecurityContext
    startup_probe: Probe
    stdin: bool
    stdin_once: bool
    target_container_name: str
    termination_message_path: str
    termination_message_policy: str
    tty: bool
    volume_devices: list[VolumeDevice]
    volume_mounts: list[VolumeMount]
    working_dir: str

    def __init__(
        self,
        args: list[str] = None,
        command: list[str] = None,
        env: list[EnvVar] = None,
        env_from: list[EnvFromSource] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: Probe = None,
        name: str = None,
        ports: list[ContainerPort] = None,
        readiness_probe: Probe = None,
        resources: ResourceRequirements = None,
        security_context: SecurityContext = None,
        startup_probe: Probe = None,
        stdin: bool = None,
        stdin_once: bool = None,
        target_container_name: str = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        tty: bool = None,
        volume_devices: list[VolumeDevice] = None,
        volume_mounts: list[VolumeMount] = None,
        working_dir: str = None,
    ):
        super().__init__(
            args=args,
            command=command,
            env=env,
            env_from=env_from,
            image=image,
            image_pull_policy=image_pull_policy,
            lifecycle=lifecycle,
            liveness_probe=liveness_probe,
            name=name,
            ports=ports,
            readiness_probe=readiness_probe,
            resources=resources,
            security_context=security_context,
            startup_probe=startup_probe,
            stdin=stdin,
            stdin_once=stdin_once,
            target_container_name=target_container_name,
            termination_message_path=termination_message_path,
            termination_message_policy=termination_message_policy,
            tty=tty,
            volume_devices=volume_devices,
            volume_mounts=volume_mounts,
            working_dir=working_dir,
        )


class TypedLocalObjectReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["kind", "name"]

    api_group: str
    kind: str
    name: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class PersistentVolumeClaimSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    access_modes: list[str]
    data_source: TypedLocalObjectReference
    data_source_ref: TypedLocalObjectReference
    resources: ResourceRequirements
    selector: meta.LabelSelector
    storage_class_name: str
    volume_mode: str
    volume_name: str

    def __init__(
        self,
        access_modes: list[str] = None,
        data_source: TypedLocalObjectReference = None,
        data_source_ref: TypedLocalObjectReference = None,
        resources: ResourceRequirements = None,
        selector: meta.LabelSelector = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            access_modes=access_modes,
            data_source=data_source,
            data_source_ref=data_source_ref,
            resources=resources,
            selector=selector,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            volume_name=volume_name,
        )


class PersistentVolumeClaimTemplate(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PersistentVolumeClaimSpec

    def __init__(self, metadata: meta.ObjectMeta = None, spec: PersistentVolumeClaimSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class EphemeralVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    volume_claim_template: PersistentVolumeClaimTemplate

    def __init__(self, volume_claim_template: PersistentVolumeClaimTemplate = None):
        super().__init__(volume_claim_template=volume_claim_template)


class EventSeries(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    count: int
    last_observed_time: meta.MicroTime

    def __init__(self, count: int = None, last_observed_time: meta.MicroTime = None):
        super().__init__(count=count, last_observed_time=last_observed_time)


class EventSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    component: str
    host: str

    def __init__(self, component: str = None, host: str = None):
        super().__init__(component=component, host=host)


class Event(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Event"
    _scope_ = "namespace"

    _required_ = ["involved_object", "metadata"]

    action: str
    count: int
    event_time: meta.MicroTime
    first_timestamp: meta.Time
    involved_object: ObjectReference
    last_timestamp: meta.Time
    message: str
    metadata: meta.ObjectMeta
    reason: str
    related: ObjectReference
    reporting_component: str
    reporting_instance: str
    series: EventSeries
    source: EventSource
    type: str

    def __init__(
        self,
        name: str,
        namespace: str = None,
        action: str = None,
        count: int = None,
        event_time: meta.MicroTime = None,
        first_timestamp: meta.Time = None,
        involved_object: ObjectReference = None,
        last_timestamp: meta.Time = None,
        message: str = None,
        metadata: meta.ObjectMeta = None,
        reason: str = None,
        related: ObjectReference = None,
        reporting_component: str = None,
        reporting_instance: str = None,
        series: EventSeries = None,
        source: EventSource = None,
        type: str = None,
    ):
        super().__init__(
            name,
            namespace,
            action=action,
            count=count,
            event_time=event_time,
            first_timestamp=first_timestamp,
            involved_object=involved_object,
            last_timestamp=last_timestamp,
            message=message,
            metadata=metadata,
            reason=reason,
            related=related,
            reporting_component=reporting_component,
            reporting_instance=reporting_instance,
            series=series,
            source=source,
            type=type,
        )


class EventList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "EventList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Event]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Event] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class FCVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "target_wwns": "targetWWNs",
    }
    _revfield_names_ = {
        "targetWWNs": "target_wwns",
    }

    fs_type: str
    lun: int
    read_only: bool
    target_wwns: list[str]
    wwids: list[str]

    def __init__(
        self, fs_type: str = None, lun: int = None, read_only: bool = None, target_wwns: list[str] = None, wwids: list[str] = None
    ):
        super().__init__(fs_type=fs_type, lun=lun, read_only=read_only, target_wwns=target_wwns, wwids=wwids)


class FlexPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    fs_type: str
    options: dict[str, str]
    read_only: bool
    secret_ref: SecretReference

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: dict[str, str] = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
    ):
        super().__init__(driver=driver, fs_type=fs_type, options=options, read_only=read_only, secret_ref=secret_ref)


class FlexVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    fs_type: str
    options: dict[str, str]
    read_only: bool
    secret_ref: LocalObjectReference

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: dict[str, str] = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
    ):
        super().__init__(driver=driver, fs_type=fs_type, options=options, read_only=read_only, secret_ref=secret_ref)


class FlockerVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "dataset_uuid": "datasetUUID",
    }
    _revfield_names_ = {
        "datasetUUID": "dataset_uuid",
    }

    dataset_name: str
    dataset_uuid: str

    def __init__(self, dataset_name: str = None, dataset_uuid: str = None):
        super().__init__(dataset_name=dataset_name, dataset_uuid=dataset_uuid)


class GCEPersistentDiskVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["pd_name"]

    fs_type: str
    partition: int
    pd_name: str
    read_only: bool

    def __init__(self, fs_type: str = None, partition: int = None, pd_name: str = None, read_only: bool = None):
        super().__init__(fs_type=fs_type, partition=partition, pd_name=pd_name, read_only=read_only)


class GitRepoVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["repository"]

    directory: str
    repository: str
    revision: str

    def __init__(self, directory: str = None, repository: str = None, revision: str = None):
        super().__init__(directory=directory, repository=repository, revision=revision)


class GlusterfsPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["endpoints", "path"]

    endpoints: str
    endpoints_namespace: str
    path: str
    read_only: bool

    def __init__(self, endpoints: str = None, endpoints_namespace: str = None, path: str = None, read_only: bool = None):
        super().__init__(endpoints=endpoints, endpoints_namespace=endpoints_namespace, path=path, read_only=read_only)


class GlusterfsVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["endpoints", "path"]

    endpoints: str
    path: str
    read_only: bool

    def __init__(self, endpoints: str = None, path: str = None, read_only: bool = None):
        super().__init__(endpoints=endpoints, path=path, read_only=read_only)


class HostAlias(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    hostnames: list[str]
    ip: str

    def __init__(self, hostnames: list[str] = None, ip: str = None):
        super().__init__(hostnames=hostnames, ip=ip)


class HostPathVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    path: str
    type: str

    def __init__(self, path: str = None, type: str = None):
        super().__init__(path=path, type=type)


IDNHostname: t.TypeAlias = str


class ISCSIPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["iqn", "lun", "target_portal"]

    chap_auth_discovery: bool
    chap_auth_session: bool
    fs_type: str
    initiator_name: str
    iqn: str
    iscsi_interface: str
    lun: int
    portals: list[str]
    read_only: bool
    secret_ref: SecretReference
    target_portal: str

    def __init__(
        self,
        chap_auth_discovery: bool = None,
        chap_auth_session: bool = None,
        fs_type: str = None,
        initiator_name: str = None,
        iqn: str = None,
        iscsi_interface: str = None,
        lun: int = None,
        portals: list[str] = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        target_portal: str = None,
    ):
        super().__init__(
            chap_auth_discovery=chap_auth_discovery,
            chap_auth_session=chap_auth_session,
            fs_type=fs_type,
            initiator_name=initiator_name,
            iqn=iqn,
            iscsi_interface=iscsi_interface,
            lun=lun,
            portals=portals,
            read_only=read_only,
            secret_ref=secret_ref,
            target_portal=target_portal,
        )


class ISCSIVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["iqn", "lun", "target_portal"]

    chap_auth_discovery: bool
    chap_auth_session: bool
    fs_type: str
    initiator_name: str
    iqn: str
    iscsi_interface: str
    lun: int
    portals: list[str]
    read_only: bool
    secret_ref: LocalObjectReference
    target_portal: str

    def __init__(
        self,
        chap_auth_discovery: bool = None,
        chap_auth_session: bool = None,
        fs_type: str = None,
        initiator_name: str = None,
        iqn: str = None,
        iscsi_interface: str = None,
        lun: int = None,
        portals: list[str] = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        target_portal: str = None,
    ):
        super().__init__(
            chap_auth_discovery=chap_auth_discovery,
            chap_auth_session=chap_auth_session,
            fs_type=fs_type,
            initiator_name=initiator_name,
            iqn=iqn,
            iscsi_interface=iscsi_interface,
            lun=lun,
            portals=portals,
            read_only=read_only,
            secret_ref=secret_ref,
            target_portal=target_portal,
        )


class Info(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["build_date", "compiler", "git_commit", "git_tree_state", "git_version", "go_version", "major", "minor", "platform"]

    build_date: str
    compiler: str
    git_commit: str
    git_tree_state: str
    git_version: str
    go_version: str
    major: str
    minor: str
    platform: str

    def __init__(
        self,
        build_date: str = None,
        compiler: str = None,
        git_commit: str = None,
        git_tree_state: str = None,
        git_version: str = None,
        go_version: str = None,
        major: str = None,
        minor: str = None,
        platform: str = None,
    ):
        super().__init__(
            build_date=build_date,
            compiler=compiler,
            git_commit=git_commit,
            git_tree_state=git_tree_state,
            git_version=git_version,
            go_version=go_version,
            major=major,
            minor=minor,
            platform=platform,
        )


class LimitRangeItem(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["type"]

    default: dict[str, Quantity]
    default_request: dict[str, Quantity]
    max: dict[str, Quantity]
    max_limit_request_ratio: dict[str, Quantity]
    min: dict[str, Quantity]
    type: str

    def __init__(
        self,
        default: dict[str, Quantity] = None,
        default_request: dict[str, Quantity] = None,
        max: dict[str, Quantity] = None,
        max_limit_request_ratio: dict[str, Quantity] = None,
        min: dict[str, Quantity] = None,
        type: str = None,
    ):
        super().__init__(
            default=default, default_request=default_request, max=max, max_limit_request_ratio=max_limit_request_ratio, min=min, type=type
        )


class LimitRangeSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["limits"]

    limits: list[LimitRangeItem]

    def __init__(self, limits: list[LimitRangeItem] = None):
        super().__init__(limits=limits)


class LimitRange(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "LimitRange"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: LimitRangeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: LimitRangeSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class LimitRangeList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "LimitRangeList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[LimitRange]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[LimitRange] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class PortStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port", "protocol"]

    error: str
    port: int
    protocol: str

    def __init__(self, error: str = None, port: int = None, protocol: str = None):
        super().__init__(error=error, port=port, protocol=protocol)


class LoadBalancerIngress(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    hostname: str
    ip: str
    ports: list[PortStatus]

    def __init__(self, hostname: str = None, ip: str = None, ports: list[PortStatus] = None):
        super().__init__(hostname=hostname, ip=ip, ports=ports)


class LoadBalancerStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    ingress: list[LoadBalancerIngress]

    def __init__(self, ingress: list[LoadBalancerIngress] = None):
        super().__init__(ingress=ingress)


class LocalVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    fs_type: str
    path: str

    def __init__(self, fs_type: str = None, path: str = None):
        super().__init__(fs_type=fs_type, path=path)


class NFSVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path", "server"]

    path: str
    read_only: bool
    server: str

    def __init__(self, path: str = None, read_only: bool = None, server: str = None):
        super().__init__(path=path, read_only=read_only, server=server)


class NamespaceSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    finalizers: list[str]

    def __init__(self, finalizers: list[str] = None):
        super().__init__(finalizers=finalizers)


class Namespace(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Namespace"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: NamespaceSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: NamespaceSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class NamespaceCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class NamespaceList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "NamespaceList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Namespace]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Namespace] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class NamespaceStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    conditions: list[NamespaceCondition]
    phase: str

    def __init__(self, conditions: list[NamespaceCondition] = None, phase: str = None):
        super().__init__(conditions=conditions, phase=phase)


class NodeConfigSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    config_map: ConfigMapNodeConfigSource

    def __init__(self, config_map: ConfigMapNodeConfigSource = None):
        super().__init__(config_map=config_map)


class Taint(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["effect", "key"]

    effect: str
    key: str
    time_added: meta.Time
    value: str

    def __init__(self, effect: str = None, key: str = None, time_added: meta.Time = None, value: str = None):
        super().__init__(effect=effect, key=key, time_added=time_added, value=value)


class NodeSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "external_id": "externalID",
        "pod_cidr": "podCIDR",
        "pod_cidrs": "podCIDRs",
        "provider_id": "providerID",
    }
    _revfield_names_ = {
        "externalID": "external_id",
        "podCIDR": "pod_cidr",
        "podCIDRs": "pod_cidrs",
        "providerID": "provider_id",
    }

    config_source: NodeConfigSource
    external_id: str
    pod_cidr: str
    pod_cidrs: list[str]
    provider_id: str
    taints: list[Taint]
    unschedulable: bool

    def __init__(
        self,
        config_source: NodeConfigSource = None,
        external_id: str = None,
        pod_cidr: str = None,
        pod_cidrs: list[str] = None,
        provider_id: str = None,
        taints: list[Taint] = None,
        unschedulable: bool = None,
    ):
        super().__init__(
            config_source=config_source,
            external_id=external_id,
            pod_cidr=pod_cidr,
            pod_cidrs=pod_cidrs,
            provider_id=provider_id,
            taints=taints,
            unschedulable=unschedulable,
        )


class Node(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Node"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: NodeSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: NodeSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class NodeAddress(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["address", "type"]

    address: str
    type: str

    def __init__(self, address: str = None, type: str = None):
        super().__init__(address=address, type=type)


class NodeCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_heartbeat_time: meta.Time
    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_heartbeat_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_heartbeat_time=last_heartbeat_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class NodeConfigStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    active: NodeConfigSource
    assigned: NodeConfigSource
    error: str
    last_known_good: NodeConfigSource

    def __init__(
        self,
        active: NodeConfigSource = None,
        assigned: NodeConfigSource = None,
        error: str = None,
        last_known_good: NodeConfigSource = None,
    ):
        super().__init__(active=active, assigned=assigned, error=error, last_known_good=last_known_good)


class NodeDaemonEndpoints(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    kubelet_endpoint: DaemonEndpoint

    def __init__(self, kubelet_endpoint: DaemonEndpoint = None):
        super().__init__(kubelet_endpoint=kubelet_endpoint)


class NodeList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "NodeList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Node]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Node] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class NodeSystemInfo(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = [
        "architecture",
        "boot_id",
        "container_runtime_version",
        "kernel_version",
        "kube_proxy_version",
        "kubelet_version",
        "machine_id",
        "operating_system",
        "os_image",
        "system_uuid",
    ]

    _field_names_ = {
        "boot_id": "bootID",
        "machine_id": "machineID",
        "system_uuid": "systemUUID",
    }
    _revfield_names_ = {
        "bootID": "boot_id",
        "machineID": "machine_id",
        "systemUUID": "system_uuid",
    }

    architecture: str
    boot_id: str
    container_runtime_version: str
    kernel_version: str
    kube_proxy_version: str
    kubelet_version: str
    machine_id: str
    operating_system: str
    os_image: str
    system_uuid: str

    def __init__(
        self,
        architecture: str = None,
        boot_id: str = None,
        container_runtime_version: str = None,
        kernel_version: str = None,
        kube_proxy_version: str = None,
        kubelet_version: str = None,
        machine_id: str = None,
        operating_system: str = None,
        os_image: str = None,
        system_uuid: str = None,
    ):
        super().__init__(
            architecture=architecture,
            boot_id=boot_id,
            container_runtime_version=container_runtime_version,
            kernel_version=kernel_version,
            kube_proxy_version=kube_proxy_version,
            kubelet_version=kubelet_version,
            machine_id=machine_id,
            operating_system=operating_system,
            os_image=os_image,
            system_uuid=system_uuid,
        )


class NodeStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    addresses: list[NodeAddress]
    allocatable: dict[str, Quantity]
    capacity: dict[str, Quantity]
    conditions: list[NodeCondition]
    config: NodeConfigStatus
    daemon_endpoints: NodeDaemonEndpoints
    images: list[ContainerImage]
    node_info: NodeSystemInfo
    phase: str
    volumes_attached: list[AttachedVolume]
    volumes_in_use: list[str]

    def __init__(
        self,
        addresses: list[NodeAddress] = None,
        allocatable: dict[str, Quantity] = None,
        capacity: dict[str, Quantity] = None,
        conditions: list[NodeCondition] = None,
        config: NodeConfigStatus = None,
        daemon_endpoints: NodeDaemonEndpoints = None,
        images: list[ContainerImage] = None,
        node_info: NodeSystemInfo = None,
        phase: str = None,
        volumes_attached: list[AttachedVolume] = None,
        volumes_in_use: list[str] = None,
    ):
        super().__init__(
            addresses=addresses,
            allocatable=allocatable,
            capacity=capacity,
            conditions=conditions,
            config=config,
            daemon_endpoints=daemon_endpoints,
            images=images,
            node_info=node_info,
            phase=phase,
            volumes_attached=volumes_attached,
            volumes_in_use=volumes_in_use,
        )


class VolumeNodeAffinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    required: NodeSelector

    def __init__(self, required: NodeSelector = None):
        super().__init__(required=required)


class PhotonPersistentDiskVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["pd_id"]

    _field_names_ = {
        "pd_id": "pdID",
    }
    _revfield_names_ = {
        "pdID": "pd_id",
    }

    fs_type: str
    pd_id: str

    def __init__(self, fs_type: str = None, pd_id: str = None):
        super().__init__(fs_type=fs_type, pd_id=pd_id)


class PortworxVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_id"]

    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    read_only: bool
    volume_id: str

    def __init__(self, fs_type: str = None, read_only: bool = None, volume_id: str = None):
        super().__init__(fs_type=fs_type, read_only=read_only, volume_id=volume_id)


class QuobyteVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["registry", "volume"]

    group: str
    read_only: bool
    registry: str
    tenant: str
    user: str
    volume: str

    def __init__(
        self, group: str = None, read_only: bool = None, registry: str = None, tenant: str = None, user: str = None, volume: str = None
    ):
        super().__init__(group=group, read_only=read_only, registry=registry, tenant=tenant, user=user, volume=volume)


class RBDPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "monitors"]

    fs_type: str
    image: str
    keyring: str
    monitors: list[str]
    pool: str
    read_only: bool
    secret_ref: SecretReference
    user: str

    def __init__(
        self,
        fs_type: str = None,
        image: str = None,
        keyring: str = None,
        monitors: list[str] = None,
        pool: str = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        user: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            image=image,
            keyring=keyring,
            monitors=monitors,
            pool=pool,
            read_only=read_only,
            secret_ref=secret_ref,
            user=user,
        )


class ScaleIOPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["gateway", "secret_ref", "system"]

    fs_type: str
    gateway: str
    protection_domain: str
    read_only: bool
    secret_ref: SecretReference
    ssl_enabled: bool
    storage_mode: str
    storage_pool: str
    system: str
    volume_name: str

    def __init__(
        self,
        fs_type: str = None,
        gateway: str = None,
        protection_domain: str = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        ssl_enabled: bool = None,
        storage_mode: str = None,
        storage_pool: str = None,
        system: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            gateway=gateway,
            protection_domain=protection_domain,
            read_only=read_only,
            secret_ref=secret_ref,
            ssl_enabled=ssl_enabled,
            storage_mode=storage_mode,
            storage_pool=storage_pool,
            system=system,
            volume_name=volume_name,
        )


class StorageOSPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    fs_type: str
    read_only: bool
    secret_ref: ObjectReference
    volume_name: str
    volume_namespace: str

    def __init__(
        self,
        fs_type: str = None,
        read_only: bool = None,
        secret_ref: ObjectReference = None,
        volume_name: str = None,
        volume_namespace: str = None,
    ):
        super().__init__(
            fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_name=volume_name, volume_namespace=volume_namespace
        )


class VsphereVirtualDiskVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["volume_path"]

    _field_names_ = {
        "storage_policy_id": "storagePolicyID",
    }
    _revfield_names_ = {
        "storagePolicyID": "storage_policy_id",
    }

    fs_type: str
    storage_policy_id: str
    storage_policy_name: str
    volume_path: str

    def __init__(self, fs_type: str = None, storage_policy_id: str = None, storage_policy_name: str = None, volume_path: str = None):
        super().__init__(
            fs_type=fs_type, storage_policy_id=storage_policy_id, storage_policy_name=storage_policy_name, volume_path=volume_path
        )


class PersistentVolumeSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "scale_io": "scaleIO",
    }
    _revfield_names_ = {
        "scaleIO": "scale_io",
    }

    access_modes: list[str]
    aws_elastic_block_store: AWSElasticBlockStoreVolumeSource
    azure_disk: AzureDiskVolumeSource
    azure_file: AzureFilePersistentVolumeSource
    capacity: dict[str, Quantity]
    cephfs: CephFSPersistentVolumeSource
    cinder: CinderPersistentVolumeSource
    claim_ref: ObjectReference
    csi: CSIPersistentVolumeSource
    fc: FCVolumeSource
    flex_volume: FlexPersistentVolumeSource
    flocker: FlockerVolumeSource
    gce_persistent_disk: GCEPersistentDiskVolumeSource
    glusterfs: GlusterfsPersistentVolumeSource
    host_path: HostPathVolumeSource
    iscsi: ISCSIPersistentVolumeSource
    local: LocalVolumeSource
    mount_options: list[str]
    nfs: NFSVolumeSource
    node_affinity: VolumeNodeAffinity
    persistent_volume_reclaim_policy: str
    photon_persistent_disk: PhotonPersistentDiskVolumeSource
    portworx_volume: PortworxVolumeSource
    quobyte: QuobyteVolumeSource
    rbd: RBDPersistentVolumeSource
    scale_io: ScaleIOPersistentVolumeSource
    storage_class_name: str
    storageos: StorageOSPersistentVolumeSource
    volume_mode: str
    vsphere_volume: VsphereVirtualDiskVolumeSource

    def __init__(
        self,
        access_modes: list[str] = None,
        aws_elastic_block_store: AWSElasticBlockStoreVolumeSource = None,
        azure_disk: AzureDiskVolumeSource = None,
        azure_file: AzureFilePersistentVolumeSource = None,
        capacity: dict[str, Quantity] = None,
        cephfs: CephFSPersistentVolumeSource = None,
        cinder: CinderPersistentVolumeSource = None,
        claim_ref: ObjectReference = None,
        csi: CSIPersistentVolumeSource = None,
        fc: FCVolumeSource = None,
        flex_volume: FlexPersistentVolumeSource = None,
        flocker: FlockerVolumeSource = None,
        gce_persistent_disk: GCEPersistentDiskVolumeSource = None,
        glusterfs: GlusterfsPersistentVolumeSource = None,
        host_path: HostPathVolumeSource = None,
        iscsi: ISCSIPersistentVolumeSource = None,
        local: LocalVolumeSource = None,
        mount_options: list[str] = None,
        nfs: NFSVolumeSource = None,
        node_affinity: VolumeNodeAffinity = None,
        persistent_volume_reclaim_policy: str = None,
        photon_persistent_disk: PhotonPersistentDiskVolumeSource = None,
        portworx_volume: PortworxVolumeSource = None,
        quobyte: QuobyteVolumeSource = None,
        rbd: RBDPersistentVolumeSource = None,
        scale_io: ScaleIOPersistentVolumeSource = None,
        storage_class_name: str = None,
        storageos: StorageOSPersistentVolumeSource = None,
        volume_mode: str = None,
        vsphere_volume: VsphereVirtualDiskVolumeSource = None,
    ):
        super().__init__(
            access_modes=access_modes,
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            capacity=capacity,
            cephfs=cephfs,
            cinder=cinder,
            claim_ref=claim_ref,
            csi=csi,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            local=local,
            mount_options=mount_options,
            nfs=nfs,
            node_affinity=node_affinity,
            persistent_volume_reclaim_policy=persistent_volume_reclaim_policy,
            photon_persistent_disk=photon_persistent_disk,
            portworx_volume=portworx_volume,
            quobyte=quobyte,
            rbd=rbd,
            scale_io=scale_io,
            storage_class_name=storage_class_name,
            storageos=storageos,
            volume_mode=volume_mode,
            vsphere_volume=vsphere_volume,
        )


class PersistentVolume(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PersistentVolume"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: PersistentVolumeSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: PersistentVolumeSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class PersistentVolumeClaim(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PersistentVolumeClaim"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PersistentVolumeClaimSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PersistentVolumeClaimSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PersistentVolumeClaimCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_probe_time: meta.Time
    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_probe_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_probe_time=last_probe_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class PersistentVolumeClaimList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PersistentVolumeClaimList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PersistentVolumeClaim]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PersistentVolumeClaim] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class PersistentVolumeClaimStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    access_modes: list[str]
    allocated_resources: dict[str, Quantity]
    capacity: dict[str, Quantity]
    conditions: list[PersistentVolumeClaimCondition]
    phase: str
    resize_status: str

    def __init__(
        self,
        access_modes: list[str] = None,
        allocated_resources: dict[str, Quantity] = None,
        capacity: dict[str, Quantity] = None,
        conditions: list[PersistentVolumeClaimCondition] = None,
        phase: str = None,
        resize_status: str = None,
    ):
        super().__init__(
            access_modes=access_modes,
            allocated_resources=allocated_resources,
            capacity=capacity,
            conditions=conditions,
            phase=phase,
            resize_status=resize_status,
        )


class PersistentVolumeClaimVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["claim_name"]

    claim_name: str
    read_only: bool

    def __init__(self, claim_name: str = None, read_only: bool = None):
        super().__init__(claim_name=claim_name, read_only=read_only)


class PersistentVolumeList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PersistentVolumeList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PersistentVolume]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PersistentVolume] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class PersistentVolumeStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    message: str
    phase: str
    reason: str

    def __init__(self, message: str = None, phase: str = None, reason: str = None):
        super().__init__(message=message, phase=phase, reason=reason)


class PodDNSConfigOption(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class PodDNSConfig(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    nameservers: list[str]
    options: list[PodDNSConfigOption]
    searches: list[str]

    def __init__(self, nameservers: list[str] = None, options: list[PodDNSConfigOption] = None, searches: list[str] = None):
        super().__init__(nameservers=nameservers, options=options, searches=searches)


class PodOS(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class PodReadinessGate(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["condition_type"]

    condition_type: str

    def __init__(self, condition_type: str = None):
        super().__init__(condition_type=condition_type)


class Sysctl(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name", "value"]

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class PodSecurityContext(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    fs_group: int
    fs_group_change_policy: str
    run_as_group: int
    run_as_non_root: bool
    run_as_user: int
    se_linux_options: SELinuxOptions
    seccomp_profile: SeccompProfile
    supplemental_groups: list[int]
    sysctls: list[Sysctl]
    windows_options: WindowsSecurityContextOptions

    def __init__(
        self,
        fs_group: int = None,
        fs_group_change_policy: str = None,
        run_as_group: int = None,
        run_as_non_root: bool = None,
        run_as_user: int = None,
        se_linux_options: SELinuxOptions = None,
        seccomp_profile: SeccompProfile = None,
        supplemental_groups: list[int] = None,
        sysctls: list[Sysctl] = None,
        windows_options: WindowsSecurityContextOptions = None,
    ):
        super().__init__(
            fs_group=fs_group,
            fs_group_change_policy=fs_group_change_policy,
            run_as_group=run_as_group,
            run_as_non_root=run_as_non_root,
            run_as_user=run_as_user,
            se_linux_options=se_linux_options,
            seccomp_profile=seccomp_profile,
            supplemental_groups=supplemental_groups,
            sysctls=sysctls,
            windows_options=windows_options,
        )


class Toleration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    effect: str
    key: str
    operator: str
    toleration_seconds: int
    value: str

    def __init__(self, effect: str = None, key: str = None, operator: str = None, toleration_seconds: int = None, value: str = None):
        super().__init__(effect=effect, key=key, operator=operator, toleration_seconds=toleration_seconds, value=value)


class TopologySpreadConstraint(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["max_skew", "topology_key", "when_unsatisfiable"]

    label_selector: meta.LabelSelector
    match_label_keys: list[str]
    max_skew: int
    min_domains: int
    node_affinity_policy: str
    node_taints_policy: str
    topology_key: str
    when_unsatisfiable: str

    def __init__(
        self,
        label_selector: meta.LabelSelector = None,
        match_label_keys: list[str] = None,
        max_skew: int = None,
        min_domains: int = None,
        node_affinity_policy: str = None,
        node_taints_policy: str = None,
        topology_key: str = None,
        when_unsatisfiable: str = None,
    ):
        super().__init__(
            label_selector=label_selector,
            match_label_keys=match_label_keys,
            max_skew=max_skew,
            min_domains=min_domains,
            node_affinity_policy=node_affinity_policy,
            node_taints_policy=node_taints_policy,
            topology_key=topology_key,
            when_unsatisfiable=when_unsatisfiable,
        )


class SecretProjection(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    items: list[KeyToPath]
    name: str
    optional: bool

    def __init__(self, items: list[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(items=items, name=name, optional=optional)


class ServiceAccountTokenProjection(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    audience: str
    expiration_seconds: int
    path: str

    def __init__(self, audience: str = None, expiration_seconds: int = None, path: str = None):
        super().__init__(audience=audience, expiration_seconds=expiration_seconds, path=path)


class VolumeProjection(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "downward_api": "downwardAPI",
    }
    _revfield_names_ = {
        "downwardAPI": "downward_api",
    }

    config_map: ConfigMapProjection
    downward_api: DownwardAPIProjection
    secret: SecretProjection
    service_account_token: ServiceAccountTokenProjection

    def __init__(
        self,
        config_map: ConfigMapProjection = None,
        downward_api: DownwardAPIProjection = None,
        secret: SecretProjection = None,
        service_account_token: ServiceAccountTokenProjection = None,
    ):
        super().__init__(config_map=config_map, downward_api=downward_api, secret=secret, service_account_token=service_account_token)


class ProjectedVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    sources: list[VolumeProjection]

    def __init__(self, default_mode: int = None, sources: list[VolumeProjection] = None):
        super().__init__(default_mode=default_mode, sources=sources)


class RBDVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "monitors"]

    fs_type: str
    image: str
    keyring: str
    monitors: list[str]
    pool: str
    read_only: bool
    secret_ref: LocalObjectReference
    user: str

    def __init__(
        self,
        fs_type: str = None,
        image: str = None,
        keyring: str = None,
        monitors: list[str] = None,
        pool: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        user: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            image=image,
            keyring=keyring,
            monitors=monitors,
            pool=pool,
            read_only=read_only,
            secret_ref=secret_ref,
            user=user,
        )


class ScaleIOVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["gateway", "secret_ref", "system"]

    fs_type: str
    gateway: str
    protection_domain: str
    read_only: bool
    secret_ref: LocalObjectReference
    ssl_enabled: bool
    storage_mode: str
    storage_pool: str
    system: str
    volume_name: str

    def __init__(
        self,
        fs_type: str = None,
        gateway: str = None,
        protection_domain: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        ssl_enabled: bool = None,
        storage_mode: str = None,
        storage_pool: str = None,
        system: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            gateway=gateway,
            protection_domain=protection_domain,
            read_only=read_only,
            secret_ref=secret_ref,
            ssl_enabled=ssl_enabled,
            storage_mode=storage_mode,
            storage_pool=storage_pool,
            system=system,
            volume_name=volume_name,
        )


class SecretVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    items: list[KeyToPath]
    optional: bool
    secret_name: str

    def __init__(self, default_mode: int = None, items: list[KeyToPath] = None, optional: bool = None, secret_name: str = None):
        super().__init__(default_mode=default_mode, items=items, optional=optional, secret_name=secret_name)


class StorageOSVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    fs_type: str
    read_only: bool
    secret_ref: LocalObjectReference
    volume_name: str
    volume_namespace: str

    def __init__(
        self,
        fs_type: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        volume_name: str = None,
        volume_namespace: str = None,
    ):
        super().__init__(
            fs_type=fs_type, read_only=read_only, secret_ref=secret_ref, volume_name=volume_name, volume_namespace=volume_namespace
        )


class Volume(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    _field_names_ = {
        "downward_api": "downwardAPI",
        "scale_io": "scaleIO",
    }
    _revfield_names_ = {
        "downwardAPI": "downward_api",
        "scaleIO": "scale_io",
    }

    aws_elastic_block_store: AWSElasticBlockStoreVolumeSource
    azure_disk: AzureDiskVolumeSource
    azure_file: AzureFileVolumeSource
    cephfs: CephFSVolumeSource
    cinder: CinderVolumeSource
    config_map: ConfigMapVolumeSource
    csi: CSIVolumeSource
    downward_api: DownwardAPIVolumeSource
    empty_dir: EmptyDirVolumeSource
    ephemeral: EphemeralVolumeSource
    fc: FCVolumeSource
    flex_volume: FlexVolumeSource
    flocker: FlockerVolumeSource
    gce_persistent_disk: GCEPersistentDiskVolumeSource
    git_repo: GitRepoVolumeSource
    glusterfs: GlusterfsVolumeSource
    host_path: HostPathVolumeSource
    iscsi: ISCSIVolumeSource
    name: str
    nfs: NFSVolumeSource
    persistent_volume_claim: PersistentVolumeClaimVolumeSource
    photon_persistent_disk: PhotonPersistentDiskVolumeSource
    portworx_volume: PortworxVolumeSource
    projected: ProjectedVolumeSource
    quobyte: QuobyteVolumeSource
    rbd: RBDVolumeSource
    scale_io: ScaleIOVolumeSource
    secret: SecretVolumeSource
    storageos: StorageOSVolumeSource
    vsphere_volume: VsphereVirtualDiskVolumeSource

    def __init__(
        self,
        aws_elastic_block_store: AWSElasticBlockStoreVolumeSource = None,
        azure_disk: AzureDiskVolumeSource = None,
        azure_file: AzureFileVolumeSource = None,
        cephfs: CephFSVolumeSource = None,
        cinder: CinderVolumeSource = None,
        config_map: ConfigMapVolumeSource = None,
        csi: CSIVolumeSource = None,
        downward_api: DownwardAPIVolumeSource = None,
        empty_dir: EmptyDirVolumeSource = None,
        ephemeral: EphemeralVolumeSource = None,
        fc: FCVolumeSource = None,
        flex_volume: FlexVolumeSource = None,
        flocker: FlockerVolumeSource = None,
        gce_persistent_disk: GCEPersistentDiskVolumeSource = None,
        git_repo: GitRepoVolumeSource = None,
        glusterfs: GlusterfsVolumeSource = None,
        host_path: HostPathVolumeSource = None,
        iscsi: ISCSIVolumeSource = None,
        name: str = None,
        nfs: NFSVolumeSource = None,
        persistent_volume_claim: PersistentVolumeClaimVolumeSource = None,
        photon_persistent_disk: PhotonPersistentDiskVolumeSource = None,
        portworx_volume: PortworxVolumeSource = None,
        projected: ProjectedVolumeSource = None,
        quobyte: QuobyteVolumeSource = None,
        rbd: RBDVolumeSource = None,
        scale_io: ScaleIOVolumeSource = None,
        secret: SecretVolumeSource = None,
        storageos: StorageOSVolumeSource = None,
        vsphere_volume: VsphereVirtualDiskVolumeSource = None,
    ):
        super().__init__(
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            cephfs=cephfs,
            cinder=cinder,
            config_map=config_map,
            csi=csi,
            downward_api=downward_api,
            empty_dir=empty_dir,
            ephemeral=ephemeral,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            git_repo=git_repo,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            name=name,
            nfs=nfs,
            persistent_volume_claim=persistent_volume_claim,
            photon_persistent_disk=photon_persistent_disk,
            portworx_volume=portworx_volume,
            projected=projected,
            quobyte=quobyte,
            rbd=rbd,
            scale_io=scale_io,
            secret=secret,
            storageos=storageos,
            vsphere_volume=vsphere_volume,
        )


class PodSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["containers"]

    _field_names_ = {
        "host_ipc": "hostIPC",
        "host_pid": "hostPID",
        "set_hostname_as_fqdn": "setHostnameAsFQDN",
    }
    _revfield_names_ = {
        "hostIPC": "host_ipc",
        "hostPID": "host_pid",
        "setHostnameAsFQDN": "set_hostname_as_fqdn",
    }

    active_deadline_seconds: int
    affinity: Affinity
    automount_service_account_token: bool
    containers: list[Container]
    dns_config: PodDNSConfig
    dns_policy: str
    enable_service_links: bool
    ephemeral_containers: list[EphemeralContainer]
    host_aliases: list[HostAlias]
    host_ipc: bool
    host_network: bool
    host_pid: bool
    host_users: bool
    hostname: str
    image_pull_secrets: list[LocalObjectReference]
    init_containers: list[Container]
    node_name: str
    node_selector: dict[str, str]
    os: PodOS
    overhead: dict[str, Quantity]
    preemption_policy: str
    priority: int
    priority_class_name: str
    readiness_gates: list[PodReadinessGate]
    restart_policy: str
    runtime_class_name: str
    scheduler_name: str
    security_context: PodSecurityContext
    service_account: str
    service_account_name: str
    set_hostname_as_fqdn: bool
    share_process_namespace: bool
    subdomain: str
    termination_grace_period_seconds: int
    tolerations: list[Toleration]
    topology_spread_constraints: list[TopologySpreadConstraint]
    volumes: list[Volume]

    def __init__(
        self,
        active_deadline_seconds: int = None,
        affinity: Affinity = None,
        automount_service_account_token: bool = None,
        containers: list[Container] = None,
        dns_config: PodDNSConfig = None,
        dns_policy: str = None,
        enable_service_links: bool = None,
        ephemeral_containers: list[EphemeralContainer] = None,
        host_aliases: list[HostAlias] = None,
        host_ipc: bool = None,
        host_network: bool = None,
        host_pid: bool = None,
        host_users: bool = None,
        hostname: str = None,
        image_pull_secrets: list[LocalObjectReference] = None,
        init_containers: list[Container] = None,
        node_name: str = None,
        node_selector: dict[str, str] = None,
        os: PodOS = None,
        overhead: dict[str, Quantity] = None,
        preemption_policy: str = None,
        priority: int = None,
        priority_class_name: str = None,
        readiness_gates: list[PodReadinessGate] = None,
        restart_policy: str = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        security_context: PodSecurityContext = None,
        service_account: str = None,
        service_account_name: str = None,
        set_hostname_as_fqdn: bool = None,
        share_process_namespace: bool = None,
        subdomain: str = None,
        termination_grace_period_seconds: int = None,
        tolerations: list[Toleration] = None,
        topology_spread_constraints: list[TopologySpreadConstraint] = None,
        volumes: list[Volume] = None,
    ):
        super().__init__(
            active_deadline_seconds=active_deadline_seconds,
            affinity=affinity,
            automount_service_account_token=automount_service_account_token,
            containers=containers,
            dns_config=dns_config,
            dns_policy=dns_policy,
            enable_service_links=enable_service_links,
            ephemeral_containers=ephemeral_containers,
            host_aliases=host_aliases,
            host_ipc=host_ipc,
            host_network=host_network,
            host_pid=host_pid,
            host_users=host_users,
            hostname=hostname,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            node_name=node_name,
            node_selector=node_selector,
            os=os,
            overhead=overhead,
            preemption_policy=preemption_policy,
            priority=priority,
            priority_class_name=priority_class_name,
            readiness_gates=readiness_gates,
            restart_policy=restart_policy,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            security_context=security_context,
            service_account=service_account,
            service_account_name=service_account_name,
            set_hostname_as_fqdn=set_hostname_as_fqdn,
            share_process_namespace=share_process_namespace,
            subdomain=subdomain,
            termination_grace_period_seconds=termination_grace_period_seconds,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            volumes=volumes,
        )


class Pod(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Pod"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PodSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PodCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_probe_time: meta.Time
    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_probe_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_probe_time=last_probe_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class PodIP(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    ip: str

    def __init__(self, ip: str = None):
        super().__init__(ip=ip)


class PodList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PodList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Pod]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Pod] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class PodStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "host_ip": "hostIP",
        "pod_ip": "podIP",
        "pod_ips": "podIPs",
    }
    _revfield_names_ = {
        "hostIP": "host_ip",
        "podIP": "pod_ip",
        "podIPs": "pod_ips",
    }

    conditions: list[PodCondition]
    container_statuses: list[ContainerStatus]
    ephemeral_container_statuses: list[ContainerStatus]
    host_ip: str
    init_container_statuses: list[ContainerStatus]
    message: str
    nominated_node_name: str
    phase: str
    pod_ip: str
    pod_ips: list[PodIP]
    qos_class: str
    reason: str
    start_time: meta.Time

    def __init__(
        self,
        conditions: list[PodCondition] = None,
        container_statuses: list[ContainerStatus] = None,
        ephemeral_container_statuses: list[ContainerStatus] = None,
        host_ip: str = None,
        init_container_statuses: list[ContainerStatus] = None,
        message: str = None,
        nominated_node_name: str = None,
        phase: str = None,
        pod_ip: str = None,
        pod_ips: list[PodIP] = None,
        qos_class: str = None,
        reason: str = None,
        start_time: meta.Time = None,
    ):
        super().__init__(
            conditions=conditions,
            container_statuses=container_statuses,
            ephemeral_container_statuses=ephemeral_container_statuses,
            host_ip=host_ip,
            init_container_statuses=init_container_statuses,
            message=message,
            nominated_node_name=nominated_node_name,
            phase=phase,
            pod_ip=pod_ip,
            pod_ips=pod_ips,
            qos_class=qos_class,
            reason=reason,
            start_time=start_time,
        )


class PodTemplateSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    metadata: meta.ObjectMeta
    spec: PodSpec

    def __init__(self, metadata: meta.ObjectMeta = None, spec: PodSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class PodTemplate(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PodTemplate"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    template: PodTemplateSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, template: PodTemplateSpec = None):
        super().__init__(name, namespace, metadata=metadata, template=template)


class PodTemplateList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "PodTemplateList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PodTemplate]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PodTemplate] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


RawExtension: t.TypeAlias = dict[str, t.Any]


class ReplicationControllerSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    min_ready_seconds: int
    replicas: int
    selector: dict[str, str]
    template: PodTemplateSpec

    def __init__(
        self, min_ready_seconds: int = None, replicas: int = None, selector: dict[str, str] = None, template: PodTemplateSpec = None
    ):
        super().__init__(min_ready_seconds=min_ready_seconds, replicas=replicas, selector=selector, template=template)


class ReplicationController(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ReplicationController"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ReplicationControllerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ReplicationControllerSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ReplicationControllerCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class ReplicationControllerList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ReplicationControllerList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ReplicationController]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ReplicationController] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ReplicationControllerStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["replicas"]

    available_replicas: int
    conditions: list[ReplicationControllerCondition]
    fully_labeled_replicas: int
    observed_generation: int
    ready_replicas: int
    replicas: int

    def __init__(
        self,
        available_replicas: int = None,
        conditions: list[ReplicationControllerCondition] = None,
        fully_labeled_replicas: int = None,
        observed_generation: int = None,
        ready_replicas: int = None,
        replicas: int = None,
    ):
        super().__init__(
            available_replicas=available_replicas,
            conditions=conditions,
            fully_labeled_replicas=fully_labeled_replicas,
            observed_generation=observed_generation,
            ready_replicas=ready_replicas,
            replicas=replicas,
        )


class ScopedResourceSelectorRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["operator", "scope_name"]

    operator: str
    scope_name: str
    values: list[str]

    def __init__(self, operator: str = None, scope_name: str = None, values: list[str] = None):
        super().__init__(operator=operator, scope_name=scope_name, values=values)


class ScopeSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    match_expressions: list[ScopedResourceSelectorRequirement]

    def __init__(self, match_expressions: list[ScopedResourceSelectorRequirement] = None):
        super().__init__(match_expressions=match_expressions)


class ResourceQuotaSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    hard: dict[str, Quantity]
    scope_selector: ScopeSelector
    scopes: list[str]

    def __init__(self, hard: dict[str, Quantity] = None, scope_selector: ScopeSelector = None, scopes: list[str] = None):
        super().__init__(hard=hard, scope_selector=scope_selector, scopes=scopes)


class ResourceQuota(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ResourceQuota"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ResourceQuotaSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceQuotaSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceQuotaList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ResourceQuotaList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ResourceQuota]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ResourceQuota] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ResourceQuotaStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    hard: dict[str, Quantity]
    used: dict[str, Quantity]

    def __init__(self, hard: dict[str, Quantity] = None, used: dict[str, Quantity] = None):
        super().__init__(hard=hard, used=used)


class Secret(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Secret"
    _scope_ = "namespace"

    data: dict[str, Base64]
    immutable: bool
    metadata: meta.ObjectMeta
    string_data: dict[str, str]
    type: str

    def __init__(
        self,
        name: str,
        namespace: str = None,
        data: dict[str, Base64] = None,
        immutable: bool = None,
        metadata: meta.ObjectMeta = None,
        string_data: dict[str, str] = None,
        type: str = None,
    ):
        super().__init__(name, namespace, data=data, immutable=immutable, metadata=metadata, string_data=string_data, type=type)


class SecretList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "SecretList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Secret]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Secret] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ServicePort(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    app_protocol: str
    name: str
    node_port: int
    port: int
    protocol: str
    target_port: IntOrString

    def __init__(
        self,
        app_protocol: str = None,
        name: str = None,
        node_port: int = None,
        port: int = None,
        protocol: str = None,
        target_port: IntOrString = None,
    ):
        super().__init__(app_protocol=app_protocol, name=name, node_port=node_port, port=port, protocol=protocol, target_port=target_port)


class SessionAffinityConfig(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "client_ip": "clientIP",
    }
    _revfield_names_ = {
        "clientIP": "client_ip",
    }

    client_ip: ClientIPConfig

    def __init__(self, client_ip: ClientIPConfig = None):
        super().__init__(client_ip=client_ip)


class ServiceSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _field_names_ = {
        "cluster_ip": "clusterIP",
        "cluster_ips": "clusterIPs",
        "external_ips": "externalIPs",
        "load_balancer_ip": "loadBalancerIP",
    }
    _revfield_names_ = {
        "clusterIP": "cluster_ip",
        "clusterIPs": "cluster_ips",
        "externalIPs": "external_ips",
        "loadBalancerIP": "load_balancer_ip",
    }

    allocate_load_balancer_node_ports: bool
    cluster_ip: str
    cluster_ips: list[str]
    external_ips: list[str]
    external_name: str
    external_traffic_policy: str
    health_check_node_port: int
    internal_traffic_policy: str
    ip_families: list[str]
    ip_family_policy: str
    load_balancer_class: str
    load_balancer_ip: str
    load_balancer_source_ranges: list[str]
    ports: list[ServicePort]
    publish_not_ready_addresses: bool
    selector: dict[str, str]
    session_affinity: str
    session_affinity_config: SessionAffinityConfig
    type: str

    def __init__(
        self,
        allocate_load_balancer_node_ports: bool = None,
        cluster_ip: str = None,
        cluster_ips: list[str] = None,
        external_ips: list[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        internal_traffic_policy: str = None,
        ip_families: list[str] = None,
        ip_family_policy: str = None,
        load_balancer_class: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: list[str] = None,
        ports: list[ServicePort] = None,
        publish_not_ready_addresses: bool = None,
        selector: dict[str, str] = None,
        session_affinity: str = None,
        session_affinity_config: SessionAffinityConfig = None,
        type: str = None,
    ):
        super().__init__(
            allocate_load_balancer_node_ports=allocate_load_balancer_node_ports,
            cluster_ip=cluster_ip,
            cluster_ips=cluster_ips,
            external_ips=external_ips,
            external_name=external_name,
            external_traffic_policy=external_traffic_policy,
            health_check_node_port=health_check_node_port,
            internal_traffic_policy=internal_traffic_policy,
            ip_families=ip_families,
            ip_family_policy=ip_family_policy,
            load_balancer_class=load_balancer_class,
            load_balancer_ip=load_balancer_ip,
            load_balancer_source_ranges=load_balancer_source_ranges,
            ports=ports,
            publish_not_ready_addresses=publish_not_ready_addresses,
            selector=selector,
            session_affinity=session_affinity,
            session_affinity_config=session_affinity_config,
            type=type,
        )


class Service(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "Service"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ServiceSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ServiceSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ServiceAccount(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ServiceAccount"
    _scope_ = "namespace"

    automount_service_account_token: bool
    image_pull_secrets: list[LocalObjectReference]
    metadata: meta.ObjectMeta
    secrets: list[ObjectReference]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        automount_service_account_token: bool = None,
        image_pull_secrets: list[LocalObjectReference] = None,
        metadata: meta.ObjectMeta = None,
        secrets: list[ObjectReference] = None,
    ):
        super().__init__(
            name,
            namespace,
            automount_service_account_token=automount_service_account_token,
            image_pull_secrets=image_pull_secrets,
            metadata=metadata,
            secrets=secrets,
        )


class ServiceAccountList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ServiceAccountList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ServiceAccount]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ServiceAccount] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ServiceList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _api_group_ = ""
    _kind_ = "ServiceList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Service]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Service] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ServiceStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    conditions: list[meta.Condition]
    load_balancer: LoadBalancerStatus

    def __init__(self, conditions: list[meta.Condition] = None, load_balancer: LoadBalancerStatus = None):
        super().__init__(conditions=conditions, load_balancer=load_balancer)


class TopologySelectorLabelRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "values"]

    key: str
    values: list[str]

    def __init__(self, key: str = None, values: list[str] = None):
        super().__init__(key=key, values=values)


class TopologySelectorTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    match_label_expressions: list[TopologySelectorLabelRequirement]

    def __init__(self, match_label_expressions: list[TopologySelectorLabelRequirement] = None):
        super().__init__(match_label_expressions=match_label_expressions)
