from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class ResourceHandle(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    data: str
    driver_name: str

    def __init__(self, data: str = None, driver_name: str = None):
        super().__init__(data=data, driver_name=driver_name)


class AllocationResult(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    available_on_nodes: core.NodeSelector
    resource_handles: list[ResourceHandle]
    shareable: bool

    def __init__(self, available_on_nodes: core.NodeSelector = None, resource_handles: list[ResourceHandle] = None, shareable: bool = None):
        super().__init__(available_on_nodes=available_on_nodes, resource_handles=resource_handles, shareable=shareable)


class PodSchedulingContextSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    potential_nodes: list[str]
    selected_node: str

    def __init__(self, potential_nodes: list[str] = None, selected_node: str = None):
        super().__init__(potential_nodes=potential_nodes, selected_node=selected_node)


class PodSchedulingContext(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "PodSchedulingContext"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: PodSchedulingContextSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodSchedulingContextSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class PodSchedulingContextList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "PodSchedulingContextList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[PodSchedulingContext]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[PodSchedulingContext] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ResourceClaimSchedulingStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    name: str
    unsuitable_nodes: list[str]

    def __init__(self, name: str = None, unsuitable_nodes: list[str] = None):
        super().__init__(name=name, unsuitable_nodes=unsuitable_nodes)


class PodSchedulingContextStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    resource_claims: list[ResourceClaimSchedulingStatus]

    def __init__(self, resource_claims: list[ResourceClaimSchedulingStatus] = None):
        super().__init__(resource_claims=resource_claims)


class ResourceClaimParametersReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["kind", "name"]

    api_group: str
    kind: str
    name: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class ResourceClaimSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["resource_class_name"]

    allocation_mode: str
    parameters_ref: ResourceClaimParametersReference
    resource_class_name: str

    def __init__(
        self, allocation_mode: str = None, parameters_ref: ResourceClaimParametersReference = None, resource_class_name: str = None
    ):
        super().__init__(allocation_mode=allocation_mode, parameters_ref=parameters_ref, resource_class_name=resource_class_name)


class ResourceClaim(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
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

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["name", "resource", "uid"]

    api_group: str
    name: str
    resource: str
    uid: str

    def __init__(self, api_group: str = None, name: str = None, resource: str = None, uid: str = None):
        super().__init__(api_group=api_group, name=name, resource=resource, uid=uid)


class ResourceClaimList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaimList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ResourceClaim]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ResourceClaim] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ResourceClaimStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    allocation: AllocationResult
    deallocation_requested: bool
    driver_name: str
    reserved_for: list[ResourceClaimConsumerReference]

    def __init__(
        self,
        allocation: AllocationResult = None,
        deallocation_requested: bool = None,
        driver_name: str = None,
        reserved_for: list[ResourceClaimConsumerReference] = None,
    ):
        super().__init__(
            allocation=allocation, deallocation_requested=deallocation_requested, driver_name=driver_name, reserved_for=reserved_for
        )


class ResourceClaimTemplateSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ResourceClaimSpec

    def __init__(self, metadata: meta.ObjectMeta = None, spec: ResourceClaimSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class ResourceClaimTemplate(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaimTemplate"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: ResourceClaimTemplateSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceClaimTemplateSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceClaimTemplateList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaimTemplateList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ResourceClaimTemplate]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ResourceClaimTemplate] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class ResourceClassParametersReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["kind", "name"]

    api_group: str
    kind: str
    name: str
    namespace: str

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace)


class ResourceClass(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClass"
    _scope_ = "namespace"

    _required_ = ["driver_name"]

    driver_name: str
    metadata: meta.ObjectMeta
    parameters_ref: ResourceClassParametersReference
    suitable_nodes: core.NodeSelector

    def __init__(
        self,
        name: str,
        namespace: str = None,
        driver_name: str = None,
        metadata: meta.ObjectMeta = None,
        parameters_ref: ResourceClassParametersReference = None,
        suitable_nodes: core.NodeSelector = None,
    ):
        super().__init__(
            name, namespace, driver_name=driver_name, metadata=metadata, parameters_ref=parameters_ref, suitable_nodes=suitable_nodes
        )


class ResourceClassList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClassList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[ResourceClass]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[ResourceClass] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)
