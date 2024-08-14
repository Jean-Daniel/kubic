from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class OpaqueDeviceConfiguration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["driver", "parameters"]

    driver: str
    parameters: core.RawExtension

    def __init__(self, driver: str = None, parameters: core.RawExtension = None):
        super().__init__(driver=driver, parameters=parameters)


class DeviceAllocationConfiguration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["source"]

    opaque: OpaqueDeviceConfiguration
    requests: list[str]
    source: str

    def __init__(self, opaque: OpaqueDeviceConfiguration = None, requests: list[str] = None, source: str = None):
        super().__init__(opaque=opaque, requests=requests, source=source)


class DeviceRequestAllocationResult(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["device", "driver", "pool", "request"]

    device: str
    driver: str
    pool: str
    request: str

    def __init__(self, device: str = None, driver: str = None, pool: str = None, request: str = None):
        super().__init__(device=device, driver=driver, pool=pool, request=request)


class DeviceAllocationResult(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    config: list[DeviceAllocationConfiguration]
    results: list[DeviceRequestAllocationResult]

    def __init__(self, config: list[DeviceAllocationConfiguration] = None, results: list[DeviceRequestAllocationResult] = None):
        super().__init__(config=config, results=results)


class AllocationResult(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    controller: str
    devices: DeviceAllocationResult
    node_selector: core.NodeSelector

    def __init__(self, controller: str = None, devices: DeviceAllocationResult = None, node_selector: core.NodeSelector = None):
        super().__init__(controller=controller, devices=devices, node_selector=node_selector)


class DeviceAttribute(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    bool: bool
    int: int
    string: str
    version: str

    def __init__(self, bool: bool = None, int: int = None, string: str = None, version: str = None):
        super().__init__(bool=bool, int=int, string=string, version=version)


class BasicDevice(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    attributes: dict[str, DeviceAttribute]
    capacity: dict[str, core.Quantity]

    def __init__(self, attributes: dict[str, DeviceAttribute] = None, capacity: dict[str, core.Quantity] = None):
        super().__init__(attributes=attributes, capacity=capacity)


class CELDeviceSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["expression"]

    expression: str

    def __init__(self, expression: str = None):
        super().__init__(expression=expression)


class Device(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["name"]

    basic: BasicDevice
    name: str

    def __init__(self, basic: BasicDevice = None, name: str = None):
        super().__init__(basic=basic, name=name)


class DeviceClaimConfiguration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    opaque: OpaqueDeviceConfiguration
    requests: list[str]

    def __init__(self, opaque: OpaqueDeviceConfiguration = None, requests: list[str] = None):
        super().__init__(opaque=opaque, requests=requests)


class DeviceConstraint(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    match_attribute: str
    requests: list[str]

    def __init__(self, match_attribute: str = None, requests: list[str] = None):
        super().__init__(match_attribute=match_attribute, requests=requests)


class DeviceSelector(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    cel: CELDeviceSelector

    def __init__(self, cel: CELDeviceSelector = None):
        super().__init__(cel=cel)


class DeviceRequest(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["device_class_name", "name"]

    admin_access: bool
    allocation_mode: str
    count: int
    device_class_name: str
    name: str
    selectors: list[DeviceSelector]

    def __init__(
        self,
        admin_access: bool = None,
        allocation_mode: str = None,
        count: int = None,
        device_class_name: str = None,
        name: str = None,
        selectors: list[DeviceSelector] = None,
    ):
        super().__init__(
            admin_access=admin_access,
            allocation_mode=allocation_mode,
            count=count,
            device_class_name=device_class_name,
            name=name,
            selectors=selectors,
        )


class DeviceClaim(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    config: list[DeviceClaimConfiguration]
    constraints: list[DeviceConstraint]
    requests: list[DeviceRequest]

    def __init__(
        self,
        config: list[DeviceClaimConfiguration] = None,
        constraints: list[DeviceConstraint] = None,
        requests: list[DeviceRequest] = None,
    ):
        super().__init__(config=config, constraints=constraints, requests=requests)


class DeviceClassConfiguration(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    opaque: OpaqueDeviceConfiguration

    def __init__(self, opaque: OpaqueDeviceConfiguration = None):
        super().__init__(opaque=opaque)


class DeviceClassSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    config: list[DeviceClassConfiguration]
    selectors: list[DeviceSelector]
    suitable_nodes: core.NodeSelector

    def __init__(
        self,
        config: list[DeviceClassConfiguration] = None,
        selectors: list[DeviceSelector] = None,
        suitable_nodes: core.NodeSelector = None,
    ):
        super().__init__(config=config, selectors=selectors, suitable_nodes=suitable_nodes)


class DeviceClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"
    _api_group_ = "resource.k8s.io"
    _kind_ = "DeviceClass"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: DeviceClassSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: DeviceClassSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PodSchedulingContextSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    potential_nodes: list[str]
    selected_node: str

    def __init__(self, potential_nodes: list[str] = None, selected_node: str = None):
        super().__init__(potential_nodes=potential_nodes, selected_node=selected_node)


class PodSchedulingContext(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"
    _api_group_ = "resource.k8s.io"
    _kind_ = "PodSchedulingContext"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PodSchedulingContextSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodSchedulingContextSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceClaimSchedulingStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["name"]

    name: str
    unsuitable_nodes: list[str]

    def __init__(self, name: str = None, unsuitable_nodes: list[str] = None):
        super().__init__(name=name, unsuitable_nodes=unsuitable_nodes)


class PodSchedulingContextStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    resource_claims: list[ResourceClaimSchedulingStatus]

    def __init__(self, resource_claims: list[ResourceClaimSchedulingStatus] = None):
        super().__init__(resource_claims=resource_claims)


class ResourceClaimSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    controller: str
    devices: DeviceClaim

    def __init__(self, controller: str = None, devices: DeviceClaim = None):
        super().__init__(controller=controller, devices=devices)


class ResourceClaim(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaim"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ResourceClaimSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceClaimSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceClaimConsumerReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["name", "resource", "uid"]

    api_group: str
    name: str
    resource: str
    uid: str

    def __init__(self, api_group: str = None, name: str = None, resource: str = None, uid: str = None):
        super().__init__(api_group=api_group, name=name, resource=resource, uid=uid)


class ResourceClaimStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    allocation: AllocationResult
    deallocation_requested: bool
    reserved_for: list[ResourceClaimConsumerReference]

    def __init__(
        self,
        allocation: AllocationResult = None,
        deallocation_requested: bool = None,
        reserved_for: list[ResourceClaimConsumerReference] = None,
    ):
        super().__init__(allocation=allocation, deallocation_requested=deallocation_requested, reserved_for=reserved_for)


class ResourceClaimTemplateSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ResourceClaimSpec

    def __init__(self, metadata: meta.ObjectMeta = None, spec: ResourceClaimSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class ResourceClaimTemplate(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaimTemplate"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ResourceClaimTemplateSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceClaimTemplateSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourcePool(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["generation", "name", "resource_slice_count"]

    generation: int
    name: str
    resource_slice_count: int

    def __init__(self, generation: int = None, name: str = None, resource_slice_count: int = None):
        super().__init__(generation=generation, name=name, resource_slice_count=resource_slice_count)


class ResourceSliceSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"

    _required_ = ["driver", "pool"]

    all_nodes: bool
    devices: list[Device]
    driver: str
    node_name: str
    node_selector: core.NodeSelector
    pool: ResourcePool

    def __init__(
        self,
        all_nodes: bool = None,
        devices: list[Device] = None,
        driver: str = None,
        node_name: str = None,
        node_selector: core.NodeSelector = None,
        pool: ResourcePool = None,
    ):
        super().__init__(all_nodes=all_nodes, devices=devices, driver=driver, node_name=node_name, node_selector=node_selector, pool=pool)


class ResourceSlice(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha3"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceSlice"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ResourceSliceSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceSliceSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)
