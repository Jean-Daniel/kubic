import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from ..api import core, meta


class Authorization2(KubernetesObject):
    __slots__ = ()

    credentials: core.ConfigMapKeySelector
    credentials_file: str
    type: str

    def __init__(self, credentials: core.ConfigMapKeySelector = None, credentials_file: str = None, type: str = None):
        super().__init__(credentials=credentials, credentials_file=credentials_file, type=type)


class BasicAuth(KubernetesObject):
    __slots__ = ()

    password: core.SecretKeySelector
    username: core.ConfigMapKeySelector

    def __init__(self, password: core.SecretKeySelector = None, username: core.ConfigMapKeySelector = None):
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


class TLSConfig2(KubernetesObject):
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


class APIserverConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["host"]

    authorization: Authorization2
    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    host: str
    tls_config: TLSConfig2

    def __init__(
        self,
        authorization: Authorization2 = None,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        host: str = None,
        tls_config: TLSConfig2 = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            bearer_token_file=bearer_token_file,
            host=host,
            tls_config=tls_config,
        )


class Confirm(KubernetesObject):
    __slots__ = ()

    _required_ = ["text"]

    dismiss_text: str
    ok_text: str
    text: str
    title: str

    def __init__(self, dismiss_text: str = None, ok_text: str = None, text: str = None, title: str = None):
        super().__init__(dismiss_text=dismiss_text, ok_text=ok_text, text=text, title=title)


class Action(KubernetesObject):
    __slots__ = ()

    _required_ = ["text", "type"]

    confirm: Confirm
    name: str
    style: str
    text: str
    type: str
    url: str
    value: str

    def __init__(
        self,
        confirm: Confirm = None,
        name: str = None,
        style: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        value: str = None,
    ):
        super().__init__(confirm=confirm, name=name, style=style, text=text, type=type, url=url, value=value)


class Alert(KubernetesObject):
    __slots__ = ()

    for_grace_period: str
    for_outage_tolerance: str
    resend_delay: str

    def __init__(self, for_grace_period: str = None, for_outage_tolerance: str = None, resend_delay: str = None):
        super().__init__(for_grace_period=for_grace_period, for_outage_tolerance=for_outage_tolerance, resend_delay=resend_delay)


class Authorization(KubernetesObject):
    __slots__ = ()

    credentials: core.ConfigMapKeySelector
    type: str

    def __init__(self, credentials: core.ConfigMapKeySelector = None, type: str = None):
        super().__init__(credentials=credentials, type=type)


