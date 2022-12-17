from kubic import KubernetesApiResource, KubernetesObject
from ..api import apps, core, meta


class BasicAuth(KubernetesObject):
    __slots__ = ()

    password: core.SecretKeySelector
    username: core.SecretKeySelector

    def __init__(self, password: core.SecretKeySelector = None, username: core.SecretKeySelector = None):
        super().__init__(password=password, username=username)


class CA(KubernetesObject):
    __slots__ = ()

    config_map: core.ConfigMapKeySelector
    secret: core.SecretKeySelector

    def __init__(self, config_map: core.ConfigMapKeySelector = None, secret: core.SecretKeySelector = None):
        super().__init__(config_map=config_map, secret=secret)


class Cert(KubernetesObject):
    __slots__ = ()

    config_map: core.ConfigMapKeySelector
    secret: core.SecretKeySelector

    def __init__(self, config_map: core.ConfigMapKeySelector = None, secret: core.SecretKeySelector = None):
        super().__init__(config_map=config_map, secret=secret)


class TLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    ca_file: str
    cert: Cert
    cert_file: str
    insecure_skip_verify: bool
    key_file: str
    key_secret: core.SecretKeySelector
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        ca_file: str = None,
        cert: Cert = None,
        cert_file: str = None,
        insecure_skip_verify: bool = None,
        key_file: str = None,
        key_secret: core.SecretKeySelector = None,
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


class APIServerConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["host"]

    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    host: str
    tls_config: TLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        host: str = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth, bearer_token=bearer_token, bearer_token_file=bearer_token_file, host=host, tls_config=tls_config
        )


class ArbitraryFSAccessThroughSM(KubernetesObject):
    __slots__ = ()

    deny: bool

    def __init__(self, deny: bool = None):
        super().__init__(deny=deny)


