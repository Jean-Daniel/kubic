from typing import Any, Dict, List

from .. import KubernetesApiResource, KubernetesObject
from .. import core, meta


class Azure(KubernetesObject):
    __slots__ = ()

    _required_ = ["container"]

    container: str

    def __init__(self, container: str = None):
        super().__init__(container=container)


class Manual(KubernetesObject):
    __slots__ = ()

    _required_ = ["repo_name"]

    options: List[str]
    repo_name: str

    def __init__(self, options: List[str] = None, repo_name: str = None):
        super().__init__(options=options, repo_name=repo_name)


class Metadata(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    labels: Dict[str, str]

    def __init__(self, annotations: Dict[str, str] = None, labels: Dict[str, str] = None):
        super().__init__(annotations=annotations, labels=labels)


class Resource(KubernetesObject):
    __slots__ = ()

    limits: Dict[str, core.IntOrString]
    requests: Dict[str, core.IntOrString]

    def __init__(self, limits: Dict[str, core.IntOrString] = None, requests: Dict[str, core.IntOrString] = None):
        super().__init__(limits=limits, requests=requests)


class Toleration(KubernetesObject):
    __slots__ = ()

    effect: str
    key: str
    operator: str
    toleration_seconds: int
    value: str

    def __init__(self, effect: str = None, key: str = None, operator: str = None, toleration_seconds: int = None, value: str = None):
        super().__init__(effect=effect, key=key, operator=operator, toleration_seconds=toleration_seconds, value=value)


class Dedicated(KubernetesObject):
    __slots__ = ()

    affinity: core.Affinity
    resources: Resource
    tolerations: List[Toleration]

    def __init__(self, affinity: core.Affinity = None, resources: Resource = None, tolerations: List[Toleration] = None):
        super().__init__(affinity=affinity, resources=resources, tolerations=tolerations)


class RepoHost(KubernetesObject):
    __slots__ = ()

    dedicated: Dedicated
    resources: core.ResourceRequirements
    ssh_config_map: core.SecretProjection
    ssh_secret: core.SecretProjection

    def __init__(
        self,
        dedicated: Dedicated = None,
        resources: core.ResourceRequirements = None,
        ssh_config_map: core.SecretProjection = None,
        ssh_secret: core.SecretProjection = None,
    ):
        super().__init__(dedicated=dedicated, resources=resources, ssh_config_map=ssh_config_map, ssh_secret=ssh_secret)


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


class Volume(KubernetesObject):
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
    volume: Volume

    def __init__(
        self, azure: Azure = None, gcs: GCS = None, name: str = None, s3: S3 = None, schedules: Schedule = None, volume: Volume = None
    ):
        super().__init__(azure=azure, gcs=gcs, name=name, s3=s3, schedules=schedules, volume=volume)


class Restore(KubernetesObject):
    __slots__ = ()

    _required_ = ["enabled", "repo_name"]

    affinity: core.Affinity
    cluster_name: str
    cluster_namespace: str
    enabled: bool
    options: List[str]
    repo_name: str
    resources: core.ResourceRequirements
    tolerations: List[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        cluster_name: str = None,
        cluster_namespace: str = None,
        enabled: bool = None,
        options: List[str] = None,
        repo_name: str = None,
        resources: core.ResourceRequirements = None,
        tolerations: List[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            cluster_name=cluster_name,
            cluster_namespace=cluster_namespace,
            enabled=enabled,
            options=options,
            repo_name=repo_name,
            resources=resources,
            tolerations=tolerations,
        )


class Pgbackrest(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "global": "global_",
    }

    configuration: List[core.VolumeProjection]
    global_: Dict[str, str]
    image: str
    manual: Manual
    metadata: Metadata
    repo_host: RepoHost
    repos: List[Repo]
    restore: Restore

    def __init__(
        self,
        configuration: List[core.VolumeProjection] = None,
        global_: Dict[str, str] = None,
        image: str = None,
        manual: Manual = None,
        metadata: Metadata = None,
        repo_host: RepoHost = None,
        repos: List[Repo] = None,
        restore: Restore = None,
    ):
        super().__init__(
            configuration=configuration,
            global_=global_,
            image=image,
            manual=manual,
            metadata=metadata,
            repo_host=repo_host,
            repos=repos,
            restore=restore,
        )


class Backup(KubernetesObject):
    __slots__ = ()

    _required_ = ["pgbackrest"]

    pgbackrest: Pgbackrest

    def __init__(self, pgbackrest: Pgbackrest = None):
        super().__init__(pgbackrest=pgbackrest)


class Config(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "global": "global_",
    }

    databases: Dict[str, str]
    files: List[core.VolumeProjection]
    global_: Dict[str, str]
    users: Dict[str, str]

    def __init__(
        self,
        databases: Dict[str, str] = None,
        files: List[core.VolumeProjection] = None,
        global_: Dict[str, str] = None,
        users: Dict[str, str] = None,
    ):
        super().__init__(databases=databases, files=files, global_=global_, users=users)


class DataSourcePostgresCluster(KubernetesObject):
    __slots__ = ()

    _required_ = ["repo_name"]

    affinity: core.Affinity
    cluster_name: str
    cluster_namespace: str
    options: List[str]
    repo_name: str
    resources: core.ResourceRequirements
    tolerations: List[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        cluster_name: str = None,
        cluster_namespace: str = None,
        options: List[str] = None,
        repo_name: str = None,
        resources: core.ResourceRequirements = None,
        tolerations: List[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            cluster_name=cluster_name,
            cluster_namespace=cluster_namespace,
            options=options,
            repo_name=repo_name,
            resources=resources,
            tolerations=tolerations,
        )


class DataSource(KubernetesObject):
    __slots__ = ()

    postgres_cluster: DataSourcePostgresCluster

    def __init__(self, postgres_cluster: DataSourcePostgresCluster = None):
        super().__init__(postgres_cluster=postgres_cluster)


class Exporter(KubernetesObject):
    __slots__ = ()

    configuration: List[core.VolumeProjection]
    image: str
    resources: core.ResourceRequirements

    def __init__(self, configuration: List[core.VolumeProjection] = None, image: str = None, resources: core.ResourceRequirements = None):
        super().__init__(configuration=configuration, image=image, resources=resources)


class Instance(KubernetesObject):
    __slots__ = ()

    _required_ = ["data_volume_claim_spec"]

    affinity: core.Affinity
    data_volume_claim_spec: core.PersistentVolumeClaimSpec
    metadata: Metadata
    name: str
    replicas: int
    resources: core.ResourceRequirements
    tolerations: List[core.Toleration]
    wal_volume_claim_spec: core.PersistentVolumeClaimSpec

    def __init__(
        self,
        affinity: core.Affinity = None,
        data_volume_claim_spec: core.PersistentVolumeClaimSpec = None,
        metadata: Metadata = None,
        name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        tolerations: List[core.Toleration] = None,
        wal_volume_claim_spec: core.PersistentVolumeClaimSpec = None,
    ):
        super().__init__(
            affinity=affinity,
            data_volume_claim_spec=data_volume_claim_spec,
            metadata=metadata,
            name=name,
            replicas=replicas,
            resources=resources,
            tolerations=tolerations,
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


class Patroni(KubernetesObject):
    __slots__ = ()

    dynamic_configuration: Dict[str, Any]
    leader_lease_duration_seconds: int
    port: int
    sync_period_seconds: int

    def __init__(
        self,
        dynamic_configuration: Dict[str, Any] = None,
        leader_lease_duration_seconds: int = None,
        port: int = None,
        sync_period_seconds: int = None,
    ):
        super().__init__(
            dynamic_configuration=dynamic_configuration,
            leader_lease_duration_seconds=leader_lease_duration_seconds,
            port=port,
            sync_period_seconds=sync_period_seconds,
        )


class PgBouncer(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "custom_tls_secret": "customTLSSecret",
    }
    _revfield_names_ = {
        "customTLSSecret": "custom_tls_secret",
    }

    affinity: core.Affinity
    config: Config
    custom_tls_secret: core.SecretProjection
    image: str
    metadata: Metadata
    port: int
    replicas: int
    resources: core.ResourceRequirements
    tolerations: List[core.Toleration]

    def __init__(
        self,
        affinity: core.Affinity = None,
        config: Config = None,
        custom_tls_secret: core.SecretProjection = None,
        image: str = None,
        metadata: Metadata = None,
        port: int = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        tolerations: List[core.Toleration] = None,
    ):
        super().__init__(
            affinity=affinity,
            config=config,
            custom_tls_secret=custom_tls_secret,
            image=image,
            metadata=metadata,
            port=port,
            replicas=replicas,
            resources=resources,
            tolerations=tolerations,
        )


class Proxy(KubernetesObject):
    __slots__ = ()

    _required_ = ["pg_bouncer"]

    pg_bouncer: PgBouncer

    def __init__(self, pg_bouncer: PgBouncer = None):
        super().__init__(pg_bouncer=pg_bouncer)


class Standby(KubernetesObject):
    __slots__ = ()

    _required_ = ["repo_name"]

    enabled: bool
    repo_name: str

    def __init__(self, enabled: bool = None, repo_name: str = None):
        super().__init__(enabled=enabled, repo_name=repo_name)


class User(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    databases: List[str]
    name: str
    options: str

    def __init__(self, databases: List[str] = None, name: str = None, options: str = None):
        super().__init__(databases=databases, name=name, options=options)


class PostgresClusterSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["backups", "instances", "postgres_version"]

    _field_names_ = {
        "custom_replication_tls_secret": "customReplicationTLSSecret",
        "custom_tls_secret": "customTLSSecret",
        "post_gis_version": "postGISVersion",
    }
    _revfield_names_ = {
        "customReplicationTLSSecret": "custom_replication_tls_secret",
        "customTLSSecret": "custom_tls_secret",
        "postGISVersion": "post_gis_version",
    }

    backups: Backup
    custom_replication_tls_secret: core.SecretProjection
    custom_tls_secret: core.SecretProjection
    data_source: DataSource
    image: str
    image_pull_secrets: List[core.LocalObjectReference]
    instances: List[Instance]
    metadata: Metadata
    monitoring: Monitoring
    openshift: bool
    patroni: Patroni
    port: int
    post_gis_version: str
    postgres_version: int
    proxy: Proxy
    shutdown: bool
    standby: Standby
    users: List[User]

    def __init__(
        self,
        backups: Backup = None,
        custom_replication_tls_secret: core.SecretProjection = None,
        custom_tls_secret: core.SecretProjection = None,
        data_source: DataSource = None,
        image: str = None,
        image_pull_secrets: List[core.LocalObjectReference] = None,
        instances: List[Instance] = None,
        metadata: Metadata = None,
        monitoring: Monitoring = None,
        openshift: bool = None,
        patroni: Patroni = None,
        port: int = None,
        post_gis_version: str = None,
        postgres_version: int = None,
        proxy: Proxy = None,
        shutdown: bool = None,
        standby: Standby = None,
        users: List[User] = None,
    ):
        super().__init__(
            backups=backups,
            custom_replication_tls_secret=custom_replication_tls_secret,
            custom_tls_secret=custom_tls_secret,
            data_source=data_source,
            image=image,
            image_pull_secrets=image_pull_secrets,
            instances=instances,
            metadata=metadata,
            monitoring=monitoring,
            openshift=openshift,
            patroni=patroni,
            port=port,
            post_gis_version=post_gis_version,
            postgres_version=postgres_version,
            proxy=proxy,
            shutdown=shutdown,
            standby=standby,
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
