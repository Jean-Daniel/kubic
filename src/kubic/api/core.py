from typing import Dict, List, Union

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
    values: List[str]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class NodeSelectorTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    match_expressions: List[NodeSelectorRequirement]
    match_fields: List[NodeSelectorRequirement]

    def __init__(self, match_expressions: List[NodeSelectorRequirement] = None, match_fields: List[NodeSelectorRequirement] = None):
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

    node_selector_terms: List[NodeSelectorTerm]

    def __init__(self, node_selector_terms: List[NodeSelectorTerm] = None):
        super().__init__(node_selector_terms=node_selector_terms)


class NodeAffinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: List[PreferredSchedulingTerm]
    required_during_scheduling_ignored_during_execution: NodeSelector

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[PreferredSchedulingTerm] = None,
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
    namespaces: List[str]
    topology_key: str

    def __init__(
        self,
        label_selector: meta.LabelSelector = None,
        namespace_selector: meta.LabelSelector = None,
        namespaces: List[str] = None,
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

    preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm]
    required_during_scheduling_ignored_during_execution: List[PodAffinityTerm]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm] = None,
        required_during_scheduling_ignored_during_execution: List[PodAffinityTerm] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAntiAffinity(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm]
    required_during_scheduling_ignored_during_execution: List[PodAffinityTerm]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm] = None,
        required_during_scheduling_ignored_during_execution: List[PodAffinityTerm] = None,
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