class Datasource(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    tls_config: TLSConfig
    url: str

    def __init__(self, basic_auth: BasicAuth = None, tls_config: TLSConfig = None, url: str = None):
        super().__init__(basic_auth=basic_auth, tls_config=tls_config, url=url)


class Metadata(KubernetesObject):
    __slots__ = ()

    annotations: dict[str, str]
    labels: dict[str, str]
    name: str

    def __init__(self, annotations: dict[str, str] = None, labels: dict[str, str] = None, name: str = None):
        super().__init__(annotations=annotations, labels=labels, name=name)


class EmbeddedPersistentVolumeClaim(KubernetesObject):
    __slots__ = ()

    api_version: str
    kind: str
    metadata: Metadata
    spec: core.PersistentVolumeClaimSpec

    def __init__(self, api_version: str = None, kind: str = None, metadata: Metadata = None, spec: core.PersistentVolumeClaimSpec = None):
        super().__init__(api_version=api_version, kind=kind, metadata=metadata, spec=spec)


class RelabelConfig(KubernetesObject):
    __slots__ = ()

    action: str
    modulus: int
    regex: str
    replacement: str
    separator: str
    source_labels: list[str]
    target_label: str

    def __init__(
        self,
        action: str = None,
        modulus: int = None,
        regex: str = None,
        replacement: str = None,
        separator: str = None,
        source_labels: list[str] = None,
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


class Endpoint(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "proxy_url": "proxyURL",
    }
    _revfield_names_ = {
        "proxyURL": "proxy_url",
    }

    basic_auth: BasicAuth
    bearer_token_file: str
    bearer_token_secret: core.ConfigMapKeySelector
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    metric_relabel_configs: list[RelabelConfig]
    params: dict[str, list[str]]
    path: str
    port: str
    proxy_url: str
    relabel_configs: list[RelabelConfig]
    scheme: str
    scrape_timeout: str
    target_port: core.IntOrString
    tls_config: TLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_file: str = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        metric_relabel_configs: list[RelabelConfig] = None,
        params: dict[str, list[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabel_configs: list[RelabelConfig] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        target_port: core.IntOrString = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_file=bearer_token_file,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            metric_relabel_configs=metric_relabel_configs,
            params=params,
            path=path,
            port=port,
            proxy_url=proxy_url,
            relabel_configs=relabel_configs,
            scheme=scheme,
            scrape_timeout=scrape_timeout,
            target_port=target_port,
            tls_config=tls_config,
        )


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

    def __init__(self, container_name: str = None, divisor: core.IntOrString = None, resource: str = None):
        super().__init__(container_name=container_name, divisor=divisor, resource=resource)


class ValueFrom(KubernetesObject):
    __slots__ = ()

    config_map_key_ref: core.ConfigMapKeySelector
    field_ref: FieldRef
    resource_field_ref: ResourceFieldRef
    secret_key_ref: core.SecretKeySelector

    def __init__(
        self,
        config_map_key_ref: core.ConfigMapKeySelector = None,
        field_ref: FieldRef = None,
        resource_field_ref: ResourceFieldRef = None,
        secret_key_ref: core.SecretKeySelector = None,
    ):
        super().__init__(
            config_map_key_ref=config_map_key_ref, field_ref=field_ref, resource_field_ref=resource_field_ref, secret_key_ref=secret_key_ref
        )


class ExtraEnv(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    name: str
    value: str
    value_from: ValueFrom

    def __init__(self, name: str = None, value: str = None, value_from: ValueFrom = None):
        super().__init__(name=name, value=value, value_from=value_from)


class Rule(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "for": "for_",
    }

    alert: str
    annotations: dict[str, str]
    expr: core.IntOrString
    for_: str
    labels: dict[str, str]
    record: str

    def __init__(
        self,
        alert: str = None,
        annotations: dict[str, str] = None,
        expr: core.IntOrString = None,
        for_: str = None,
        labels: dict[str, str] = None,
        record: str = None,
    ):
        super().__init__(alert=alert, annotations=annotations, expr=expr, for_=for_, labels=labels, record=record)


class Group(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "rules"]

    concurrency: int
    interval: str
    name: str
    rules: list[Rule]

    def __init__(self, concurrency: int = None, interval: str = None, name: str = None, rules: list[Rule] = None):
        super().__init__(concurrency=concurrency, interval=interval, name=name, rules=rules)


class Host_aliase(KubernetesObject):
    __slots__ = ()

    hostnames: list[str]
    ip: str

    def __init__(self, hostnames: list[str] = None, ip: str = None):
        super().__init__(hostnames=hostnames, ip=ip)


class Image(KubernetesObject):
    __slots__ = ()

    pull_policy: str
    repository: str
    tag: str

    def __init__(self, pull_policy: str = None, repository: str = None, tag: str = None):
        super().__init__(pull_policy=pull_policy, repository=repository, tag=tag)


class NamespaceSelector(KubernetesObject):
    __slots__ = ()

    any: bool
    match_names: list[str]

    def __init__(self, any: bool = None, match_names: list[str] = None):
        super().__init__(any=any, match_names=match_names)


class Ingress(KubernetesObject):
    __slots__ = ()

    namespace_selector: NamespaceSelector
    relabeling_configs: list[RelabelConfig]
    selector: meta.LabelSelector

    def __init__(
        self,
        namespace_selector: NamespaceSelector = None,
        relabeling_configs: list[RelabelConfig] = None,
        selector: meta.LabelSelector = None,
    ):
        super().__init__(namespace_selector=namespace_selector, relabeling_configs=relabeling_configs, selector=selector)


class InsertPort(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "open_tsdbhttp_port": "openTSDBHTTPPort",
        "open_tsdb_port": "openTSDBPort",
    }
    _revfield_names_ = {
        "openTSDBHTTPPort": "open_tsdbhttp_port",
        "openTSDBPort": "open_tsdb_port",
    }

    graphite_port: str
    influx_port: str
    open_tsdbhttp_port: str
    open_tsdb_port: str

    def __init__(self, graphite_port: str = None, influx_port: str = None, open_tsdbhttp_port: str = None, open_tsdb_port: str = None):
        super().__init__(
            graphite_port=graphite_port, influx_port=influx_port, open_tsdbhttp_port=open_tsdbhttp_port, open_tsdb_port=open_tsdb_port
        )


class Notifier(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    tls_config: TLSConfig
    url: str

    def __init__(self, basic_auth: BasicAuth = None, tls_config: TLSConfig = None, url: str = None):
        super().__init__(basic_auth=basic_auth, tls_config=tls_config, url=url)


class PodDisruptionBudget(KubernetesObject):
    __slots__ = ()

    max_unavailable: core.IntOrString
    min_available: core.IntOrString

    def __init__(self, max_unavailable: core.IntOrString = None, min_available: core.IntOrString = None):
        super().__init__(max_unavailable=max_unavailable, min_available=min_available)


class PodMetadata(KubernetesObject):
    __slots__ = ()

    annotations: dict[str, str]
    labels: dict[str, str]
    name: str

    def __init__(self, annotations: dict[str, str] = None, labels: dict[str, str] = None, name: str = None):
        super().__init__(annotations=annotations, labels=labels, name=name)


class RemoteRead(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    lookback: str
    tls_config: TLSConfig
    url: str

    def __init__(self, basic_auth: BasicAuth = None, lookback: str = None, tls_config: TLSConfig = None, url: str = None):
        super().__init__(basic_auth=basic_auth, lookback=lookback, tls_config=tls_config, url=url)


class RemoteWriteSetting(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "max_disk_usage_per_url": "maxDiskUsagePerURL",
        "show_url": "showURL",
    }
    _revfield_names_ = {
        "maxDiskUsagePerURL": "max_disk_usage_per_url",
        "showURL": "show_url",
    }

    flush_interval: str
    max_block_size: int
    max_disk_usage_per_url: int
    queues: int
    show_url: bool
    tmp_data_path: str

    def __init__(
        self,
        flush_interval: str = None,
        max_block_size: int = None,
        max_disk_usage_per_url: int = None,
        queues: int = None,
        show_url: bool = None,
        tmp_data_path: str = None,
    ):
        super().__init__(
            flush_interval=flush_interval,
            max_block_size=max_block_size,
            max_disk_usage_per_url=max_disk_usage_per_url,
            queues=queues,
            show_url=show_url,
            tmp_data_path=tmp_data_path,
        )


class Resource(KubernetesObject):
    __slots__ = ()

    limits: dict[str, core.IntOrString]
    requests: dict[str, core.IntOrString]

    def __init__(self, limits: dict[str, core.IntOrString] = None, requests: dict[str, core.IntOrString] = None):
        super().__init__(limits=limits, requests=requests)


class RollingUpdate(KubernetesObject):
    __slots__ = ()

    max_surge: core.IntOrString
    max_unavailable: core.IntOrString

    def __init__(self, max_surge: core.IntOrString = None, max_unavailable: core.IntOrString = None):
        super().__init__(max_surge=max_surge, max_unavailable=max_unavailable)


class ServiceSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["spec"]

    metadata: Metadata
    spec: core.ServiceSpec

    def __init__(self, metadata: Metadata = None, spec: core.ServiceSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class StaticConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["targets"]

    labels: dict[str, str]
    relabeling_configs: list[RelabelConfig]
    targets: list[str]

    def __init__(self, labels: dict[str, str] = None, relabeling_configs: list[RelabelConfig] = None, targets: list[str] = None):
        super().__init__(labels=labels, relabeling_configs=relabeling_configs, targets=targets)


class StorageSpec(KubernetesObject):
    __slots__ = ()

    disable_mount_sub_path: bool
    empty_dir: core.EmptyDirVolumeSource
    volume_claim_template: EmbeddedPersistentVolumeClaim

    def __init__(
        self,
        disable_mount_sub_path: bool = None,
        empty_dir: core.EmptyDirVolumeSource = None,
        volume_claim_template: EmbeddedPersistentVolumeClaim = None,
    ):
        super().__init__(disable_mount_sub_path=disable_mount_sub_path, empty_dir=empty_dir, volume_claim_template=volume_claim_template)


class Target(KubernetesObject):
    __slots__ = ()

    ingress: Ingress
    static_config: StaticConfig

    def __init__(self, ingress: Ingress = None, static_config: StaticConfig = None):
        super().__init__(ingress=ingress, static_config=static_config)


class TargetEndpoint(KubernetesObject):
    __slots__ = ()

    _required_ = ["targets"]

    _field_names_ = {
        "proxy_url": "proxyURL",
    }
    _revfield_names_ = {
        "proxyURL": "proxy_url",
    }

    basic_auth: BasicAuth
    bearer_token_file: str
    bearer_token_secret: core.ConfigMapKeySelector
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    labels: dict[str, str]
    metric_relabel_configs: list[RelabelConfig]
    params: dict[str, list[str]]
    path: str
    port: str
    proxy_url: str
    relabel_configs: list[RelabelConfig]
    scheme: str
    scrape_timeout: str
    targets: list[str]
    tls_config: TLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_file: str = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        labels: dict[str, str] = None,
        metric_relabel_configs: list[RelabelConfig] = None,
        params: dict[str, list[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabel_configs: list[RelabelConfig] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        targets: list[str] = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_file=bearer_token_file,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            labels=labels,
            metric_relabel_configs=metric_relabel_configs,
            params=params,
            path=path,
            port=port,
            proxy_url=proxy_url,
            relabel_configs=relabel_configs,
            scheme=scheme,
            scrape_timeout=scrape_timeout,
            targets=targets,
            tls_config=tls_config,
        )


class VMAgentSpecRemoteWrite(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    bearer_token_secret: core.ConfigMapKeySelector
    inline_url_relabel_config: list[RelabelConfig]
    label: dict[str, str]
    send_timeout: str
    tls_config: TLSConfig
    url: str
    url_relabel_config: core.ConfigMapKeySelector

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        inline_url_relabel_config: list[RelabelConfig] = None,
        label: dict[str, str] = None,
        send_timeout: str = None,
        tls_config: TLSConfig = None,
        url: str = None,
        url_relabel_config: core.ConfigMapKeySelector = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_secret=bearer_token_secret,
            inline_url_relabel_config=inline_url_relabel_config,
            label=label,
            send_timeout=send_timeout,
            tls_config=tls_config,
            url=url,
            url_relabel_config=url_relabel_config,
        )


class VMAgentSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "api_server_config": "aPIServerConfig",
        "arbitrary_fs_access_through_sms": "arbitraryFSAccessThroughSMs",
        "host_aliases": "host_aliases",
    }
    _revfield_names_ = {
        "aPIServerConfig": "api_server_config",
        "arbitraryFSAccessThroughSMs": "arbitrary_fs_access_through_sms",
    }

    api_server_config: APIServerConfig
    additional_scrape_configs: core.SecretKeySelector
    affinity: core.Affinity
    arbitrary_fs_access_through_sms: ArbitraryFSAccessThroughSM
    config_maps: list[str]
    containers: list[core.Container]
    dns_policy: str
    enforced_namespace_label: str
    external_labels: dict[str, str]
    extra_args: dict[str, str]
    extra_envs: list[core.EnvVar]
    host_network: bool
    host_aliases: list[Host_aliase]
    ignore_namespace_selectors: bool
    image: Image
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    inline_relabel_config: list[RelabelConfig]
    inline_scrape_config: str
    insert_ports: InsertPort
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    node_scrape_namespace_selector: meta.LabelSelector
    node_scrape_selector: meta.LabelSelector
    override_honor_labels: bool
    override_honor_timestamps: bool
    pod_disruption_budget: PodDisruptionBudget
    pod_metadata: PodMetadata
    pod_scrape_namespace_selector: meta.LabelSelector
    pod_scrape_selector: meta.LabelSelector
    pod_security_policy_name: str
    port: str
    priority_class_name: str
    probe_namespace_selector: meta.LabelSelector
    probe_selector: meta.LabelSelector
    readiness_probe: core.Probe
    relabel_config: core.ConfigMapKeySelector
    remote_write: list[VMAgentSpecRemoteWrite]
    remote_write_settings: RemoteWriteSetting
    replica_count: int
    resources: core.ResourceRequirements
    rolling_update: apps.RollingUpdateDeployment
    runtime_class_name: str
    scheduler_name: str
    scrape_interval: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    service_scrape_namespace_selector: meta.LabelSelector
    service_scrape_selector: meta.LabelSelector
    service_spec: ServiceSpec
    shard_count: int
    startup_probe: core.Probe
    static_scrape_namespace_selector: meta.LabelSelector
    static_scrape_selector: meta.LabelSelector
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    update_strategy: str
    vm_agent_external_label_name: str
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        api_server_config: APIServerConfig = None,
        additional_scrape_configs: core.SecretKeySelector = None,
        affinity: core.Affinity = None,
        arbitrary_fs_access_through_sms: ArbitraryFSAccessThroughSM = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        dns_policy: str = None,
        enforced_namespace_label: str = None,
        external_labels: dict[str, str] = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[core.EnvVar] = None,
        host_network: bool = None,
        host_aliases: list[Host_aliase] = None,
        ignore_namespace_selectors: bool = None,
        image: Image = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        inline_relabel_config: list[RelabelConfig] = None,
        inline_scrape_config: str = None,
        insert_ports: InsertPort = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        node_scrape_namespace_selector: meta.LabelSelector = None,
        node_scrape_selector: meta.LabelSelector = None,
        override_honor_labels: bool = None,
        override_honor_timestamps: bool = None,
        pod_disruption_budget: PodDisruptionBudget = None,
        pod_metadata: PodMetadata = None,
        pod_scrape_namespace_selector: meta.LabelSelector = None,
        pod_scrape_selector: meta.LabelSelector = None,
        pod_security_policy_name: str = None,
        port: str = None,
        priority_class_name: str = None,
        probe_namespace_selector: meta.LabelSelector = None,
        probe_selector: meta.LabelSelector = None,
        readiness_probe: core.Probe = None,
        relabel_config: core.ConfigMapKeySelector = None,
        remote_write: list[VMAgentSpecRemoteWrite] = None,
        remote_write_settings: RemoteWriteSetting = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        rolling_update: apps.RollingUpdateDeployment = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        scrape_interval: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        service_scrape_namespace_selector: meta.LabelSelector = None,
        service_scrape_selector: meta.LabelSelector = None,
        service_spec: ServiceSpec = None,
        shard_count: int = None,
        startup_probe: core.Probe = None,
        static_scrape_namespace_selector: meta.LabelSelector = None,
        static_scrape_selector: meta.LabelSelector = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        update_strategy: str = None,
        vm_agent_external_label_name: str = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            api_server_config=api_server_config,
            additional_scrape_configs=additional_scrape_configs,
            affinity=affinity,
            arbitrary_fs_access_through_sms=arbitrary_fs_access_through_sms,
            config_maps=config_maps,
            containers=containers,
            dns_policy=dns_policy,
            enforced_namespace_label=enforced_namespace_label,
            external_labels=external_labels,
            extra_args=extra_args,
            extra_envs=extra_envs,
            host_network=host_network,
            host_aliases=host_aliases,
            ignore_namespace_selectors=ignore_namespace_selectors,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            inline_relabel_config=inline_relabel_config,
            inline_scrape_config=inline_scrape_config,
            insert_ports=insert_ports,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            node_scrape_namespace_selector=node_scrape_namespace_selector,
            node_scrape_selector=node_scrape_selector,
            override_honor_labels=override_honor_labels,
            override_honor_timestamps=override_honor_timestamps,
            pod_disruption_budget=pod_disruption_budget,
            pod_metadata=pod_metadata,
            pod_scrape_namespace_selector=pod_scrape_namespace_selector,
            pod_scrape_selector=pod_scrape_selector,
            pod_security_policy_name=pod_security_policy_name,
            port=port,
            priority_class_name=priority_class_name,
            probe_namespace_selector=probe_namespace_selector,
            probe_selector=probe_selector,
            readiness_probe=readiness_probe,
            relabel_config=relabel_config,
            remote_write=remote_write,
            remote_write_settings=remote_write_settings,
            replica_count=replica_count,
            resources=resources,
            rolling_update=rolling_update,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            scrape_interval=scrape_interval,
            secrets=secrets,
            security_context=security_context,
            service_account_name=service_account_name,
            service_scrape_namespace_selector=service_scrape_namespace_selector,
            service_scrape_selector=service_scrape_selector,
            service_spec=service_spec,
            shard_count=shard_count,
            startup_probe=startup_probe,
            static_scrape_namespace_selector=static_scrape_namespace_selector,
            static_scrape_selector=static_scrape_selector,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            update_strategy=update_strategy,
            vm_agent_external_label_name=vm_agent_external_label_name,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VMAgent(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMAgent"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VMAgentSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMAgentSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMAgent", name, namespace, metadata=metadata, spec=spec)


class VMAlertSpecRemoteWrite(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    basic_auth: BasicAuth
    concurrency: int
    flush_interval: str
    max_batch_size: int
    max_queue_size: int
    tls_config: TLSConfig
    url: str

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        concurrency: int = None,
        flush_interval: str = None,
        max_batch_size: int = None,
        max_queue_size: int = None,
        tls_config: TLSConfig = None,
        url: str = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            concurrency=concurrency,
            flush_interval=flush_interval,
            max_batch_size=max_batch_size,
            max_queue_size=max_queue_size,
            tls_config=tls_config,
            url=url,
        )


class VMAlertSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["datasource"]

    affinity: core.Affinity
    config_maps: list[str]
    containers: list[core.Container]
    datasource: Datasource
    dns_policy: str
    enforced_namespace_label: str
    evaluation_interval: str
    external_labels: dict[str, str]
    extra_args: dict[str, str]
    extra_envs: list[core.EnvVar]
    host_network: bool
    image: Image
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    notifier: Notifier
    notifiers: list[Notifier]
    pod_disruption_budget: PodDisruptionBudget
    pod_metadata: PodMetadata
    pod_security_policy_name: str
    port: str
    priority_class_name: str
    readiness_probe: core.Probe
    remote_read: RemoteRead
    remote_write: VMAlertSpecRemoteWrite
    replica_count: int
    resources: core.ResourceRequirements
    rolling_update: RollingUpdate
    rule_namespace_selector: meta.LabelSelector
    rule_path: list[str]
    rule_selector: meta.LabelSelector
    runtime_class_name: str
    scheduler_name: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    service_spec: ServiceSpec
    startup_probe: core.Probe
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    update_strategy: str
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        datasource: Datasource = None,
        dns_policy: str = None,
        enforced_namespace_label: str = None,
        evaluation_interval: str = None,
        external_labels: dict[str, str] = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[core.EnvVar] = None,
        host_network: bool = None,
        image: Image = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        notifier: Notifier = None,
        notifiers: list[Notifier] = None,
        pod_disruption_budget: PodDisruptionBudget = None,
        pod_metadata: PodMetadata = None,
        pod_security_policy_name: str = None,
        port: str = None,
        priority_class_name: str = None,
        readiness_probe: core.Probe = None,
        remote_read: RemoteRead = None,
        remote_write: VMAlertSpecRemoteWrite = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        rolling_update: RollingUpdate = None,
        rule_namespace_selector: meta.LabelSelector = None,
        rule_path: list[str] = None,
        rule_selector: meta.LabelSelector = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        service_spec: ServiceSpec = None,
        startup_probe: core.Probe = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        update_strategy: str = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            config_maps=config_maps,
            containers=containers,
            datasource=datasource,
            dns_policy=dns_policy,
            enforced_namespace_label=enforced_namespace_label,
            evaluation_interval=evaluation_interval,
            external_labels=external_labels,
            extra_args=extra_args,
            extra_envs=extra_envs,
            host_network=host_network,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            notifier=notifier,
            notifiers=notifiers,
            pod_disruption_budget=pod_disruption_budget,
            pod_metadata=pod_metadata,
            pod_security_policy_name=pod_security_policy_name,
            port=port,
            priority_class_name=priority_class_name,
            readiness_probe=readiness_probe,
            remote_read=remote_read,
            remote_write=remote_write,
            replica_count=replica_count,
            resources=resources,
            rolling_update=rolling_update,
            rule_namespace_selector=rule_namespace_selector,
            rule_path=rule_path,
            rule_selector=rule_selector,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            secrets=secrets,
            security_context=security_context,
            service_account_name=service_account_name,
            service_spec=service_spec,
            startup_probe=startup_probe,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            update_strategy=update_strategy,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VMAlert(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMAlert"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VMAlertSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMAlertSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMAlert", name, namespace, metadata=metadata, spec=spec)


class VMAlertmanagerSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "external_url": "externalURL",
    }
    _revfield_names_ = {
        "externalURL": "external_url",
    }

    additional_peers: list[str]
    affinity: core.Affinity
    cluster_advertise_address: str
    config_maps: list[str]
    config_raw_yaml: str
    config_secret: str
    containers: list[core.Container]
    dns_policy: str
    external_url: str
    host_network: bool
    image: Image
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    listen_local: bool
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    node_selector: dict[str, str]
    paused: bool
    pod_disruption_budget: PodDisruptionBudget
    pod_metadata: PodMetadata
    pod_security_policy_name: str
    port_name: str
    priority_class_name: str
    readiness_probe: core.Probe
    replica_count: int
    resources: core.ResourceRequirements
    retention: str
    route_prefix: str
    runtime_class_name: str
    scheduler_name: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    service_spec: ServiceSpec
    startup_probe: core.Probe
    storage: StorageSpec
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        additional_peers: list[str] = None,
        affinity: core.Affinity = None,
        cluster_advertise_address: str = None,
        config_maps: list[str] = None,
        config_raw_yaml: str = None,
        config_secret: str = None,
        containers: list[core.Container] = None,
        dns_policy: str = None,
        external_url: str = None,
        host_network: bool = None,
        image: Image = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        listen_local: bool = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        node_selector: dict[str, str] = None,
        paused: bool = None,
        pod_disruption_budget: PodDisruptionBudget = None,
        pod_metadata: PodMetadata = None,
        pod_security_policy_name: str = None,
        port_name: str = None,
        priority_class_name: str = None,
        readiness_probe: core.Probe = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        retention: str = None,
        route_prefix: str = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        service_spec: ServiceSpec = None,
        startup_probe: core.Probe = None,
        storage: StorageSpec = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            additional_peers=additional_peers,
            affinity=affinity,
            cluster_advertise_address=cluster_advertise_address,
            config_maps=config_maps,
            config_raw_yaml=config_raw_yaml,
            config_secret=config_secret,
            containers=containers,
            dns_policy=dns_policy,
            external_url=external_url,
            host_network=host_network,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            listen_local=listen_local,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            node_selector=node_selector,
            paused=paused,
            pod_disruption_budget=pod_disruption_budget,
            pod_metadata=pod_metadata,
            pod_security_policy_name=pod_security_policy_name,
            port_name=port_name,
            priority_class_name=priority_class_name,
            readiness_probe=readiness_probe,
            replica_count=replica_count,
            resources=resources,
            retention=retention,
            route_prefix=route_prefix,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            secrets=secrets,
            security_context=security_context,
            service_account_name=service_account_name,
            service_spec=service_spec,
            startup_probe=startup_probe,
            storage=storage,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VMAlertmanager(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMAlertmanager"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VMAlertmanagerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMAlertmanagerSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMAlertmanager", name, namespace, metadata=metadata, spec=spec)


class VMInsert(KubernetesObject):
    __slots__ = ()

    _required_ = ["replica_count"]

    affinity: core.Affinity
    config_maps: list[str]
    containers: list[core.Container]
    dns_policy: str
    extra_args: dict[str, str]
    extra_envs: list[core.EnvVar]
    host_network: bool
    image: Image
    init_containers: list[core.Container]
    insert_ports: InsertPort
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    name: str
    pod_disruption_budget: PodDisruptionBudget
    pod_metadata: PodMetadata
    port: str
    priority_class_name: str
    readiness_probe: core.Probe
    replica_count: int
    resources: core.ResourceRequirements
    rolling_update: RollingUpdate
    runtime_class_name: str
    scheduler_name: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_spec: ServiceSpec
    startup_probe: core.Probe
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    update_strategy: str
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        dns_policy: str = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[core.EnvVar] = None,
        host_network: bool = None,
        image: Image = None,
        init_containers: list[core.Container] = None,
        insert_ports: InsertPort = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        name: str = None,
        pod_disruption_budget: PodDisruptionBudget = None,
        pod_metadata: PodMetadata = None,
        port: str = None,
        priority_class_name: str = None,
        readiness_probe: core.Probe = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        rolling_update: RollingUpdate = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_spec: ServiceSpec = None,
        startup_probe: core.Probe = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        update_strategy: str = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            config_maps=config_maps,
            containers=containers,
            dns_policy=dns_policy,
            extra_args=extra_args,
            extra_envs=extra_envs,
            host_network=host_network,
            image=image,
            init_containers=init_containers,
            insert_ports=insert_ports,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            name=name,
            pod_disruption_budget=pod_disruption_budget,
            pod_metadata=pod_metadata,
            port=port,
            priority_class_name=priority_class_name,
            readiness_probe=readiness_probe,
            replica_count=replica_count,
            resources=resources,
            rolling_update=rolling_update,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            secrets=secrets,
            security_context=security_context,
            service_spec=service_spec,
            startup_probe=startup_probe,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            update_strategy=update_strategy,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VMSelect(KubernetesObject):
    __slots__ = ()

    _required_ = ["replica_count"]

    affinity: core.Affinity
    cache_mount_path: str
    config_maps: list[str]
    containers: list[core.Container]
    dns_policy: str
    extra_args: dict[str, str]
    extra_envs: list[core.EnvVar]
    host_network: bool
    image: Image
    init_containers: list[core.Container]
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    name: str
    persistent_volume: StorageSpec
    pod_disruption_budget: PodDisruptionBudget
    pod_metadata: PodMetadata
    port: str
    priority_class_name: str
    readiness_probe: core.Probe
    replica_count: int
    resources: core.ResourceRequirements
    runtime_class_name: str
    scheduler_name: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_spec: ServiceSpec
    startup_probe: core.Probe
    storage: StorageSpec
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        cache_mount_path: str = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        dns_policy: str = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[core.EnvVar] = None,
        host_network: bool = None,
        image: Image = None,
        init_containers: list[core.Container] = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        name: str = None,
        persistent_volume: StorageSpec = None,
        pod_disruption_budget: PodDisruptionBudget = None,
        pod_metadata: PodMetadata = None,
        port: str = None,
        priority_class_name: str = None,
        readiness_probe: core.Probe = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_spec: ServiceSpec = None,
        startup_probe: core.Probe = None,
        storage: StorageSpec = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            cache_mount_path=cache_mount_path,
            config_maps=config_maps,
            containers=containers,
            dns_policy=dns_policy,
            extra_args=extra_args,
            extra_envs=extra_envs,
            host_network=host_network,
            image=image,
            init_containers=init_containers,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            name=name,
            persistent_volume=persistent_volume,
            pod_disruption_budget=pod_disruption_budget,
            pod_metadata=pod_metadata,
            port=port,
            priority_class_name=priority_class_name,
            readiness_probe=readiness_probe,
            replica_count=replica_count,
            resources=resources,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            secrets=secrets,
            security_context=security_context,
            service_spec=service_spec,
            startup_probe=startup_probe,
            storage=storage,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VmBackup(KubernetesObject):
    __slots__ = ()

    _required_ = ["accept_eula"]

    _field_names_ = {
        "accept_eula": "acceptEULA",
    }
    _revfield_names_ = {
        "acceptEULA": "accept_eula",
    }

    accept_eula: bool
    concurrency: int
    credentials_secret: core.ConfigMapKeySelector
    custom_s3_endpoint: str
    destination: str
    disable_daily: bool
    disable_hourly: bool
    disable_monthly: bool
    disable_weekly: bool
    extra_args: dict[str, str]
    extra_envs: list[ExtraEnv]
    image: Image
    log_format: str
    log_level: str
    port: str
    resources: Resource

    def __init__(
        self,
        accept_eula: bool = None,
        concurrency: int = None,
        credentials_secret: core.ConfigMapKeySelector = None,
        custom_s3_endpoint: str = None,
        destination: str = None,
        disable_daily: bool = None,
        disable_hourly: bool = None,
        disable_monthly: bool = None,
        disable_weekly: bool = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[ExtraEnv] = None,
        image: Image = None,
        log_format: str = None,
        log_level: str = None,
        port: str = None,
        resources: Resource = None,
    ):
        super().__init__(
            accept_eula=accept_eula,
            concurrency=concurrency,
            credentials_secret=credentials_secret,
            custom_s3_endpoint=custom_s3_endpoint,
            destination=destination,
            disable_daily=disable_daily,
            disable_hourly=disable_hourly,
            disable_monthly=disable_monthly,
            disable_weekly=disable_weekly,
            extra_args=extra_args,
            extra_envs=extra_envs,
            image=image,
            log_format=log_format,
            log_level=log_level,
            port=port,
            resources=resources,
        )


class VMStorage(KubernetesObject):
    __slots__ = ()

    _required_ = ["replica_count"]

    _field_names_ = {
        "maintenance_insert_node_ids": "maintenanceInsertNodeIDs",
        "maintenance_select_node_ids": "maintenanceSelectNodeIDs",
    }
    _revfield_names_ = {
        "maintenanceInsertNodeIDs": "maintenance_insert_node_ids",
        "maintenanceSelectNodeIDs": "maintenance_select_node_ids",
    }

    affinity: core.Affinity
    config_maps: list[str]
    containers: list[core.Container]
    dns_policy: str
    extra_args: dict[str, str]
    extra_envs: list[core.EnvVar]
    host_network: bool
    image: Image
    init_containers: list[core.Container]
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    maintenance_insert_node_ids: list[int]
    maintenance_select_node_ids: list[int]
    name: str
    pod_disruption_budget: PodDisruptionBudget
    pod_metadata: PodMetadata
    port: str
    priority_class_name: str
    readiness_probe: core.Probe
    replica_count: int
    resources: core.ResourceRequirements
    runtime_class_name: str
    scheduler_name: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_spec: ServiceSpec
    startup_probe: core.Probe
    storage: StorageSpec
    storage_data_path: str
    termination_grace_period_seconds: int
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    vm_backup: VmBackup
    vm_insert_port: str
    vm_select_port: str
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        dns_policy: str = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[core.EnvVar] = None,
        host_network: bool = None,
        image: Image = None,
        init_containers: list[core.Container] = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        maintenance_insert_node_ids: list[int] = None,
        maintenance_select_node_ids: list[int] = None,
        name: str = None,
        pod_disruption_budget: PodDisruptionBudget = None,
        pod_metadata: PodMetadata = None,
        port: str = None,
        priority_class_name: str = None,
        readiness_probe: core.Probe = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_spec: ServiceSpec = None,
        startup_probe: core.Probe = None,
        storage: StorageSpec = None,
        storage_data_path: str = None,
        termination_grace_period_seconds: int = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        vm_backup: VmBackup = None,
        vm_insert_port: str = None,
        vm_select_port: str = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            config_maps=config_maps,
            containers=containers,
            dns_policy=dns_policy,
            extra_args=extra_args,
            extra_envs=extra_envs,
            host_network=host_network,
            image=image,
            init_containers=init_containers,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            maintenance_insert_node_ids=maintenance_insert_node_ids,
            maintenance_select_node_ids=maintenance_select_node_ids,
            name=name,
            pod_disruption_budget=pod_disruption_budget,
            pod_metadata=pod_metadata,
            port=port,
            priority_class_name=priority_class_name,
            readiness_probe=readiness_probe,
            replica_count=replica_count,
            resources=resources,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            secrets=secrets,
            security_context=security_context,
            service_spec=service_spec,
            startup_probe=startup_probe,
            storage=storage,
            storage_data_path=storage_data_path,
            termination_grace_period_seconds=termination_grace_period_seconds,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            vm_backup=vm_backup,
            vm_insert_port=vm_insert_port,
            vm_select_port=vm_select_port,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VMClusterSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["retention_period"]

    cluster_version: str
    image_pull_secrets: list[core.LocalObjectReference]
    pod_security_policy_name: str
    replication_factor: int
    retention_period: str
    service_account_name: str
    vminsert: VMInsert
    vmselect: VMSelect
    vmstorage: VMStorage

    def __init__(
        self,
        cluster_version: str = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        pod_security_policy_name: str = None,
        replication_factor: int = None,
        retention_period: str = None,
        service_account_name: str = None,
        vminsert: VMInsert = None,
        vmselect: VMSelect = None,
        vmstorage: VMStorage = None,
    ):
        super().__init__(
            cluster_version=cluster_version,
            image_pull_secrets=image_pull_secrets,
            pod_security_policy_name=pod_security_policy_name,
            replication_factor=replication_factor,
            retention_period=retention_period,
            service_account_name=service_account_name,
            vminsert=vminsert,
            vmselect=vmselect,
            vmstorage=vmstorage,
        )


class VMCluster(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMCluster"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VMClusterSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMClusterSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMCluster", name, namespace, metadata=metadata, spec=spec)


class VMNodeScrapeSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "proxy_url": "proxyURL",
    }
    _revfield_names_ = {
        "proxyURL": "proxy_url",
    }

    basic_auth: BasicAuth
    bearer_token_file: str
    bearer_token_secret: core.ConfigMapKeySelector
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    job_label: str
    metric_relabel_configs: list[RelabelConfig]
    params: dict[str, list[str]]
    path: str
    port: str
    proxy_url: str
    relabel_configs: list[RelabelConfig]
    sample_limit: int
    scheme: str
    scrape_timeout: str
    selector: meta.LabelSelector
    target_labels: list[str]
    tls_config: TLSConfig

    def __init__(
        self,
        basic_auth: BasicAuth = None,
        bearer_token_file: str = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        job_label: str = None,
        metric_relabel_configs: list[RelabelConfig] = None,
        params: dict[str, list[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabel_configs: list[RelabelConfig] = None,
        sample_limit: int = None,
        scheme: str = None,
        scrape_timeout: str = None,
        selector: meta.LabelSelector = None,
        target_labels: list[str] = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            basic_auth=basic_auth,
            bearer_token_file=bearer_token_file,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            job_label=job_label,
            metric_relabel_configs=metric_relabel_configs,
            params=params,
            path=path,
            port=port,
            proxy_url=proxy_url,
            relabel_configs=relabel_configs,
            sample_limit=sample_limit,
            scheme=scheme,
            scrape_timeout=scrape_timeout,
            selector=selector,
            target_labels=target_labels,
            tls_config=tls_config,
        )


class VMNodeScrape(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMNodeScrape"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VMNodeScrapeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMNodeScrapeSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMNodeScrape", name, namespace, metadata=metadata, spec=spec)


class VMPodScrapeSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["pod_metrics_endpoints", "selector"]

    job_label: str
    namespace_selector: NamespaceSelector
    pod_metrics_endpoints: list[Endpoint]
    pod_target_labels: list[str]
    sample_limit: int
    selector: meta.LabelSelector

    def __init__(
        self,
        job_label: str = None,
        namespace_selector: NamespaceSelector = None,
        pod_metrics_endpoints: list[Endpoint] = None,
        pod_target_labels: list[str] = None,
        sample_limit: int = None,
        selector: meta.LabelSelector = None,
    ):
        super().__init__(
            job_label=job_label,
            namespace_selector=namespace_selector,
            pod_metrics_endpoints=pod_metrics_endpoints,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
        )


class VMPodScrape(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMPodScrape"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VMPodScrapeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMPodScrapeSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMPodScrape", name, namespace, metadata=metadata, spec=spec)


class VmProberSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    path: str
    scheme: str
    url: str

    def __init__(self, path: str = None, scheme: str = None, url: str = None):
        super().__init__(path=path, scheme=scheme, url=url)


class VMProbeSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["vm_prober_spec"]

    interval: str
    job_name: str
    module: str
    scrape_timeout: str
    targets: Target
    vm_prober_spec: VmProberSpec

    def __init__(
        self,
        interval: str = None,
        job_name: str = None,
        module: str = None,
        scrape_timeout: str = None,
        targets: Target = None,
        vm_prober_spec: VmProberSpec = None,
    ):
        super().__init__(
            interval=interval,
            job_name=job_name,
            module=module,
            scrape_timeout=scrape_timeout,
            targets=targets,
            vm_prober_spec=vm_prober_spec,
        )


class VMProbe(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMProbe"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VMProbeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMProbeSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMProbe", name, namespace, metadata=metadata, spec=spec)


class VMRuleSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["groups"]

    groups: list[Group]

    def __init__(self, groups: list[Group] = None):
        super().__init__(groups=groups)


class VMRule(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMRule"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VMRuleSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMRuleSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMRule", name, namespace, metadata=metadata, spec=spec)


class VMServiceScrapeSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["endpoints", "selector"]

    discovery_role: str
    endpoints: list[Endpoint]
    job_label: str
    namespace_selector: NamespaceSelector
    pod_target_labels: list[str]
    sample_limit: int
    selector: meta.LabelSelector
    target_labels: list[str]

    def __init__(
        self,
        discovery_role: str = None,
        endpoints: list[Endpoint] = None,
        job_label: str = None,
        namespace_selector: NamespaceSelector = None,
        pod_target_labels: list[str] = None,
        sample_limit: int = None,
        selector: meta.LabelSelector = None,
        target_labels: list[str] = None,
    ):
        super().__init__(
            discovery_role=discovery_role,
            endpoints=endpoints,
            job_label=job_label,
            namespace_selector=namespace_selector,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
            target_labels=target_labels,
        )


class VMServiceScrape(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMServiceScrape"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: VMServiceScrapeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMServiceScrapeSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMServiceScrape", name, namespace, metadata=metadata, spec=spec)


class VMSingleSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["retention_period"]

    affinity: core.Affinity
    config_maps: list[str]
    containers: list[core.Container]
    dns_policy: str
    extra_args: dict[str, str]
    extra_envs: list[core.EnvVar]
    host_aliases: list[core.HostAlias]
    host_network: bool
    image: Image
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    insert_ports: InsertPort
    liveness_probe: core.Probe
    log_format: str
    log_level: str
    pod_metadata: PodMetadata
    pod_security_policy_name: str
    port: str
    priority_class_name: str
    readiness_probe: core.Probe
    remove_pvc_after_delete: bool
    replica_count: int
    resources: core.ResourceRequirements
    retention_period: str
    runtime_class_name: str
    scheduler_name: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    service_spec: ServiceSpec
    startup_probe: core.Probe
    storage: core.PersistentVolumeClaimSpec
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    vm_backup: VmBackup
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        dns_policy: str = None,
        extra_args: dict[str, str] = None,
        extra_envs: list[core.EnvVar] = None,
        host_aliases: list[core.HostAlias] = None,
        host_network: bool = None,
        image: Image = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        insert_ports: InsertPort = None,
        liveness_probe: core.Probe = None,
        log_format: str = None,
        log_level: str = None,
        pod_metadata: PodMetadata = None,
        pod_security_policy_name: str = None,
        port: str = None,
        priority_class_name: str = None,
        readiness_probe: core.Probe = None,
        remove_pvc_after_delete: bool = None,
        replica_count: int = None,
        resources: core.ResourceRequirements = None,
        retention_period: str = None,
        runtime_class_name: str = None,
        scheduler_name: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        service_spec: ServiceSpec = None,
        startup_probe: core.Probe = None,
        storage: core.PersistentVolumeClaimSpec = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        vm_backup: VmBackup = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            config_maps=config_maps,
            containers=containers,
            dns_policy=dns_policy,
            extra_args=extra_args,
            extra_envs=extra_envs,
            host_aliases=host_aliases,
            host_network=host_network,
            image=image,
            image_pull_secrets=image_pull_secrets,
            init_containers=init_containers,
            insert_ports=insert_ports,
            liveness_probe=liveness_probe,
            log_format=log_format,
            log_level=log_level,
            pod_metadata=pod_metadata,
            pod_security_policy_name=pod_security_policy_name,
            port=port,
            priority_class_name=priority_class_name,
            readiness_probe=readiness_probe,
            remove_pvc_after_delete=remove_pvc_after_delete,
            replica_count=replica_count,
            resources=resources,
            retention_period=retention_period,
            runtime_class_name=runtime_class_name,
            scheduler_name=scheduler_name,
            secrets=secrets,
            security_context=security_context,
            service_account_name=service_account_name,
            service_spec=service_spec,
            startup_probe=startup_probe,
            storage=storage,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            vm_backup=vm_backup,
            volume_mounts=volume_mounts,
            volumes=volumes,
        )


class VMSingle(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMSingle"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VMSingleSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMSingleSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMSingle", name, namespace, metadata=metadata, spec=spec)


class VMStaticScrapeSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["target_endpoints"]

    job_name: str
    sample_limit: int
    target_endpoints: list[TargetEndpoint]

    def __init__(self, job_name: str = None, sample_limit: int = None, target_endpoints: list[TargetEndpoint] = None):
        super().__init__(job_name=job_name, sample_limit=sample_limit, target_endpoints=target_endpoints)


class VMStaticScrape(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "operator.victoriametrics.com/v1beta1"
    _kind_ = "VMStaticScrape"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VMStaticScrapeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VMStaticScrapeSpec = None):
        super().__init__("operator.victoriametrics.com/v1beta1", "VMStaticScrape", name, namespace, metadata=metadata, spec=spec)
