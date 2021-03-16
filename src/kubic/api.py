from typing import Any, Dict, List, Union

from .base import KubernetesObject, KubernetesApiResource


Time = str


FieldsV1 = Dict[str, Any]


class ManagedFieldsEntry(KubernetesObject):
    __slots__ = ()

    api_version: str
    fields_type: str
    fields_v1: FieldsV1
    manager: str
    operation: str
    time: Time

    def __init__(
        self,
        api_version: str = None,
        fields_type: str = None,
        fields_v1: FieldsV1 = None,
        manager: str = None,
        operation: str = None,
        time: Time = None,
    ):
        super().__init__(
            api_version=api_version,
            fields_type=fields_type,
            fields_v1=fields_v1,
            manager=manager,
            operation=operation,
            time=time,
        )


class OwnerReference(KubernetesObject):
    __slots__ = ()

    api_version: str
    block_owner_deletion: bool
    controller: bool
    kind: str
    name: str
    uid: str

    _required_ = ["api_version", "kind", "name", "uid"]

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
            api_version=api_version,
            block_owner_deletion=block_owner_deletion,
            controller=controller,
            kind=kind,
            name=name,
            uid=uid,
        )


class ObjectMeta(KubernetesObject):
    __slots__ = ()

    annotations: Dict[str, str]
    cluster_name: str
    creation_timestamp: Time
    deletion_grace_period_seconds: int
    deletion_timestamp: Time
    finalizers: List[str]
    generate_name: str
    generation: int
    labels: Dict[str, str]
    managed_fields: List[ManagedFieldsEntry]
    name: str
    namespace: str
    owner_references: List[OwnerReference]
    resource_version: str
    self_link: str
    uid: str

    def __init__(
        self,
        annotations: Dict[str, str] = None,
        cluster_name: str = None,
        creation_timestamp: Time = None,
        deletion_grace_period_seconds: int = None,
        deletion_timestamp: Time = None,
        finalizers: List[str] = None,
        generate_name: str = None,
        generation: int = None,
        labels: Dict[str, str] = None,
        managed_fields: List[ManagedFieldsEntry] = None,
        name: str = None,
        namespace: str = None,
        owner_references: List[OwnerReference] = None,
        resource_version: str = None,
        self_link: str = None,
        uid: str = None,
    ):
        super().__init__(
            annotations=annotations,
            cluster_name=cluster_name,
            creation_timestamp=creation_timestamp,
            deletion_grace_period_seconds=deletion_grace_period_seconds,
            deletion_timestamp=deletion_timestamp,
            finalizers=finalizers,
            generate_name=generate_name,
            generation=generation,
            labels=labels,
            managed_fields=managed_fields,
            name=name,
            namespace=namespace,
            owner_references=owner_references,
            resource_version=resource_version,
            self_link=self_link,
            uid=uid,
        )


class NamespaceSpec(KubernetesObject):
    __slots__ = ()

    finalizers: List[str]

    def __init__(self, finalizers: List[str] = None):
        super().__init__(finalizers=finalizers)


class Namespace(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    metadata: ObjectMeta
    spec: NamespaceSpec

    def __init__(
        self, name: str, metadata: ObjectMeta = None, spec: NamespaceSpec = None
    ):
        super().__init__("v1", "Namespace", name, "", metadata=metadata, spec=spec)


class PolicyRule(KubernetesObject):
    __slots__ = ()
    _field_names_ = {
        "non_resource_urls": "nonResourceURLs",
    }
    _revfield_names_ = {
        "nonResourceURLs": "non_resource_urls",
    }

    api_groups: List[str]
    non_resource_urls: List[str]
    resource_names: List[str]
    resources: List[str]
    verbs: List[str]

    _required_ = ["verbs"]

    def __init__(
        self,
        api_groups: List[str] = None,
        non_resource_urls: List[str] = None,
        resource_names: List[str] = None,
        resources: List[str] = None,
        verbs: List[str] = None,
    ):
        super().__init__(
            api_groups=api_groups,
            non_resource_urls=non_resource_urls,
            resource_names=resource_names,
            resources=resources,
            verbs=verbs,
        )


class Role(KubernetesApiResource):
    __slots__ = ()

    _group_ = "rbac.authorization.k8s.io"

    metadata: ObjectMeta
    rules: List[PolicyRule]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        rules: List[PolicyRule] = None,
    ):
        super().__init__(
            "rbac.authorization.k8s.io/v1",
            "Role",
            name,
            namespace,
            metadata=metadata,
            rules=rules,
        )


class RoleRef(KubernetesObject):
    __slots__ = ()

    api_group: str
    kind: str
    name: str

    _required_ = ["api_group", "kind", "name"]

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class Subject(KubernetesObject):
    __slots__ = ()

    api_group: str
    kind: str
    name: str
    namespace: str

    _required_ = ["kind", "name"]

    def __init__(
        self,
        api_group: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
    ):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace)


class RoleBinding(KubernetesApiResource):
    __slots__ = ()

    _group_ = "rbac.authorization.k8s.io"

    metadata: ObjectMeta
    role_ref: RoleRef
    subjects: List[Subject]

    _required_ = ["role_ref"]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        role_ref: RoleRef = None,
        subjects: List[Subject] = None,
    ):
        super().__init__(
            "rbac.authorization.k8s.io/v1",
            "RoleBinding",
            name,
            namespace,
            metadata=metadata,
            role_ref=role_ref,
            subjects=subjects,
        )


class LabelSelectorRequirement(KubernetesObject):
    __slots__ = ()

    key: str
    operator: str
    values: List[str]

    _required_ = ["key", "operator"]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class LabelSelector(KubernetesObject):
    __slots__ = ()

    match_expressions: List[LabelSelectorRequirement]
    match_labels: Dict[str, str]

    def __init__(
        self,
        match_expressions: List[LabelSelectorRequirement] = None,
        match_labels: Dict[str, str] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_labels=match_labels)


class AggregationRule(KubernetesObject):
    __slots__ = ()

    cluster_role_selectors: List[LabelSelector]

    def __init__(self, cluster_role_selectors: List[LabelSelector] = None):
        super().__init__(cluster_role_selectors=cluster_role_selectors)


class ClusterRole(KubernetesApiResource):
    __slots__ = ()

    _group_ = "rbac.authorization.k8s.io"

    aggregation_rule: AggregationRule
    metadata: ObjectMeta
    rules: List[PolicyRule]

    def __init__(
        self,
        name: str,
        aggregation_rule: AggregationRule = None,
        metadata: ObjectMeta = None,
        rules: List[PolicyRule] = None,
    ):
        super().__init__(
            "rbac.authorization.k8s.io/v1",
            "ClusterRole",
            name,
            "",
            aggregation_rule=aggregation_rule,
            metadata=metadata,
            rules=rules,
        )


class ClusterRoleBinding(KubernetesApiResource):
    __slots__ = ()

    _group_ = "rbac.authorization.k8s.io"

    metadata: ObjectMeta
    role_ref: RoleRef
    subjects: List[Subject]

    _required_ = ["role_ref"]

    def __init__(
        self,
        name: str,
        metadata: ObjectMeta = None,
        role_ref: RoleRef = None,
        subjects: List[Subject] = None,
    ):
        super().__init__(
            "rbac.authorization.k8s.io/v1",
            "ClusterRoleBinding",
            name,
            "",
            metadata=metadata,
            role_ref=role_ref,
            subjects=subjects,
        )


Base64 = str


