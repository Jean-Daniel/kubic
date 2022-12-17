import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from ..api import core, meta


class Azure(KubernetesObject):
    __slots__ = ()

    _required_ = ["container"]

    container: str

    def __init__(self, container: str = None):
        super().__init__(container=container)


class JOB(KubernetesObject):
    __slots__ = ()

    affinity: core.Affinity
    priority_class_name: str
    resources: core.ResourceRequirements
    tolerations: list[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
        tolerations: list[core.Toleration] = None,
    ):
        super().__init__(affinity=affinity, priority_class_name=priority_class_name, resources=resources, tolerations=tolerations)


class Manual(KubernetesObject):
    __slots__ = ()

    _required_ = ["repo_name"]

    options: list[str]
    repo_name: str

    def __init__(self, options: list[str] = None, repo_name: str = None):
        super().__init__(options=options, repo_name=repo_name)


class Metadata(KubernetesObject):
    __slots__ = ()

    annotations: dict[str, str]
    labels: dict[str, str]

    def __init__(self, annotations: dict[str, str] = None, labels: dict[str, str] = None):
        super().__init__(annotations=annotations, labels=labels)


class RepoHost(KubernetesObject):
    __slots__ = ()

    affinity: core.Affinity
    priority_class_name: str
    resources: core.ResourceRequirements
    ssh_config_map: core.SecretProjection
    ssh_secret: core.SecretProjection
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]

    def __init__(
        self,
        affinity: core.Affinity = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
        ssh_config_map: core.SecretProjection = None,
        ssh_secret: core.SecretProjection = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
    ):
        super().__init__(
            affinity=affinity,
            priority_class_name=priority_class_name,
            resources=resources,
            ssh_config_map=ssh_config_map,
            ssh_secret=ssh_secret,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
        )


class GCS(KubernetesObject):
    __slots__ = ()

    _required_ = ["bucket"]

    bucket: str

    def __init__(self, bucket: str = None):
        super().__init__(bucket=bucket)


class S3(KubernetesObject):
    __slots__ = ()

    _required_ = ["bucket", "endpoint", "region"]

    bucket: str
    endpoint: str
    region: str

    def __init__(self, bucket: str = None, endpoint: str = None, region: str = None):
        super().__init__(bucket=bucket, endpoint=endpoint, region=region)


class Schedule(KubernetesObject):
    __slots__ = ()

    differential: str
    full: str
    incremental: str

    def __init__(self, differential: str = None, full: str = None, incremental: str = None):
        super().__init__(differential=differential, full=full, incremental=incremental)


class RepoVolume(KubernetesObject):
    __slots__ = ()

    _required_ = ["volume_claim_spec"]

    volume_claim_spec: core.PersistentVolumeClaimSpec

    def __init__(self, volume_claim_spec: core.PersistentVolumeClaimSpec = None):
        super().__init__(volume_claim_spec=volume_claim_spec)


