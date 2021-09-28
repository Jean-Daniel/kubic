from typing import Any, Dict, List

from .. import KubernetesApiResource, KubernetesObject
from .. import core, meta


class Attachment(KubernetesObject):
    __slots__ = ()

    _required_ = ["cluster_name", "mount_dir", "node", "pod_name", "pod_namespace", "read_only"]

    cluster_name: str
    mount_dir: str
    node: str
    pod_name: str
    pod_namespace: str
    read_only: bool

    def __init__(
        self,
        cluster_name: str = None,
        mount_dir: str = None,
        node: str = None,
        pod_name: str = None,
        pod_namespace: str = None,
        read_only: bool = None,
    ):
        super().__init__(
            cluster_name=cluster_name, mount_dir=mount_dir, node=node, pod_name=pod_name, pod_namespace=pod_namespace, read_only=read_only
        )


class Bucket(KubernetesObject):
    __slots__ = ()

    disabled: bool
    interval: str
    timeout: str

    def __init__(self, disabled: bool = None, interval: str = None, timeout: str = None):
        super().__init__(disabled=disabled, interval=interval, timeout=timeout)


class Capabilitie(KubernetesObject):
    __slots__ = ()

    bucket: str
    metadata: str
    usage: str
    user: str
    zone: str

    def __init__(self, bucket: str = None, metadata: str = None, usage: str = None, user: str = None, zone: str = None):
        super().__init__(bucket=bucket, metadata=metadata, usage=usage, user=user, zone=zone)


class ErasureCoded(KubernetesObject):
    __slots__ = ()

    _required_ = ["coding_chunks", "data_chunks"]

    algorithm: str
    coding_chunks: int
    data_chunks: int

    def __init__(self, algorithm: str = None, coding_chunks: int = None, data_chunks: int = None):
        super().__init__(algorithm=algorithm, coding_chunks=coding_chunks, data_chunks=data_chunks)


class Peer(KubernetesObject):
    __slots__ = ()

    secret_names: List[str]

    def __init__(self, secret_names: List[str] = None):
        super().__init__(secret_names=secret_names)


class SnapshotSchedule(KubernetesObject):
    __slots__ = ()

    interval: str
    path: str
    start_time: str

    def __init__(self, interval: str = None, path: str = None, start_time: str = None):
        super().__init__(interval=interval, path=path, start_time=start_time)


class CephBlockPoolSpecMirroring(KubernetesObject):
    __slots__ = ()

    enabled: bool
    mode: str
    peers: Peer
    snapshot_schedules: List[SnapshotSchedule]

    def __init__(self, enabled: bool = None, mode: str = None, peers: Peer = None, snapshot_schedules: List[SnapshotSchedule] = None):
        super().__init__(enabled=enabled, mode=mode, peers=peers, snapshot_schedules=snapshot_schedules)


class CephBlockPoolSpecQuota(KubernetesObject):
    __slots__ = ()

    max_bytes: int
    max_objects: int
    max_size: str

    def __init__(self, max_bytes: int = None, max_objects: int = None, max_size: str = None):
        super().__init__(max_bytes=max_bytes, max_objects=max_objects, max_size=max_size)


class HybridStorage(KubernetesObject):
    __slots__ = ()

    _required_ = ["primary_device_class", "secondary_device_class"]

    primary_device_class: str
    secondary_device_class: str

    def __init__(self, primary_device_class: str = None, secondary_device_class: str = None):
        super().__init__(primary_device_class=primary_device_class, secondary_device_class=secondary_device_class)


class Replicated(KubernetesObject):
    __slots__ = ()

    _required_ = ["size"]

    hybrid_storage: HybridStorage
    replicas_per_failure_domain: int
    require_safe_replica_size: bool
    size: int
    sub_failure_domain: str
    target_size_ratio: int

    def __init__(
        self,
        hybrid_storage: HybridStorage = None,
        replicas_per_failure_domain: int = None,
        require_safe_replica_size: bool = None,
        size: int = None,
        sub_failure_domain: str = None,
        target_size_ratio: int = None,
    ):
        super().__init__(
            hybrid_storage=hybrid_storage,
            replicas_per_failure_domain=replicas_per_failure_domain,
            require_safe_replica_size=require_safe_replica_size,
            size=size,
            sub_failure_domain=sub_failure_domain,
            target_size_ratio=target_size_ratio,
        )


class Mirror(KubernetesObject):
    __slots__ = ()

    disabled: bool
    interval: str
    timeout: str

    def __init__(self, disabled: bool = None, interval: str = None, timeout: str = None):
        super().__init__(disabled=disabled, interval=interval, timeout=timeout)


class StatusCheck(KubernetesObject):
    __slots__ = ()

    mirror: Mirror

    def __init__(self, mirror: Mirror = None):
        super().__init__(mirror=mirror)


class CephBlockPoolSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "enable_rbd_stats": "enableRBDStats",
    }
    _revfield_names_ = {
        "enableRBDStats": "enable_rbd_stats",
    }

    compression_mode: str
    crush_root: str
    device_class: str
    enable_rbd_stats: bool
    erasure_coded: ErasureCoded
    failure_domain: str
    mirroring: CephBlockPoolSpecMirroring
    parameters: Dict[str, str]
    quotas: CephBlockPoolSpecQuota
    replicated: Replicated
    status_check: StatusCheck

    def __init__(
        self,
        compression_mode: str = None,
        crush_root: str = None,
        device_class: str = None,
        enable_rbd_stats: bool = None,
        erasure_coded: ErasureCoded = None,
        failure_domain: str = None,
        mirroring: CephBlockPoolSpecMirroring = None,
        parameters: Dict[str, str] = None,
        quotas: CephBlockPoolSpecQuota = None,
        replicated: Replicated = None,
        status_check: StatusCheck = None,
    ):
        super().__init__(
            compression_mode=compression_mode,
            crush_root=crush_root,
            device_class=device_class,
            enable_rbd_stats=enable_rbd_stats,
            erasure_coded=erasure_coded,
            failure_domain=failure_domain,
            mirroring=mirroring,
            parameters=parameters,
            quotas=quotas,
            replicated=replicated,
            status_check=status_check,
        )