class ConfigMap(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    binary_data: Dict[str, Base64]
    data: Dict[str, str]
    immutable: bool
    metadata: ObjectMeta

    def __init__(
        self,
        name: str,
        namespace: str = None,
        binary_data: Dict[str, Base64] = None,
        data: Dict[str, str] = None,
        immutable: bool = None,
        metadata: ObjectMeta = None,
    ):
        super().__init__(
            "v1",
            "ConfigMap",
            name,
            namespace,
            binary_data=binary_data,
            data=data,
            immutable=immutable,
            metadata=metadata,
        )


class Secret(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    data: Dict[str, Base64]
    immutable: bool
    metadata: ObjectMeta
    string_data: Dict[str, str]
    type: str

    def __init__(
        self,
        name: str,
        namespace: str = None,
        data: Dict[str, Base64] = None,
        immutable: bool = None,
        metadata: ObjectMeta = None,
        string_data: Dict[str, str] = None,
        type: str = None,
    ):
        super().__init__(
            "v1",
            "Secret",
            name,
            namespace,
            data=data,
            immutable=immutable,
            metadata=metadata,
            string_data=string_data,
            type=type,
        )


IntOrString = Union[int, str]


class RollingUpdateDeployment(KubernetesObject):
    __slots__ = ()

    max_surge: IntOrString
    max_unavailable: IntOrString

    def __init__(
        self, max_surge: IntOrString = None, max_unavailable: IntOrString = None
    ):
        super().__init__(max_surge=max_surge, max_unavailable=max_unavailable)


class DeploymentStrategy(KubernetesObject):
    __slots__ = ()

    rolling_update: RollingUpdateDeployment
    type: str

    def __init__(
        self, rolling_update: RollingUpdateDeployment = None, type: str = None
    ):
        super().__init__(rolling_update=rolling_update, type=type)


class NodeSelectorRequirement(KubernetesObject):
    __slots__ = ()

    key: str
    operator: str
    values: List[str]

    _required_ = ["key", "operator"]

    def __init__(self, key: str = None, operator: str = None, values: List[str] = None):
        super().__init__(key=key, operator=operator, values=values)


class NodeSelectorTerm(KubernetesObject):
    __slots__ = ()

    match_expressions: List[NodeSelectorRequirement]
    match_fields: List[NodeSelectorRequirement]

    def __init__(
        self,
        match_expressions: List[NodeSelectorRequirement] = None,
        match_fields: List[NodeSelectorRequirement] = None,
    ):
        super().__init__(match_expressions=match_expressions, match_fields=match_fields)


class PreferredSchedulingTerm(KubernetesObject):
    __slots__ = ()

    preference: NodeSelectorTerm
    weight: int

    _required_ = ["preference", "weight"]

    def __init__(self, preference: NodeSelectorTerm = None, weight: int = None):
        super().__init__(preference=preference, weight=weight)


class NodeSelector(KubernetesObject):
    __slots__ = ()

    node_selector_terms: List[NodeSelectorTerm]

    _required_ = ["node_selector_terms"]

    def __init__(self, node_selector_terms: List[NodeSelectorTerm] = None):
        super().__init__(node_selector_terms=node_selector_terms)


class NodeAffinity(KubernetesObject):
    __slots__ = ()

    preferred_during_scheduling_ignored_during_execution: List[PreferredSchedulingTerm]
    required_during_scheduling_ignored_during_execution: NodeSelector

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[
            PreferredSchedulingTerm
        ] = None,
        required_during_scheduling_ignored_during_execution: NodeSelector = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAffinityTerm(KubernetesObject):
    __slots__ = ()

    label_selector: LabelSelector
    namespaces: List[str]
    topology_key: str

    _required_ = ["topology_key"]

    def __init__(
        self,
        label_selector: LabelSelector = None,
        namespaces: List[str] = None,
        topology_key: str = None,
    ):
        super().__init__(
            label_selector=label_selector,
            namespaces=namespaces,
            topology_key=topology_key,
        )


class WeightedPodAffinityTerm(KubernetesObject):
    __slots__ = ()

    pod_affinity_term: PodAffinityTerm
    weight: int

    _required_ = ["pod_affinity_term", "weight"]

    def __init__(self, pod_affinity_term: PodAffinityTerm = None, weight: int = None):
        super().__init__(pod_affinity_term=pod_affinity_term, weight=weight)


class PodAffinity(KubernetesObject):
    __slots__ = ()

    preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm]
    required_during_scheduling_ignored_during_execution: List[PodAffinityTerm]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[
            WeightedPodAffinityTerm
        ] = None,
        required_during_scheduling_ignored_during_execution: List[
            PodAffinityTerm
        ] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class PodAntiAffinity(KubernetesObject):
    __slots__ = ()

    preferred_during_scheduling_ignored_during_execution: List[WeightedPodAffinityTerm]
    required_during_scheduling_ignored_during_execution: List[PodAffinityTerm]

    def __init__(
        self,
        preferred_during_scheduling_ignored_during_execution: List[
            WeightedPodAffinityTerm
        ] = None,
        required_during_scheduling_ignored_during_execution: List[
            PodAffinityTerm
        ] = None,
    ):
        super().__init__(
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
        )


class Affinity(KubernetesObject):
    __slots__ = ()

    node_affinity: NodeAffinity
    pod_affinity: PodAffinity
    pod_anti_affinity: PodAntiAffinity

    def __init__(
        self,
        node_affinity: NodeAffinity = None,
        pod_affinity: PodAffinity = None,
        pod_anti_affinity: PodAntiAffinity = None,
    ):
        super().__init__(
            node_affinity=node_affinity,
            pod_affinity=pod_affinity,
            pod_anti_affinity=pod_anti_affinity,
        )


class ConfigMapKeySelector(KubernetesObject):
    __slots__ = ()

    key: str
    name: str
    optional: bool

    _required_ = ["key"]

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class ObjectFieldSelector(KubernetesObject):
    __slots__ = ()

    api_version: str
    field_path: str

    _required_ = ["field_path"]

    def __init__(self, api_version: str = None, field_path: str = None):
        super().__init__(api_version=api_version, field_path=field_path)


Quantity = Union[str, int, float]


class ResourceFieldSelector(KubernetesObject):
    __slots__ = ()

    container_name: str
    divisor: Quantity
    resource: str

    _required_ = ["resource"]

    def __init__(
        self, container_name: str = None, divisor: Quantity = None, resource: str = None
    ):
        super().__init__(
            container_name=container_name, divisor=divisor, resource=resource
        )


class SecretKeySelector(KubernetesObject):
    __slots__ = ()

    key: str
    name: str
    optional: bool

    _required_ = ["key"]

    def __init__(self, key: str = None, name: str = None, optional: bool = None):
        super().__init__(key=key, name=name, optional=optional)


class EnvVarSource(KubernetesObject):
    __slots__ = ()

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
            config_map_key_ref=config_map_key_ref,
            field_ref=field_ref,
            resource_field_ref=resource_field_ref,
            secret_key_ref=secret_key_ref,
        )


class EnvVar(KubernetesObject):
    __slots__ = ()

    name: str
    value: str
    value_from: EnvVarSource

    _required_ = ["name"]

    def __init__(
        self, name: str = None, value: str = None, value_from: EnvVarSource = None
    ):
        super().__init__(name=name, value=value, value_from=value_from)


class ConfigMapEnvSource(KubernetesObject):
    __slots__ = ()

    name: str
    optional: bool

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class SecretEnvSource(KubernetesObject):
    __slots__ = ()

    name: str
    optional: bool

    def __init__(self, name: str = None, optional: bool = None):
        super().__init__(name=name, optional=optional)


class EnvFromSource(KubernetesObject):
    __slots__ = ()

    config_map_ref: ConfigMapEnvSource
    prefix: str
    secret_ref: SecretEnvSource

    def __init__(
        self,
        config_map_ref: ConfigMapEnvSource = None,
        prefix: str = None,
        secret_ref: SecretEnvSource = None,
    ):
        super().__init__(
            config_map_ref=config_map_ref, prefix=prefix, secret_ref=secret_ref
        )


class ExecAction(KubernetesObject):
    __slots__ = ()

    command: List[str]

    def __init__(self, command: List[str] = None):
        super().__init__(command=command)


class HTTPHeader(KubernetesObject):
    __slots__ = ()

    name: str
    value: str

    _required_ = ["name", "value"]

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class HTTPGetAction(KubernetesObject):
    __slots__ = ()

    host: str
    http_headers: List[HTTPHeader]
    path: str
    port: IntOrString
    scheme: str

    _required_ = ["port"]

    def __init__(
        self,
        host: str = None,
        http_headers: List[HTTPHeader] = None,
        path: str = None,
        port: IntOrString = None,
        scheme: str = None,
    ):
        super().__init__(
            host=host, http_headers=http_headers, path=path, port=port, scheme=scheme
        )


class TCPSocketAction(KubernetesObject):
    __slots__ = ()

    host: str
    port: IntOrString

    _required_ = ["port"]

    def __init__(self, host: str = None, port: IntOrString = None):
        super().__init__(host=host, port=port)


class Handler(KubernetesObject):
    __slots__ = ()

    exec: ExecAction
    http_get: HTTPGetAction
    tcp_socket: TCPSocketAction

    def __init__(
        self,
        exec: ExecAction = None,
        http_get: HTTPGetAction = None,
        tcp_socket: TCPSocketAction = None,
    ):
        super().__init__(exec=exec, http_get=http_get, tcp_socket=tcp_socket)


class Lifecycle(KubernetesObject):
    __slots__ = ()

    post_start: Handler
    pre_stop: Handler

    def __init__(self, post_start: Handler = None, pre_stop: Handler = None):
        super().__init__(post_start=post_start, pre_stop=pre_stop)


class Probe(KubernetesObject):
    __slots__ = ()

    exec: ExecAction
    failure_threshold: int
    http_get: HTTPGetAction
    initial_delay_seconds: int
    period_seconds: int
    success_threshold: int
    tcp_socket: TCPSocketAction
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