Base64 = str


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
    node_publish_secret_ref: SecretReference
    node_stage_secret_ref: SecretReference
    read_only: bool
    volume_attributes: Dict[str, str]
    volume_handle: str

    def __init__(
        self,
        controller_expand_secret_ref: SecretReference = None,
        controller_publish_secret_ref: SecretReference = None,
        driver: str = None,
        fs_type: str = None,
        node_publish_secret_ref: SecretReference = None,
        node_stage_secret_ref: SecretReference = None,
        read_only: bool = None,
        volume_attributes: Dict[str, str] = None,
        volume_handle: str = None,
    ):
        super().__init__(
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            driver=driver,
            fs_type=fs_type,
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
    volume_attributes: Dict[str, str]

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        node_publish_secret_ref: LocalObjectReference = None,
        read_only: bool = None,
        volume_attributes: Dict[str, str] = None,
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

    add: List[str]
    drop: List[str]

    def __init__(self, add: List[str] = None, drop: List[str] = None):
        super().__init__(add=add, drop=drop)


class CephFSPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["monitors"]

    monitors: List[str]
    path: str
    read_only: bool
    secret_file: str
    secret_ref: SecretReference
    user: str

    def __init__(
        self,
        monitors: List[str] = None,
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

    monitors: List[str]
    path: str
    read_only: bool
    secret_file: str
    secret_ref: LocalObjectReference
    user: str

    def __init__(
        self,
        monitors: List[str] = None,
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


class ConfigMap(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "ConfigMap"
    _scope_ = "namespace"

    binary_data: Dict[str, Base64]
    data: Dict[str, str]
    immutable: bool
    metadata: meta.ObjectMeta

    def __init__(
        self,
        name: str,
        namespace: str = None,
        binary_data: Dict[str, Base64] = None,
        data: Dict[str, str] = None,
        immutable: bool = None,
        metadata: meta.ObjectMeta = None,
    ):
        super().__init__("v1", "ConfigMap", name, namespace, binary_data=binary_data, data=data, immutable=immutable, metadata=metadata)


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

    items: List[KeyToPath]
    name: str
    optional: bool

    def __init__(self, items: List[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(items=items, name=name, optional=optional)


class ConfigMapVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    items: List[KeyToPath]
    name: str
    optional: bool

    def __init__(self, default_mode: int = None, items: List[KeyToPath] = None, name: str = None, optional: bool = None):
        super().__init__(default_mode=default_mode, items=items, name=name, optional=optional)


class ObjectFieldSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["field_path"]

    api_version: str
    field_path: str

    def __init__(self, api_version: str = None, field_path: str = None):
        super().__init__(api_version=api_version, field_path=field_path)


Quantity = Union[str, int, float]


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

    command: List[str]

    def __init__(self, command: List[str] = None):
        super().__init__(command=command)


class HTTPHeader(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name", "value"]

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


IntOrString = Union[str, int]


class HTTPGetAction(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["port"]

    host: str
    http_headers: List[HTTPHeader]
    path: str
    port: IntOrString
    scheme: str

    def __init__(
        self, host: str = None, http_headers: List[HTTPHeader] = None, path: str = None, port: IntOrString = None, scheme: str = None
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


class Handler(KubernetesObject):
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

    post_start: Handler
    pre_stop: Handler

    def __init__(self, post_start: Handler = None, pre_stop: Handler = None):
        super().__init__(post_start=post_start, pre_stop=pre_stop)


class Probe(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    exec: ExecAction
    failure_threshold: int
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

    limits: Dict[str, Quantity]
    requests: Dict[str, Quantity]

    def __init__(self, limits: Dict[str, Quantity] = None, requests: Dict[str, Quantity] = None):
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

    args: List[str]
    command: List[str]
    env: List[EnvVar]
    env_from: List[EnvFromSource]
    image: str
    image_pull_policy: str
    lifecycle: Lifecycle
    liveness_probe: Probe
    name: str
    ports: List[ContainerPort]
    readiness_probe: Probe
    resources: ResourceRequirements
    security_context: SecurityContext
    startup_probe: Probe
    stdin: bool
    stdin_once: bool
    termination_message_path: str
    termination_message_policy: str
    tty: bool
    volume_devices: List[VolumeDevice]
    volume_mounts: List[VolumeMount]
    working_dir: str

    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        env: List[EnvVar] = None,
        env_from: List[EnvFromSource] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: Probe = None,
        name: str = None,
        ports: List[ContainerPort] = None,
        readiness_probe: Probe = None,
        resources: ResourceRequirements = None,
        security_context: SecurityContext = None,
        startup_probe: Probe = None,
        stdin: bool = None,
        stdin_once: bool = None,
        termination_message_path: str = None,
        termination_message_policy: str = None,
        tty: bool = None,
        volume_devices: List[VolumeDevice] = None,
        volume_mounts: List[VolumeMount] = None,
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

    items: List[DownwardAPIVolumeFile]

    def __init__(self, items: List[DownwardAPIVolumeFile] = None):
        super().__init__(items=items)


class DownwardAPIVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    default_mode: int
    items: List[DownwardAPIVolumeFile]

    def __init__(self, default_mode: int = None, items: List[DownwardAPIVolumeFile] = None):
        super().__init__(default_mode=default_mode, items=items)


class EmptyDirVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    medium: str
    size_limit: Quantity

    def __init__(self, medium: str = None, size_limit: Quantity = None):
        super().__init__(medium=medium, size_limit=size_limit)


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

    addresses: List[EndpointAddress]
    not_ready_addresses: List[EndpointAddress]
    ports: List[EndpointPort]

    def __init__(
        self, addresses: List[EndpointAddress] = None, not_ready_addresses: List[EndpointAddress] = None, ports: List[EndpointPort] = None
    ):
        super().__init__(addresses=addresses, not_ready_addresses=not_ready_addresses, ports=ports)


class Endpoints(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "Endpoints"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    subsets: List[EndpointSubset]

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, subsets: List[EndpointSubset] = None):
        super().__init__("v1", "Endpoints", name, namespace, metadata=metadata, subsets=subsets)


class EphemeralContainer(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["name"]

    args: List[str]
    command: List[str]
    env: List[EnvVar]
    env_from: List[EnvFromSource]
    image: str
    image_pull_policy: str
    lifecycle: Lifecycle
    liveness_probe: Probe
    name: str
    ports: List[ContainerPort]
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
    volume_devices: List[VolumeDevice]
    volume_mounts: List[VolumeMount]
    working_dir: str

    def __init__(
        self,
        args: List[str] = None,
        command: List[str] = None,
        env: List[EnvVar] = None,
        env_from: List[EnvFromSource] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: Probe = None,
        name: str = None,
        ports: List[ContainerPort] = None,
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
        volume_devices: List[VolumeDevice] = None,
        volume_mounts: List[VolumeMount] = None,
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

    access_modes: List[str]
    data_source: TypedLocalObjectReference
    data_source_ref: TypedLocalObjectReference
    resources: ResourceRequirements
    selector: meta.LabelSelector
    storage_class_name: str
    volume_mode: str
    volume_name: str

    def __init__(
        self,
        access_modes: List[str] = None,
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
    target_wwns: List[str]
    wwids: List[str]

    def __init__(
        self, fs_type: str = None, lun: int = None, read_only: bool = None, target_wwns: List[str] = None, wwids: List[str] = None
    ):
        super().__init__(fs_type=fs_type, lun=lun, read_only=read_only, target_wwns=target_wwns, wwids=wwids)


class FlexPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["driver"]

    driver: str
    fs_type: str
    options: Dict[str, str]
    read_only: bool
    secret_ref: SecretReference

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: Dict[str, str] = None,
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
    options: Dict[str, str]
    read_only: bool
    secret_ref: LocalObjectReference

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: Dict[str, str] = None,
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

    hostnames: List[str]
    ip: str

    def __init__(self, hostnames: List[str] = None, ip: str = None):
        super().__init__(hostnames=hostnames, ip=ip)


class HostPathVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["path"]

    path: str
    type: str

    def __init__(self, path: str = None, type: str = None):
        super().__init__(path=path, type=type)


IDNHostname = str


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
    portals: List[str]
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
        portals: List[str] = None,
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
    portals: List[str]
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
        portals: List[str] = None,
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

    finalizers: List[str]

    def __init__(self, finalizers: List[str] = None):
        super().__init__(finalizers=finalizers)


class Namespace(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "Namespace"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: NamespaceSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: NamespaceSpec = None):
        super().__init__("v1", "Namespace", name, "", metadata=metadata, spec=spec)


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
    monitors: List[str]
    pool: str
    read_only: bool
    secret_ref: SecretReference
    user: str

    def __init__(
        self,
        fs_type: str = None,
        image: str = None,
        keyring: str = None,
        monitors: List[str] = None,
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

    access_modes: List[str]
    aws_elastic_block_store: AWSElasticBlockStoreVolumeSource
    azure_disk: AzureDiskVolumeSource
    azure_file: AzureFilePersistentVolumeSource
    capacity: Dict[str, Quantity]
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
    mount_options: List[str]
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
        access_modes: List[str] = None,
        aws_elastic_block_store: AWSElasticBlockStoreVolumeSource = None,
        azure_disk: AzureDiskVolumeSource = None,
        azure_file: AzureFilePersistentVolumeSource = None,
        capacity: Dict[str, Quantity] = None,
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
        mount_options: List[str] = None,
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
    _kind_ = "PersistentVolume"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: PersistentVolumeSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: PersistentVolumeSpec = None):
        super().__init__("v1", "PersistentVolume", name, "", metadata=metadata, spec=spec)


class PersistentVolumeClaim(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "PersistentVolumeClaim"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PersistentVolumeClaimSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PersistentVolumeClaimSpec = None):
        super().__init__("v1", "PersistentVolumeClaim", name, namespace, metadata=metadata, spec=spec)


class PersistentVolumeClaimVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["claim_name"]

    claim_name: str
    read_only: bool

    def __init__(self, claim_name: str = None, read_only: bool = None):
        super().__init__(claim_name=claim_name, read_only=read_only)


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

    nameservers: List[str]
    options: List[PodDNSConfigOption]
    searches: List[str]

    def __init__(self, nameservers: List[str] = None, options: List[PodDNSConfigOption] = None, searches: List[str] = None):
        super().__init__(nameservers=nameservers, options=options, searches=searches)


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
    supplemental_groups: List[int]
    sysctls: List[Sysctl]
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
        supplemental_groups: List[int] = None,
        sysctls: List[Sysctl] = None,
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
    max_skew: int
    topology_key: str
    when_unsatisfiable: str

    def __init__(
        self, label_selector: meta.LabelSelector = None, max_skew: int = None, topology_key: str = None, when_unsatisfiable: str = None
    ):
        super().__init__(label_selector=label_selector, max_skew=max_skew, topology_key=topology_key, when_unsatisfiable=when_unsatisfiable)


class SecretProjection(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    items: List[KeyToPath]
    name: str
    optional: bool

    def __init__(self, items: List[KeyToPath] = None, name: str = None, optional: bool = None):
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
    sources: List[VolumeProjection]

    def __init__(self, default_mode: int = None, sources: List[VolumeProjection] = None):
        super().__init__(default_mode=default_mode, sources=sources)


class RBDVolumeSource(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["image", "monitors"]

    fs_type: str
    image: str
    keyring: str
    monitors: List[str]
    pool: str
    read_only: bool
    secret_ref: LocalObjectReference
    user: str

    def __init__(
        self,
        fs_type: str = None,
        image: str = None,
        keyring: str = None,
        monitors: List[str] = None,
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
    items: List[KeyToPath]
    optional: bool
    secret_name: str

    def __init__(self, default_mode: int = None, items: List[KeyToPath] = None, optional: bool = None, secret_name: str = None):
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
    containers: List[Container]
    dns_config: PodDNSConfig
    dns_policy: str
    enable_service_links: bool
    ephemeral_containers: List[EphemeralContainer]
    host_aliases: List[HostAlias]
    host_ipc: bool
    host_network: bool
    host_pid: bool
    hostname: str
    image_pull_secrets: List[LocalObjectReference]
    init_containers: List[Container]
    node_name: str
    node_selector: Dict[str, str]
    overhead: Dict[str, Quantity]
    preemption_policy: str
    priority: int
    priority_class_name: str
    readiness_gates: List[PodReadinessGate]
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
    tolerations: List[Toleration]
    topology_spread_constraints: List[TopologySpreadConstraint]
    volumes: List[Volume]

    def __init__(
        self,
        active_deadline_seconds: int = None,
        affinity: Affinity = None,
        automount_service_account_token: bool = None,
        containers: List[Container] = None,
        dns_config: PodDNSConfig = None,
        dns_policy: str = None,
        enable_service_links: bool = None,
        ephemeral_containers: List[EphemeralContainer] = None,
        host_aliases: List[HostAlias] = None,
        host_ipc: bool = None,
        host_network: bool = None,
        host_pid: bool = None,
        hostname: str = None,
        image_pull_secrets: List[LocalObjectReference] = None,
        init_containers: List[Container] = None,
        node_name: str = None,
        node_selector: Dict[str, str] = None,
        overhead: Dict[str, Quantity] = None,
        preemption_policy: str = None,
        priority: int = None,
        priority_class_name: str = None,
        readiness_gates: List[PodReadinessGate] = None,
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
        tolerations: List[Toleration] = None,
        topology_spread_constraints: List[TopologySpreadConstraint] = None,
        volumes: List[Volume] = None,
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
            hostname=hostname,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            node_name=node_name,
            node_selector=node_selector,
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


class PodTemplateSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    metadata: meta.ObjectMeta
    spec: PodSpec

    def __init__(self, metadata: meta.ObjectMeta = None, spec: PodSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class ScopedResourceSelectorRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["operator", "scope_name"]

    operator: str
    scope_name: str
    values: List[str]

    def __init__(self, operator: str = None, scope_name: str = None, values: List[str] = None):
        super().__init__(operator=operator, scope_name=scope_name, values=values)


class ScopeSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    match_expressions: List[ScopedResourceSelectorRequirement]

    def __init__(self, match_expressions: List[ScopedResourceSelectorRequirement] = None):
        super().__init__(match_expressions=match_expressions)


class ResourceQuotaSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    hard: Dict[str, Quantity]
    scope_selector: ScopeSelector
    scopes: List[str]

    def __init__(self, hard: Dict[str, Quantity] = None, scope_selector: ScopeSelector = None, scopes: List[str] = None):
        super().__init__(hard=hard, scope_selector=scope_selector, scopes=scopes)


class ResourceQuota(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "ResourceQuota"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ResourceQuotaSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceQuotaSpec = None):
        super().__init__("v1", "ResourceQuota", name, namespace, metadata=metadata, spec=spec)


class Secret(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "Secret"
    _scope_ = "namespace"

    data: Dict[str, Base64]
    immutable: bool
    metadata: meta.ObjectMeta
    string_data: Dict[str, str]
    type: str

    def __init__(
        self,
        name: str,
        namespace: str = None,
        data: Dict[str, Base64] = None,
        immutable: bool = None,
        metadata: meta.ObjectMeta = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        super().__init__(
            "v1", "Secret", name, namespace, data=data, immutable=immutable, metadata=metadata, string_data=string_data, type=type
        )


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
    cluster_ips: List[str]
    external_ips: List[str]
    external_name: str
    external_traffic_policy: str
    health_check_node_port: int
    internal_traffic_policy: str
    ip_families: List[str]
    ip_family_policy: str
    load_balancer_class: str
    load_balancer_ip: str
    load_balancer_source_ranges: List[str]
    ports: List[ServicePort]
    publish_not_ready_addresses: bool
    selector: Dict[str, str]
    session_affinity: str
    session_affinity_config: SessionAffinityConfig
    type: str

    def __init__(
        self,
        allocate_load_balancer_node_ports: bool = None,
        cluster_ip: str = None,
        cluster_ips: List[str] = None,
        external_ips: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        internal_traffic_policy: str = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        load_balancer_class: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        ports: List[ServicePort] = None,
        publish_not_ready_addresses: bool = None,
        selector: Dict[str, str] = None,
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
    _kind_ = "Service"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ServiceSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ServiceSpec = None):
        super().__init__("v1", "Service", name, namespace, metadata=metadata, spec=spec)


class ServiceAccount(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "v1"
    _kind_ = "ServiceAccount"
    _scope_ = "namespace"

    automount_service_account_token: bool
    image_pull_secrets: List[LocalObjectReference]
    metadata: meta.ObjectMeta
    secrets: List[ObjectReference]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        automount_service_account_token: bool = None,
        image_pull_secrets: List[LocalObjectReference] = None,
        metadata: meta.ObjectMeta = None,
        secrets: List[ObjectReference] = None,
    ):
        super().__init__(
            "v1",
            "ServiceAccount",
            name,
            namespace,
            automount_service_account_token=automount_service_account_token,
            image_pull_secrets=image_pull_secrets,
            metadata=metadata,
            secrets=secrets,
        )


class TopologySelectorLabelRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    _required_ = ["key", "values"]

    key: str
    values: List[str]

    def __init__(self, key: str = None, values: List[str] = None):
        super().__init__(key=key, values=values)


class TopologySelectorTerm(KubernetesObject):
    __slots__ = ()

    _api_version_ = "v1"

    match_label_expressions: List[TopologySelectorLabelRequirement]

    def __init__(self, match_label_expressions: List[TopologySelectorLabelRequirement] = None):
        super().__init__(match_label_expressions=match_label_expressions)