class CephBlockPool(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephBlockPool"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephBlockPoolSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephBlockPoolSpec = None):
        super().__init__("ceph.rook.io/v1", "CephBlockPool", name, namespace, metadata=metadata, spec=spec)


class CephClientSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["caps"]

    caps: Dict[str, str]
    name: str

    def __init__(self, caps: Dict[str, str] = None, name: str = None):
        super().__init__(caps=caps, name=name)


class CephClient(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephClient"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephClientSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephClientSpec = None):
        super().__init__("ceph.rook.io/v1", "CephClient", name, namespace, metadata=metadata, spec=spec)


class CephVersion(KubernetesObject):
    __slots__ = ()

    allow_unsupported: bool
    image: str

    def __init__(self, allow_unsupported: bool = None, image: str = None):
        super().__init__(allow_unsupported=allow_unsupported, image=image)


class SanitizeDisk(KubernetesObject):
    __slots__ = ()

    data_source: str
    iteration: int
    method: str

    def __init__(self, data_source: str = None, iteration: int = None, method: str = None):
        super().__init__(data_source=data_source, iteration=iteration, method=method)


class CleanupPolicy(KubernetesObject):
    __slots__ = ()

    allow_uninstall_with_volumes: bool
    confirmation: str
    sanitize_disks: SanitizeDisk

    def __init__(self, allow_uninstall_with_volumes: bool = None, confirmation: str = None, sanitize_disks: SanitizeDisk = None):
        super().__init__(
            allow_uninstall_with_volumes=allow_uninstall_with_volumes, confirmation=confirmation, sanitize_disks=sanitize_disks
        )


class CrashCollector(KubernetesObject):
    __slots__ = ()

    days_to_retain: int
    disable: bool

    def __init__(self, days_to_retain: int = None, disable: bool = None):
        super().__init__(days_to_retain=days_to_retain, disable=disable)


class Dashboard(KubernetesObject):
    __slots__ = ()

    enabled: bool
    port: int
    ssl: bool
    url_prefix: str

    def __init__(self, enabled: bool = None, port: int = None, ssl: bool = None, url_prefix: str = None):
        super().__init__(enabled=enabled, port=port, ssl=ssl, url_prefix=url_prefix)


class DisruptionManagement(KubernetesObject):
    __slots__ = ()

    machine_disruption_budget_namespace: str
    manage_machine_disruption_budgets: bool
    manage_pod_budgets: bool
    osd_maintenance_timeout: int
    pg_health_check_timeout: int

    def __init__(
        self,
        machine_disruption_budget_namespace: str = None,
        manage_machine_disruption_budgets: bool = None,
        manage_pod_budgets: bool = None,
        osd_maintenance_timeout: int = None,
        pg_health_check_timeout: int = None,
    ):
        super().__init__(
            machine_disruption_budget_namespace=machine_disruption_budget_namespace,
            manage_machine_disruption_budgets=manage_machine_disruption_budgets,
            manage_pod_budgets=manage_pod_budgets,
            osd_maintenance_timeout=osd_maintenance_timeout,
            pg_health_check_timeout=pg_health_check_timeout,
        )


class External(KubernetesObject):
    __slots__ = ()

    enable: bool

    def __init__(self, enable: bool = None):
        super().__init__(enable=enable)


class DaemonHealthMON(KubernetesObject):
    __slots__ = ()

    disabled: bool
    interval: str
    timeout: str

    def __init__(self, disabled: bool = None, interval: str = None, timeout: str = None):
        super().__init__(disabled=disabled, interval=interval, timeout=timeout)


class OSD(KubernetesObject):
    __slots__ = ()

    disabled: bool
    interval: str
    timeout: str

    def __init__(self, disabled: bool = None, interval: str = None, timeout: str = None):
        super().__init__(disabled=disabled, interval=interval, timeout=timeout)


class Status(KubernetesObject):
    __slots__ = ()

    disabled: bool
    interval: str
    timeout: str

    def __init__(self, disabled: bool = None, interval: str = None, timeout: str = None):
        super().__init__(disabled=disabled, interval=interval, timeout=timeout)


class DaemonHealth(KubernetesObject):
    __slots__ = ()

    mon: DaemonHealthMON
    osd: OSD
    status: Status

    def __init__(self, mon: DaemonHealthMON = None, osd: OSD = None, status: Status = None):
        super().__init__(mon=mon, osd=osd, status=status)


class CephClusterSpecHealthCheck(KubernetesObject):
    __slots__ = ()

    daemon_health: DaemonHealth
    liveness_probe: Dict[str, core.Probe]

    def __init__(self, daemon_health: DaemonHealth = None, liveness_probe: Dict[str, core.Probe] = None):
        super().__init__(daemon_health=daemon_health, liveness_probe=liveness_probe)


class LogCollector(KubernetesObject):
    __slots__ = ()

    enabled: bool
    periodicity: str

    def __init__(self, enabled: bool = None, periodicity: str = None):
        super().__init__(enabled=enabled, periodicity=periodicity)


class Module(KubernetesObject):
    __slots__ = ()

    enabled: bool
    name: str

    def __init__(self, enabled: bool = None, name: str = None):
        super().__init__(enabled=enabled, name=name)


class MGR(KubernetesObject):
    __slots__ = ()

    allow_multiple_per_node: bool
    count: int
    modules: List[Module]

    def __init__(self, allow_multiple_per_node: bool = None, count: int = None, modules: List[Module] = None):
        super().__init__(allow_multiple_per_node=allow_multiple_per_node, count=count, modules=modules)


class StretchClusterZone(KubernetesObject):
    __slots__ = ()

    arbiter: bool
    name: str
    volume_claim_template: core.PersistentVolumeClaimTemplate

    def __init__(self, arbiter: bool = None, name: str = None, volume_claim_template: core.PersistentVolumeClaimTemplate = None):
        super().__init__(arbiter=arbiter, name=name, volume_claim_template=volume_claim_template)


class StretchCluster(KubernetesObject):
    __slots__ = ()

    failure_domain_label: str
    sub_failure_domain: str
    zones: List[StretchClusterZone]

    def __init__(self, failure_domain_label: str = None, sub_failure_domain: str = None, zones: List[StretchClusterZone] = None):
        super().__init__(failure_domain_label=failure_domain_label, sub_failure_domain=sub_failure_domain, zones=zones)


class CephClusterSpecMON(KubernetesObject):
    __slots__ = ()

    allow_multiple_per_node: bool
    count: int
    stretch_cluster: StretchCluster
    volume_claim_template: core.PersistentVolumeClaimTemplate

    def __init__(
        self,
        allow_multiple_per_node: bool = None,
        count: int = None,
        stretch_cluster: StretchCluster = None,
        volume_claim_template: core.PersistentVolumeClaimTemplate = None,
    ):
        super().__init__(
            allow_multiple_per_node=allow_multiple_per_node,
            count=count,
            stretch_cluster=stretch_cluster,
            volume_claim_template=volume_claim_template,
        )


class TargetRef(KubernetesObject):
    __slots__ = ()

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


class ExternalMgrEndpoint(KubernetesObject):
    __slots__ = ()

    _required_ = ["ip"]

    hostname: str
    ip: str
    node_name: str
    target_ref: TargetRef

    def __init__(self, hostname: str = None, ip: str = None, node_name: str = None, target_ref: TargetRef = None):
        super().__init__(hostname=hostname, ip=ip, node_name=node_name, target_ref=target_ref)


class Monitoring(KubernetesObject):
    __slots__ = ()

    enabled: bool
    external_mgr_endpoints: List[ExternalMgrEndpoint]
    external_mgr_prometheus_port: int
    rules_namespace: str

    def __init__(
        self,
        enabled: bool = None,
        external_mgr_endpoints: List[ExternalMgrEndpoint] = None,
        external_mgr_prometheus_port: int = None,
        rules_namespace: str = None,
    ):
        super().__init__(
            enabled=enabled,
            external_mgr_endpoints=external_mgr_endpoints,
            external_mgr_prometheus_port=external_mgr_prometheus_port,
            rules_namespace=rules_namespace,
        )


class Network(KubernetesObject):
    __slots__ = ()

    dual_stack: bool
    host_network: bool
    ip_family: str
    provider: str
    selectors: Dict[str, str]

    def __init__(
        self,
        dual_stack: bool = None,
        host_network: bool = None,
        ip_family: str = None,
        provider: str = None,
        selectors: Dict[str, str] = None,
    ):
        super().__init__(dual_stack=dual_stack, host_network=host_network, ip_family=ip_family, provider=provider, selectors=selectors)


class MatchExpression(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: List[str]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class MatchField(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "operator"]

    key: str
    operator: str
    values: List[str]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class Preference(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_fields: List[MatchField]

    def __init__(self, match_expressions: List[MatchExpression] = None, match_fields: List[MatchField] = None):
        super().__init__(match_expressions=match_expressions, match_fields=match_fields)


class NodeAffinityPreferredDuringSchedulingIgnoredDuringExecution(KubernetesObject):
    __slots__ = ()

    _required_ = ["preference", "weight"]

    preference: Preference
    weight: int

    def __init__(self, preference: Preference = None, weight: int = None):
        super().__init__(preference=preference, weight=weight)


class NodeSelectorTerm(KubernetesObject):
    __slots__ = ()

    match_expressions: List[MatchExpression]
    match_fields: List[MatchField]

    def __init__(self, match_expressions: List[MatchExpression] = None, match_fields: List[MatchField] = None):
        super().__init__(match_expressions=match_expressions, match_fields=match_fields)


class NodeAffinityRequiredDuringSchedulingIgnoredDuringExecution(KubernetesObject):
    __slots__ = ()

    _required_ = ["node_selector_terms"]

    node_selector_terms: List[NodeSelectorTerm]

    def __init__(self, node_selector_terms: List[NodeSelectorTerm] = None):
        super().__init__(node_selector_terms=node_selector_terms)


class NodeAffinity(KubernetesObject):
    __slots__ = ()

    preferred_during_scheduling_ignored_during_execution: List[NodeAffinityPreferredDuringSchedulingIgnoredDuringExecution]
    required_during_scheduling_ignored_during_execution: NodeAffinityRequiredDuringSchedulingIgnoredDuringExecution

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[NodeAffinityPreferredDuringSchedulingIgnoredDuringExecution] = None,
        required_during_scheduling_ignored_during_execution: NodeAffinityRequiredDuringSchedulingIgnoredDuringExecution = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAffinityTerm(KubernetesObject):
    __slots__ = ()

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


class PodAffinityPreferredDuringSchedulingIgnoredDuringExecution(KubernetesObject):
    __slots__ = ()

    _required_ = ["pod_affinity_term", "weight"]

    pod_affinity_term: PodAffinityTerm
    weight: int

    def __init__(self, pod_affinity_term: PodAffinityTerm = None, weight: int = None):
        super().__init__(pod_affinity_term=pod_affinity_term, weight=weight)


class PodAffinityRequiredDuringSchedulingIgnoredDuringExecution(KubernetesObject):
    __slots__ = ()

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


class PodAffinity(KubernetesObject):
    __slots__ = ()

    preferred_during_scheduling_ignored_during_execution: List[PodAffinityPreferredDuringSchedulingIgnoredDuringExecution]
    required_during_scheduling_ignored_during_execution: List[PodAffinityRequiredDuringSchedulingIgnoredDuringExecution]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[PodAffinityPreferredDuringSchedulingIgnoredDuringExecution] = None,
        required_during_scheduling_ignored_during_execution: List[PodAffinityRequiredDuringSchedulingIgnoredDuringExecution] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution(KubernetesObject):
    __slots__ = ()

    _required_ = ["pod_affinity_term", "weight"]

    pod_affinity_term: PodAffinityTerm
    weight: int

    def __init__(self, pod_affinity_term: PodAffinityTerm = None, weight: int = None):
        super().__init__(pod_affinity_term=pod_affinity_term, weight=weight)


class PodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution(KubernetesObject):
    __slots__ = ()

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


class PodAntiAffinity(KubernetesObject):
    __slots__ = ()

    preferred_during_scheduling_ignored_during_execution: List[PodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution]
    required_during_scheduling_ignored_during_execution: List[PodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[PodAntiAffinityPreferredDuringSchedulingIgnoredDuringExecution] = None,
        required_during_scheduling_ignored_during_execution: List[PodAntiAffinityRequiredDuringSchedulingIgnoredDuringExecution] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class TopologySpreadConstraint(KubernetesObject):
    __slots__ = ()

    _required_ = ["max_skew", "topology_key", "when_unsatisfiable"]

    label_selector: meta.LabelSelector
    max_skew: int
    topology_key: str
    when_unsatisfiable: str

    def __init__(
        self, label_selector: meta.LabelSelector = None, max_skew: int = None, topology_key: str = None, when_unsatisfiable: str = None
    ):
        super().__init__(label_selector=label_selector, max_skew=max_skew, topology_key=topology_key, when_unsatisfiable=when_unsatisfiable)


class Placement(KubernetesObject):
    __slots__ = ()

    node_affinity: NodeAffinity
    pod_affinity: PodAffinity
    pod_anti_affinity: PodAntiAffinity
    tolerations: List[core.Toleration]
    topology_spread_constraints: List[TopologySpreadConstraint]

    def __init__(
        self,
        node_affinity: NodeAffinity = None,
        pod_affinity: PodAffinity = None,
        pod_anti_affinity: PodAntiAffinity = None,
        tolerations: List[core.Toleration] = None,
        topology_spread_constraints: List[TopologySpreadConstraint] = None,
    ):
        super().__init__(
            node_affinity=node_affinity,
            pod_affinity=pod_affinity,
            pod_anti_affinity=pod_anti_affinity,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
        )


class KMS(KubernetesObject):
    __slots__ = ()

    connection_details: Dict[str, str]
    token_secret_name: str

    def __init__(self, connection_details: Dict[str, str] = None, token_secret_name: str = None):
        super().__init__(connection_details=connection_details, token_secret_name=token_secret_name)


class Security(KubernetesObject):
    __slots__ = ()

    kms: KMS

    def __init__(self, kms: KMS = None):
        super().__init__(kms=kms)


class Device(KubernetesObject):
    __slots__ = ()

    config: Dict[str, str]
    fullpath: str
    name: str

    def __init__(self, config: Dict[str, str] = None, fullpath: str = None, name: str = None):
        super().__init__(config=config, fullpath=fullpath, name=name)


class Node(KubernetesObject):
    __slots__ = ()

    config: Dict[str, str]
    device_filter: str
    device_path_filter: str
    devices: List[Device]
    name: str
    resources: core.ResourceRequirements
    use_all_devices: bool
    volume_claim_templates: List[core.PersistentVolumeClaimTemplate]

    def __init__(
        self,
        config: Dict[str, str] = None,
        device_filter: str = None,
        device_path_filter: str = None,
        devices: List[Device] = None,
        name: str = None,
        resources: core.ResourceRequirements = None,
        use_all_devices: bool = None,
        volume_claim_templates: List[core.PersistentVolumeClaimTemplate] = None,
    ):
        super().__init__(
            config=config,
            device_filter=device_filter,
            device_path_filter=device_path_filter,
            devices=devices,
            name=name,
            resources=resources,
            use_all_devices=use_all_devices,
            volume_claim_templates=volume_claim_templates,
        )


class StorageClassDeviceSet(KubernetesObject):
    __slots__ = ()

    _required_ = ["count", "name", "volume_claim_templates"]

    config: Dict[str, str]
    count: int
    encrypted: bool
    name: str
    placement: Placement
    portable: bool
    prepare_placement: Placement
    resources: core.ResourceRequirements
    scheduler_name: str
    tune_device_class: bool
    tune_fast_device_class: bool
    volume_claim_templates: List[core.PersistentVolumeClaimTemplate]

    def __init__(
        self,
        config: Dict[str, str] = None,
        count: int = None,
        encrypted: bool = None,
        name: str = None,
        placement: Placement = None,
        portable: bool = None,
        prepare_placement: Placement = None,
        resources: core.ResourceRequirements = None,
        scheduler_name: str = None,
        tune_device_class: bool = None,
        tune_fast_device_class: bool = None,
        volume_claim_templates: List[core.PersistentVolumeClaimTemplate] = None,
    ):
        super().__init__(
            config=config,
            count=count,
            encrypted=encrypted,
            name=name,
            placement=placement,
            portable=portable,
            prepare_placement=prepare_placement,
            resources=resources,
            scheduler_name=scheduler_name,
            tune_device_class=tune_device_class,
            tune_fast_device_class=tune_fast_device_class,
            volume_claim_templates=volume_claim_templates,
        )


class Storage(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "only_apply_osd_placement": "onlyApplyOSDPlacement",
    }
    _revfield_names_ = {
        "onlyApplyOSDPlacement": "only_apply_osd_placement",
    }

    config: Dict[str, str]
    device_filter: str
    device_path_filter: str
    devices: List[Device]
    nodes: List[Node]
    only_apply_osd_placement: bool
    storage_class_device_sets: List[StorageClassDeviceSet]
    use_all_devices: bool
    use_all_nodes: bool
    volume_claim_templates: List[core.PersistentVolumeClaimTemplate]

    def __init__(
        self,
        config: Dict[str, str] = None,
        device_filter: str = None,
        device_path_filter: str = None,
        devices: List[Device] = None,
        nodes: List[Node] = None,
        only_apply_osd_placement: bool = None,
        storage_class_device_sets: List[StorageClassDeviceSet] = None,
        use_all_devices: bool = None,
        use_all_nodes: bool = None,
        volume_claim_templates: List[core.PersistentVolumeClaimTemplate] = None,
    ):
        super().__init__(
            config=config,
            device_filter=device_filter,
            device_path_filter=device_path_filter,
            devices=devices,
            nodes=nodes,
            only_apply_osd_placement=only_apply_osd_placement,
            storage_class_device_sets=storage_class_device_sets,
            use_all_devices=use_all_devices,
            use_all_nodes=use_all_nodes,
            volume_claim_templates=volume_claim_templates,
        )


class CephClusterSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "remove_os_ds_if_out_and_safe_to_remove": "removeOSDsIfOutAndSafeToRemove",
        "wait_timeout_for_healthy_osd_in_minutes": "waitTimeoutForHealthyOSDInMinutes",
    }
    _revfield_names_ = {
        "removeOSDsIfOutAndSafeToRemove": "remove_os_ds_if_out_and_safe_to_remove",
        "waitTimeoutForHealthyOSDInMinutes": "wait_timeout_for_healthy_osd_in_minutes",
    }

    annotations: Dict[str, Dict[str, str]]
    ceph_version: CephVersion
    cleanup_policy: CleanupPolicy
    continue_upgrade_after_checks_even_if_not_healthy: bool
    crash_collector: CrashCollector
    dashboard: Dashboard
    data_dir_host_path: str
    disruption_management: DisruptionManagement
    external: External
    health_check: CephClusterSpecHealthCheck
    labels: Dict[str, Dict[str, str]]
    log_collector: LogCollector
    mgr: MGR
    mon: CephClusterSpecMON
    monitoring: Monitoring
    network: Network
    placement: Dict[str, Placement]
    priority_class_names: Dict[str, str]
    remove_os_ds_if_out_and_safe_to_remove: bool
    resources: Dict[str, core.ResourceRequirements]
    security: Security
    skip_upgrade_checks: bool
    storage: Storage
    wait_timeout_for_healthy_osd_in_minutes: int

    def __init__(
        self,
        annotations: Dict[str, Dict[str, str]] = None,
        ceph_version: CephVersion = None,
        cleanup_policy: CleanupPolicy = None,
        continue_upgrade_after_checks_even_if_not_healthy: bool = None,
        crash_collector: CrashCollector = None,
        dashboard: Dashboard = None,
        data_dir_host_path: str = None,
        disruption_management: DisruptionManagement = None,
        external: External = None,
        health_check: CephClusterSpecHealthCheck = None,
        labels: Dict[str, Dict[str, str]] = None,
        log_collector: LogCollector = None,
        mgr: MGR = None,
        mon: CephClusterSpecMON = None,
        monitoring: Monitoring = None,
        network: Network = None,
        placement: Dict[str, Placement] = None,
        priority_class_names: Dict[str, str] = None,
        remove_os_ds_if_out_and_safe_to_remove: bool = None,
        resources: Dict[str, core.ResourceRequirements] = None,
        security: Security = None,
        skip_upgrade_checks: bool = None,
        storage: Storage = None,
        wait_timeout_for_healthy_osd_in_minutes: int = None,
    ):
        super().__init__(
            annotations=annotations,
            ceph_version=ceph_version,
            cleanup_policy=cleanup_policy,
            continue_upgrade_after_checks_even_if_not_healthy=continue_upgrade_after_checks_even_if_not_healthy,
            crash_collector=crash_collector,
            dashboard=dashboard,
            data_dir_host_path=data_dir_host_path,
            disruption_management=disruption_management,
            external=external,
            health_check=health_check,
            labels=labels,
            log_collector=log_collector,
            mgr=mgr,
            mon=mon,
            monitoring=monitoring,
            network=network,
            placement=placement,
            priority_class_names=priority_class_names,
            remove_os_ds_if_out_and_safe_to_remove=remove_os_ds_if_out_and_safe_to_remove,
            resources=resources,
            security=security,
            skip_upgrade_checks=skip_upgrade_checks,
            storage=storage,
            wait_timeout_for_healthy_osd_in_minutes=wait_timeout_for_healthy_osd_in_minutes,
        )


class CephCluster(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephCluster"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephClusterSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephClusterSpec = None):
        super().__init__("ceph.rook.io/v1", "CephCluster", name, namespace, metadata=metadata, spec=spec)


class MetadataServer(KubernetesObject):
    __slots__ = ()

    _required_ = ["active_count"]

    active_count: int
    active_standby: bool
    annotations: Dict[str, str]
    labels: Dict[str, str]
    placement: Placement
    priority_class_name: str
    resources: core.ResourceRequirements

    def __init__(
        self,
        active_count: int = None,
        active_standby: bool = None,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        placement: Placement = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
    ):
        super().__init__(
            active_count=active_count,
            active_standby=active_standby,
            annotations=annotations,
            labels=labels,
            placement=placement,
            priority_class_name=priority_class_name,
            resources=resources,
        )


class SnapshotRetention(KubernetesObject):
    __slots__ = ()

    duration: str
    path: str

    def __init__(self, duration: str = None, path: str = None):
        super().__init__(duration=duration, path=path)


class CephFilesystemSpecMirroring(KubernetesObject):
    __slots__ = ()

    enabled: bool
    peers: Peer
    snapshot_retention: List[SnapshotRetention]
    snapshot_schedules: List[SnapshotSchedule]

    def __init__(
        self,
        enabled: bool = None,
        peers: Peer = None,
        snapshot_retention: List[SnapshotRetention] = None,
        snapshot_schedules: List[SnapshotSchedule] = None,
    ):
        super().__init__(enabled=enabled, peers=peers, snapshot_retention=snapshot_retention, snapshot_schedules=snapshot_schedules)


class CephFilesystemSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["data_pools", "metadata_pool", "metadata_server"]

    data_pools: List[CephBlockPoolSpec]
    metadata_pool: CephBlockPoolSpec
    metadata_server: MetadataServer
    mirroring: CephFilesystemSpecMirroring
    preserve_filesystem_on_delete: bool
    preserve_pools_on_delete: bool
    status_check: StatusCheck

    def __init__(
        self,
        data_pools: List[CephBlockPoolSpec] = None,
        metadata_pool: CephBlockPoolSpec = None,
        metadata_server: MetadataServer = None,
        mirroring: CephFilesystemSpecMirroring = None,
        preserve_filesystem_on_delete: bool = None,
        preserve_pools_on_delete: bool = None,
        status_check: StatusCheck = None,
    ):
        super().__init__(
            data_pools=data_pools,
            metadata_pool=metadata_pool,
            metadata_server=metadata_server,
            mirroring=mirroring,
            preserve_filesystem_on_delete=preserve_filesystem_on_delete,
            preserve_pools_on_delete=preserve_pools_on_delete,
            status_check=status_check,
        )


class CephFilesystem(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephFilesystem"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephFilesystemSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephFilesystemSpec = None):
        super().__init__("ceph.rook.io/v1", "CephFilesystem", name, namespace, metadata=metadata, spec=spec)


class CephFilesystemMirrorSpec(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    labels: Dict[str, str]
    placement: Placement
    priority_class_name: str
    resources: core.ResourceRequirements

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        placement: Placement = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
    ):
        super().__init__(
            annotations=annotations, labels=labels, placement=placement, priority_class_name=priority_class_name, resources=resources
        )


class CephFilesystemMirror(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephFilesystemMirror"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephFilesystemMirrorSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephFilesystemMirrorSpec = None):
        super().__init__("ceph.rook.io/v1", "CephFilesystemMirror", name, namespace, metadata=metadata, spec=spec)


class Rado(KubernetesObject):
    __slots__ = ()

    _required_ = ["namespace", "pool"]

    namespace: str
    pool: str

    def __init__(self, namespace: str = None, pool: str = None):
        super().__init__(namespace=namespace, pool=pool)


class Server(KubernetesObject):
    __slots__ = ()

    _required_ = ["active"]

    active: int
    annotations: Dict[str, str]
    labels: Dict[str, str]
    log_level: str
    placement: Placement
    priority_class_name: str
    resources: core.ResourceRequirements

    def __init__(
        self,
        active: int = None,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        log_level: str = None,
        placement: Placement = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
    ):
        super().__init__(
            active=active,
            annotations=annotations,
            labels=labels,
            log_level=log_level,
            placement=placement,
            priority_class_name=priority_class_name,
            resources=resources,
        )


class CephNFSSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["rados", "server"]

    rados: Rado
    server: Server

    def __init__(self, rados: Rado = None, server: Server = None):
        super().__init__(rados=rados, server=server)


class CephNFS(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephNFS"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephNFSSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephNFSSpec = None):
        super().__init__("ceph.rook.io/v1", "CephNFS", name, namespace, metadata=metadata, spec=spec)


class Pull(KubernetesObject):
    __slots__ = ()

    _required_ = ["endpoint"]

    endpoint: str

    def __init__(self, endpoint: str = None):
        super().__init__(endpoint=endpoint)


class CephObjectRealmSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["pull"]

    pull: Pull

    def __init__(self, pull: Pull = None):
        super().__init__(pull=pull)


class CephObjectRealm(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephObjectRealm"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CephObjectRealmSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephObjectRealmSpec = None):
        super().__init__("ceph.rook.io/v1", "CephObjectRealm", name, namespace, metadata=metadata, spec=spec)


class ExternalRgwEndpoint(KubernetesObject):
    __slots__ = ()

    _required_ = ["ip"]

    hostname: str
    ip: str
    node_name: str
    target_ref: TargetRef

    def __init__(self, hostname: str = None, ip: str = None, node_name: str = None, target_ref: TargetRef = None):
        super().__init__(hostname=hostname, ip=ip, node_name=node_name, target_ref=target_ref)


class Service(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]

    def __init__(self, annotations: Dict[str, str] = None):
        super().__init__(annotations=annotations)


class Gateway(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    ca_bundle_ref: str
    external_rgw_endpoints: List[ExternalRgwEndpoint]
    instances: int
    labels: Dict[str, str]
    placement: Placement
    port: int
    priority_class_name: str
    resources: core.ResourceRequirements
    secure_port: int
    service: Service
    ssl_certificate_ref: str

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        ca_bundle_ref: str = None,
        external_rgw_endpoints: List[ExternalRgwEndpoint] = None,
        instances: int = None,
        labels: Dict[str, str] = None,
        placement: Placement = None,
        port: int = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
        secure_port: int = None,
        service: Service = None,
        ssl_certificate_ref: str = None,
    ):
        super().__init__(
            annotations=annotations,
            ca_bundle_ref=ca_bundle_ref,
            external_rgw_endpoints=external_rgw_endpoints,
            instances=instances,
            labels=labels,
            placement=placement,
            port=port,
            priority_class_name=priority_class_name,
            resources=resources,
            secure_port=secure_port,
            service=service,
            ssl_certificate_ref=ssl_certificate_ref,
        )


class CephObjectStoreSpecHealthCheck(KubernetesObject):
    __slots__ = ()

    bucket: Bucket
    liveness_probe: core.Probe

    def __init__(self, bucket: Bucket = None, liveness_probe: core.Probe = None):
        super().__init__(bucket=bucket, liveness_probe=liveness_probe)


class CephObjectStoreSpecZone(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class CephObjectStoreSpec(KubernetesObject):
    __slots__ = ()

    data_pool: CephBlockPoolSpec
    gateway: Gateway
    health_check: CephObjectStoreSpecHealthCheck
    metadata_pool: CephBlockPoolSpec
    preserve_pools_on_delete: bool
    security: Security
    zone: CephObjectStoreSpecZone

    def __init__(
        self,
        data_pool: CephBlockPoolSpec = None,
        gateway: Gateway = None,
        health_check: CephObjectStoreSpecHealthCheck = None,
        metadata_pool: CephBlockPoolSpec = None,
        preserve_pools_on_delete: bool = None,
        security: Security = None,
        zone: CephObjectStoreSpecZone = None,
    ):
        super().__init__(
            data_pool=data_pool,
            gateway=gateway,
            health_check=health_check,
            metadata_pool=metadata_pool,
            preserve_pools_on_delete=preserve_pools_on_delete,
            security=security,
            zone=zone,
        )


class CephObjectStore(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephObjectStore"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephObjectStoreSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephObjectStoreSpec = None):
        super().__init__("ceph.rook.io/v1", "CephObjectStore", name, namespace, metadata=metadata, spec=spec)


class CephObjectStoreUserSpecQuota(KubernetesObject):
    __slots__ = ()

    max_buckets: int
    max_objects: int
    max_size: core.IntOrString

    def __init__(self, max_buckets: int = None, max_objects: int = None, max_size: core.IntOrString = None):
        super().__init__(max_buckets=max_buckets, max_objects=max_objects, max_size=max_size)


class CephObjectStoreUserSpec(KubernetesObject):
    __slots__ = ()

    capabilities: Capabilitie
    display_name: str
    quotas: CephObjectStoreUserSpecQuota
    store: str

    def __init__(
        self, capabilities: Capabilitie = None, display_name: str = None, quotas: CephObjectStoreUserSpecQuota = None, store: str = None
    ):
        super().__init__(capabilities=capabilities, display_name=display_name, quotas=quotas, store=store)


class CephObjectStoreUser(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephObjectStoreUser"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephObjectStoreUserSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephObjectStoreUserSpec = None):
        super().__init__("ceph.rook.io/v1", "CephObjectStoreUser", name, namespace, metadata=metadata, spec=spec)


class CephObjectZoneSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["data_pool", "metadata_pool", "zone_group"]

    data_pool: CephBlockPoolSpec
    metadata_pool: CephBlockPoolSpec
    zone_group: str

    def __init__(self, data_pool: CephBlockPoolSpec = None, metadata_pool: CephBlockPoolSpec = None, zone_group: str = None):
        super().__init__(data_pool=data_pool, metadata_pool=metadata_pool, zone_group=zone_group)


class CephObjectZone(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephObjectZone"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephObjectZoneSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephObjectZoneSpec = None):
        super().__init__("ceph.rook.io/v1", "CephObjectZone", name, namespace, metadata=metadata, spec=spec)


class CephObjectZoneGroupSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["realm"]

    realm: str

    def __init__(self, realm: str = None):
        super().__init__(realm=realm)


class CephObjectZoneGroup(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephObjectZoneGroup"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephObjectZoneGroupSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephObjectZoneGroupSpec = None):
        super().__init__("ceph.rook.io/v1", "CephObjectZoneGroup", name, namespace, metadata=metadata, spec=spec)


class CephRBDMirrorSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["count"]

    annotations: Dict[str, str]
    count: int
    labels: Dict[str, str]
    peers: Peer
    placement: Placement
    priority_class_name: str
    resources: core.ResourceRequirements

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        count: int = None,
        labels: Dict[str, str] = None,
        peers: Peer = None,
        placement: Placement = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
    ):
        super().__init__(
            annotations=annotations,
            count=count,
            labels=labels,
            peers=peers,
            placement=placement,
            priority_class_name=priority_class_name,
            resources=resources,
        )


class CephRBDMirror(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "ceph.rook.io/v1"
    _kind_ = "CephRBDMirror"
    _scope_ = "namespace"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CephRBDMirrorSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CephRBDMirrorSpec = None):
        super().__init__("ceph.rook.io/v1", "CephRBDMirror", name, namespace, metadata=metadata, spec=spec)


class DataSource(KubernetesObject):
    __slots__ = ()

    _required_ = ["kind", "name"]

    api_group: str
    kind: str
    name: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class Endpoint(KubernetesObject):
    __slots__ = ()

    additional_config: Dict[str, Any]
    bucket_host: str
    bucket_name: str
    bucket_port: int
    region: str
    sub_region: str

    def __init__(
        self,
        additional_config: Dict[str, Any] = None,
        bucket_host: str = None,
        bucket_name: str = None,
        bucket_port: int = None,
        region: str = None,
        sub_region: str = None,
    ):
        super().__init__(
            additional_config=additional_config,
            bucket_host=bucket_host,
            bucket_name=bucket_name,
            bucket_port=bucket_port,
            region=region,
            sub_region=sub_region,
        )


class ObjectBucketSpec(KubernetesObject):
    __slots__ = ()

    additional_state: Dict[str, Any]
    authentication: Dict[str, Any]
    claim_ref: Dict[str, Any]
    endpoint: Endpoint
    reclaim_policy: str
    storage_class_name: str

    def __init__(
        self,
        additional_state: Dict[str, Any] = None,
        authentication: Dict[str, Any] = None,
        claim_ref: Dict[str, Any] = None,
        endpoint: Endpoint = None,
        reclaim_policy: str = None,
        storage_class_name: str = None,
    ):
        super().__init__(
            additional_state=additional_state,
            authentication=authentication,
            claim_ref=claim_ref,
            endpoint=endpoint,
            reclaim_policy=reclaim_policy,
            storage_class_name=storage_class_name,
        )


class ObjectBucket(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "objectbucket.io/v1alpha1"
    _kind_ = "ObjectBucket"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: ObjectBucketSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: ObjectBucketSpec = None):
        super().__init__("objectbucket.io/v1alpha1", "ObjectBucket", name, "", metadata=metadata, spec=spec)


class ObjectBucketClaimSpec(KubernetesObject):
    __slots__ = ()

    additional_config: Dict[str, Any]
    bucket_name: str
    generate_bucket_name: str
    object_bucket_name: str
    storage_class_name: str

    def __init__(
        self,
        additional_config: Dict[str, Any] = None,
        bucket_name: str = None,
        generate_bucket_name: str = None,
        object_bucket_name: str = None,
        storage_class_name: str = None,
    ):
        super().__init__(
            additional_config=additional_config,
            bucket_name=bucket_name,
            generate_bucket_name=generate_bucket_name,
            object_bucket_name=object_bucket_name,
            storage_class_name=storage_class_name,
        )


class ObjectBucketClaim(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "objectbucket.io/v1alpha1"
    _kind_ = "ObjectBucketClaim"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: ObjectBucketClaimSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ObjectBucketClaimSpec = None):
        super().__init__("objectbucket.io/v1alpha1", "ObjectBucketClaim", name, namespace, metadata=metadata, spec=spec)


class Volume(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "rook.io/v1alpha2"
    _kind_ = "Volume"
    _scope_ = "namespace"

    _required_ = ["attachments", "metadata"]

    attachments: List[Attachment]
    metadata: meta.ObjectMeta

    def __init__(self, name: str, namespace: str = None, attachments: List[Attachment] = None, metadata: meta.ObjectMeta = None):
        super().__init__("rook.io/v1alpha2", "Volume", name, namespace, attachments=attachments, metadata=metadata)


class VolumeReplicationSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["data_source", "replication_state", "volume_replication_class"]

    data_source: DataSource
    replication_state: str
    volume_replication_class: str

    def __init__(self, data_source: DataSource = None, replication_state: str = None, volume_replication_class: str = None):
        super().__init__(data_source=data_source, replication_state=replication_state, volume_replication_class=volume_replication_class)


class VolumeReplication(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "replication.storage.openshift.io/v1alpha1"
    _kind_ = "VolumeReplication"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: VolumeReplicationSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: VolumeReplicationSpec = None):
        super().__init__("replication.storage.openshift.io/v1alpha1", "VolumeReplication", name, namespace, metadata=metadata, spec=spec)


class VolumeReplicationClassSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["provisioner"]

    parameters: Dict[str, str]
    provisioner: str

    def __init__(self, parameters: Dict[str, str] = None, provisioner: str = None):
        super().__init__(parameters=parameters, provisioner=provisioner)


class VolumeReplicationClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "replication.storage.openshift.io/v1alpha1"
    _kind_ = "VolumeReplicationClass"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: VolumeReplicationClassSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: VolumeReplicationClassSpec = None):
        super().__init__("replication.storage.openshift.io/v1alpha1", "VolumeReplicationClass", name, "", metadata=metadata, spec=spec)