class ContainerPort(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["container_port"]

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


class ResourceRequirements(KubernetesObject):
    __slots__ = ()

    limits: Dict[str, Quantity]
    requests: Dict[str, Quantity]

    def __init__(
        self, limits: Dict[str, Quantity] = None, requests: Dict[str, Quantity] = None
    ):
        super().__init__(limits=limits, requests=requests)


class Capabilities(KubernetesObject):
    __slots__ = ()

    add: List[str]
    drop: List[str]

    def __init__(self, add: List[str] = None, drop: List[str] = None):
        super().__init__(add=add, drop=drop)


class SELinuxOptions(KubernetesObject):
    __slots__ = ()

    level: str
    role: str
    type: str
    user: str

    def __init__(
        self, level: str = None, role: str = None, type: str = None, user: str = None
    ):
        super().__init__(level=level, role=role, type=type, user=user)


class SeccompProfile(KubernetesObject):
    __slots__ = ()

    localhost_profile: str
    type: str

    _required_ = ["type"]

    def __init__(self, localhost_profile: str = None, type: str = None):
        super().__init__(localhost_profile=localhost_profile, type=type)


class WindowsSecurityContextOptions(KubernetesObject):
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

    device_path: str
    name: str

    _required_ = ["device_path", "name"]

    def __init__(self, device_path: str = None, name: str = None):
        super().__init__(device_path=device_path, name=name)


class VolumeMount(KubernetesObject):
    __slots__ = ()

    mount_path: str
    mount_propagation: str
    name: str
    read_only: bool
    sub_path: str
    sub_path_expr: str

    _required_ = ["mount_path", "name"]

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

    _required_ = ["name"]

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


class PodDNSConfigOption(KubernetesObject):
    __slots__ = ()

    name: str
    value: str

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class PodDNSConfig(KubernetesObject):
    __slots__ = ()

    nameservers: List[str]
    options: List[PodDNSConfigOption]
    searches: List[str]

    def __init__(
        self,
        nameservers: List[str] = None,
        options: List[PodDNSConfigOption] = None,
        searches: List[str] = None,
    ):
        super().__init__(nameservers=nameservers, options=options, searches=searches)


class EphemeralContainer(KubernetesObject):
    __slots__ = ()

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

    _required_ = ["name"]

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


class HostAlias(KubernetesObject):
    __slots__ = ()

    hostnames: List[str]
    ip: str

    def __init__(self, hostnames: List[str] = None, ip: str = None):
        super().__init__(hostnames=hostnames, ip=ip)


class LocalObjectReference(KubernetesObject):
    __slots__ = ()

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class PodReadinessGate(KubernetesObject):
    __slots__ = ()

    condition_type: str

    _required_ = ["condition_type"]

    def __init__(self, condition_type: str = None):
        super().__init__(condition_type=condition_type)


class Sysctl(KubernetesObject):
    __slots__ = ()

    name: str
    value: str

    _required_ = ["name", "value"]

    def __init__(self, name: str = None, value: str = None):
        super().__init__(name=name, value=value)


class PodSecurityContext(KubernetesObject):
    __slots__ = ()

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

    effect: str
    key: str
    operator: str
    toleration_seconds: int
    value: str

    def __init__(
        self,
        effect: str = None,
        key: str = None,
        operator: str = None,
        toleration_seconds: int = None,
        value: str = None,
    ):
        super().__init__(
            effect=effect,
            key=key,
            operator=operator,
            toleration_seconds=toleration_seconds,
            value=value,
        )


class TopologySpreadConstraint(KubernetesObject):
    __slots__ = ()

    label_selector: LabelSelector
    max_skew: int
    topology_key: str
    when_unsatisfiable: str

    _required_ = ["max_skew", "topology_key", "when_unsatisfiable"]

    def __init__(
        self,
        label_selector: LabelSelector = None,
        max_skew: int = None,
        topology_key: str = None,
        when_unsatisfiable: str = None,
    ):
        super().__init__(
            label_selector=label_selector,
            max_skew=max_skew,
            topology_key=topology_key,
            when_unsatisfiable=when_unsatisfiable,
        )


class AWSElasticBlockStoreVolumeSource(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["volume_id"]

    def __init__(
        self,
        fs_type: str = None,
        partition: int = None,
        read_only: bool = None,
        volume_id: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
            volume_id=volume_id,
        )


class AzureDiskVolumeSource(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["disk_name", "disk_uri"]

    def __init__(
        self,
        caching_mode: str = None,
        disk_name: str = None,
        disk_uri: str = None,
        fs_type: str = None,
        kind: str = None,
        read_only: bool = None,
    ):
        super().__init__(
            caching_mode=caching_mode,
            disk_name=disk_name,
            disk_uri=disk_uri,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
        )


class AzureFileVolumeSource(KubernetesObject):
    __slots__ = ()

    read_only: bool
    secret_name: str
    share_name: str

    _required_ = ["secret_name", "share_name"]

    def __init__(
        self, read_only: bool = None, secret_name: str = None, share_name: str = None
    ):
        super().__init__(
            read_only=read_only, secret_name=secret_name, share_name=share_name
        )


class CephFSVolumeSource(KubernetesObject):
    __slots__ = ()

    monitors: List[str]
    path: str
    read_only: bool
    secret_file: str
    secret_ref: LocalObjectReference
    user: str

    _required_ = ["monitors"]

    def __init__(
        self,
        monitors: List[str] = None,
        path: str = None,
        read_only: bool = None,
        secret_file: str = None,
        secret_ref: LocalObjectReference = None,
        user: str = None,
    ):
        super().__init__(
            monitors=monitors,
            path=path,
            read_only=read_only,
            secret_file=secret_file,
            secret_ref=secret_ref,
            user=user,
        )


class CinderVolumeSource(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["volume_id"]

    def __init__(
        self,
        fs_type: str = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
        volume_id: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            read_only=read_only,
            secret_ref=secret_ref,
            volume_id=volume_id,
        )


class KeyToPath(KubernetesObject):
    __slots__ = ()

    key: str
    mode: int
    path: str

    _required_ = ["key", "path"]

    def __init__(self, key: str = None, mode: int = None, path: str = None):
        super().__init__(key=key, mode=mode, path=path)


class ConfigMapVolumeSource(KubernetesObject):
    __slots__ = ()

    default_mode: int
    items: List[KeyToPath]
    name: str
    optional: bool

    def __init__(
        self,
        default_mode: int = None,
        items: List[KeyToPath] = None,
        name: str = None,
        optional: bool = None,
    ):
        super().__init__(
            default_mode=default_mode, items=items, name=name, optional=optional
        )


class CSIVolumeSource(KubernetesObject):
    __slots__ = ()

    driver: str
    fs_type: str
    node_publish_secret_ref: LocalObjectReference
    read_only: bool
    volume_attributes: Dict[str, str]

    _required_ = ["driver"]

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


class DownwardAPIVolumeFile(KubernetesObject):
    __slots__ = ()

    field_ref: ObjectFieldSelector
    mode: int
    path: str
    resource_field_ref: ResourceFieldSelector

    _required_ = ["path"]

    def __init__(
        self,
        field_ref: ObjectFieldSelector = None,
        mode: int = None,
        path: str = None,
        resource_field_ref: ResourceFieldSelector = None,
    ):
        super().__init__(
            field_ref=field_ref,
            mode=mode,
            path=path,
            resource_field_ref=resource_field_ref,
        )


class DownwardAPIVolumeSource(KubernetesObject):
    __slots__ = ()

    default_mode: int
    items: List[DownwardAPIVolumeFile]

    def __init__(
        self, default_mode: int = None, items: List[DownwardAPIVolumeFile] = None
    ):
        super().__init__(default_mode=default_mode, items=items)


class EmptyDirVolumeSource(KubernetesObject):
    __slots__ = ()

    medium: str
    size_limit: Quantity

    def __init__(self, medium: str = None, size_limit: Quantity = None):
        super().__init__(medium=medium, size_limit=size_limit)


class TypedLocalObjectReference(KubernetesObject):
    __slots__ = ()

    api_group: str
    kind: str
    name: str

    _required_ = ["kind", "name"]

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class PersistentVolumeClaimSpec(KubernetesObject):
    __slots__ = ()

    access_modes: List[str]
    data_source: TypedLocalObjectReference
    resources: ResourceRequirements
    selector: LabelSelector
    storage_class_name: str
    volume_mode: str
    volume_name: str

    def __init__(
        self,
        access_modes: List[str] = None,
        data_source: TypedLocalObjectReference = None,
        resources: ResourceRequirements = None,
        selector: LabelSelector = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        volume_name: str = None,
    ):
        super().__init__(
            access_modes=access_modes,
            data_source=data_source,
            resources=resources,
            selector=selector,
            storage_class_name=storage_class_name,
            volume_mode=volume_mode,
            volume_name=volume_name,
        )


class PersistentVolumeClaimTemplate(KubernetesObject):
    __slots__ = ()

    metadata: ObjectMeta
    spec: PersistentVolumeClaimSpec

    _required_ = ["spec"]

    def __init__(
        self, metadata: ObjectMeta = None, spec: PersistentVolumeClaimSpec = None
    ):
        super().__init__(metadata=metadata, spec=spec)


class EphemeralVolumeSource(KubernetesObject):
    __slots__ = ()

    read_only: bool
    volume_claim_template: PersistentVolumeClaimTemplate

    def __init__(
        self,
        read_only: bool = None,
        volume_claim_template: PersistentVolumeClaimTemplate = None,
    ):
        super().__init__(
            read_only=read_only, volume_claim_template=volume_claim_template
        )


class FCVolumeSource(KubernetesObject):
    __slots__ = ()
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
        self,
        fs_type: str = None,
        lun: int = None,
        read_only: bool = None,
        target_wwns: List[str] = None,
        wwids: List[str] = None,
    ):
        super().__init__(
            fs_type=fs_type,
            lun=lun,
            read_only=read_only,
            target_wwns=target_wwns,
            wwids=wwids,
        )


class FlexVolumeSource(KubernetesObject):
    __slots__ = ()

    driver: str
    fs_type: str
    options: Dict[str, str]
    read_only: bool
    secret_ref: LocalObjectReference

    _required_ = ["driver"]

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: Dict[str, str] = None,
        read_only: bool = None,
        secret_ref: LocalObjectReference = None,
    ):
        super().__init__(
            driver=driver,
            fs_type=fs_type,
            options=options,
            read_only=read_only,
            secret_ref=secret_ref,
        )


class FlockerVolumeSource(KubernetesObject):
    __slots__ = ()
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

    fs_type: str
    partition: int
    pd_name: str
    read_only: bool

    _required_ = ["pd_name"]

    def __init__(
        self,
        fs_type: str = None,
        partition: int = None,
        pd_name: str = None,
        read_only: bool = None,
    ):
        super().__init__(
            fs_type=fs_type, partition=partition, pd_name=pd_name, read_only=read_only
        )


class GitRepoVolumeSource(KubernetesObject):
    __slots__ = ()

    directory: str
    repository: str
    revision: str

    _required_ = ["repository"]

    def __init__(
        self, directory: str = None, repository: str = None, revision: str = None
    ):
        super().__init__(directory=directory, repository=repository, revision=revision)


class GlusterfsVolumeSource(KubernetesObject):
    __slots__ = ()

    endpoints: str
    path: str
    read_only: bool

    _required_ = ["endpoints", "path"]

    def __init__(self, endpoints: str = None, path: str = None, read_only: bool = None):
        super().__init__(endpoints=endpoints, path=path, read_only=read_only)


class HostPathVolumeSource(KubernetesObject):
    __slots__ = ()

    path: str
    type: str

    _required_ = ["path"]

    def __init__(self, path: str = None, type: str = None):
        super().__init__(path=path, type=type)


class ISCSIVolumeSource(KubernetesObject):
    __slots__ = ()

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

    _required_ = ["iqn", "lun", "target_portal"]

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


class NFSVolumeSource(KubernetesObject):
    __slots__ = ()

    path: str
    read_only: bool
    server: str

    _required_ = ["path", "server"]

    def __init__(self, path: str = None, read_only: bool = None, server: str = None):
        super().__init__(path=path, read_only=read_only, server=server)


class PersistentVolumeClaimVolumeSource(KubernetesObject):
    __slots__ = ()

    claim_name: str
    read_only: bool

    _required_ = ["claim_name"]

    def __init__(self, claim_name: str = None, read_only: bool = None):
        super().__init__(claim_name=claim_name, read_only=read_only)


class PhotonPersistentDiskVolumeSource(KubernetesObject):
    __slots__ = ()
    _field_names_ = {
        "pd_id": "pdID",
    }
    _revfield_names_ = {
        "pdID": "pd_id",
    }

    fs_type: str
    pd_id: str

    _required_ = ["pd_id"]

    def __init__(self, fs_type: str = None, pd_id: str = None):
        super().__init__(fs_type=fs_type, pd_id=pd_id)


class PortworxVolumeSource(KubernetesObject):
    __slots__ = ()
    _field_names_ = {
        "volume_id": "volumeID",
    }
    _revfield_names_ = {
        "volumeID": "volume_id",
    }

    fs_type: str
    read_only: bool
    volume_id: str

    _required_ = ["volume_id"]

    def __init__(
        self, fs_type: str = None, read_only: bool = None, volume_id: str = None
    ):
        super().__init__(fs_type=fs_type, read_only=read_only, volume_id=volume_id)


class ConfigMapProjection(KubernetesObject):
    __slots__ = ()

    items: List[KeyToPath]
    name: str
    optional: bool

    def __init__(
        self, items: List[KeyToPath] = None, name: str = None, optional: bool = None
    ):
        super().__init__(items=items, name=name, optional=optional)


class DownwardAPIProjection(KubernetesObject):
    __slots__ = ()

    items: List[DownwardAPIVolumeFile]

    def __init__(self, items: List[DownwardAPIVolumeFile] = None):
        super().__init__(items=items)


class SecretProjection(KubernetesObject):
    __slots__ = ()

    items: List[KeyToPath]
    name: str
    optional: bool

    def __init__(
        self, items: List[KeyToPath] = None, name: str = None, optional: bool = None
    ):
        super().__init__(items=items, name=name, optional=optional)


class ServiceAccountTokenProjection(KubernetesObject):
    __slots__ = ()

    audience: str
    expiration_seconds: int
    path: str

    _required_ = ["path"]

    def __init__(
        self, audience: str = None, expiration_seconds: int = None, path: str = None
    ):
        super().__init__(
            audience=audience, expiration_seconds=expiration_seconds, path=path
        )


class VolumeProjection(KubernetesObject):
    __slots__ = ()
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
        super().__init__(
            config_map=config_map,
            downward_api=downward_api,
            secret=secret,
            service_account_token=service_account_token,
        )


class ProjectedVolumeSource(KubernetesObject):
    __slots__ = ()

    default_mode: int
    sources: List[VolumeProjection]

    def __init__(
        self, default_mode: int = None, sources: List[VolumeProjection] = None
    ):
        super().__init__(default_mode=default_mode, sources=sources)


class QuobyteVolumeSource(KubernetesObject):
    __slots__ = ()

    group: str
    read_only: bool
    registry: str
    tenant: str
    user: str
    volume: str

    _required_ = ["registry", "volume"]

    def __init__(
        self,
        group: str = None,
        read_only: bool = None,
        registry: str = None,
        tenant: str = None,
        user: str = None,
        volume: str = None,
    ):
        super().__init__(
            group=group,
            read_only=read_only,
            registry=registry,
            tenant=tenant,
            user=user,
            volume=volume,
        )


class RBDVolumeSource(KubernetesObject):
    __slots__ = ()

    fs_type: str
    image: str
    keyring: str
    monitors: List[str]
    pool: str
    read_only: bool
    secret_ref: LocalObjectReference
    user: str

    _required_ = ["image", "monitors"]

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

    _required_ = ["gateway", "secret_ref", "system"]

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

    default_mode: int
    items: List[KeyToPath]
    optional: bool
    secret_name: str

    def __init__(
        self,
        default_mode: int = None,
        items: List[KeyToPath] = None,
        optional: bool = None,
        secret_name: str = None,
    ):
        super().__init__(
            default_mode=default_mode,
            items=items,
            optional=optional,
            secret_name=secret_name,
        )


class StorageOSVolumeSource(KubernetesObject):
    __slots__ = ()

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
            fs_type=fs_type,
            read_only=read_only,
            secret_ref=secret_ref,
            volume_name=volume_name,
            volume_namespace=volume_namespace,
        )


class VsphereVirtualDiskVolumeSource(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["volume_path"]

    def __init__(
        self,
        fs_type: str = None,
        storage_policy_id: str = None,
        storage_policy_name: str = None,
        volume_path: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            storage_policy_id=storage_policy_id,
            storage_policy_name=storage_policy_name,
            volume_path=volume_path,
        )


class Volume(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["name"]

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

    _required_ = ["containers"]

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

    metadata: ObjectMeta
    spec: PodSpec

    def __init__(self, metadata: ObjectMeta = None, spec: PodSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class DeploymentSpec(KubernetesObject):
    __slots__ = ()

    min_ready_seconds: int
    paused: bool
    progress_deadline_seconds: int
    replicas: int
    revision_history_limit: int
    selector: LabelSelector
    strategy: DeploymentStrategy
    template: PodTemplateSpec

    _required_ = ["selector", "template"]

    def __init__(
        self,
        min_ready_seconds: int = None,
        paused: bool = None,
        progress_deadline_seconds: int = None,
        replicas: int = None,
        revision_history_limit: int = None,
        selector: LabelSelector = None,
        strategy: DeploymentStrategy = None,
        template: PodTemplateSpec = None,
    ):
        super().__init__(
            min_ready_seconds=min_ready_seconds,
            paused=paused,
            progress_deadline_seconds=progress_deadline_seconds,
            replicas=replicas,
            revision_history_limit=revision_history_limit,
            selector=selector,
            strategy=strategy,
            template=template,
        )


class Deployment(KubernetesApiResource):
    __slots__ = ()

    _group_ = "apps"

    metadata: ObjectMeta
    spec: DeploymentSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: DeploymentSpec = None,
    ):
        super().__init__(
            "apps/v1", "Deployment", name, namespace, metadata=metadata, spec=spec
        )


class RollingUpdateStatefulSetStrategy(KubernetesObject):
    __slots__ = ()

    partition: int

    def __init__(self, partition: int = None):
        super().__init__(partition=partition)


class StatefulSetUpdateStrategy(KubernetesObject):
    __slots__ = ()

    rolling_update: RollingUpdateStatefulSetStrategy
    type: str

    def __init__(
        self, rolling_update: RollingUpdateStatefulSetStrategy = None, type: str = None
    ):
        super().__init__(rolling_update=rolling_update, type=type)


class PersistentVolumeClaim(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    metadata: ObjectMeta
    spec: PersistentVolumeClaimSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: PersistentVolumeClaimSpec = None,
    ):
        super().__init__(
            "v1", "PersistentVolumeClaim", name, namespace, metadata=metadata, spec=spec
        )


class StatefulSetSpec(KubernetesObject):
    __slots__ = ()

    pod_management_policy: str
    replicas: int
    revision_history_limit: int
    selector: LabelSelector
    service_name: str
    template: PodTemplateSpec
    update_strategy: StatefulSetUpdateStrategy
    volume_claim_templates: List[PersistentVolumeClaim]

    _required_ = ["selector", "service_name", "template"]

    def __init__(
        self,
        pod_management_policy: str = None,
        replicas: int = None,
        revision_history_limit: int = None,
        selector: LabelSelector = None,
        service_name: str = None,
        template: PodTemplateSpec = None,
        update_strategy: StatefulSetUpdateStrategy = None,
        volume_claim_templates: List[PersistentVolumeClaim] = None,
    ):
        super().__init__(
            pod_management_policy=pod_management_policy,
            replicas=replicas,
            revision_history_limit=revision_history_limit,
            selector=selector,
            service_name=service_name,
            template=template,
            update_strategy=update_strategy,
            volume_claim_templates=volume_claim_templates,
        )


class StatefulSet(KubernetesApiResource):
    __slots__ = ()

    _group_ = "apps"

    metadata: ObjectMeta
    spec: StatefulSetSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: StatefulSetSpec = None,
    ):
        super().__init__(
            "apps/v1", "StatefulSet", name, namespace, metadata=metadata, spec=spec
        )


class RollingUpdateDaemonSet(KubernetesObject):
    __slots__ = ()

    max_unavailable: IntOrString

    def __init__(self, max_unavailable: IntOrString = None):
        super().__init__(max_unavailable=max_unavailable)


class DaemonSetUpdateStrategy(KubernetesObject):
    __slots__ = ()

    rolling_update: RollingUpdateDaemonSet
    type: str

    def __init__(self, rolling_update: RollingUpdateDaemonSet = None, type: str = None):
        super().__init__(rolling_update=rolling_update, type=type)


class DaemonSetSpec(KubernetesObject):
    __slots__ = ()

    min_ready_seconds: int
    revision_history_limit: int
    selector: LabelSelector
    template: PodTemplateSpec
    update_strategy: DaemonSetUpdateStrategy

    _required_ = ["selector", "template"]

    def __init__(
        self,
        min_ready_seconds: int = None,
        revision_history_limit: int = None,
        selector: LabelSelector = None,
        template: PodTemplateSpec = None,
        update_strategy: DaemonSetUpdateStrategy = None,
    ):
        super().__init__(
            min_ready_seconds=min_ready_seconds,
            revision_history_limit=revision_history_limit,
            selector=selector,
            template=template,
            update_strategy=update_strategy,
        )


class DaemonSet(KubernetesApiResource):
    __slots__ = ()

    _group_ = "apps"

    metadata: ObjectMeta
    spec: DaemonSetSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: DaemonSetSpec = None,
    ):
        super().__init__(
            "apps/v1", "DaemonSet", name, namespace, metadata=metadata, spec=spec
        )


class JobSpec(KubernetesObject):
    __slots__ = ()

    active_deadline_seconds: int
    backoff_limit: int
    completions: int
    manual_selector: bool
    parallelism: int
    selector: LabelSelector
    template: PodTemplateSpec
    ttl_seconds_after_finished: int

    _required_ = ["template"]

    def __init__(
        self,
        active_deadline_seconds: int = None,
        backoff_limit: int = None,
        completions: int = None,
        manual_selector: bool = None,
        parallelism: int = None,
        selector: LabelSelector = None,
        template: PodTemplateSpec = None,
        ttl_seconds_after_finished: int = None,
    ):
        super().__init__(
            active_deadline_seconds=active_deadline_seconds,
            backoff_limit=backoff_limit,
            completions=completions,
            manual_selector=manual_selector,
            parallelism=parallelism,
            selector=selector,
            template=template,
            ttl_seconds_after_finished=ttl_seconds_after_finished,
        )


class Job(KubernetesApiResource):
    __slots__ = ()

    _group_ = "batch"

    metadata: ObjectMeta
    spec: JobSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: JobSpec = None,
    ):
        super().__init__(
            "batch/v1", "Job", name, namespace, metadata=metadata, spec=spec
        )