class AlertingAlertmanager(KubernetesObject):
    __slots__ = ()

    _required_ = ["name", "namespace", "port"]

    api_version: str
    authorization: Authorization
    bearer_token_file: str
    name: str
    namespace: str
    path_prefix: str
    port: core.IntOrString
    scheme: str
    timeout: str
    tls_config: TLSConfig2

    def __init__(
        self,
        api_version: str = None,
        authorization: Authorization = None,
        bearer_token_file: str = None,
        name: str = None,
        namespace: str = None,
        path_prefix: str = None,
        port: core.IntOrString = None,
        scheme: str = None,
        timeout: str = None,
        tls_config: TLSConfig2 = None,
    ):
        super().__init__(
            api_version=api_version,
            authorization=authorization,
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

    alertmanagers: list[AlertingAlertmanager]

    def __init__(self, alertmanagers: list[AlertingAlertmanager] = None):
        super().__init__(alertmanagers=alertmanagers)


class PodMetadata(KubernetesObject):
    __slots__ = ()

    annotations: dict[str, str]
    labels: dict[str, str]
    name: str

    def __init__(self, annotations: dict[str, str] = None, labels: dict[str, str] = None, name: str = None):
        super().__init__(annotations=annotations, labels=labels, name=name)


class Storage(KubernetesObject):
    __slots__ = ()

    disable_mount_sub_path: bool
    empty_dir: core.EmptyDirVolumeSource
    ephemeral: core.EphemeralVolumeSource
    volume_claim_template: core.PersistentVolumeClaim

    def __init__(
        self,
        disable_mount_sub_path: bool = None,
        empty_dir: core.EmptyDirVolumeSource = None,
        ephemeral: core.EphemeralVolumeSource = None,
        volume_claim_template: core.PersistentVolumeClaim = None,
    ):
        super().__init__(
            disable_mount_sub_path=disable_mount_sub_path,
            empty_dir=empty_dir,
            ephemeral=ephemeral,
            volume_claim_template=volume_claim_template,
        )


class AlertmanagerSpec(KubernetesObject):
    __slots__ = ()

    additional_peers: list[str]
    affinity: core.Affinity
    alertmanager_config_namespace_selector: meta.LabelSelector
    alertmanager_config_selector: meta.LabelSelector
    base_image: str
    cluster_advertise_address: str
    cluster_gossip_interval: str
    cluster_peer_timeout: str
    cluster_pushpull_interval: str
    config_maps: list[str]
    config_secret: str
    containers: list[core.Container]
    external_url: str
    force_enable_cluster_mode: bool
    image: str
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    listen_local: bool
    log_format: str
    log_level: str
    min_ready_seconds: int
    node_selector: dict[str, str]
    paused: bool
    pod_metadata: PodMetadata
    port_name: str
    priority_class_name: str
    replicas: int
    resources: core.ResourceRequirements
    retention: str
    route_prefix: str
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    sha: str
    storage: Storage
    tag: str
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    version: str
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]

    def __init__(
        self,
        additional_peers: list[str] = None,
        affinity: core.Affinity = None,
        alertmanager_config_namespace_selector: meta.LabelSelector = None,
        alertmanager_config_selector: meta.LabelSelector = None,
        base_image: str = None,
        cluster_advertise_address: str = None,
        cluster_gossip_interval: str = None,
        cluster_peer_timeout: str = None,
        cluster_pushpull_interval: str = None,
        config_maps: list[str] = None,
        config_secret: str = None,
        containers: list[core.Container] = None,
        external_url: str = None,
        force_enable_cluster_mode: bool = None,
        image: str = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        min_ready_seconds: int = None,
        node_selector: dict[str, str] = None,
        paused: bool = None,
        pod_metadata: PodMetadata = None,
        port_name: str = None,
        priority_class_name: str = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        retention: str = None,
        route_prefix: str = None,
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        sha: str = None,
        storage: Storage = None,
        tag: str = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        version: str = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
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
            min_ready_seconds=min_ready_seconds,
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


class Alertmanager(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "Alertmanager"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: AlertmanagerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: AlertmanagerSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class SourceMatch(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    match_type: str
    name: str
    regex: bool
    value: str

    def __init__(self, match_type: str = None, name: str = None, regex: bool = None, value: str = None):
        super().__init__(match_type=match_type, name=name, regex=regex, value=value)


class TargetMatch(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    match_type: str
    name: str
    regex: bool
    value: str

    def __init__(self, match_type: str = None, name: str = None, regex: bool = None, value: str = None):
        super().__init__(match_type=match_type, name=name, regex=regex, value=value)


class InhibitRule(KubernetesObject):
    __slots__ = ()

    equal: list[str]
    source_match: list[SourceMatch]
    target_match: list[TargetMatch]

    def __init__(self, equal: list[str] = None, source_match: list[SourceMatch] = None, target_match: list[TargetMatch] = None):
        super().__init__(equal=equal, source_match=source_match, target_match=target_match)


class DaysOfMonth(KubernetesObject):
    __slots__ = ()

    end: int
    start: int

    def __init__(self, end: int = None, start: int = None):
        super().__init__(end=end, start=start)


class Time(KubernetesObject):
    __slots__ = ()

    end_time: str
    start_time: str

    def __init__(self, end_time: str = None, start_time: str = None):
        super().__init__(end_time=end_time, start_time=start_time)


class TimeInterval(KubernetesObject):
    __slots__ = ()

    days_of_month: list[DaysOfMonth]
    months: list[str]
    times: list[Time]
    weekdays: list[str]
    years: list[str]

    def __init__(
        self,
        days_of_month: list[DaysOfMonth] = None,
        months: list[str] = None,
        times: list[Time] = None,
        weekdays: list[str] = None,
        years: list[str] = None,
    ):
        super().__init__(days_of_month=days_of_month, months=months, times=times, weekdays=weekdays, years=years)


class MuteTimeInterval(KubernetesObject):
    __slots__ = ()

    name: str
    time_intervals: list[TimeInterval]

    def __init__(self, name: str = None, time_intervals: list[TimeInterval] = None):
        super().__init__(name=name, time_intervals=time_intervals)


class Header(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "value"]

    key: str
    value: str

    def __init__(self, key: str = None, value: str = None):
        super().__init__(key=key, value=value)


class TLSConfig(KubernetesObject):
    __slots__ = ()

    ca: CA
    cert: Cert
    insecure_skip_verify: bool
    key_secret: core.SecretKeySelector
    server_name: str

    def __init__(
        self,
        ca: CA = None,
        cert: Cert = None,
        insecure_skip_verify: bool = None,
        key_secret: core.SecretKeySelector = None,
        server_name: str = None,
    ):
        super().__init__(ca=ca, cert=cert, insecure_skip_verify=insecure_skip_verify, key_secret=key_secret, server_name=server_name)


class EmailConfig(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "require_tls": "requireTLS",
    }
    _revfield_names_ = {
        "from": "from_",
        "requireTLS": "require_tls",
    }

    auth_identity: str
    auth_password: core.ConfigMapKeySelector
    auth_secret: core.ConfigMapKeySelector
    auth_username: str
    from_: str
    headers: list[Header]
    hello: str
    html: str
    require_tls: bool
    send_resolved: bool
    smarthost: str
    text: str
    tls_config: TLSConfig
    to: str

    def __init__(
        self,
        auth_identity: str = None,
        auth_password: core.ConfigMapKeySelector = None,
        auth_secret: core.ConfigMapKeySelector = None,
        auth_username: str = None,
        from_: str = None,
        headers: list[Header] = None,
        hello: str = None,
        html: str = None,
        require_tls: bool = None,
        send_resolved: bool = None,
        smarthost: str = None,
        text: str = None,
        tls_config: TLSConfig = None,
        to: str = None,
    ):
        super().__init__(
            auth_identity=auth_identity,
            auth_password=auth_password,
            auth_secret=auth_secret,
            auth_username=auth_username,
            from_=from_,
            headers=headers,
            hello=hello,
            html=html,
            require_tls=require_tls,
            send_resolved=send_resolved,
            smarthost=smarthost,
            text=text,
            tls_config=tls_config,
            to=to,
        )


class Detail(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "value"]

    key: str
    value: str

    def __init__(self, key: str = None, value: str = None):
        super().__init__(key=key, value=value)


class HttpConfig(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "proxy_url": "proxyURL",
    }
    _revfield_names_ = {
        "proxyURL": "proxy_url",
    }

    authorization: Authorization
    basic_auth: BasicAuth
    bearer_token_secret: core.ConfigMapKeySelector
    proxy_url: str
    tls_config: TLSConfig

    def __init__(
        self,
        authorization: Authorization = None,
        basic_auth: BasicAuth = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        proxy_url: str = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token_secret=bearer_token_secret,
            proxy_url=proxy_url,
            tls_config=tls_config,
        )


class Responder(KubernetesObject):
    __slots__ = ()

    _required_ = ["type"]

    id: str
    name: str
    type: str
    username: str

    def __init__(self, id: str = None, name: str = None, type: str = None, username: str = None):
        super().__init__(id=id, name=name, type=type, username=username)


class OpsgenieConfig(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "api_url": "apiURL",
    }
    _revfield_names_ = {
        "apiURL": "api_url",
    }

    api_key: core.ConfigMapKeySelector
    api_url: str
    description: str
    details: list[Detail]
    http_config: HttpConfig
    message: str
    note: str
    priority: str
    responders: list[Responder]
    send_resolved: bool
    source: str
    tags: str

    def __init__(
        self,
        api_key: core.ConfigMapKeySelector = None,
        api_url: str = None,
        description: str = None,
        details: list[Detail] = None,
        http_config: HttpConfig = None,
        message: str = None,
        note: str = None,
        priority: str = None,
        responders: list[Responder] = None,
        send_resolved: bool = None,
        source: str = None,
        tags: str = None,
    ):
        super().__init__(
            api_key=api_key,
            api_url=api_url,
            description=description,
            details=details,
            http_config=http_config,
            message=message,
            note=note,
            priority=priority,
            responders=responders,
            send_resolved=send_resolved,
            source=source,
            tags=tags,
        )


class PagerDutyImageConfig(KubernetesObject):
    __slots__ = ()

    alt: str
    href: str
    src: str

    def __init__(self, alt: str = None, href: str = None, src: str = None):
        super().__init__(alt=alt, href=href, src=src)


class PagerDutyLinkConfig(KubernetesObject):
    __slots__ = ()

    alt: str
    href: str

    def __init__(self, alt: str = None, href: str = None):
        super().__init__(alt=alt, href=href)


class PagerdutyConfig(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "client_url": "clientURL",
    }
    _revfield_names_ = {
        "class": "class_",
        "clientURL": "client_url",
    }

    class_: str
    client: str
    client_url: str
    component: str
    description: str
    details: list[Detail]
    group: str
    http_config: HttpConfig
    pager_duty_image_configs: list[PagerDutyImageConfig]
    pager_duty_link_configs: list[PagerDutyLinkConfig]
    routing_key: core.ConfigMapKeySelector
    send_resolved: bool
    service_key: core.ConfigMapKeySelector
    severity: str
    url: str

    def __init__(
        self,
        class_: str = None,
        client: str = None,
        client_url: str = None,
        component: str = None,
        description: str = None,
        details: list[Detail] = None,
        group: str = None,
        http_config: HttpConfig = None,
        pager_duty_image_configs: list[PagerDutyImageConfig] = None,
        pager_duty_link_configs: list[PagerDutyLinkConfig] = None,
        routing_key: core.ConfigMapKeySelector = None,
        send_resolved: bool = None,
        service_key: core.ConfigMapKeySelector = None,
        severity: str = None,
        url: str = None,
    ):
        super().__init__(
            class_=class_,
            client=client,
            client_url=client_url,
            component=component,
            description=description,
            details=details,
            group=group,
            http_config=http_config,
            pager_duty_image_configs=pager_duty_image_configs,
            pager_duty_link_configs=pager_duty_link_configs,
            routing_key=routing_key,
            send_resolved=send_resolved,
            service_key=service_key,
            severity=severity,
            url=url,
        )


class PushoverConfig(KubernetesObject):
    __slots__ = ()

    expire: str
    html: bool
    http_config: HttpConfig
    message: str
    priority: str
    retry: str
    send_resolved: bool
    sound: str
    title: str
    token: core.ConfigMapKeySelector
    url: str
    url_title: str
    user_key: core.ConfigMapKeySelector

    def __init__(
        self,
        expire: str = None,
        html: bool = None,
        http_config: HttpConfig = None,
        message: str = None,
        priority: str = None,
        retry: str = None,
        send_resolved: bool = None,
        sound: str = None,
        title: str = None,
        token: core.ConfigMapKeySelector = None,
        url: str = None,
        url_title: str = None,
        user_key: core.ConfigMapKeySelector = None,
    ):
        super().__init__(
            expire=expire,
            html=html,
            http_config=http_config,
            message=message,
            priority=priority,
            retry=retry,
            send_resolved=send_resolved,
            sound=sound,
            title=title,
            token=token,
            url=url,
            url_title=url_title,
            user_key=user_key,
        )


class Field(KubernetesObject):
    __slots__ = ()

    _required_ = ["title", "value"]

    short: bool
    title: str
    value: str

    def __init__(self, short: bool = None, title: str = None, value: str = None):
        super().__init__(short=short, title=title, value=value)


class SlackConfig(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "api_url": "apiURL",
        "icon_url": "iconURL",
        "image_url": "imageURL",
        "thumb_url": "thumbURL",
    }
    _revfield_names_ = {
        "apiURL": "api_url",
        "iconURL": "icon_url",
        "imageURL": "image_url",
        "thumbURL": "thumb_url",
    }

    actions: list[Action]
    api_url: core.ConfigMapKeySelector
    callback_id: str
    channel: str
    color: str
    fallback: str
    fields: list[Field]
    footer: str
    http_config: HttpConfig
    icon_emoji: str
    icon_url: str
    image_url: str
    link_names: bool
    mrkdwn_in: list[str]
    pretext: str
    send_resolved: bool
    short_fields: bool
    text: str
    thumb_url: str
    title: str
    title_link: str
    username: str

    def __init__(
        self,
        actions: list[Action] = None,
        api_url: core.ConfigMapKeySelector = None,
        callback_id: str = None,
        channel: str = None,
        color: str = None,
        fallback: str = None,
        fields: list[Field] = None,
        footer: str = None,
        http_config: HttpConfig = None,
        icon_emoji: str = None,
        icon_url: str = None,
        image_url: str = None,
        link_names: bool = None,
        mrkdwn_in: list[str] = None,
        pretext: str = None,
        send_resolved: bool = None,
        short_fields: bool = None,
        text: str = None,
        thumb_url: str = None,
        title: str = None,
        title_link: str = None,
        username: str = None,
    ):
        super().__init__(
            actions=actions,
            api_url=api_url,
            callback_id=callback_id,
            channel=channel,
            color=color,
            fallback=fallback,
            fields=fields,
            footer=footer,
            http_config=http_config,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            image_url=image_url,
            link_names=link_names,
            mrkdwn_in=mrkdwn_in,
            pretext=pretext,
            send_resolved=send_resolved,
            short_fields=short_fields,
            text=text,
            thumb_url=thumb_url,
            title=title,
            title_link=title_link,
            username=username,
        )


class CustomField(KubernetesObject):
    __slots__ = ()

    _required_ = ["key", "value"]

    key: str
    value: str

    def __init__(self, key: str = None, value: str = None):
        super().__init__(key=key, value=value)


class VictoropsConfig(KubernetesObject):
    __slots__ = ()

    api_key: core.ConfigMapKeySelector
    api_url: str
    custom_fields: list[CustomField]
    entity_display_name: str
    http_config: HttpConfig
    message_type: str
    monitoring_tool: str
    routing_key: str
    send_resolved: bool
    state_message: str

    def __init__(
        self,
        api_key: core.ConfigMapKeySelector = None,
        api_url: str = None,
        custom_fields: list[CustomField] = None,
        entity_display_name: str = None,
        http_config: HttpConfig = None,
        message_type: str = None,
        monitoring_tool: str = None,
        routing_key: str = None,
        send_resolved: bool = None,
        state_message: str = None,
    ):
        super().__init__(
            api_key=api_key,
            api_url=api_url,
            custom_fields=custom_fields,
            entity_display_name=entity_display_name,
            http_config=http_config,
            message_type=message_type,
            monitoring_tool=monitoring_tool,
            routing_key=routing_key,
            send_resolved=send_resolved,
            state_message=state_message,
        )


class WebhookConfig(KubernetesObject):
    __slots__ = ()

    http_config: HttpConfig
    max_alerts: int
    send_resolved: bool
    url: str
    url_secret: core.ConfigMapKeySelector

    def __init__(
        self,
        http_config: HttpConfig = None,
        max_alerts: int = None,
        send_resolved: bool = None,
        url: str = None,
        url_secret: core.ConfigMapKeySelector = None,
    ):
        super().__init__(http_config=http_config, max_alerts=max_alerts, send_resolved=send_resolved, url=url, url_secret=url_secret)


class WechatConfig(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "agent_id": "agentID",
        "api_url": "apiURL",
        "corp_id": "corpID",
    }
    _revfield_names_ = {
        "agentID": "agent_id",
        "apiURL": "api_url",
        "corpID": "corp_id",
    }

    agent_id: str
    api_secret: core.ConfigMapKeySelector
    api_url: str
    corp_id: str
    http_config: HttpConfig
    message: str
    message_type: str
    send_resolved: bool
    to_party: str
    to_tag: str
    to_user: str

    def __init__(
        self,
        agent_id: str = None,
        api_secret: core.ConfigMapKeySelector = None,
        api_url: str = None,
        corp_id: str = None,
        http_config: HttpConfig = None,
        message: str = None,
        message_type: str = None,
        send_resolved: bool = None,
        to_party: str = None,
        to_tag: str = None,
        to_user: str = None,
    ):
        super().__init__(
            agent_id=agent_id,
            api_secret=api_secret,
            api_url=api_url,
            corp_id=corp_id,
            http_config=http_config,
            message=message,
            message_type=message_type,
            send_resolved=send_resolved,
            to_party=to_party,
            to_tag=to_tag,
            to_user=to_user,
        )


class Receiver(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    email_configs: list[EmailConfig]
    name: str
    opsgenie_configs: list[OpsgenieConfig]
    pagerduty_configs: list[PagerdutyConfig]
    pushover_configs: list[PushoverConfig]
    slack_configs: list[SlackConfig]
    victorops_configs: list[VictoropsConfig]
    webhook_configs: list[WebhookConfig]
    wechat_configs: list[WechatConfig]

    def __init__(
        self,
        email_configs: list[EmailConfig] = None,
        name: str = None,
        opsgenie_configs: list[OpsgenieConfig] = None,
        pagerduty_configs: list[PagerdutyConfig] = None,
        pushover_configs: list[PushoverConfig] = None,
        slack_configs: list[SlackConfig] = None,
        victorops_configs: list[VictoropsConfig] = None,
        webhook_configs: list[WebhookConfig] = None,
        wechat_configs: list[WechatConfig] = None,
    ):
        super().__init__(
            email_configs=email_configs,
            name=name,
            opsgenie_configs=opsgenie_configs,
            pagerduty_configs=pagerduty_configs,
            pushover_configs=pushover_configs,
            slack_configs=slack_configs,
            victorops_configs=victorops_configs,
            webhook_configs=webhook_configs,
            wechat_configs=wechat_configs,
        )


class Matcher(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    match_type: str
    name: str
    regex: bool
    value: str

    def __init__(self, match_type: str = None, name: str = None, regex: bool = None, value: str = None):
        super().__init__(match_type=match_type, name=name, regex=regex, value=value)


class Route(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "continue": "continue_",
    }

    continue_: bool
    group_by: list[str]
    group_interval: str
    group_wait: str
    matchers: list[Matcher]
    mute_time_intervals: list[str]
    receiver: str
    repeat_interval: str
    routes: list[t.Any]

    def __init__(
        self,
        continue_: bool = None,
        group_by: list[str] = None,
        group_interval: str = None,
        group_wait: str = None,
        matchers: list[Matcher] = None,
        mute_time_intervals: list[str] = None,
        receiver: str = None,
        repeat_interval: str = None,
        routes: list[t.Any] = None,
    ):
        super().__init__(
            continue_=continue_,
            group_by=group_by,
            group_interval=group_interval,
            group_wait=group_wait,
            matchers=matchers,
            mute_time_intervals=mute_time_intervals,
            receiver=receiver,
            repeat_interval=repeat_interval,
            routes=routes,
        )


class AlertmanagerConfigSpec(KubernetesObject):
    __slots__ = ()

    inhibit_rules: list[InhibitRule]
    mute_time_intervals: list[MuteTimeInterval]
    receivers: list[Receiver]
    route: Route

    def __init__(
        self,
        inhibit_rules: list[InhibitRule] = None,
        mute_time_intervals: list[MuteTimeInterval] = None,
        receivers: list[Receiver] = None,
        route: Route = None,
    ):
        super().__init__(inhibit_rules=inhibit_rules, mute_time_intervals=mute_time_intervals, receivers=receivers, route=route)


class AlertmanagerConfig(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1alpha1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "AlertmanagerConfig"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: AlertmanagerConfigSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: AlertmanagerConfigSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ArbitraryFSAccessThroughSM(KubernetesObject):
    __slots__ = ()

    deny: bool

    def __init__(self, deny: bool = None):
        super().__init__(deny=deny)


class ClientId(KubernetesObject):
    __slots__ = ()

    config_map: core.ConfigMapKeySelector
    secret: core.SecretKeySelector

    def __init__(self, config_map: core.ConfigMapKeySelector = None, secret: core.SecretKeySelector = None):
        super().__init__(config_map=config_map, secret=secret)


class MetricRelabeling(KubernetesObject):
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


class Oauth2(KubernetesObject):
    __slots__ = ()

    _required_ = ["client_id", "client_secret", "token_url"]

    client_id: ClientId
    client_secret: core.ConfigMapKeySelector
    endpoint_params: dict[str, str]
    scopes: list[str]
    token_url: str

    def __init__(
        self,
        client_id: ClientId = None,
        client_secret: core.ConfigMapKeySelector = None,
        endpoint_params: dict[str, str] = None,
        scopes: list[str] = None,
        token_url: str = None,
    ):
        super().__init__(
            client_id=client_id, client_secret=client_secret, endpoint_params=endpoint_params, scopes=scopes, token_url=token_url
        )


class Relabeling(KubernetesObject):
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

    authorization: Authorization
    basic_auth: BasicAuth
    bearer_token_file: str
    bearer_token_secret: core.ConfigMapKeySelector
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    metric_relabelings: list[MetricRelabeling]
    oauth2: Oauth2
    params: dict[str, list[str]]
    path: str
    port: str
    proxy_url: str
    relabelings: list[Relabeling]
    scheme: str
    scrape_timeout: str
    target_port: core.IntOrString
    tls_config: TLSConfig2

    def __init__(
        self,
        authorization: Authorization = None,
        basic_auth: BasicAuth = None,
        bearer_token_file: str = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        metric_relabelings: list[MetricRelabeling] = None,
        oauth2: Oauth2 = None,
        params: dict[str, list[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabelings: list[Relabeling] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        target_port: core.IntOrString = None,
        tls_config: TLSConfig2 = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token_file=bearer_token_file,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            metric_relabelings=metric_relabelings,
            oauth2=oauth2,
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

    _field_names_ = {
        "partial_response_strategy": "partial_response_strategy",
    }

    interval: str
    name: str
    partial_response_strategy: str
    rules: list[GroupRule]

    def __init__(self, interval: str = None, name: str = None, partial_response_strategy: str = None, rules: list[GroupRule] = None):
        super().__init__(interval=interval, name=name, partial_response_strategy=partial_response_strategy, rules=rules)


class GrpcServerTlsConfig(KubernetesObject):
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


class NamespaceSelector(KubernetesObject):
    __slots__ = ()

    any: bool
    match_names: list[str]

    def __init__(self, any: bool = None, match_names: list[str] = None):
        super().__init__(any=any, match_names=match_names)


class RelabelingConfig(KubernetesObject):
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


class Ingress(KubernetesObject):
    __slots__ = ()

    namespace_selector: NamespaceSelector
    relabeling_configs: list[RelabelingConfig]
    selector: meta.LabelSelector

    def __init__(
        self,
        namespace_selector: NamespaceSelector = None,
        relabeling_configs: list[RelabelingConfig] = None,
        selector: meta.LabelSelector = None,
    ):
        super().__init__(namespace_selector=namespace_selector, relabeling_configs=relabeling_configs, selector=selector)


class MetadataConfig(KubernetesObject):
    __slots__ = ()

    send: bool
    send_interval: str

    def __init__(self, send: bool = None, send_interval: str = None):
        super().__init__(send=send, send_interval=send_interval)


class PodMetricsEndpoint(KubernetesObject):
    __slots__ = ()

    authorization: Authorization
    basic_auth: BasicAuth
    bearer_token_secret: core.ConfigMapKeySelector
    honor_labels: bool
    honor_timestamps: bool
    interval: str
    metric_relabelings: list[MetricRelabeling]
    oauth2: Oauth2
    params: dict[str, list[str]]
    path: str
    port: str
    proxy_url: str
    relabelings: list[Relabeling]
    scheme: str
    scrape_timeout: str
    target_port: core.IntOrString
    tls_config: TLSConfig

    def __init__(
        self,
        authorization: Authorization = None,
        basic_auth: BasicAuth = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        honor_labels: bool = None,
        honor_timestamps: bool = None,
        interval: str = None,
        metric_relabelings: list[MetricRelabeling] = None,
        oauth2: Oauth2 = None,
        params: dict[str, list[str]] = None,
        path: str = None,
        port: str = None,
        proxy_url: str = None,
        relabelings: list[Relabeling] = None,
        scheme: str = None,
        scrape_timeout: str = None,
        target_port: core.IntOrString = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token_secret=bearer_token_secret,
            honor_labels=honor_labels,
            honor_timestamps=honor_timestamps,
            interval=interval,
            metric_relabelings=metric_relabelings,
            oauth2=oauth2,
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
    label_limit: int
    label_name_length_limit: int
    label_value_length_limit: int
    namespace_selector: NamespaceSelector
    pod_metrics_endpoints: list[PodMetricsEndpoint]
    pod_target_labels: list[str]
    sample_limit: int
    selector: meta.LabelSelector
    target_limit: int

    def __init__(
        self,
        job_label: str = None,
        label_limit: int = None,
        label_name_length_limit: int = None,
        label_value_length_limit: int = None,
        namespace_selector: NamespaceSelector = None,
        pod_metrics_endpoints: list[PodMetricsEndpoint] = None,
        pod_target_labels: list[str] = None,
        sample_limit: int = None,
        selector: meta.LabelSelector = None,
        target_limit: int = None,
    ):
        super().__init__(
            job_label=job_label,
            label_limit=label_limit,
            label_name_length_limit=label_name_length_limit,
            label_value_length_limit=label_value_length_limit,
            namespace_selector=namespace_selector,
            pod_metrics_endpoints=pod_metrics_endpoints,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
            target_limit=target_limit,
        )


class PodMonitor(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "PodMonitor"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PodMonitorSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodMonitorSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class Prober(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    path: str
    proxy_url: str
    scheme: str
    url: str

    def __init__(self, path: str = None, proxy_url: str = None, scheme: str = None, url: str = None):
        super().__init__(path=path, proxy_url=proxy_url, scheme=scheme, url=url)


class StaticConfig(KubernetesObject):
    __slots__ = ()

    labels: dict[str, str]
    relabeling_configs: list[RelabelingConfig]
    static: list[str]

    def __init__(self, labels: dict[str, str] = None, relabeling_configs: list[RelabelingConfig] = None, static: list[str] = None):
        super().__init__(labels=labels, relabeling_configs=relabeling_configs, static=static)


class Target(KubernetesObject):
    __slots__ = ()

    ingress: Ingress
    static_config: StaticConfig

    def __init__(self, ingress: Ingress = None, static_config: StaticConfig = None):
        super().__init__(ingress=ingress, static_config=static_config)


class ProbeSpec(KubernetesObject):
    __slots__ = ()

    authorization: Authorization
    basic_auth: BasicAuth
    bearer_token_secret: core.ConfigMapKeySelector
    interval: str
    job_name: str
    label_limit: int
    label_name_length_limit: int
    label_value_length_limit: int
    metric_relabelings: list[MetricRelabeling]
    module: str
    oauth2: Oauth2
    prober: Prober
    sample_limit: int
    scrape_timeout: str
    target_limit: int
    targets: Target
    tls_config: TLSConfig

    def __init__(
        self,
        authorization: Authorization = None,
        basic_auth: BasicAuth = None,
        bearer_token_secret: core.ConfigMapKeySelector = None,
        interval: str = None,
        job_name: str = None,
        label_limit: int = None,
        label_name_length_limit: int = None,
        label_value_length_limit: int = None,
        metric_relabelings: list[MetricRelabeling] = None,
        module: str = None,
        oauth2: Oauth2 = None,
        prober: Prober = None,
        sample_limit: int = None,
        scrape_timeout: str = None,
        target_limit: int = None,
        targets: Target = None,
        tls_config: TLSConfig = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token_secret=bearer_token_secret,
            interval=interval,
            job_name=job_name,
            label_limit=label_limit,
            label_name_length_limit=label_name_length_limit,
            label_value_length_limit=label_value_length_limit,
            metric_relabelings=metric_relabelings,
            module=module,
            oauth2=oauth2,
            prober=prober,
            sample_limit=sample_limit,
            scrape_timeout=scrape_timeout,
            target_limit=target_limit,
            targets=targets,
            tls_config=tls_config,
        )


class Probe(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "Probe"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ProbeSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ProbeSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


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

    def __init__(self, lookback_delta: str = None, max_concurrency: int = None, max_samples: int = None, timeout: str = None):
        super().__init__(lookback_delta=lookback_delta, max_concurrency=max_concurrency, max_samples=max_samples, timeout=timeout)


class RemoteRead(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    authorization: Authorization2
    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    headers: dict[str, str]
    name: str
    oauth2: Oauth2
    proxy_url: str
    read_recent: bool
    remote_timeout: str
    required_matchers: dict[str, str]
    tls_config: TLSConfig2
    url: str

    def __init__(
        self,
        authorization: Authorization2 = None,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        headers: dict[str, str] = None,
        name: str = None,
        oauth2: Oauth2 = None,
        proxy_url: str = None,
        read_recent: bool = None,
        remote_timeout: str = None,
        required_matchers: dict[str, str] = None,
        tls_config: TLSConfig2 = None,
        url: str = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            bearer_token_file=bearer_token_file,
            headers=headers,
            name=name,
            oauth2=oauth2,
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
    retry_on_rate_limit: bool

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
        retry_on_rate_limit: bool = None,
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
            retry_on_rate_limit=retry_on_rate_limit,
        )


class Sigv4(KubernetesObject):
    __slots__ = ()

    access_key: core.ConfigMapKeySelector
    profile: str
    region: str
    role_arn: str
    secret_key: core.SecretKeySelector

    def __init__(
        self,
        access_key: core.ConfigMapKeySelector = None,
        profile: str = None,
        region: str = None,
        role_arn: str = None,
        secret_key: core.SecretKeySelector = None,
    ):
        super().__init__(access_key=access_key, profile=profile, region=region, role_arn=role_arn, secret_key=secret_key)


class WriteRelabelConfig(KubernetesObject):
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


class RemoteWrite(KubernetesObject):
    __slots__ = ()

    _required_ = ["url"]

    authorization: Authorization2
    basic_auth: BasicAuth
    bearer_token: str
    bearer_token_file: str
    headers: dict[str, str]
    metadata_config: MetadataConfig
    name: str
    oauth2: Oauth2
    proxy_url: str
    queue_config: QueueConfig
    remote_timeout: str
    send_exemplars: bool
    sigv4: Sigv4
    tls_config: TLSConfig2
    url: str
    write_relabel_configs: list[WriteRelabelConfig]

    def __init__(
        self,
        authorization: Authorization2 = None,
        basic_auth: BasicAuth = None,
        bearer_token: str = None,
        bearer_token_file: str = None,
        headers: dict[str, str] = None,
        metadata_config: MetadataConfig = None,
        name: str = None,
        oauth2: Oauth2 = None,
        proxy_url: str = None,
        queue_config: QueueConfig = None,
        remote_timeout: str = None,
        send_exemplars: bool = None,
        sigv4: Sigv4 = None,
        tls_config: TLSConfig2 = None,
        url: str = None,
        write_relabel_configs: list[WriteRelabelConfig] = None,
    ):
        super().__init__(
            authorization=authorization,
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            bearer_token_file=bearer_token_file,
            headers=headers,
            metadata_config=metadata_config,
            name=name,
            oauth2=oauth2,
            proxy_url=proxy_url,
            queue_config=queue_config,
            remote_timeout=remote_timeout,
            send_exemplars=send_exemplars,
            sigv4=sigv4,
            tls_config=tls_config,
            url=url,
            write_relabel_configs=write_relabel_configs,
        )


class PrometheusSpecRule(KubernetesObject):
    __slots__ = ()

    alert: Alert

    def __init__(self, alert: Alert = None):
        super().__init__(alert=alert)


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


class Thano(KubernetesObject):
    __slots__ = ()

    base_image: str
    grpc_server_tls_config: GrpcServerTlsConfig
    image: str
    listen_local: bool
    log_format: str
    log_level: str
    min_time: str
    object_storage_config: core.ConfigMapKeySelector
    object_storage_config_file: str
    ready_timeout: str
    resources: core.ResourceRequirements
    sha: str
    tag: str
    tracing_config: core.ConfigMapKeySelector
    tracing_config_file: str
    version: str
    volume_mounts: list[VolumeMount]

    def __init__(
        self,
        base_image: str = None,
        grpc_server_tls_config: GrpcServerTlsConfig = None,
        image: str = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        min_time: str = None,
        object_storage_config: core.ConfigMapKeySelector = None,
        object_storage_config_file: str = None,
        ready_timeout: str = None,
        resources: core.ResourceRequirements = None,
        sha: str = None,
        tag: str = None,
        tracing_config: core.ConfigMapKeySelector = None,
        tracing_config_file: str = None,
        version: str = None,
        volume_mounts: list[VolumeMount] = None,
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
            ready_timeout=ready_timeout,
            resources=resources,
            sha=sha,
            tag=tag,
            tracing_config=tracing_config,
            tracing_config_file=tracing_config_file,
            version=version,
            volume_mounts=volume_mounts,
        )


class WEBTLSConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["cert", "key_secret"]

    _field_names_ = {
        "client_ca": "client_ca",
    }

    cert: Cert
    cipher_suites: list[str]
    client_auth_type: str
    client_ca: CA
    curve_preferences: list[str]
    key_secret: core.SecretKeySelector
    max_version: str
    min_version: str
    prefer_server_cipher_suites: bool

    def __init__(
        self,
        cert: Cert = None,
        cipher_suites: list[str] = None,
        client_auth_type: str = None,
        client_ca: CA = None,
        curve_preferences: list[str] = None,
        key_secret: core.SecretKeySelector = None,
        max_version: str = None,
        min_version: str = None,
        prefer_server_cipher_suites: bool = None,
    ):
        super().__init__(
            cert=cert,
            cipher_suites=cipher_suites,
            client_auth_type=client_auth_type,
            client_ca=client_ca,
            curve_preferences=curve_preferences,
            key_secret=key_secret,
            max_version=max_version,
            min_version=min_version,
            prefer_server_cipher_suites=prefer_server_cipher_suites,
        )


class WEB(KubernetesObject):
    __slots__ = ()

    page_title: str
    tls_config: WEBTLSConfig

    def __init__(self, page_title: str = None, tls_config: WEBTLSConfig = None):
        super().__init__(page_title=page_title, tls_config=tls_config)


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

    additional_alert_manager_configs: core.ConfigMapKeySelector
    additional_alert_relabel_configs: core.ConfigMapKeySelector
    additional_scrape_configs: core.ConfigMapKeySelector
    affinity: core.Affinity
    alerting: Alerting
    allow_overlapping_blocks: bool
    apiserver_config: APIserverConfig
    arbitrary_fs_access_through_sms: ArbitraryFSAccessThroughSM
    base_image: str
    config_maps: list[str]
    containers: list[core.Container]
    disable_compaction: bool
    enable_admin_api: bool
    enable_features: list[str]
    enforced_body_size_limit: str
    enforced_label_limit: int
    enforced_label_name_length_limit: int
    enforced_label_value_length_limit: int
    enforced_namespace_label: str
    enforced_sample_limit: int
    enforced_target_limit: int
    evaluation_interval: str
    external_labels: dict[str, str]
    external_url: str
    ignore_namespace_selectors: bool
    image: str
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    listen_local: bool
    log_format: str
    log_level: str
    min_ready_seconds: int
    node_selector: dict[str, str]
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
    prometheus_rules_excluded_from_enforce: list[PrometheusRulesExcludedFromEnforce]
    query: Query
    query_log_file: str
    remote_read: list[RemoteRead]
    remote_write: list[RemoteWrite]
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
    secrets: list[str]
    security_context: core.PodSecurityContext
    service_account_name: str
    service_monitor_namespace_selector: meta.LabelSelector
    service_monitor_selector: meta.LabelSelector
    sha: str
    shards: int
    storage: Storage
    tag: str
    thanos: Thano
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    version: str
    volume_mounts: list[core.VolumeMount]
    volumes: list[core.Volume]
    wal_compression: bool
    web: WEB

    def __init__(
        self,
        additional_alert_manager_configs: core.ConfigMapKeySelector = None,
        additional_alert_relabel_configs: core.ConfigMapKeySelector = None,
        additional_scrape_configs: core.ConfigMapKeySelector = None,
        affinity: core.Affinity = None,
        alerting: Alerting = None,
        allow_overlapping_blocks: bool = None,
        apiserver_config: APIserverConfig = None,
        arbitrary_fs_access_through_sms: ArbitraryFSAccessThroughSM = None,
        base_image: str = None,
        config_maps: list[str] = None,
        containers: list[core.Container] = None,
        disable_compaction: bool = None,
        enable_admin_api: bool = None,
        enable_features: list[str] = None,
        enforced_body_size_limit: str = None,
        enforced_label_limit: int = None,
        enforced_label_name_length_limit: int = None,
        enforced_label_value_length_limit: int = None,
        enforced_namespace_label: str = None,
        enforced_sample_limit: int = None,
        enforced_target_limit: int = None,
        evaluation_interval: str = None,
        external_labels: dict[str, str] = None,
        external_url: str = None,
        ignore_namespace_selectors: bool = None,
        image: str = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        min_ready_seconds: int = None,
        node_selector: dict[str, str] = None,
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
        prometheus_rules_excluded_from_enforce: list[PrometheusRulesExcludedFromEnforce] = None,
        query: Query = None,
        query_log_file: str = None,
        remote_read: list[RemoteRead] = None,
        remote_write: list[RemoteWrite] = None,
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
        secrets: list[str] = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        service_monitor_namespace_selector: meta.LabelSelector = None,
        service_monitor_selector: meta.LabelSelector = None,
        sha: str = None,
        shards: int = None,
        storage: Storage = None,
        tag: str = None,
        thanos: Thano = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        version: str = None,
        volume_mounts: list[core.VolumeMount] = None,
        volumes: list[core.Volume] = None,
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
            enable_features=enable_features,
            enforced_body_size_limit=enforced_body_size_limit,
            enforced_label_limit=enforced_label_limit,
            enforced_label_name_length_limit=enforced_label_name_length_limit,
            enforced_label_value_length_limit=enforced_label_value_length_limit,
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
            min_ready_seconds=min_ready_seconds,
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


class Prometheus(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "Prometheus"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PrometheusSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PrometheusSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PrometheusRuleSpec(KubernetesObject):
    __slots__ = ()

    groups: list[Group]

    def __init__(self, groups: list[Group] = None):
        super().__init__(groups=groups)


class PrometheusRule(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "PrometheusRule"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PrometheusRuleSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PrometheusRuleSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ServiceMonitorSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["endpoints", "selector"]

    endpoints: list[Endpoint]
    job_label: str
    label_limit: int
    label_name_length_limit: int
    label_value_length_limit: int
    namespace_selector: NamespaceSelector
    pod_target_labels: list[str]
    sample_limit: int
    selector: meta.LabelSelector
    target_labels: list[str]
    target_limit: int

    def __init__(
        self,
        endpoints: list[Endpoint] = None,
        job_label: str = None,
        label_limit: int = None,
        label_name_length_limit: int = None,
        label_value_length_limit: int = None,
        namespace_selector: NamespaceSelector = None,
        pod_target_labels: list[str] = None,
        sample_limit: int = None,
        selector: meta.LabelSelector = None,
        target_labels: list[str] = None,
        target_limit: int = None,
    ):
        super().__init__(
            endpoints=endpoints,
            job_label=job_label,
            label_limit=label_limit,
            label_name_length_limit=label_name_length_limit,
            label_value_length_limit=label_value_length_limit,
            namespace_selector=namespace_selector,
            pod_target_labels=pod_target_labels,
            sample_limit=sample_limit,
            selector=selector,
            target_labels=target_labels,
            target_limit=target_limit,
        )


class ServiceMonitor(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "ServiceMonitor"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ServiceMonitorSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ServiceMonitorSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ThanosRulerSpec(KubernetesObject):
    __slots__ = ()

    affinity: core.Affinity
    alert_drop_labels: list[str]
    alert_query_url: str
    alert_relabel_config_file: str
    alert_relabel_configs: core.ConfigMapKeySelector
    alertmanagers_config: core.ConfigMapKeySelector
    alertmanagers_url: list[str]
    containers: list[core.Container]
    enforced_namespace_label: str
    evaluation_interval: str
    external_prefix: str
    grpc_server_tls_config: GrpcServerTlsConfig
    image: str
    image_pull_secrets: list[core.LocalObjectReference]
    init_containers: list[core.Container]
    labels: dict[str, str]
    listen_local: bool
    log_format: str
    log_level: str
    min_ready_seconds: int
    node_selector: dict[str, str]
    object_storage_config: core.ConfigMapKeySelector
    object_storage_config_file: str
    paused: bool
    pod_metadata: PodMetadata
    port_name: str
    priority_class_name: str
    prometheus_rules_excluded_from_enforce: list[PrometheusRulesExcludedFromEnforce]
    query_config: core.ConfigMapKeySelector
    query_endpoints: list[str]
    replicas: int
    resources: core.ResourceRequirements
    retention: str
    route_prefix: str
    rule_namespace_selector: meta.LabelSelector
    rule_selector: meta.LabelSelector
    security_context: core.PodSecurityContext
    service_account_name: str
    storage: Storage
    tolerations: list[core.Toleration]
    topology_spread_constraints: list[core.TopologySpreadConstraint]
    tracing_config: core.ConfigMapKeySelector
    volumes: list[core.Volume]

    def __init__(
        self,
        affinity: core.Affinity = None,
        alert_drop_labels: list[str] = None,
        alert_query_url: str = None,
        alert_relabel_config_file: str = None,
        alert_relabel_configs: core.ConfigMapKeySelector = None,
        alertmanagers_config: core.ConfigMapKeySelector = None,
        alertmanagers_url: list[str] = None,
        containers: list[core.Container] = None,
        enforced_namespace_label: str = None,
        evaluation_interval: str = None,
        external_prefix: str = None,
        grpc_server_tls_config: GrpcServerTlsConfig = None,
        image: str = None,
        image_pull_secrets: list[core.LocalObjectReference] = None,
        init_containers: list[core.Container] = None,
        labels: dict[str, str] = None,
        listen_local: bool = None,
        log_format: str = None,
        log_level: str = None,
        min_ready_seconds: int = None,
        node_selector: dict[str, str] = None,
        object_storage_config: core.ConfigMapKeySelector = None,
        object_storage_config_file: str = None,
        paused: bool = None,
        pod_metadata: PodMetadata = None,
        port_name: str = None,
        priority_class_name: str = None,
        prometheus_rules_excluded_from_enforce: list[PrometheusRulesExcludedFromEnforce] = None,
        query_config: core.ConfigMapKeySelector = None,
        query_endpoints: list[str] = None,
        replicas: int = None,
        resources: core.ResourceRequirements = None,
        retention: str = None,
        route_prefix: str = None,
        rule_namespace_selector: meta.LabelSelector = None,
        rule_selector: meta.LabelSelector = None,
        security_context: core.PodSecurityContext = None,
        service_account_name: str = None,
        storage: Storage = None,
        tolerations: list[core.Toleration] = None,
        topology_spread_constraints: list[core.TopologySpreadConstraint] = None,
        tracing_config: core.ConfigMapKeySelector = None,
        volumes: list[core.Volume] = None,
    ):
        super().__init__(
            affinity=affinity,
            alert_drop_labels=alert_drop_labels,
            alert_query_url=alert_query_url,
            alert_relabel_config_file=alert_relabel_config_file,
            alert_relabel_configs=alert_relabel_configs,
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
            min_ready_seconds=min_ready_seconds,
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

    _api_version_ = "monitoring.coreos.com/v1"
    _api_group_ = "monitoring.coreos.com"
    _kind_ = "ThanosRuler"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ThanosRulerSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ThanosRulerSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