class Repo(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    azure: Azure
    gcs: GCS
    name: str
    s3: S3
    schedules: Schedule
    volume: RepoVolume

    def __init__(
        self, azure: Azure = None, gcs: GCS = None, name: str = None, s3: S3 = None, schedules: Schedule = None, volume: RepoVolume = None
    ):
        super().__init__(azure=azure, gcs=gcs, name=name, s3=s3, schedules=schedules, volume=volume)


class Restore(KubernetesObject):
    __slots__ = ()

    _required_ = ["enabled", "repo_name"]

    affinity: core.Affinity
    cluster_name: str
    cluster_namespace: str
    enabled: bool
    options: list[str]
    priority_class_name: str
    repo_name: str
    resources: core.ResourceRequirements
    tolerations: list[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        cluster_name: str = None,
        cluster_namespace: str = None,
        enabled: bool = None,
        options: list[str] = None,
        priority_class_name: str = None,
        repo_name: str = None,
        resources: core.ResourceRequirements = None,
        tolerations: list[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            cluster_name=cluster_name,
            cluster_namespace=cluster_namespace,
            enabled=enabled,
            options=options,
            priority_class_name=priority_class_name,
            repo_name=repo_name,
            resources=resources,
            tolerations=tolerations,
        )


class SidecarPgbackrest(KubernetesObject):
    __slots__ = ()

    resources: core.ResourceRequirements

    def __init__(self, resources: core.ResourceRequirements = None):
        super().__init__(resources=resources)


class PgbackrestConfig(KubernetesObject):
    __slots__ = ()

    resources: core.ResourceRequirements

    def __init__(self, resources: core.ResourceRequirements = None):
        super().__init__(resources=resources)


class PgbackrestSidecar(KubernetesObject):
    __slots__ = ()

    pgbackrest: SidecarPgbackrest
    pgbackrest_config: PgbackrestConfig

    def __init__(self, pgbackrest: SidecarPgbackrest = None, pgbackrest_config: PgbackrestConfig = None):
        super().__init__(pgbackrest=pgbackrest, pgbackrest_config=pgbackrest_config)


class BackupPgbackrest(KubernetesObject):
    __slots__ = ()

    _required_ = ["repos"]

    _revfield_names_ = {
        "global": "global_",
    }

    configuration: list[core.VolumeProjection]
    global_: dict[str, str]
    image: str
    jobs: JOB
    manual: Manual
    metadata: Metadata
    repo_host: RepoHost
    repos: list[Repo]
    restore: Restore
    sidecars: PgbackrestSidecar

    def __init__(
        self,
        configuration: list[core.VolumeProjection] = None,
        global_: dict[str, str] = None,
        image: str = None,
        jobs: JOB = None,
        manual: Manual = None,
        metadata: Metadata = None,
        repo_host: RepoHost = None,
        repos: list[Repo] = None,
        restore: Restore = None,
        sidecars: PgbackrestSidecar = None,
    ):
        super().__init__(
            configuration=configuration,
            global_=global_,
            image=image,
            jobs=jobs,
            manual=manual,
            metadata=metadata,
            repo_host=repo_host,
            repos=repos,
            restore=restore,
            sidecars=sidecars,
        )


class Backup(KubernetesObject):
    __slots__ = ()

    _required_ = ["pgbackrest"]

    pgbackrest: BackupPgbackrest

    def __init__(self, pgbackrest: BackupPgbackrest = None):
        super().__init__(pgbackrest=pgbackrest)


class DataSourcePgbackrest(KubernetesObject):
    __slots__ = ()

    _required_ = ["repo", "stanza"]

    _revfield_names_ = {
        "global": "global_",
    }

    affinity: core.Affinity
    configuration: list[core.VolumeProjection]
    global_: dict[str, str]
    options: list[str]
    priority_class_name: str
    repo: Repo
    resources: core.ResourceRequirements
    stanza: str
    tolerations: list[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        configuration: list[core.VolumeProjection] = None,
        global_: dict[str, str] = None,
        options: list[str] = None,
        priority_class_name: str = None,
        repo: Repo = None,
        resources: core.ResourceRequirements = None,
        stanza: str = None,
        tolerations: list[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            configuration=configuration,
            global_=global_,
            options=options,
            priority_class_name=priority_class_name,
            repo=repo,
            resources=resources,
            stanza=stanza,
            tolerations=tolerations,
        )


class DataSourcePostgresCluster(KubernetesObject):
    __slots__ = ()

    _required_ = ["repo_name"]

    affinity: core.Affinity
    cluster_name: str
    cluster_namespace: str
    options: list[str]
    priority_class_name: str
    repo_name: str
    resources: core.ResourceRequirements
    tolerations: list[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        cluster_name: str = None,
        cluster_namespace: str = None,
        options: list[str] = None,
        priority_class_name: str = None,
        repo_name: str = None,
        resources: core.ResourceRequirements = None,
        tolerations: list[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            cluster_name=cluster_name,
            cluster_namespace=cluster_namespace,
            options=options,
            priority_class_name=priority_class_name,
            repo_name=repo_name,
            resources=resources,
            tolerations=tolerations,
        )


class PgBackRestVolume(KubernetesObject):
    __slots__ = ()

    _required_ = ["pvc_name"]

    directory: str
    pvc_name: str

    def __init__(self, directory: str = None, pvc_name: str = None):
        super().__init__(directory=directory, pvc_name=pvc_name)


class PgDataVolume(KubernetesObject):
    __slots__ = ()

    _required_ = ["pvc_name"]

    directory: str
    pvc_name: str

    def __init__(self, directory: str = None, pvc_name: str = None):
        super().__init__(directory=directory, pvc_name=pvc_name)


class PgWALVolume(KubernetesObject):
    __slots__ = ()

    _required_ = ["pvc_name"]

    directory: str
    pvc_name: str

    def __init__(self, directory: str = None, pvc_name: str = None):
        super().__init__(directory=directory, pvc_name=pvc_name)


class DataSourceVolume(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "pg_wal_volume": "pgWALVolume",
    }
    _revfield_names_ = {
        "pgWALVolume": "pg_wal_volume",
    }

    pg_back_rest_volume: PgBackRestVolume
    pg_data_volume: PgDataVolume
    pg_wal_volume: PgWALVolume

    def __init__(
        self, pg_back_rest_volume: PgBackRestVolume = None, pg_data_volume: PgDataVolume = None, pg_wal_volume: PgWALVolume = None
    ):
        super().__init__(pg_back_rest_volume=pg_back_rest_volume, pg_data_volume=pg_data_volume, pg_wal_volume=pg_wal_volume)


class DataSource(KubernetesObject):
    __slots__ = ()

    pgbackrest: DataSourcePgbackrest
    postgres_cluster: DataSourcePostgresCluster
    volumes: DataSourceVolume

    def __init__(
        self, pgbackrest: DataSourcePgbackrest = None, postgres_cluster: DataSourcePostgresCluster = None, volumes: DataSourceVolume = None
    ):
        super().__init__(pgbackrest=pgbackrest, postgres_cluster=postgres_cluster, volumes=volumes)


class DatabaseInitSQL(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "name"]

    key: str
    name: str

    def __init__(self, key: str = None, name: str = None):
        super().__init__(key=key, name=name)


class Exporter(KubernetesObject):
    __slots__ = ()

    configuration: list[core.VolumeProjection]
    image: str
    resources: core.ResourceRequirements

    def __init__(self, configuration: list[core.VolumeProjection] = None, image: str = None, resources: core.ResourceRequirements = None):
        super().__init__(configuration=configuration, image=image, resources=resources)


class ReplicaCertCopy(KubernetesObject):
    __slots__ = ()

    resources: core.ResourceRequirements

    def __init__(self, resources: core.ResourceRequirements = None):
        super().__init__(resources=resources)


class InstanceSidecar(KubernetesObject):
    __slots__ = ()

    replica_cert_copy: ReplicaCertCopy

    def __init__(self, replica_cert_copy: ReplicaCertCopy = None):
        super().__init__(replica_cert_copy=replica_cert_copy)


class Instance(KubernetesObject):
    __slots__ = ()

    _required_ = ["data_volume_claim_spec"]

    affinity: core.Affinity
    containers: list[core.Container]
    data_volume_claim_spec: core.PersistentVolumeClaimSpec
    metadata: Metadata
    min_available: core.IntOrString
    name: str
    priority_class_name: str
    replicas: int
    resources: core.ResourceRequirements
    sidecars: InstanceSidecar
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    wal_volume_claim_spec: core.PersistentVolumeClaimSpec

    def __init__(
        self,
        affinity: core.Affinity = None,
        containers: list[core.Container] = None,
        data_volume_claim_spec: core.PersistentVolumeClaimSpec = None,
        metadata: Metadata = None,
        min_available: core.IntOrString = None,
        name: str = None,
        priority_class_name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        sidecars: InstanceSidecar = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        wal_volume_claim_spec: core.PersistentVolumeClaimSpec = None,
    ):
        super().__init__(
            affinity=affinity,
            containers=containers,
            data_volume_claim_spec=data_volume_claim_spec,
            metadata=metadata,
            min_available=min_available,
            name=name,
            priority_class_name=priority_class_name,
            replicas=replicas,
            resources=resources,
            sidecars=sidecars,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
            wal_volume_claim_spec=wal_volume_claim_spec,
        )


class Pgmonitor(KubernetesObject):
    __slots__ = ()

    exporter: Exporter

    def __init__(self, exporter: Exporter = None):
        super().__init__(exporter=exporter)


class Monitoring(KubernetesObject):
    __slots__ = ()

    pgmonitor: Pgmonitor

    def __init__(self, pgmonitor: Pgmonitor = None):
        super().__init__(pgmonitor=pgmonitor)


class PGUpgradeSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["from_postgres_version", "postgres_cluster_name", "to_postgres_version"]

    affinity: core.Affinity
    from_postgres_version: int
    image: str
    image_pull_policy: str
    image_pull_secrets: list[core.LocalObjectReference]
    metadata: Metadata
    postgres_cluster_name: str
    priority_class_name: str
    resources: core.ResourceRequirements
    to_postgres_image: str
    to_postgres_version: int
    tolerations: list[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        from_postgres_version: int = None,
        image: str = None,
        image_pull_policy: str = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        metadata: Metadata = None,
        postgres_cluster_name: str = None,
        priority_class_name: str = None,
        resources: core.ResourceRequirements = None,
        to_postgres_image: str = None,
        to_postgres_version: int = None,
        tolerations: list[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            from_postgres_version=from_postgres_version,
            image=image,
            image_pull_policy=image_pull_policy,
            image_pull_secrets=image_pull_secrets,
            metadata=metadata,
            postgres_cluster_name=postgres_cluster_name,
            priority_class_name=priority_class_name,
            resources=resources,
            to_postgres_image=to_postgres_image,
            to_postgres_version=to_postgres_version,
            tolerations=tolerations,
        )


class PGUpgrade(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "postgres-operator.crunchydata.com/v1beta1"
    _kind_ = "PGUpgrade"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PGUpgradeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PGUpgradeSpec = None):
        super().__init__("postgres-operator.crunchydata.com/v1beta1", "PGUpgrade", name, namespace, metadata=metadata, spec=spec)


class Password(KubernetesObject):
    __slots__ = ()

    _required_ = ["type"]

    type: str

    def __init__(self, type: str = None):
        super().__init__(type=type)


class Switchover(KubernetesObject):
    __slots__ = ()

    _required_ = ["enabled"]

    enabled: bool
    target_instance: str
    type: str

    def __init__(self, enabled: bool = None, target_instance: str = None, type: str = None):
        super().__init__(enabled=enabled, target_instance=target_instance, type=type)


class Patroni(KubernetesObject):
    __slots__ = ()

    dynamic_configuration: dict[str, t.Any]
    leader_lease_duration_seconds: int
    port: int
    switchover: Switchover
    sync_period_seconds: int

    def __init__(
        self,
        dynamic_configuration: dict[str, t.Any] = None,
        leader_lease_duration_seconds: int = None,
        port: int = None,
        switchover: Switchover = None,
        sync_period_seconds: int = None,
    ):
        super().__init__(
            dynamic_configuration=dynamic_configuration,
            leader_lease_duration_seconds=leader_lease_duration_seconds,
            port=port,
            switchover=switchover,
            sync_period_seconds=sync_period_seconds,
        )


class PgAdminConfig(KubernetesObject):
    __slots__ = ()

    files: list[core.VolumeProjection]
    ldap_bind_password: core.ConfigMapKeySelector
    settings: dict[str, t.Any]

    def __init__(
        self,
        files: list[core.VolumeProjection] = None,
        ldap_bind_password: core.ConfigMapKeySelector = None,
        settings: dict[str, t.Any] = None,
    ):
        super().__init__(files=files, ldap_bind_password=ldap_bind_password, settings=settings)


class Service(KubernetesObject):
    __slots__ = ()

    metadata: Metadata
    node_port: int
    type: str

    def __init__(self, metadata: Metadata = None, node_port: int = None, type: str = None):
        super().__init__(metadata=metadata, node_port=node_port, type=type)


class PgAdmin(KubernetesObject):
    __slots__ = ()

    _required_ = ["data_volume_claim_spec"]

    affinity: core.Affinity
    config: PgAdminConfig
    data_volume_claim_spec: core.PersistentVolumeClaimSpec
    image: str
    metadata: Metadata
    priority_class_name: str
    replicas: int
    resources: core.ResourceRequirements
    service: Service
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config: PgAdminConfig = None,
        data_volume_claim_spec: core.PersistentVolumeClaimSpec = None,
        image: str = None,
        metadata: Metadata = None,
        priority_class_name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        service: Service = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
    ):
        super().__init__(
            affinity=affinity,
            config=config,
            data_volume_claim_spec=data_volume_claim_spec,
            image=image,
            metadata=metadata,
            priority_class_name=priority_class_name,
            replicas=replicas,
            resources=resources,
            service=service,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
        )


class PgBouncerConfig(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "global": "global_",
    }

    databases: dict[str, str]
    files: list[core.VolumeProjection]
    global_: dict[str, str]
    users: dict[str, str]

    def __init__(
        self,
        databases: dict[str, str] = None,
        files: list[core.VolumeProjection] = None,
        global_: dict[str, str] = None,
        users: dict[str, str] = None,
    ):
        super().__init__(databases=databases, files=files, global_=global_, users=users)


class PgbouncerConfig(KubernetesObject):
    __slots__ = ()

    resources: core.ResourceRequirements

    def __init__(self, resources: core.ResourceRequirements = None):
        super().__init__(resources=resources)


class PgBouncerSidecar(KubernetesObject):
    __slots__ = ()

    pgbouncer_config: PgbouncerConfig

    def __init__(self, pgbouncer_config: PgbouncerConfig = None):
        super().__init__(pgbouncer_config=pgbouncer_config)


class PgBouncer(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "custom_tls_secret": "customTLSSecret",
    }
    _revfield_names_ = {
        "customTLSSecret": "custom_tls_secret",
    }

    affinity: core.Affinity
    config: PgBouncerConfig
    containers: list[core.Container]
    custom_tls_secret: core.SecretProjection
    image: str
    metadata: Metadata
    min_available: core.IntOrString
    port: int
    priority_class_name: str
    replicas: int
    resources: core.ResourceRequirements
    service: Service
    sidecars: PgBouncerSidecar
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config: PgBouncerConfig = None,
        containers: list[core.Container] = None,
        custom_tls_secret: core.SecretProjection = None,
        image: str = None,
        metadata: Metadata = None,
        min_available: core.IntOrString = None,
        port: int = None,
        priority_class_name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        service: Service = None,
        sidecars: PgBouncerSidecar = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
    ):
        super().__init__(
            affinity=affinity,
            config=config,
            containers=containers,
            custom_tls_secret=custom_tls_secret,
            image=image,
            metadata=metadata,
            min_available=min_available,
            port=port,
            priority_class_name=priority_class_name,
            replicas=replicas,
            resources=resources,
            service=service,
            sidecars=sidecars,
            tolerations=tolerations,
            topology_spread_constraints=topology_spread_constraints,
        )


class PostgresClusterSpecConfig(KubernetesObject):
    __slots__ = ()

    files: list[core.VolumeProjection]

    def __init__(self, files: list[core.VolumeProjection] = None):
        super().__init__(files=files)


class Proxy(KubernetesObject):
    __slots__ = ()

    _required_ = ["pg_bouncer"]

    pg_bouncer: PgBouncer

    def __init__(self, pg_bouncer: PgBouncer = None):
        super().__init__(pg_bouncer=pg_bouncer)


class Standby(KubernetesObject):
    __slots__ = ()

    enabled: bool
    host: str
    port: int
    repo_name: str

    def __init__(self, enabled: bool = None, host: str = None, port: int = None, repo_name: str = None):
        super().__init__(enabled=enabled, host=host, port=port, repo_name=repo_name)


class UserInterface(KubernetesObject):
    __slots__ = ()

    _required_ = ["pg_admin"]

    pg_admin: PgAdmin

    def __init__(self, pg_admin: PgAdmin = None):
        super().__init__(pg_admin=pg_admin)


class User(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    databases: list[str]
    name: str
    options: str
    password: Password

    def __init__(self, databases: list[str] = None, name: str = None, options: str = None, password: Password = None):
        super().__init__(databases=databases, name=name, options=options, password=password)


class PostgresClusterSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["backups", "instances", "postgres_version"]

    _field_names_ = {
        "custom_replication_tls_secret": "customReplicationTLSSecret",
        "custom_tls_secret": "customTLSSecret",
        "database_init_sql": "databaseInitSQL",
        "post_gis_version": "postGISVersion",
    }
    _revfield_names_ = {
        "customReplicationTLSSecret": "custom_replication_tls_secret",
        "customTLSSecret": "custom_tls_secret",
        "databaseInitSQL": "database_init_sql",
        "postGISVersion": "post_gis_version",
    }

    backups: Backup
    config: PostgresClusterSpecConfig
    custom_replication_tls_secret: core.SecretProjection
    custom_tls_secret: core.SecretProjection
    data_source: DataSource
    database_init_sql: DatabaseInitSQL
    disable_default_pod_scheduling: bool
    image: str
    image_pull_policy: str
    image_pull_secrets: list[core.LocalObjectReference]
    instances: list[Instance]
    metadata: Metadata
    monitoring: Monitoring
    openshift: bool
    patroni: Patroni
    paused: bool
    port: int
    post_gis_version: str
    postgres_version: int
    proxy: Proxy
    service: Service
    shutdown: bool
    standby: Standby
    supplemental_groups: list[int]
    user_interface: UserInterface
    users: list[User]

    def __init__(
        self,
        backups: Backup = None,
        config: PostgresClusterSpecConfig = None,
        custom_replication_tls_secret: core.SecretProjection = None,
        custom_tls_secret: core.SecretProjection = None,
        data_source: DataSource = None,
        database_init_sql: DatabaseInitSQL = None,
        disable_default_pod_scheduling: bool = None,
        image: str = None,
        image_pull_policy: str = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        instances: list[Instance] = None,
        metadata: Metadata = None,
        monitoring: Monitoring = None,
        openshift: bool = None,
        patroni: Patroni = None,
        paused: bool = None,
        port: int = None,
        post_gis_version: str = None,
        postgres_version: int = None,
        proxy: Proxy = None,
        service: Service = None,
        shutdown: bool = None,
        standby: Standby = None,
        supplemental_groups: list[int] = None,
        user_interface: UserInterface = None,
        users: list[User] = None,
    ):
        super().__init__(
            backups=backups,
            config=config,
            custom_replication_tls_secret=custom_replication_tls_secret,
            custom_tls_secret=custom_tls_secret,
            data_source=data_source,
            database_init_sql=database_init_sql,
            disable_default_pod_scheduling=disable_default_pod_scheduling,
            image=image,
            image_pull_policy=image_pull_policy,
            image_pull_secrets=image_pull_secrets,
            instances=instances,
            metadata=metadata,
            monitoring=monitoring,
            openshift=openshift,
            patroni=patroni,
            paused=paused,
            port=port,
            post_gis_version=post_gis_version,
            postgres_version=postgres_version,
            proxy=proxy,
            service=service,
            shutdown=shutdown,
            standby=standby,
            supplemental_groups=supplemental_groups,
            user_interface=user_interface,
            users=users,
        )


class PostgresCluster(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "postgres-operator.crunchydata.com/v1beta1"
    _kind_ = "PostgresCluster"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PostgresClusterSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PostgresClusterSpec = None):
        super().__init__("postgres-operator.crunchydata.com/v1beta1", "PostgresCluster", name, namespace, metadata=metadata, spec=spec)