class JobTemplateSpec(KubernetesObject):
    __slots__ = ()

    metadata: ObjectMeta
    spec: JobSpec

    def __init__(self, metadata: ObjectMeta = None, spec: JobSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class CronJobSpec(KubernetesObject):
    __slots__ = ()

    concurrency_policy: str
    failed_jobs_history_limit: int
    job_template: JobTemplateSpec
    schedule: str
    starting_deadline_seconds: int
    successful_jobs_history_limit: int
    suspend: bool

    _required_ = ["job_template", "schedule"]

    def __init__(
        self,
        concurrency_policy: str = None,
        failed_jobs_history_limit: int = None,
        job_template: JobTemplateSpec = None,
        schedule: str = None,
        starting_deadline_seconds: int = None,
        successful_jobs_history_limit: int = None,
        suspend: bool = None,
    ):
        super().__init__(
            concurrency_policy=concurrency_policy,
            failed_jobs_history_limit=failed_jobs_history_limit,
            job_template=job_template,
            schedule=schedule,
            starting_deadline_seconds=starting_deadline_seconds,
            successful_jobs_history_limit=successful_jobs_history_limit,
            suspend=suspend,
        )


class CronJob(KubernetesApiResource):
    __slots__ = ()

    _group_ = "batch"

    metadata: ObjectMeta
    spec: CronJobSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: CronJobSpec = None,
    ):
        super().__init__(
            "batch/v1beta1", "CronJob", name, namespace, metadata=metadata, spec=spec
        )


