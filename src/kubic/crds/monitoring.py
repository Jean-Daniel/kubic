from typing import Dict, List

from .. import KubernetesApiResource, KubernetesObject
from .. import core, meta


class AdditionalAlertManagerConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class AdditionalAlertRelabelConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class AdditionalScrapeConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Alert(KubernetesObject):
    __slots__ = ()

    for_grace_period: str
    for_outage_tolerance: str
    resend_delay: str

    def __init__(
        self,
        for_grace_period: str = None,
        for_outage_tolerance: str = None,
        resend_delay: str = None,
    ):
        super().__init__(
            for_grace_period=for_grace_period,
            for_outage_tolerance=for_outage_tolerance,
            resend_delay=resend_delay,
        )


class ConfigMap(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Secret(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class CA(KubernetesObject):
    __slots__ = ()

    config_map: ConfigMap
    secret: Secret

    def __init__(self, config_map: ConfigMap = None, secret: Secret = None):
        super().__init__(config_map=config_map, secret=secret)


class Cert(KubernetesObject):
    __slots__ = ()

    config_map: ConfigMap
    secret: Secret

    def __init__(self, config_map: ConfigMap = None, secret: Secret = None):
        super().__init__(config_map=config_map, secret=secret)


class KeySecret(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class AlertmanagerTLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class Alertmanager(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "namespace", "port"]

    api_version: str
    bearer_token_file: str
    name: str
    namespace: str
    path_prefix: str
    port: core.IntOrString
    scheme: str
    timeout: str
    tls_config: AlertmanagerTLSConfig

    def __init__(
        self,
        api_version: str = None,
        bearer_token_file: str = None,
        name: str = None,
        namespace: str = None,
        path_prefix: str = None,
        port: core.IntOrString = None,
        scheme: str = None,
        timeout: str = None,
        tls_config: AlertmanagerTLSConfig = None,
    ):
        super().__init__(
            api_version=api_version,
            bearer_token_file=bearer_token_file,
            name=name,
            namespace=namespace,
            path_prefix=path_prefix,
            port=port,
            scheme=scheme,
            timeout=timeout,
            tls_config=tls_config,
        )


class Alerting(KubernetesObject):
    __slots__ = ()

    _required_ = ["alertmanagers"]

    alertmanagers: List[Alertmanager]

    def __init__(self, alertmanagers: List[Alertmanager] = None):
        super().__init__(alertmanagers=alertmanagers)


class PodMetadata(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    labels: Dict[str, str]
    name: str

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        name: str = None,
    ):
        super().__init__(annotations=annotations, labels=labels, name=name)


class Storage(KubernetesObject):
    __slots__ = ()

    disable_mount_sub_path: bool
    empty_dir: core.EmptyDirVolumeSource
    volume_claim_template: core.PersistentVolumeClaim

    def __init__(
        self,
        disable_mount_sub_path: bool = None,
        empty_dir: core.EmptyDirVolumeSource = None,
        volume_claim_template: core.PersistentVolumeClaim = None,
    ):
        super().__init__(
            disable_mount_sub_path=disable_mount_sub_path,
            empty_dir=empty_dir,
            volume_claim_template=volume_claim_template,
        )


class AlertmanagerSpec(KubernetesObject):
    __slots__ = ()

    additional_peers: List[str]
    affinity: core.Affinity
    alertmanager_config_namespace_selector: meta.LabelSelector
    alertmanager_config_selector: meta.LabelSelector
    base_image: str
    cluster_advertise_address: str
    cluster_gossip_interval: str
    cluster_peer_timeout: str
    cluster_pushpull_interval: str
    config_maps: List[str]
    config_secret: str
    containers: List[core.Container]
    external_url: str
    force_enable_cluster_mode: bool
    image: str
    image_pull_secrets: List[core.LocalObjectReference]
    init_containers: List[core.Container]
    listen_local: bool
    log_format: str
    log_level: str
    node_selector: Dict[str, str]
    paused: bool
    pod_metadata: PodMetadata
    port_name: str
    priority_class_name: str
    replicas: int
    resources: core.ResourceRequirements
    retention: str
    route_prefix: str
    secrets: List[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    sha: str
    storage: Storage
    tag: str
    tolerations: List[core.Toleration]
    topology_spread_constraints: List[core.TopologySpreadConstraint]
    version: str
    volume_mounts: List[core.VolumeMount]
    volumes: List[core.Volume]

    def __init__(
        self,
        additional_peers: List[str] = None,
        affinity: core.Affinity = None,
        alertmanager_config_namespace_selector: meta.LabelSelector = None,
        alertmanager_config_selector: meta.LabelSelector = None,
        base_image: str = None,
        cluster_advertise_address: str = None,
        cluster_gossip_interval: str = None,
        cluster_peer_timeout: str = None,
        cluster_pushpull_interval: str = None,
        config_maps: List[str] = None,
        config_secret: str = None,
        containers: List[core.Container] = None,
        external_url: str = None,
        force_enable_cluster_mode: bool = None,
        image: str = None,
        image_pull_secrets: List[core.LocalObjectReference] = None,
        init_containers: List[core.Container] = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        node_selector: Dict[str, str] = None,
        paused: bool = None,
        pod_metadata: PodMetadata = None,
        port_name: str = None,
        priority_class_name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        retention: str = None,
        route_prefix: str = None,
        secrets: List[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        sha: str = None,
        storage: Storage = None,
        tag: str = None,
        tolerations: List[core.Toleration] = None,
        topology_spread_constraints: List[core.TopologySpreadConstraint] = None,
        version: str = None,
        volume_mounts: List[core.VolumeMount] = None,
        volumes: List[core.Volume] = None,
    ):
        super().__init__(
            additional_peers=additional_peers,
            affinity=affinity,
            alertmanager_config_namespace_selector=alertmanager_config_namespace_selector,
            alertmanager_config_selector=alertmanager_config_selector,
            base_image=base_image,
            cluster_advertise_address=cluster_advertise_address,
            cluster_gossip_interval=cluster_gossip_interval,
            cluster_peer_timeout=cluster_peer_timeout,
            cluster_pushpull_interval=cluster_pushpull_interval,
            config_maps=config_maps,
            config_secret=config_secret,
            containers=containers,
            external_url=external_url,
            force_enable_cluster_mode=force_enable_cluster_mode,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            listen_local=listen_local,
            log_format=log_format,
            log_level=log_level,
            node_selector=node_selector,
            paused=paused,
            pod_metadata=pod_metadata,
            port_name=port_name,
            priority_class_name=priority_class_name,
            replicas=replicas,
            resources=resources,
            retention=retention,
            route_prefix=route_prefix,
            secrets=secrets,
            security_context=security_context,
            service_account_name=service_account_name,
            sha=sha,
            storage=storage,
            tag=tag,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            version=version,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class AlertmanagersConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Password(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Username(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class BasicAuth(KubernetesObject):
    __slots__ = ()

    password: Password
    username: Username

    def __init__(self, password: Password = None, username: Username = None):
        super().__init__(password=password, username=username)


class ApiserverConfigTLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class ApiserverConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["host"]

    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    host: str
    tls_config: ApiserverConfigTLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        host: str = None,
        tls_config: ApiserverConfigTLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            bearer_token_file=bearer_token_file,
            host=host,
            tls_config=tls_config,
        )


class ArbitraryFSAccessThroughSM(KubernetesObject):
    __slots__ = ()

    deny: bool

    def __init__(self, deny: bool = None):
        super().__init__(deny=deny)


class BearerTokenSecret(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Capabilitie(KubernetesObject):
    __slots__ = ()

    add: List[str]
    drop: List[str]

    def __init__(self, add: List[str] = None, drop: List[str] = None):
        super().__init__(add=add, drop=drop)


class ConfigMapKeyRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class ConfigMapRef(KubernetesObject):
    __slots__ = ()

    name: str
    optional: bool

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class FieldRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["field_path"]

    api_version: str
    field_path: str

    def __init__(self, api_version: str = None, field_path: str = None):
        super().__init__(api_version=api_version, field_path=field_path)


class ResourceFieldRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["resource"]

    container_name: str
    divisor: core.IntOrString
    resource: str

    def __init__(
        self,
        container_name: str = None,
        divisor: core.IntOrString = None,
        resource: str = None,
    ):
        super().__init__(
            container_name=container_name, divisor=divisor, resource=resource
        )


class SecretKeyRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class ValueFrom(KubernetesObject):
    __slots__ = ()

    config_map_key_ref: ConfigMapKeyRef
    field_ref: FieldRef
    resource_field_ref: ResourceFieldRef
    secret_key_ref: SecretKeyRef

    def __init__(
        self,
        config_map_key_ref: ConfigMapKeyRef = None,
        field_ref: FieldRef = None,
        resource_field_ref: ResourceFieldRef = None,
        secret_key_ref: SecretKeyRef = None,
    ):
        super().__init__(
            config_map_key_ref=config_map_key_ref,
            field_ref=field_ref,
            resource_field_ref=resource_field_ref,
            secret_key_ref=secret_key_ref,
        )


class ENV(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    name: str
    value: str
    value_from: ValueFrom

    def __init__(
        self, name: str = None, value: str = None, value_from: ValueFrom = None
    ):
        super().__init__(name=name, value=value, value_from=value_from)


class SecretRef(KubernetesObject):
    __slots__ = ()

    name: str
    optional: bool

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class EnvFrom(KubernetesObject):
    __slots__ = ()

    config_map_ref: ConfigMapRef
    prefix: str
    secret_ref: SecretRef

    def __init__(
        self,
        config_map_ref: ConfigMapRef = None,
        prefix: str = None,
        secret_ref: SecretRef = None,
    ):
        super().__init__(
            config_map_ref=config_map_ref, prefix=prefix, secret_ref=secret_ref
        )


class Exec(KubernetesObject):
    __slots__ = ()

    command: List[str]

    def __init__(self, command: List[str] = None):
        super().__init__(command=command)


class HttpHeader(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "value"]

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class HttpGet(KubernetesObject):
    __slots__ = ()

    _required_ = ["port"]

    host: str
    http_headers: List[HttpHeader]
    path: str
    port: core.IntOrString
    scheme: str

    def __init__(
        self,
        host: str = None,
        http_headers: List[HttpHeader] = None,
        path: str = None,
        port: core.IntOrString = None,
        scheme: str = None,
    ):
        super().__init__(
            host=host, http_headers=http_headers, path=path, port=port, scheme=scheme
        )


class TcpSocket(KubernetesObject):
    __slots__ = ()

    _required_ = ["port"]

    host: str
    port: core.IntOrString

    def __init__(self, host: str = None, port: core.IntOrString = None):
        super().__init__(host=host, port=port)


class PostStart(KubernetesObject):
    __slots__ = ()

    exec: Exec
    http_get: HttpGet
    tcp_socket: TcpSocket

    def __init__(
        self, exec: Exec = None, http_get: HttpGet = None, tcp_socket: TcpSocket = None
    ):
        super().__init__(exec=exec, http_get=http_get, tcp_socket=tcp_socket)


class PreStop(KubernetesObject):
    __slots__ = ()

    exec: Exec
    http_get: HttpGet
    tcp_socket: TcpSocket

    def __init__(
        self, exec: Exec = None, http_get: HttpGet = None, tcp_socket: TcpSocket = None
    ):
        super().__init__(exec=exec, http_get=http_get, tcp_socket=tcp_socket)


class Lifecycle(KubernetesObject):
    __slots__ = ()

    post_start: PostStart
    pre_stop: PreStop

    def __init__(self, post_start: PostStart = None, pre_stop: PreStop = None):
        super().__init__(post_start=post_start, pre_stop=pre_stop)


class LivenessProbe(KubernetesObject):
    __slots__ = ()

    exec: Exec
    failure_threshold: int
    http_get: HttpGet
    initial_delay_seconds: int
    period_seconds: int
    success_threshold: int
    tcp_socket: TcpSocket
    timeout_seconds: int

    def __init__(
        self,
        exec: Exec = None,
        failure_threshold: int = None,
        http_get: HttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: TcpSocket = None,
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
            timeout_seconds=timeout_seconds,
        )


class Port(KubernetesObject):
    __slots__ = ()

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

    def __init__(
        self,
        container_port: int = None,
        host_ip: str = None,
        host_port: int = None,
        name: str = None,
        protocol: str = None,
    ):
        super().__init__(
            container_port=container_port,
            host_ip=host_ip,
            host_port=host_port,
            name=name,
            protocol=protocol,
        )


class ReadinessProbe(KubernetesObject):
    __slots__ = ()

    exec: Exec
    failure_threshold: int
    http_get: HttpGet
    initial_delay_seconds: int
    period_seconds: int
    success_threshold: int
    tcp_socket: TcpSocket
    timeout_seconds: int

    def __init__(
        self,
        exec: Exec = None,
        failure_threshold: int = None,
        http_get: HttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: TcpSocket = None,
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
            timeout_seconds=timeout_seconds,
        )


class Resource(KubernetesObject):
    __slots__ = ()

    limits: Dict[str, core.IntOrString]
    requests: Dict[str, core.IntOrString]

    def __init__(
        self,
        limits: Dict[str, core.IntOrString] = None,
        requests: Dict[str, core.IntOrString] = None,
    ):
        super().__init__(limits=limits, requests=requests)


class SeLinuxOption(KubernetesObject):
    __slots__ = ()

    level: str
    role: str
    type: str
    user: str

    def __init__(
        self, level: str = None, role: str = None, type: str = None, user: str = None
    ):
        super().__init__(level=level, role=role, type=type, user=user)


class WindowsOption(KubernetesObject):
    __slots__ = ()

    gmsa_credential_spec: str
    gmsa_credential_spec_name: str
    run_as_user_name: str

    def __init__(
        self,
        gmsa_credential_spec: str = None,
        gmsa_credential_spec_name: str = None,
        run_as_user_name: str = None,
    ):
        super().__init__(
            gmsa_credential_spec=gmsa_credential_spec,
            gmsa_credential_spec_name=gmsa_credential_spec_name,
            run_as_user_name=run_as_user_name,
        )


class SecurityContext(KubernetesObject):
    __slots__ = ()

    allow_privilege_escalation: bool
    capabilities: Capabilitie
    privileged: bool
    proc_mount: str
    read_only_root_filesystem: bool
    run_as_group: int
    run_as_non_root: bool
    run_as_user: int
    se_linux_options: SeLinuxOption
    windows_options: WindowsOption

    def __init__(
        self,
        allow_privilege_escalation: bool = None,
        capabilities: Capabilitie = None,
        privileged: bool = None,
        proc_mount: str = None,
        read_only_root_filesystem: bool = None,
        run_as_group: int = None,
        run_as_non_root: bool = None,
        run_as_user: int = None,
        se_linux_options: SeLinuxOption = None,
        windows_options: WindowsOption = None,
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
            windows_options=windows_options,
        )


class StartupProbe(KubernetesObject):
    __slots__ = ()

    exec: Exec
    failure_threshold: int
    http_get: HttpGet
    initial_delay_seconds: int
    period_seconds: int
    success_threshold: int
    tcp_socket: TcpSocket
    timeout_seconds: int

    def __init__(
        self,
        exec: Exec = None,
        failure_threshold: int = None,
        http_get: HttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: TcpSocket = None,
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
            timeout_seconds=timeout_seconds,
        )


class VolumeDevice(KubernetesObject):
    __slots__ = ()

    _required_ = ["device_path", "name"]

    device_path: str
    name: str

    def __init__(self, device_path: str = None, name: str = None):
        super().__init__(device_path=device_path, name=name)


class VolumeMount(KubernetesObject):
    __slots__ = ()

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

    _required_ = ["name"]

    args: List[str]
    command: List[str]
    env: List[ENV]
    env_from: List[EnvFrom]
    image: str
    image_pull_policy: str
    lifecycle: Lifecycle
    liveness_probe: LivenessProbe
    name: str
    ports: List[Port]
    readiness_probe: ReadinessProbe
    resources: Resource
    security_context: SecurityContext
    startup_probe: StartupProbe
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
        env: List[ENV] = None,
        env_from: List[EnvFrom] = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle: Lifecycle = None,
        liveness_probe: LivenessProbe = None,
        name: str = None,
        ports: List[Port] = None,
        readiness_probe: ReadinessProbe = None,
        resources: Resource = None,
        security_context: SecurityContext = None,
        startup_probe: StartupProbe = None,
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


class MetricRelabeling(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: List[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: List[str] = None,
        target_label: str = None,
    ):
        super().__init__(
            action=action,
            modulus=modulus,
            regex=regex,
            replacement=replacement,
            separator=separator,
            source_labels=source_labels,
            target_label=target_label,
        )


class Relabeling(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: List[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: List[str] = None,
        target_label: str = None,
    ):
        super().__init__(
            action=action,
            modulus=modulus,
            regex=regex,
            replacement=replacement,
            separator=separator,
            source_labels=source_labels,
            target_label=target_label,
        )


class EndpointTLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class Endpoint(KubernetesObject):
    __slots__ = ()

    basic_auth: BasicAuth
    bearer_token_file: str
    bearer_token_secret: BearerTokenSecret
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    metric_relabelings: List[MetricRelabeling]
    params: Dict[str, List[str]]
    path: str
    port: str
    proxy_url: str
    relabelings: List[Relabeling]
    scheme: str
    scrape_timeout: str
    target_port: core.IntOrString
    tls_config: EndpointTLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_file: str = None,
        bearer_token_secret: BearerTokenSecret = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        metric_relabelings: List[MetricRelabeling] = None,
        params: Dict[str, List[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabelings: List[Relabeling] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        target_port: core.IntOrString = None,
        tls_config: EndpointTLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_file=bearer_token_file,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            metric_relabelings=metric_relabelings,
            params=params,
            path=path,
            port=port,
            proxy_url=proxy_url,
            relabelings=relabelings,
            scheme=scheme,
            scrape_timeout=scrape_timeout,
            target_port=target_port,
            tls_config=tls_config,
        )


class GroupRule(KubernetesObject):
    __slots__ = ()

    _required_ = ["expr"]

    _revfield_names_ = {
        "for": "for_",
    }

    alert: str
    annotations: Dict[str, str]
    expr: core.IntOrString
    for_: str
    labels: Dict[str, str]
    record: str

    def __init__(
        self,
        alert: str = None,
        annotations: Dict[str, str] = None,
        expr: core.IntOrString = None,
        for_: str = None,
        labels: Dict[str, str] = None,
        record: str = None,
    ):
        super().__init__(
            alert=alert,
            annotations=annotations,
            expr=expr,
            for_=for_,
            labels=labels,
            record=record,
        )


class Group(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "rules"]

    _field_names_ = {
        "partial_response_strategy": "partial_response_strategy",
    }

    interval: str
    name: str
    partial_response_strategy: str
    rules: List[GroupRule]

    def __init__(
        self,
        interval: str = None,
        name: str = None,
        partial_response_strategy: str = None,
        rules: List[GroupRule] = None,
    ):
        super().__init__(
            interval=interval,
            name=name,
            partial_response_strategy=partial_response_strategy,
            rules=rules,
        )


class GrpcServerTlsConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class NamespaceSelector(KubernetesObject):
    __slots__ = ()

    any: bool
    match_names: List[str]

    def __init__(self, any: bool = None, match_names: List[str] = None):
        super().__init__(any=any, match_names=match_names)


class RelabelingConfig(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: List[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: List[str] = None,
        target_label: str = None,
    ):
        super().__init__(
            action=action,
            modulus=modulus,
            regex=regex,
            replacement=replacement,
            separator=separator,
            source_labels=source_labels,
            target_label=target_label,
        )


class Ingress(KubernetesObject):
    __slots__ = ()

    namespace_selector: NamespaceSelector
    relabeling_configs: List[RelabelingConfig]
    selector: meta.LabelSelector

    def __init__(
        self,
        namespace_selector: NamespaceSelector = None,
        relabeling_configs: List[RelabelingConfig] = None,
        selector: meta.LabelSelector = None,
    ):
        super().__init__(
            namespace_selector=namespace_selector,
            relabeling_configs=relabeling_configs,
            selector=selector,
        )


class ObjectStorageConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class PodMetricsEndpointTLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    cert: Cert
    insecure_skip_verify: bool
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        cert: Cert = None,
        insecure_skip_verify: bool = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            cert=cert,
            insecure_skip_verify=insecure_skip_verify,
            key_secret=key_secret,
            server_name=server_name,
        )


class PodMetricsEndpoint(KubernetesObject):
    __slots__ = ()

    basic_auth: BasicAuth
    bearer_token_secret: BearerTokenSecret
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    metric_relabelings: List[MetricRelabeling]
    params: Dict[str, List[str]]
    path: str
    port: str
    proxy_url: str
    relabelings: List[Relabeling]
    scheme: str
    scrape_timeout: str
    target_port: core.IntOrString
    tls_config: PodMetricsEndpointTLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_secret: BearerTokenSecret = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        metric_relabelings: List[MetricRelabeling] = None,
        params: Dict[str, List[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabelings: List[Relabeling] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        target_port: core.IntOrString = None,
        tls_config: PodMetricsEndpointTLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            metric_relabelings=metric_relabelings,
            params=params,
            path=path,
            port=port,
            proxy_url=proxy_url,
            relabelings=relabelings,
            scheme=scheme,
            scrape_timeout=scrape_timeout,
            target_port=target_port,
            tls_config=tls_config,
        )


class PodMonitorSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["pod_metrics_endpoints", "selector"]

    job_label: str
    namespace_selector: NamespaceSelector
    pod_metrics_endpoints: List[PodMetricsEndpoint]
    pod_target_labels: List[str]
    sample_limit: int
    selector: meta.LabelSelector
    target_limit: int

    def __init__(
        self,
        job_label: str = None,
        namespace_selector: NamespaceSelector = None,
        pod_metrics_endpoints: List[PodMetricsEndpoint] = None,
        pod_target_labels: List[str] = None,
        sample_limit: int = None,
        selector: meta.LabelSelector = None,
        target_limit: int = None,
    ):
        super().__init__(
            job_label=job_label,
            namespace_selector=namespace_selector,
            pod_metrics_endpoints=pod_metrics_endpoints,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
            target_limit=target_limit,
        )


class PodMonitor(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PodMonitorSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: PodMonitorSpec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "PodMonitor",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class Prober(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    path: str
    scheme: str
    url: str

    def __init__(self, path: str = None, scheme: str = None, url: str = None):
        super().__init__(path=path, scheme=scheme, url=url)


class StaticConfig(KubernetesObject):
    __slots__ = ()

    labels: Dict[str, str]
    static: List[str]

    def __init__(self, labels: Dict[str, str] = None, static: List[str] = None):
        super().__init__(labels=labels, static=static)


class Target(KubernetesObject):
    __slots__ = ()

    ingress: Ingress
    static_config: StaticConfig

    def __init__(self, ingress: Ingress = None, static_config: StaticConfig = None):
        super().__init__(ingress=ingress, static_config=static_config)


class ProbeSpec(KubernetesObject):
    __slots__ = ()

    interval: str
    job_name: str
    module: str
    prober: Prober
    scrape_timeout: str
    targets: Target

    def __init__(
        self,
        interval: str = None,
        job_name: str = None,
        module: str = None,
        prober: Prober = None,
        scrape_timeout: str = None,
        targets: Target = None,
    ):
        super().__init__(
            interval=interval,
            job_name=job_name,
            module=module,
            prober=prober,
            scrape_timeout=scrape_timeout,
            targets=targets,
        )


class Probe(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ProbeSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: ProbeSpec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "Probe",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class PrometheusRulesExcludedFromEnforce(KubernetesObject):
    __slots__ = ()

    _required_ = ["rule_name", "rule_namespace"]

    rule_name: str
    rule_namespace: str

    def __init__(self, rule_name: str = None, rule_namespace: str = None):
        super().__init__(rule_name=rule_name, rule_namespace=rule_namespace)


class Query(KubernetesObject):
    __slots__ = ()

    lookback_delta: str
    max_concurrency: int
    max_samples: int
    timeout: str

    def __init__(
        self,
        lookback_delta: str = None,
        max_concurrency: int = None,
        max_samples: int = None,
        timeout: str = None,
    ):
        super().__init__(
            lookback_delta=lookback_delta,
            max_concurrency=max_concurrency,
            max_samples=max_samples,
            timeout=timeout,
        )


class RemoteReadTLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class RemoteRead(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    name: str
    proxy_url: str
    read_recent: bool
    remote_timeout: str
    required_matchers: Dict[str, str]
    tls_config: RemoteReadTLSConfig
    url: str

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        name: str = None,
        proxy_url: str = None,
        read_recent: bool = None,
        remote_timeout: str = None,
        required_matchers: Dict[str, str] = None,
        tls_config: RemoteReadTLSConfig = None,
        url: str = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            bearer_token_file=bearer_token_file,
            name=name,
            proxy_url=proxy_url,
            read_recent=read_recent,
            remote_timeout=remote_timeout,
            required_matchers=required_matchers,
            tls_config=tls_config,
            url=url,
        )


class QueueConfig(KubernetesObject):
    __slots__ = ()

    batch_send_deadline: str
    capacity: int
    max_backoff: str
    max_retries: int
    max_samples_per_send: int
    max_shards: int
    min_backoff: str
    min_shards: int

    def __init__(
        self,
        batch_send_deadline: str = None,
        capacity: int = None,
        max_backoff: str = None,
        max_retries: int = None,
        max_samples_per_send: int = None,
        max_shards: int = None,
        min_backoff: str = None,
        min_shards: int = None,
    ):
        super().__init__(
            batch_send_deadline=batch_send_deadline,
            capacity=capacity,
            max_backoff=max_backoff,
            max_retries=max_retries,
            max_samples_per_send=max_samples_per_send,
            max_shards=max_shards,
            min_backoff=min_backoff,
            min_shards=min_shards,
        )


class RemoteWriteTLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: KeySecret
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: KeySecret = None,
        server_name: str = None,
    ):
        super().__init__(
            ca=ca,
            ca_file=ca_file,
            cert=cert,
            cert_file=cert_file,
            insecure_skip_verify=insecure_skip_verify,
            key_file=key_file,
            key_secret=key_secret,
            server_name=server_name,
        )


class WriteRelabelConfig(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: List[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: List[str] = None,
        target_label: str = None,
    ):
        super().__init__(
            action=action,
            modulus=modulus,
            regex=regex,
            replacement=replacement,
            separator=separator,
            source_labels=source_labels,
            target_label=target_label,
        )


class RemoteWrite(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    name: str
    proxy_url: str
    queue_config: QueueConfig
    remote_timeout: str
    tls_config: RemoteWriteTLSConfig
    url: str
    write_relabel_configs: List[WriteRelabelConfig]

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        name: str = None,
        proxy_url: str = None,
        queue_config: QueueConfig = None,
        remote_timeout: str = None,
        tls_config: RemoteWriteTLSConfig = None,
        url: str = None,
        write_relabel_configs: List[WriteRelabelConfig] = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            bearer_token_file=bearer_token_file,
            name=name,
            proxy_url=proxy_url,
            queue_config=queue_config,
            remote_timeout=remote_timeout,
            tls_config=tls_config,
            url=url,
            write_relabel_configs=write_relabel_configs,
        )


class PrometheusSpecRule(KubernetesObject):
    __slots__ = ()

    alert: Alert

    def __init__(self, alert: Alert = None):
        super().__init__(alert=alert)


class TracingConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class Thano(KubernetesObject):
    __slots__ = ()

    base_image: str
    grpc_server_tls_config: GrpcServerTlsConfig
    image: str
    listen_local: bool
    log_format: str
    log_level: str
    min_time: str
    object_storage_config: ObjectStorageConfig
    object_storage_config_file: str
    resources: core.ResourceRequirements
    sha: str
    tag: str
    tracing_config: TracingConfig
    tracing_config_file: str
    version: str

    def __init__(
        self,
        base_image: str = None,
        grpc_server_tls_config: GrpcServerTlsConfig = None,
        image: str = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        min_time: str = None,
        object_storage_config: ObjectStorageConfig = None,
        object_storage_config_file: str = None,
        resources: core.ResourceRequirements = None,
        sha: str = None,
        tag: str = None,
        tracing_config: TracingConfig = None,
        tracing_config_file: str = None,
        version: str = None,
    ):
        super().__init__(
            base_image=base_image,
            grpc_server_tls_config=grpc_server_tls_config,
            image=image,
            listen_local=listen_local,
            log_format=log_format,
            log_level=log_level,
            min_time=min_time,
            object_storage_config=object_storage_config,
            object_storage_config_file=object_storage_config_file,
            resources=resources,
            sha=sha,
            tag=tag,
            tracing_config=tracing_config,
            tracing_config_file=tracing_config_file,
            version=version,
        )


class WEB(KubernetesObject):
    __slots__ = ()

    page_title: str

    def __init__(self, page_title: str = None):
        super().__init__(page_title=page_title)


class PrometheusSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "arbitrary_fs_access_through_sms": "arbitraryFSAccessThroughSMs",
        "enable_admin_api": "enableAdminAPI",
    }
    _revfield_names_ = {
        "arbitraryFSAccessThroughSMs": "arbitrary_fs_access_through_sms",
        "enableAdminAPI": "enable_admin_api",
    }

    additional_alert_manager_configs: AdditionalAlertManagerConfig
    additional_alert_relabel_configs: AdditionalAlertRelabelConfig
    additional_scrape_configs: AdditionalScrapeConfig
    affinity: core.Affinity
    alerting: Alerting
    allow_overlapping_blocks: bool
    apiserver_config: ApiserverConfig
    arbitrary_fs_access_through_sms: ArbitraryFSAccessThroughSM
    base_image: str
    config_maps: List[str]
    containers: List[core.Container]
    disable_compaction: bool
    enable_admin_api: bool
    enforced_namespace_label: str
    enforced_sample_limit: int
    enforced_target_limit: int
    evaluation_interval: str
    external_labels: Dict[str, str]
    external_url: str
    ignore_namespace_selectors: bool
    image: str
    image_pull_secrets: List[core.LocalObjectReference]
    init_containers: List[core.Container]
    listen_local: bool
    log_format: str
    log_level: str
    node_selector: Dict[str, str]
    override_honor_labels: bool
    override_honor_timestamps: bool
    paused: bool
    pod_metadata: PodMetadata
    pod_monitor_namespace_selector: meta.LabelSelector
    pod_monitor_selector: meta.LabelSelector
    port_name: str
    priority_class_name: str
    probe_namespace_selector: meta.LabelSelector
    probe_selector: meta.LabelSelector
    prometheus_external_label_name: str
    prometheus_rules_excluded_from_enforce: List[PrometheusRulesExcludedFromEnforce]
    query: Query
    query_log_file: str
    remote_read: List[RemoteRead]
    remote_write: List[RemoteWrite]
    replica_external_label_name: str
    replicas: int
    resources: core.ResourceRequirements
    retention: str
    retention_size: str
    route_prefix: str
    rule_namespace_selector: meta.LabelSelector
    rule_selector: meta.LabelSelector
    rules: PrometheusSpecRule
    scrape_interval: str
    scrape_timeout: str
    secrets: List[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    service_monitor_namespace_selector: meta.LabelSelector
    service_monitor_selector: meta.LabelSelector
    sha: str
    shards: int
    storage: Storage
    tag: str
    thanos: Thano
    tolerations: List[core.Toleration]
    topology_spread_constraints: List[core.TopologySpreadConstraint]
    version: str
    volume_mounts: List[core.VolumeMount]
    volumes: List[core.Volume]
    wal_compression: bool
    web: WEB

    def __init__(
        self,
        additional_alert_manager_configs: AdditionalAlertManagerConfig = None,
        additional_alert_relabel_configs: AdditionalAlertRelabelConfig = None,
        additional_scrape_configs: AdditionalScrapeConfig = None,
        affinity: core.Affinity = None,
        alerting: Alerting = None,
        allow_overlapping_blocks: bool = None,
        apiserver_config: ApiserverConfig = None,
        arbitrary_fs_access_through_sms: ArbitraryFSAccessThroughSM = None,
        base_image: str = None,
        config_maps: List[str] = None,
        containers: List[core.Container] = None,
        disable_compaction: bool = None,
        enable_admin_api: bool = None,
        enforced_namespace_label: str = None,
        enforced_sample_limit: int = None,
        enforced_target_limit: int = None,
        evaluation_interval: str = None,
        external_labels: Dict[str, str] = None,
        external_url: str = None,
        ignore_namespace_selectors: bool = None,
        image: str = None,
        image_pull_secrets: List[core.LocalObjectReference] = None,
        init_containers: List[core.Container] = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        node_selector: Dict[str, str] = None,
        override_honor_labels: bool = None,
        override_honor_timestamps: bool = None,
        paused: bool = None,
        pod_metadata: PodMetadata = None,
        pod_monitor_namespace_selector: meta.LabelSelector = None,
        pod_monitor_selector: meta.LabelSelector = None,
        port_name: str = None,
        priority_class_name: str = None,
        probe_namespace_selector: meta.LabelSelector = None,
        probe_selector: meta.LabelSelector = None,
        prometheus_external_label_name: str = None,
        prometheus_rules_excluded_from_enforce: List[
            PrometheusRulesExcludedFromEnforce
        ] = None,
        query: Query = None,
        query_log_file: str = None,
        remote_read: List[RemoteRead] = None,
        remote_write: List[RemoteWrite] = None,
        replica_external_label_name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        retention: str = None,
        retention_size: str = None,
        route_prefix: str = None,
        rule_namespace_selector: meta.LabelSelector = None,
        rule_selector: meta.LabelSelector = None,
        rules: PrometheusSpecRule = None,
        scrape_interval: str = None,
        scrape_timeout: str = None,
        secrets: List[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        service_monitor_namespace_selector: meta.LabelSelector = None,
        service_monitor_selector: meta.LabelSelector = None,
        sha: str = None,
        shards: int = None,
        storage: Storage = None,
        tag: str = None,
        thanos: Thano = None,
        tolerations: List[core.Toleration] = None,
        topology_spread_constraints: List[core.TopologySpreadConstraint] = None,
        version: str = None,
        volume_mounts: List[core.VolumeMount] = None,
        volumes: List[core.Volume] = None,
        wal_compression: bool = None,
        web: WEB = None,
    ):
        super().__init__(
            additional_alert_manager_configs=additional_alert_manager_configs,
            additional_alert_relabel_configs=additional_alert_relabel_configs,
            additional_scrape_configs=additional_scrape_configs,
            affinity=affinity,
            alerting=alerting,
            allow_overlapping_blocks=allow_overlapping_blocks,
            apiserver_config=apiserver_config,
            arbitrary_fs_access_through_sms=arbitrary_fs_access_through_sms,
            base_image=base_image,
            config_maps=config_maps,
            containers=containers,
            disable_compaction=disable_compaction,
            enable_admin_api=enable_admin_api,
            enforced_namespace_label=enforced_namespace_label,
            enforced_sample_limit=enforced_sample_limit,
            enforced_target_limit=enforced_target_limit,
            evaluation_interval=evaluation_interval,
            external_labels=external_labels,
            external_url=external_url,
            ignore_namespace_selectors=ignore_namespace_selectors,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            listen_local=listen_local,
            log_format=log_format,
            log_level=log_level,
            node_selector=node_selector,
            override_honor_labels=override_honor_labels,
            override_honor_timestamps=override_honor_timestamps,
            paused=paused,
            pod_metadata=pod_metadata,
            pod_monitor_namespace_selector=pod_monitor_namespace_selector,
            pod_monitor_selector=pod_monitor_selector,
            port_name=port_name,
            priority_class_name=priority_class_name,
            probe_namespace_selector=probe_namespace_selector,
            probe_selector=probe_selector,
            prometheus_external_label_name=prometheus_external_label_name,
            prometheus_rules_excluded_from_enforce=prometheus_rules_excluded_from_enforce,
            query=query,
            query_log_file=query_log_file,
            remote_read=remote_read,
            remote_write=remote_write,
            replica_external_label_name=replica_external_label_name,
            replicas=replicas,
            resources=resources,
            retention=retention,
            retention_size=retention_size,
            route_prefix=route_prefix,
            rule_namespace_selector=rule_namespace_selector,
            rule_selector=rule_selector,
            rules=rules,
            scrape_interval=scrape_interval,
            scrape_timeout=scrape_timeout,
            secrets=secrets,
            security_context=security_context,
            service_account_name=service_account_name,
            service_monitor_namespace_selector=service_monitor_namespace_selector,
            service_monitor_selector=service_monitor_selector,
            sha=sha,
            shards=shards,
            storage=storage,
            tag=tag,
            thanos=thanos,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            version=version,
            volume_mounts=volume_mounts,
            volumes=volumes,
            wal_compression=wal_compression,
            web=web,
        )


class Status(KubernetesObject):
    __slots__ = ()

    _required_ = [
        "available_replicas",
        "paused",
        "replicas",
        "unavailable_replicas",
        "updated_replicas",
    ]

    available_replicas: int
    paused: bool
    replicas: int
    unavailable_replicas: int
    updated_replicas: int

    def __init__(
        self,
        available_replicas: int = None,
        paused: bool = None,
        replicas: int = None,
        unavailable_replicas: int = None,
        updated_replicas: int = None,
    ):
        super().__init__(
            available_replicas=available_replicas,
            paused=paused,
            replicas=replicas,
            unavailable_replicas=unavailable_replicas,
            updated_replicas=updated_replicas,
        )


class Prometheus(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PrometheusSpec
    status: Status

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: PrometheusSpec = None,
        status: Status = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "Prometheus",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
            status=status,
        )


class PrometheusRuleSpec(KubernetesObject):
    __slots__ = ()

    groups: List[Group]

    def __init__(self, groups: List[Group] = None):
        super().__init__(groups=groups)


class PrometheusRule(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PrometheusRuleSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: PrometheusRuleSpec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "PrometheusRule",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class QueryConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    name: str
    optional: bool

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class ServiceMonitorSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["endpoints", "selector"]

    endpoints: List[Endpoint]
    job_label: str
    namespace_selector: NamespaceSelector
    pod_target_labels: List[str]
    sample_limit: int
    selector: meta.LabelSelector
    target_labels: List[str]
    target_limit: int

    def __init__(
        self,
        endpoints: List[Endpoint] = None,
        job_label: str = None,
        namespace_selector: NamespaceSelector = None,
        pod_target_labels: List[str] = None,
        sample_limit: int = None,
        selector: meta.LabelSelector = None,
        target_labels: List[str] = None,
        target_limit: int = None,
    ):
        super().__init__(
            endpoints=endpoints,
            job_label=job_label,
            namespace_selector=namespace_selector,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
            target_labels=target_labels,
            target_limit=target_limit,
        )


class ServiceMonitor(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ServiceMonitorSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: ServiceMonitorSpec = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "ServiceMonitor",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class ThanosRulerSpec(KubernetesObject):
    __slots__ = ()

    affinity: core.Affinity
    alert_drop_labels: List[str]
    alert_query_url: str
    alertmanagers_config: AlertmanagersConfig
    alertmanagers_url: List[str]
    containers: List[Container]
    enforced_namespace_label: str
    evaluation_interval: str
    external_prefix: str
    grpc_server_tls_config: GrpcServerTlsConfig
    image: str
    image_pull_secrets: List[core.LocalObjectReference]
    init_containers: List[core.Container]
    labels: Dict[str, str]
    listen_local: bool
    log_format: str
    log_level: str
    node_selector: Dict[str, str]
    object_storage_config: ObjectStorageConfig
    object_storage_config_file: str
    paused: bool
    pod_metadata: PodMetadata
    port_name: str
    priority_class_name: str
    prometheus_rules_excluded_from_enforce: List[PrometheusRulesExcludedFromEnforce]
    query_config: QueryConfig
    query_endpoints: List[str]
    replicas: int
    resources: core.ResourceRequirements
    retention: str
    route_prefix: str
    rule_namespace_selector: meta.LabelSelector
    rule_selector: meta.LabelSelector
    security_context: core.PodSecurityContext
    service_account_name: str
    storage: Storage
    tolerations: List[core.Toleration]
    topology_spread_constraints: List[core.TopologySpreadConstraint]
    tracing_config: TracingConfig
    volumes: List[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        alert_drop_labels: List[str] = None,
        alert_query_url: str = None,
        alertmanagers_config: AlertmanagersConfig = None,
        alertmanagers_url: List[str] = None,
        containers: List[Container] = None,
        enforced_namespace_label: str = None,
        evaluation_interval: str = None,
        external_prefix: str = None,
        grpc_server_tls_config: GrpcServerTlsConfig = None,
        image: str = None,
        image_pull_secrets: List[core.LocalObjectReference] = None,
        init_containers: List[core.Container] = None,
        labels: Dict[str, str] = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        node_selector: Dict[str, str] = None,
        object_storage_config: ObjectStorageConfig = None,
        object_storage_config_file: str = None,
        paused: bool = None,
        pod_metadata: PodMetadata = None,
        port_name: str = None,
        priority_class_name: str = None,
        prometheus_rules_excluded_from_enforce: List[
            PrometheusRulesExcludedFromEnforce
        ] = None,
        query_config: QueryConfig = None,
        query_endpoints: List[str] = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        retention: str = None,
        route_prefix: str = None,
        rule_namespace_selector: meta.LabelSelector = None,
        rule_selector: meta.LabelSelector = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        storage: Storage = None,
        tolerations: List[core.Toleration] = None,
        topology_spread_constraints: List[core.TopologySpreadConstraint] = None,
        tracing_config: TracingConfig = None,
        volumes: List[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            alert_drop_labels=alert_drop_labels,
            alert_query_url=alert_query_url,
            alertmanagers_config=alertmanagers_config,
            alertmanagers_url=alertmanagers_url,
            containers=containers,
            enforced_namespace_label=enforced_namespace_label,
            evaluation_interval=evaluation_interval,
            external_prefix=external_prefix,
            grpc_server_tls_config=grpc_server_tls_config,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            labels=labels,
            listen_local=listen_local,
            log_format=log_format,
            log_level=log_level,
            node_selector=node_selector,
            object_storage_config=object_storage_config,
            object_storage_config_file=object_storage_config_file,
            paused=paused,
            pod_metadata=pod_metadata,
            port_name=port_name,
            priority_class_name=priority_class_name,
            prometheus_rules_excluded_from_enforce=prometheus_rules_excluded_from_enforce,
            query_config=query_config,
            query_endpoints=query_endpoints,
            replicas=replicas,
            resources=resources,
            retention=retention,
            route_prefix=route_prefix,
            rule_namespace_selector=rule_namespace_selector,
            rule_selector=rule_selector,
            security_context=security_context,
            service_account_name=service_account_name,
            storage=storage,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            tracing_config=tracing_config,
            volumes=volumes,
        )


class ThanosRuler(KubernetesApiResource):
    __slots__ = ()

    _group_ = "monitoring.coreos.com"
    _version_ = "v1"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ThanosRulerSpec
    status: Status

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: ThanosRulerSpec = None,
        status: Status = None,
    ):
        super().__init__(
            "monitoring.coreos.com/v1",
            "ThanosRuler",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
            status=status,
        )
