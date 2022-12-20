from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class AllowedCSIDriver(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["name"]

    name: str

    def __init__(self, name: str = None):
        super().__init__(name=name)


class AllowedFlexVolume(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["driver"]

    driver: str

    def __init__(self, driver: str = None):
        super().__init__(driver=driver)


class AllowedHostPath(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    path_prefix: str
    read_only: bool

    def __init__(self, path_prefix: str = None, read_only: bool = None):
        super().__init__(path_prefix=path_prefix, read_only=read_only)


class IDRange(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["max", "min"]

    max: int
    min: int

    def __init__(self, max: int = None, min: int = None):
        super().__init__(max=max, min=min)


class FSGroupStrategyOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    ranges: list[IDRange]
    rule: str

    def __init__(self, ranges: list[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class HostPortRange(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["max", "min"]

    max: int
    min: int

    def __init__(self, max: int = None, min: int = None):
        super().__init__(max=max, min=min)


class PodDisruptionBudgetSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1"

    max_unavailable: core.IntOrString
    min_available: core.IntOrString
    selector: meta.LabelSelector

    def __init__(
        self, max_unavailable: core.IntOrString = None, min_available: core.IntOrString = None, selector: meta.LabelSelector = None
    ):
        super().__init__(max_unavailable=max_unavailable, min_available=min_available, selector=selector)


class PodDisruptionBudget(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "policy/v1"
    _api_group_ = "policy"
    _kind_ = "PodDisruptionBudget"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: PodDisruptionBudgetSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodDisruptionBudgetSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class RunAsGroupStrategyOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["rule"]

    ranges: list[IDRange]
    rule: str

    def __init__(self, ranges: list[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class RunAsUserStrategyOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["rule"]

    ranges: list[IDRange]
    rule: str

    def __init__(self, ranges: list[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class RuntimeClassStrategyOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["allowed_runtime_class_names"]

    allowed_runtime_class_names: list[str]
    default_runtime_class_name: str

    def __init__(self, allowed_runtime_class_names: list[str] = None, default_runtime_class_name: str = None):
        super().__init__(allowed_runtime_class_names=allowed_runtime_class_names, default_runtime_class_name=default_runtime_class_name)


class SELinuxStrategyOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["rule"]

    rule: str
    se_linux_options: core.SELinuxOptions

    def __init__(self, rule: str = None, se_linux_options: core.SELinuxOptions = None):
        super().__init__(rule=rule, se_linux_options=se_linux_options)


class SupplementalGroupsStrategyOptions(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    ranges: list[IDRange]
    rule: str

    def __init__(self, ranges: list[IDRange] = None, rule: str = None):
        super().__init__(ranges=ranges, rule=rule)


class PodSecurityPolicySpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "policy/v1beta1"

    _required_ = ["fs_group", "run_as_user", "se_linux", "supplemental_groups"]

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
    allowed_csi_drivers: list[AllowedCSIDriver]
    allowed_capabilities: list[str]
    allowed_flex_volumes: list[AllowedFlexVolume]
    allowed_host_paths: list[AllowedHostPath]
    allowed_proc_mount_types: list[str]
    allowed_unsafe_sysctls: list[str]
    default_add_capabilities: list[str]
    default_allow_privilege_escalation: bool
    forbidden_sysctls: list[str]
    fs_group: FSGroupStrategyOptions
    host_ipc: bool
    host_network: bool
    host_pid: bool
    host_ports: list[HostPortRange]
    privileged: bool
    read_only_root_filesystem: bool
    required_drop_capabilities: list[str]
    run_as_group: RunAsGroupStrategyOptions
    run_as_user: RunAsUserStrategyOptions
    runtime_class: RuntimeClassStrategyOptions
    se_linux: SELinuxStrategyOptions
    supplemental_groups: SupplementalGroupsStrategyOptions
    volumes: list[str]

    def __init__(
        self,
        allow_privilege_escalation: bool = None,
        allowed_csi_drivers: list[AllowedCSIDriver] = None,
        allowed_capabilities: list[str] = None,
        allowed_flex_volumes: list[AllowedFlexVolume] = None,
        allowed_host_paths: list[AllowedHostPath] = None,
        allowed_proc_mount_types: list[str] = None,
        allowed_unsafe_sysctls: list[str] = None,
        default_add_capabilities: list[str] = None,
        default_allow_privilege_escalation: bool = None,
        forbidden_sysctls: list[str] = None,
        fs_group: FSGroupStrategyOptions = None,
        host_ipc: bool = None,
        host_network: bool = None,
        host_pid: bool = None,
        host_ports: list[HostPortRange] = None,
        privileged: bool = None,
        read_only_root_filesystem: bool = None,
        required_drop_capabilities: list[str] = None,
        run_as_group: RunAsGroupStrategyOptions = None,
        run_as_user: RunAsUserStrategyOptions = None,
        runtime_class: RuntimeClassStrategyOptions = None,
        se_linux: SELinuxStrategyOptions = None,
        supplemental_groups: SupplementalGroupsStrategyOptions = None,
        volumes: list[str] = None,
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

    _api_version_ = "policy/v1beta1"
    _api_group_ = "policy"
    _kind_ = "PodSecurityPolicy"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    spec: PodSecurityPolicySpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: PodSecurityPolicySpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)