class NetworkPolicyPort(KubernetesObject):
    __slots__ = ()

    port: IntOrString
    protocol: str

    def __init__(self, port: IntOrString = None, protocol: str = None):
        super().__init__(port=port, protocol=protocol)


class IPBlock(KubernetesObject):
    __slots__ = ()
    _revfield_names_ = {
        "except": "except_",
    }

    cidr: str
    except_: List[str]

    _required_ = ["cidr"]

    def __init__(self, cidr: str = None, except_: List[str] = None):
        super().__init__(cidr=cidr, except_=except_)


class NetworkPolicyPeer(KubernetesObject):
    __slots__ = ()

    ip_block: IPBlock
    namespace_selector: LabelSelector
    pod_selector: LabelSelector

    def __init__(
        self,
        ip_block: IPBlock = None,
        namespace_selector: LabelSelector = None,
        pod_selector: LabelSelector = None,
    ):
        super().__init__(
            ip_block=ip_block,
            namespace_selector=namespace_selector,
            pod_selector=pod_selector,
        )


class NetworkPolicyEgressRule(KubernetesObject):
    __slots__ = ()

    ports: List[NetworkPolicyPort]
    to: List[NetworkPolicyPeer]

    def __init__(
        self, ports: List[NetworkPolicyPort] = None, to: List[NetworkPolicyPeer] = None
    ):
        super().__init__(ports=ports, to=to)


class NetworkPolicyIngressRule(KubernetesObject):
    __slots__ = ()
    _revfield_names_ = {
        "from": "from_",
    }

    from_: List[NetworkPolicyPeer]
    ports: List[NetworkPolicyPort]

    def __init__(
        self,
        from_: List[NetworkPolicyPeer] = None,
        ports: List[NetworkPolicyPort] = None,
    ):
        super().__init__(from_=from_, ports=ports)


class NetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    egress: List[NetworkPolicyEgressRule]
    ingress: List[NetworkPolicyIngressRule]
    pod_selector: LabelSelector
    policy_types: List[str]

    _required_ = ["pod_selector"]

    def __init__(
        self,
        egress: List[NetworkPolicyEgressRule] = None,
        ingress: List[NetworkPolicyIngressRule] = None,
        pod_selector: LabelSelector = None,
        policy_types: List[str] = None,
    ):
        super().__init__(
            egress=egress,
            ingress=ingress,
            pod_selector=pod_selector,
            policy_types=policy_types,
        )


class NetworkPolicy(KubernetesApiResource):
    __slots__ = ()

    _group_ = "networking.k8s.io"

    metadata: ObjectMeta
    spec: NetworkPolicySpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: NetworkPolicySpec = None,
    ):
        super().__init__(
            "networking.k8s.io/v1",
            "NetworkPolicy",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class ScopedResourceSelectorRequirement(KubernetesObject):
    __slots__ = ()

    operator: str
    scope_name: str
    values: List[str]

    _required_ = ["operator", "scope_name"]

    def __init__(
        self, operator: str = None, scope_name: str = None, values: List[str] = None
    ):
        super().__init__(operator=operator, scope_name=scope_name, values=values)


class ScopeSelector(KubernetesObject):
    __slots__ = ()

    match_expressions: List[ScopedResourceSelectorRequirement]

    def __init__(
        self, match_expressions: List[ScopedResourceSelectorRequirement] = None
    ):
        super().__init__(match_expressions=match_expressions)


class ResourceQuotaSpec(KubernetesObject):
    __slots__ = ()

    hard: Dict[str, Quantity]
    scope_selector: ScopeSelector
    scopes: List[str]

    def __init__(
        self,
        hard: Dict[str, Quantity] = None,
        scope_selector: ScopeSelector = None,
        scopes: List[str] = None,
    ):
        super().__init__(hard=hard, scope_selector=scope_selector, scopes=scopes)


class ResourceQuota(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    metadata: ObjectMeta
    spec: ResourceQuotaSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: ResourceQuotaSpec = None,
    ):
        super().__init__(
            "v1", "ResourceQuota", name, namespace, metadata=metadata, spec=spec
        )


class AzureFilePersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    read_only: bool
    secret_name: str
    secret_namespace: str
    share_name: str

    _required_ = ["secret_name", "share_name"]

    def __init__(
        self,
        read_only: bool = None,
        secret_name: str = None,
        secret_namespace: str = None,
        share_name: str = None,
    ):
        super().__init__(
            read_only=read_only,
            secret_name=secret_name,
            secret_namespace=secret_namespace,
            share_name=share_name,
        )


class SecretReference(KubernetesObject):
    __slots__ = ()

    name: str
    namespace: str

    def __init__(self, name: str = None, namespace: str = None):
        super().__init__(name=name, namespace=namespace)


class CephFSPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    monitors: List[str]
    path: str
    read_only: bool
    secret_file: str
    secret_ref: SecretReference
    user: str

    _required_ = ["monitors"]

    def __init__(
        self,
        monitors: List[str] = None,
        path: str = None,
        read_only: bool = None,
        secret_file: str = None,
        secret_ref: SecretReference = None,
        user: str = None,
    ):
        super().__init__(
            monitors=monitors,
            path=path,
            read_only=read_only,
            secret_file=secret_file,
            secret_ref=secret_ref,
            user=user,
        )


class CinderPersistentVolumeSource(KubernetesObject):
    __slots__ = ()
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

    _required_ = ["volume_id"]

    def __init__(
        self,
        fs_type: str = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
        volume_id: str = None,
    ):
        super().__init__(
            fs_type=fs_type,
            read_only=read_only,
            secret_ref=secret_ref,
            volume_id=volume_id,
        )


class ObjectReference(KubernetesObject):
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


class CSIPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    controller_expand_secret_ref: SecretReference
    controller_publish_secret_ref: SecretReference
    driver: str
    fs_type: str
    node_publish_secret_ref: SecretReference
    node_stage_secret_ref: SecretReference
    read_only: bool
    volume_attributes: Dict[str, str]
    volume_handle: str

    _required_ = ["driver", "volume_handle"]

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


class FlexPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    driver: str
    fs_type: str
    options: Dict[str, str]
    read_only: bool
    secret_ref: SecretReference

    _required_ = ["driver"]

    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: Dict[str, str] = None,
        read_only: bool = None,
        secret_ref: SecretReference = None,
    ):
        super().__init__(
            driver=driver,
            fs_type=fs_type,
            options=options,
            read_only=read_only,
            secret_ref=secret_ref,
        )


class GlusterfsPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    endpoints: str
    endpoints_namespace: str
    path: str
    read_only: bool

    _required_ = ["endpoints", "path"]

    def __init__(
        self,
        endpoints: str = None,
        endpoints_namespace: str = None,
        path: str = None,
        read_only: bool = None,
    ):
        super().__init__(
            endpoints=endpoints,
            endpoints_namespace=endpoints_namespace,
            path=path,
            read_only=read_only,
        )


class ISCSIPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

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

    _required_ = ["iqn", "lun", "target_portal"]

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


class LocalVolumeSource(KubernetesObject):
    __slots__ = ()

    fs_type: str
    path: str

    _required_ = ["path"]

    def __init__(self, fs_type: str = None, path: str = None):
        super().__init__(fs_type=fs_type, path=path)


class VolumeNodeAffinity(KubernetesObject):
    __slots__ = ()

    required: NodeSelector

    def __init__(self, required: NodeSelector = None):
        super().__init__(required=required)


class RBDPersistentVolumeSource(KubernetesObject):
    __slots__ = ()

    fs_type: str
    image: str
    keyring: str
    monitors: List[str]
    pool: str
    read_only: bool
    secret_ref: SecretReference
    user: str

    _required_ = ["image", "monitors"]

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

    _required_ = ["gateway", "secret_ref", "system"]

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
            fs_type=fs_type,
            read_only=read_only,
            secret_ref=secret_ref,
            volume_name=volume_name,
            volume_namespace=volume_namespace,
        )


class PersistentVolumeSpec(KubernetesObject):
    __slots__ = ()
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

    _group_ = ""

    metadata: ObjectMeta
    spec: PersistentVolumeSpec

    def __init__(
        self, name: str, metadata: ObjectMeta = None, spec: PersistentVolumeSpec = None
    ):
        super().__init__(
            "v1", "PersistentVolume", name, "", metadata=metadata, spec=spec
        )


class AllowedCSIDriver(KubernetesObject):
    __slots__ = ()

    name: str

    _required_ = ["name"]

    def __init__(self, name: str = None):
        super().__init__(name=name)


class AllowedFlexVolume(KubernetesObject):
    __slots__ = ()

    driver: str

    _required_ = ["driver"]

    def __init__(self, driver: str = None):
        super().__init__(driver=driver)


class AllowedHostPath(KubernetesObject):
    __slots__ = ()

    path_prefix: str
    read_only: bool

    def __init__(self, path_prefix: str = None, read_only: bool = None):
        super().__init__(path_prefix=path_prefix, read_only=read_only)


class IDRange(KubernetesObject):
    __slots__ = ()

    max: int
    min: int

    _required_ = ["max", "min"]

    def __init__(self, max: int = None, min: int = None):
        super().__init__(max=max, min=min)


class FSGroupStrategyOptions(KubernetesObject):
    __slots__ = ()

    ranges: List[IDRange]
    rule: str

    def __init__(self, ranges: List[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class HostPortRange(KubernetesObject):
    __slots__ = ()

    max: int
    min: int

    _required_ = ["max", "min"]

    def __init__(self, max: int = None, min: int = None):
        super().__init__(max=max, min=min)


class RunAsGroupStrategyOptions(KubernetesObject):
    __slots__ = ()

    ranges: List[IDRange]
    rule: str

    _required_ = ["rule"]

    def __init__(self, ranges: List[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class RunAsUserStrategyOptions(KubernetesObject):
    __slots__ = ()

    ranges: List[IDRange]
    rule: str

    _required_ = ["rule"]

    def __init__(self, ranges: List[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class RuntimeClassStrategyOptions(KubernetesObject):
    __slots__ = ()

    allowed_runtime_class_names: List[str]
    default_runtime_class_name: str

    _required_ = ["allowed_runtime_class_names"]

    def __init__(
        self,
        allowed_runtime_class_names: List[str] = None,
        default_runtime_class_name: str = None,
    ):
        super().__init__(
            allowed_runtime_class_names=allowed_runtime_class_names,
            default_runtime_class_name=default_runtime_class_name,
        )


class SELinuxStrategyOptions(KubernetesObject):
    __slots__ = ()

    rule: str
    se_linux_options: SELinuxOptions

    _required_ = ["rule"]

    def __init__(self, rule: str = None, se_linux_options: SELinuxOptions = None):
        super().__init__(rule=rule, se_linux_options=se_linux_options)


class SupplementalGroupsStrategyOptions(KubernetesObject):
    __slots__ = ()

    ranges: List[IDRange]
    rule: str

    def __init__(self, ranges: List[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class PodSecurityPolicySpec(KubernetesObject):
    __slots__ = ()
    _field_names_ = {
        "allowed_csi_drivers": "allowedCSIDrivers",
        "host_ipc": "hostIPC",
        "host_pid": "hostPID",
    }
    _revfield_names_ = {
        "allowedCSIDrivers": "allowed_csi_drivers",
        "hostIPC": "host_ipc",
        "hostPID": "host_pid",
    }

    allow_privilege_escalation: bool
    allowed_csi_drivers: List[AllowedCSIDriver]
    allowed_capabilities: List[str]
    allowed_flex_volumes: List[AllowedFlexVolume]
    allowed_host_paths: List[AllowedHostPath]
    allowed_proc_mount_types: List[str]
    allowed_unsafe_sysctls: List[str]
    default_add_capabilities: List[str]
    default_allow_privilege_escalation: bool
    forbidden_sysctls: List[str]
    fs_group: FSGroupStrategyOptions
    host_ipc: bool
    host_network: bool
    host_pid: bool
    host_ports: List[HostPortRange]
    privileged: bool
    read_only_root_filesystem: bool
    required_drop_capabilities: List[str]
    run_as_group: RunAsGroupStrategyOptions
    run_as_user: RunAsUserStrategyOptions
    runtime_class: RuntimeClassStrategyOptions
    se_linux: SELinuxStrategyOptions
    supplemental_groups: SupplementalGroupsStrategyOptions
    volumes: List[str]

    _required_ = ["fs_group", "run_as_user", "se_linux", "supplemental_groups"]

    def __init__(
        self,
        allow_privilege_escalation: bool = None,
        allowed_csi_drivers: List[AllowedCSIDriver] = None,
        allowed_capabilities: List[str] = None,
        allowed_flex_volumes: List[AllowedFlexVolume] = None,
        allowed_host_paths: List[AllowedHostPath] = None,
        allowed_proc_mount_types: List[str] = None,
        allowed_unsafe_sysctls: List[str] = None,
        default_add_capabilities: List[str] = None,
        default_allow_privilege_escalation: bool = None,
        forbidden_sysctls: List[str] = None,
        fs_group: FSGroupStrategyOptions = None,
        host_ipc: bool = None,
        host_network: bool = None,
        host_pid: bool = None,
        host_ports: List[HostPortRange] = None,
        privileged: bool = None,
        read_only_root_filesystem: bool = None,
        required_drop_capabilities: List[str] = None,
        run_as_group: RunAsGroupStrategyOptions = None,
        run_as_user: RunAsUserStrategyOptions = None,
        runtime_class: RuntimeClassStrategyOptions = None,
        se_linux: SELinuxStrategyOptions = None,
        supplemental_groups: SupplementalGroupsStrategyOptions = None,
        volumes: List[str] = None,
    ):
        super().__init__(
            allow_privilege_escalation=allow_privilege_escalation,
            allowed_csi_drivers=allowed_csi_drivers,
            allowed_capabilities=allowed_capabilities,
            allowed_flex_volumes=allowed_flex_volumes,
            allowed_host_paths=allowed_host_paths,
            allowed_proc_mount_types=allowed_proc_mount_types,
            allowed_unsafe_sysctls=allowed_unsafe_sysctls,
            default_add_capabilities=default_add_capabilities,
            default_allow_privilege_escalation=default_allow_privilege_escalation,
            forbidden_sysctls=forbidden_sysctls,
            fs_group=fs_group,
            host_ipc=host_ipc,
            host_network=host_network,
            host_pid=host_pid,
            host_ports=host_ports,
            privileged=privileged,
            read_only_root_filesystem=read_only_root_filesystem,
            required_drop_capabilities=required_drop_capabilities,
            run_as_group=run_as_group,
            run_as_user=run_as_user,
            runtime_class=runtime_class,
            se_linux=se_linux,
            supplemental_groups=supplemental_groups,
            volumes=volumes,
        )


class PodSecurityPolicy(KubernetesApiResource):
    __slots__ = ()

    _group_ = "policy"

    metadata: ObjectMeta
    spec: PodSecurityPolicySpec

    def __init__(
        self, name: str, metadata: ObjectMeta = None, spec: PodSecurityPolicySpec = None
    ):
        super().__init__(
            "policy/v1beta1",
            "PodSecurityPolicy",
            name,
            "",
            metadata=metadata,
            spec=spec,
        )


class PodDisruptionBudgetSpec(KubernetesObject):
    __slots__ = ()

    max_unavailable: IntOrString
    min_available: IntOrString
    selector: LabelSelector

    def __init__(
        self,
        max_unavailable: IntOrString = None,
        min_available: IntOrString = None,
        selector: LabelSelector = None,
    ):
        super().__init__(
            max_unavailable=max_unavailable,
            min_available=min_available,
            selector=selector,
        )


class PodDisruptionBudget(KubernetesApiResource):
    __slots__ = ()

    _group_ = "policy"

    metadata: ObjectMeta
    spec: PodDisruptionBudgetSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: PodDisruptionBudgetSpec = None,
    ):
        super().__init__(
            "policy/v1beta1",
            "PodDisruptionBudget",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class CrossVersionObjectReference(KubernetesObject):
    __slots__ = ()

    api_version: str
    kind: str
    name: str

    _required_ = ["kind", "name"]

    def __init__(self, api_version: str = None, kind: str = None, name: str = None):
        super().__init__(api_version=api_version, kind=kind, name=name)


class HorizontalPodAutoscalerSpec(KubernetesObject):
    __slots__ = ()
    _field_names_ = {
        "target_cpu_utilization_percentage": "targetCPUUtilizationPercentage",
    }
    _revfield_names_ = {
        "targetCPUUtilizationPercentage": "target_cpu_utilization_percentage",
    }

    max_replicas: int
    min_replicas: int
    scale_target_ref: CrossVersionObjectReference
    target_cpu_utilization_percentage: int

    _required_ = ["max_replicas", "scale_target_ref"]

    def __init__(
        self,
        max_replicas: int = None,
        min_replicas: int = None,
        scale_target_ref: CrossVersionObjectReference = None,
        target_cpu_utilization_percentage: int = None,
    ):
        super().__init__(
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            scale_target_ref=scale_target_ref,
            target_cpu_utilization_percentage=target_cpu_utilization_percentage,
        )


class HorizontalPodAutoscaler(KubernetesApiResource):
    __slots__ = ()

    _group_ = "autoscaling"

    metadata: ObjectMeta
    spec: HorizontalPodAutoscalerSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: HorizontalPodAutoscalerSpec = None,
    ):
        super().__init__(
            "autoscaling/v1",
            "HorizontalPodAutoscaler",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class ServiceReference(KubernetesObject):
    __slots__ = ()

    name: str
    namespace: str
    path: str
    port: int

    _required_ = ["name", "namespace"]

    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        path: str = None,
        port: int = None,
    ):
        super().__init__(name=name, namespace=namespace, path=path, port=port)


class WebhookClientConfig(KubernetesObject):
    __slots__ = ()

    ca_bundle: Base64
    service: ServiceReference
    url: str

    def __init__(
        self,
        ca_bundle: Base64 = None,
        service: ServiceReference = None,
        url: str = None,
    ):
        super().__init__(ca_bundle=ca_bundle, service=service, url=url)


class RuleWithOperations(KubernetesObject):
    __slots__ = ()

    api_groups: List[str]
    api_versions: List[str]
    operations: List[str]
    resources: List[str]
    scope: str

    def __init__(
        self,
        api_groups: List[str] = None,
        api_versions: List[str] = None,
        operations: List[str] = None,
        resources: List[str] = None,
        scope: str = None,
    ):
        super().__init__(
            api_groups=api_groups,
            api_versions=api_versions,
            operations=operations,
            resources=resources,
            scope=scope,
        )


class MutatingWebhook(KubernetesObject):
    __slots__ = ()

    admission_review_versions: List[str]
    client_config: WebhookClientConfig
    failure_policy: str
    match_policy: str
    name: str
    namespace_selector: LabelSelector
    object_selector: LabelSelector
    reinvocation_policy: str
    rules: List[RuleWithOperations]
    side_effects: str
    timeout_seconds: int

    _required_ = ["admission_review_versions", "client_config", "name", "side_effects"]

    def __init__(
        self,
        admission_review_versions: List[str] = None,
        client_config: WebhookClientConfig = None,
        failure_policy: str = None,
        match_policy: str = None,
        name: str = None,
        namespace_selector: LabelSelector = None,
        object_selector: LabelSelector = None,
        reinvocation_policy: str = None,
        rules: List[RuleWithOperations] = None,
        side_effects: str = None,
        timeout_seconds: int = None,
    ):
        super().__init__(
            admission_review_versions=admission_review_versions,
            client_config=client_config,
            failure_policy=failure_policy,
            match_policy=match_policy,
            name=name,
            namespace_selector=namespace_selector,
            object_selector=object_selector,
            reinvocation_policy=reinvocation_policy,
            rules=rules,
            side_effects=side_effects,
            timeout_seconds=timeout_seconds,
        )


class MutatingWebhookConfiguration(KubernetesApiResource):
    __slots__ = ()

    _group_ = "admissionregistration.k8s.io"

    metadata: ObjectMeta
    webhooks: List[MutatingWebhook]

    def __init__(
        self,
        name: str,
        metadata: ObjectMeta = None,
        webhooks: List[MutatingWebhook] = None,
    ):
        super().__init__(
            "admissionregistration.k8s.io/v1",
            "MutatingWebhookConfiguration",
            name,
            "",
            metadata=metadata,
            webhooks=webhooks,
        )


class ServicePort(KubernetesObject):
    __slots__ = ()

    app_protocol: str
    name: str
    node_port: int
    port: int
    protocol: str
    target_port: IntOrString

    _required_ = ["port"]

    def __init__(
        self,
        app_protocol: str = None,
        name: str = None,
        node_port: int = None,
        port: int = None,
        protocol: str = None,
        target_port: IntOrString = None,
    ):
        super().__init__(
            app_protocol=app_protocol,
            name=name,
            node_port=node_port,
            port=port,
            protocol=protocol,
            target_port=target_port,
        )


class ClientIPConfig(KubernetesObject):
    __slots__ = ()

    timeout_seconds: int

    def __init__(self, timeout_seconds: int = None):
        super().__init__(timeout_seconds=timeout_seconds)


class SessionAffinityConfig(KubernetesObject):
    __slots__ = ()
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
    _field_names_ = {
        "cluster_ip": "clusterIP",
        "load_balancer_ip": "loadBalancerIP",
    }
    _revfield_names_ = {
        "clusterIP": "cluster_ip",
        "loadBalancerIP": "load_balancer_ip",
    }

    allocate_load_balancer_node_ports: bool
    cluster_ip: str
    cluster_i_ps: List[str]
    external_i_ps: List[str]
    external_name: str
    external_traffic_policy: str
    health_check_node_port: int
    ip_families: List[str]
    ip_family_policy: str
    load_balancer_ip: str
    load_balancer_source_ranges: List[str]
    ports: List[ServicePort]
    publish_not_ready_addresses: bool
    selector: Dict[str, str]
    session_affinity: str
    session_affinity_config: SessionAffinityConfig
    topology_keys: List[str]
    type: str

    def __init__(
        self,
        allocate_load_balancer_node_ports: bool = None,
        cluster_ip: str = None,
        cluster_i_ps: List[str] = None,
        external_i_ps: List[str] = None,
        external_name: str = None,
        external_traffic_policy: str = None,
        health_check_node_port: int = None,
        ip_families: List[str] = None,
        ip_family_policy: str = None,
        load_balancer_ip: str = None,
        load_balancer_source_ranges: List[str] = None,
        ports: List[ServicePort] = None,
        publish_not_ready_addresses: bool = None,
        selector: Dict[str, str] = None,
        session_affinity: str = None,
        session_affinity_config: SessionAffinityConfig = None,
        topology_keys: List[str] = None,
        type: str = None,
    ):
        super().__init__(
            allocate_load_balancer_node_ports=allocate_load_balancer_node_ports,
            cluster_ip=cluster_ip,
            cluster_i_ps=cluster_i_ps,
            external_i_ps=external_i_ps,
            external_name=external_name,
            external_traffic_policy=external_traffic_policy,
            health_check_node_port=health_check_node_port,
            ip_families=ip_families,
            ip_family_policy=ip_family_policy,
            load_balancer_ip=load_balancer_ip,
            load_balancer_source_ranges=load_balancer_source_ranges,
            ports=ports,
            publish_not_ready_addresses=publish_not_ready_addresses,
            selector=selector,
            session_affinity=session_affinity,
            session_affinity_config=session_affinity_config,
            topology_keys=topology_keys,
            type=type,
        )


class Service(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    metadata: ObjectMeta
    spec: ServiceSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: ServiceSpec = None,
    ):
        super().__init__("v1", "Service", name, namespace, metadata=metadata, spec=spec)


class ServiceAccount(KubernetesApiResource):
    __slots__ = ()

    _group_ = ""

    automount_service_account_token: bool
    image_pull_secrets: List[LocalObjectReference]
    metadata: ObjectMeta
    secrets: List[ObjectReference]

    def __init__(
        self,
        name: str,
        namespace: str = None,
        automount_service_account_token: bool = None,
        image_pull_secrets: List[LocalObjectReference] = None,
        metadata: ObjectMeta = None,
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


class ServiceBackendPort(KubernetesObject):
    __slots__ = ()

    name: str
    number: int

    def __init__(self, name: str = None, number: int = None):
        super().__init__(name=name, number=number)


class IngressServiceBackend(KubernetesObject):
    __slots__ = ()

    name: str
    port: ServiceBackendPort

    _required_ = ["name"]

    def __init__(self, name: str = None, port: ServiceBackendPort = None):
        super().__init__(name=name, port=port)


class IngressBackend(KubernetesObject):
    __slots__ = ()

    resource: TypedLocalObjectReference
    service: IngressServiceBackend

    def __init__(
        self,
        resource: TypedLocalObjectReference = None,
        service: IngressServiceBackend = None,
    ):
        super().__init__(resource=resource, service=service)


class HTTPIngressPath(KubernetesObject):
    __slots__ = ()

    backend: IngressBackend
    path: str
    path_type: str

    _required_ = ["backend"]

    def __init__(
        self, backend: IngressBackend = None, path: str = None, path_type: str = None
    ):
        super().__init__(backend=backend, path=path, path_type=path_type)


class HTTPIngressRuleValue(KubernetesObject):
    __slots__ = ()

    paths: List[HTTPIngressPath]

    _required_ = ["paths"]

    def __init__(self, paths: List[HTTPIngressPath] = None):
        super().__init__(paths=paths)


class IngressRule(KubernetesObject):
    __slots__ = ()

    host: str
    http: HTTPIngressRuleValue

    def __init__(self, host: str = None, http: HTTPIngressRuleValue = None):
        super().__init__(host=host, http=http)


class IngressTLS(KubernetesObject):
    __slots__ = ()

    hosts: List[str]
    secret_name: str

    def __init__(self, hosts: List[str] = None, secret_name: str = None):
        super().__init__(hosts=hosts, secret_name=secret_name)


class IngressSpec(KubernetesObject):
    __slots__ = ()

    default_backend: IngressBackend
    ingress_class_name: str
    rules: List[IngressRule]
    tls: List[IngressTLS]

    def __init__(
        self,
        default_backend: IngressBackend = None,
        ingress_class_name: str = None,
        rules: List[IngressRule] = None,
        tls: List[IngressTLS] = None,
    ):
        super().__init__(
            default_backend=default_backend,
            ingress_class_name=ingress_class_name,
            rules=rules,
            tls=tls,
        )


class Ingress(KubernetesApiResource):
    __slots__ = ()

    _group_ = "networking.k8s.io"

    metadata: ObjectMeta
    spec: IngressSpec

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: ObjectMeta = None,
        spec: IngressSpec = None,
    ):
        super().__init__(
            "networking.k8s.io/v1",
            "Ingress",
            name,
            namespace,
            metadata=metadata,
            spec=spec,
        )


class IngressClassSpec(KubernetesObject):
    __slots__ = ()

    controller: str
    parameters: TypedLocalObjectReference

    def __init__(
        self, controller: str = None, parameters: TypedLocalObjectReference = None
    ):
        super().__init__(controller=controller, parameters=parameters)


class IngressClass(KubernetesApiResource):
    __slots__ = ()

    _group_ = "networking.k8s.io"

    metadata: ObjectMeta
    spec: IngressClassSpec

    def __init__(
        self, name: str, metadata: ObjectMeta = None, spec: IngressClassSpec = None
    ):
        super().__init__(
            "networking.k8s.io/v1",
            "IngressClass",
            name,
            "",
            metadata=metadata,
            spec=spec,
        )
