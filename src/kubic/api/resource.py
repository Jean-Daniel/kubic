from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class NamedResourcesAllocationResult(KubernetesObject):
    """NamedResourcesAllocationResult is used in AllocationResultModel."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["name"]

    name: str
    """ Name is the name of the selected resource instance. """

    def __init__(self, name: str = None):
        super().__init__(name=name)


class DriverAllocationResult(KubernetesObject):
    """DriverAllocationResult contains vendor parameters and the allocation result for one request."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    named_resources: NamedResourcesAllocationResult
    """ NamedResources describes the allocation result when using the named resources model. """
    vendor_request_parameters: core.RawExtension
    """ VendorRequestParameters are the per-request configuration parameters from the time that the claim was allocated. """

    def __init__(self, named_resources: NamedResourcesAllocationResult = None, vendor_request_parameters: core.RawExtension = None):
        super().__init__(named_resources=named_resources, vendor_request_parameters=vendor_request_parameters)


class StructuredResourceHandle(KubernetesObject):
    """StructuredResourceHandle is the in-tree representation of the allocation result."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["results"]

    node_name: str
    """ NodeName is the name of the node providing the necessary resources if the resources are local to a node. """
    results: list[DriverAllocationResult]
    """ Results lists all allocated driver resources. """
    vendor_claim_parameters: core.RawExtension
    """ VendorClaimParameters are the per-claim configuration parameters from the resource claim parameters at the time that the claim was allocated. """
    vendor_class_parameters: core.RawExtension
    """ VendorClassParameters are the per-claim configuration parameters from the resource class at the time that the claim was allocated. """

    def __init__(
        self,
        node_name: str = None,
        results: list[DriverAllocationResult] = None,
        vendor_claim_parameters: core.RawExtension = None,
        vendor_class_parameters: core.RawExtension = None,
    ):
        super().__init__(
            node_name=node_name,
            results=results,
            vendor_claim_parameters=vendor_claim_parameters,
            vendor_class_parameters=vendor_class_parameters,
        )


class ResourceHandle(KubernetesObject):
    """ResourceHandle holds opaque resource data for processing by a specific kubelet plugin."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    data: str
    """
    Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.
    
    The maximum size of this field is 16KiB. This may get increased in the future, but not reduced.
    """
    driver_name: str
    """ DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in. """
    structured_data: StructuredResourceHandle
    """ If StructuredData is set, then it needs to be used instead of Data. """

    def __init__(self, data: str = None, driver_name: str = None, structured_data: StructuredResourceHandle = None):
        super().__init__(data=data, driver_name=driver_name, structured_data=structured_data)


class AllocationResult(KubernetesObject):
    """AllocationResult contains attributes of an allocated resource."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    available_on_nodes: core.NodeSelector
    """
    This field will get set by the resource driver after it has allocated the resource to inform the scheduler where it can schedule Pods using the ResourceClaim.
    
    Setting this field is optional. If null, the resource is available everywhere.
    """
    resource_handles: list[ResourceHandle]
    """
    ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.
    
    Setting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in.
    """
    shareable: bool
    """ Shareable determines whether the resource supports more than one consumer at a time. """

    def __init__(self, available_on_nodes: core.NodeSelector = None, resource_handles: list[ResourceHandle] = None, shareable: bool = None):
        super().__init__(available_on_nodes=available_on_nodes, resource_handles=resource_handles, shareable=shareable)


class NamedResourcesRequest(KubernetesObject):
    """NamedResourcesRequest is used in ResourceRequestModel."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["selector"]

    selector: str
    """
    Selector is a CEL expression which must evaluate to true if a resource instance is suitable. The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/
    
    In addition, for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding value of the instance under evaluation. For example:
    
       attributes.quantity["a"].isGreaterThan(quantity("0")) &&
       attributes.stringslice["b"].isSorted()
    """

    def __init__(self, selector: str = None):
        super().__init__(selector=selector)


class ResourceRequest(KubernetesObject):
    """ResourceRequest is a request for resources from one particular driver."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    named_resources: NamedResourcesRequest
    """ NamedResources describes a request for resources with the named resources model. """
    vendor_parameters: core.RawExtension
    """ VendorParameters are arbitrary setup parameters for the requested resource. They are ignored while allocating a claim. """

    def __init__(self, named_resources: NamedResourcesRequest = None, vendor_parameters: core.RawExtension = None):
        super().__init__(named_resources=named_resources, vendor_parameters=vendor_parameters)


class DriverRequests(KubernetesObject):
    """DriverRequests describes all resources that are needed from one particular driver."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    driver_name: str
    """ DriverName is the name used by the DRA driver kubelet plugin. """
    requests: list[ResourceRequest]
    """ Requests describes all resources that are needed from the driver. """
    vendor_parameters: core.RawExtension
    """ VendorParameters are arbitrary setup parameters for all requests of the claim. They are ignored while allocating the claim. """

    def __init__(self, driver_name: str = None, requests: list[ResourceRequest] = None, vendor_parameters: core.RawExtension = None):
        super().__init__(driver_name=driver_name, requests=requests, vendor_parameters=vendor_parameters)


class NamedResourcesIntSlice(KubernetesObject):
    """NamedResourcesIntSlice contains a slice of 64-bit integers."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["ints"]

    ints: list[int]
    """ Ints is the slice of 64-bit integers. """

    def __init__(self, ints: list[int] = None):
        super().__init__(ints=ints)


class NamedResourcesStringSlice(KubernetesObject):
    """NamedResourcesStringSlice contains a slice of strings."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["strings"]

    strings: list[str]
    """ Strings is the slice of strings. """

    def __init__(self, strings: list[str] = None):
        super().__init__(strings=strings)


class NamedResourcesAttribute(KubernetesObject):
    """NamedResourcesAttribute is a combination of an attribute name and its value."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["name"]

    bool: bool
    """ BoolValue is a true/false value. """
    int: int
    """ IntValue is a 64-bit integer. """
    int_slice: NamedResourcesIntSlice
    """ IntSliceValue is an array of 64-bit integers. """
    name: str
    """ Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain. """
    quantity: core.Quantity
    """ QuantityValue is a quantity. """
    string: str
    """ StringValue is a string. """
    string_slice: NamedResourcesStringSlice
    """ StringSliceValue is an array of strings. """
    version: str
    """ VersionValue is a semantic version according to semver.org spec 2.0.0. """

    def __init__(
        self,
        bool: bool = None,
        int: int = None,
        int_slice: NamedResourcesIntSlice = None,
        name: str = None,
        quantity: core.Quantity = None,
        string: str = None,
        string_slice: NamedResourcesStringSlice = None,
        version: str = None,
    ):
        super().__init__(
            bool=bool, int=int, int_slice=int_slice, name=name, quantity=quantity, string=string, string_slice=string_slice, version=version
        )


class NamedResourcesFilter(KubernetesObject):
    """NamedResourcesFilter is used in ResourceFilterModel."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["selector"]

    selector: str
    """
    Selector is a CEL expression which must evaluate to true if a resource instance is suitable. The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/
    
    In addition, for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding value of the instance under evaluation. For example:
    
       attributes.quantity["a"].isGreaterThan(quantity("0")) &&
       attributes.stringslice["b"].isSorted()
    """

    def __init__(self, selector: str = None):
        super().__init__(selector=selector)


class NamedResourcesInstance(KubernetesObject):
    """NamedResourcesInstance represents one individual hardware instance that can be selected based on its attributes."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["name"]

    attributes: list[NamedResourcesAttribute]
    """ Attributes defines the attributes of this resource instance. The name of each attribute must be unique. """
    name: str
    """ Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain. """

    def __init__(self, attributes: list[NamedResourcesAttribute] = None, name: str = None):
        super().__init__(attributes=attributes, name=name)


class NamedResourcesResources(KubernetesObject):
    """NamedResourcesResources is used in ResourceModel."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["instances"]

    instances: list[NamedResourcesInstance]
    """ The list of all individual resources instances currently available. """

    def __init__(self, instances: list[NamedResourcesInstance] = None):
        super().__init__(instances=instances)


class PodSchedulingContextSpec(KubernetesObject):
    """PodSchedulingContextSpec describes where resources for the Pod are needed."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    potential_nodes: list[str]
    """
    PotentialNodes lists nodes where the Pod might be able to run.
    
    The size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced.
    """
    selected_node: str
    """ SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use "WaitForFirstConsumer" allocation is to be attempted. """

    def __init__(self, potential_nodes: list[str] = None, selected_node: str = None):
        super().__init__(potential_nodes=potential_nodes, selected_node=selected_node)


class PodSchedulingContext(KubernetesApiResource):
    """
    PodSchedulingContext objects hold information that is needed to schedule a Pod with ResourceClaims that use "WaitForFirstConsumer" allocation mode.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
    """

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "PodSchedulingContext"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard object metadata """
    spec: PodSchedulingContextSpec
    """ Spec describes where resources for the Pod are needed. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: PodSchedulingContextSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceClaimSchedulingStatus(KubernetesObject):
    """ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with "WaitForFirstConsumer" allocation mode."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    name: str
    """ Name matches the pod.spec.resourceClaims[*].Name field. """
    unsuitable_nodes: list[str]
    """
    UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.
    
    The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced.
    """

    def __init__(self, name: str = None, unsuitable_nodes: list[str] = None):
        super().__init__(name=name, unsuitable_nodes=unsuitable_nodes)


class PodSchedulingContextStatus(KubernetesObject):
    """PodSchedulingContextStatus describes where resources for the Pod can be allocated."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    resource_claims: list[ResourceClaimSchedulingStatus]
    """ ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses "WaitForFirstConsumer" allocation mode. """

    def __init__(self, resource_claims: list[ResourceClaimSchedulingStatus] = None):
        super().__init__(resource_claims=resource_claims)


class ResourceClaimParametersReference(KubernetesObject):
    """ResourceClaimParametersReference contains enough information to let you locate the parameters for a ResourceClaim. The object must be in the same namespace as the ResourceClaim."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["kind", "name"]

    api_group: str
    """ APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """
    kind: str
    """ Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata, for example "ConfigMap". """
    name: str
    """ Name is the name of resource being referenced. """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name)


class ResourceClaimSpec(KubernetesObject):
    """ResourceClaimSpec defines how a resource is to be allocated."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["resource_class_name"]

    allocation_mode: str
    """ Allocation can start immediately or when a Pod wants to use the resource. "WaitForFirstConsumer" is the default. """
    parameters_ref: ResourceClaimParametersReference
    """
    ParametersRef references a separate object with arbitrary parameters that will be used by the driver when allocating a resource for the claim.
    
    The object must be in the same namespace as the ResourceClaim.
    """
    resource_class_name: str
    """ ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. """

    def __init__(
        self, allocation_mode: str = None, parameters_ref: ResourceClaimParametersReference = None, resource_class_name: str = None
    ):
        super().__init__(allocation_mode=allocation_mode, parameters_ref=parameters_ref, resource_class_name=resource_class_name)


class ResourceClaim(KubernetesApiResource):
    """
    ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether the resource has been allocated and what the resulting attributes are.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
    """

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaim"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard object metadata """
    spec: ResourceClaimSpec
    """ Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim. """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceClaimSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceClaimConsumerReference(KubernetesObject):
    """ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["name", "resource", "uid"]

    api_group: str
    """ APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """
    name: str
    """ Name is the name of resource being referenced. """
    resource: str
    """ Resource is the type of resource being referenced, for example "pods". """
    uid: str
    """ UID identifies exactly one incarnation of the resource. """

    def __init__(self, api_group: str = None, name: str = None, resource: str = None, uid: str = None):
        super().__init__(api_group=api_group, name=name, resource=resource, uid=uid)


class ResourceClaimParameters(KubernetesApiResource):
    """ResourceClaimParameters defines resource requests for a ResourceClaim in an in-tree format understood by Kubernetes."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaimParameters"
    _scope_ = "namespace"

    driver_requests: list[DriverRequests]
    """
    DriverRequests describes all resources that are needed for the allocated claim. A single claim may use resources coming from different drivers. For each driver, this array has at most one entry which then may have one or more per-driver requests.
    
    May be empty, in which case the claim can always be allocated.
    """
    generated_from: ResourceClaimParametersReference
    """ If this object was created from some other resource, then this links back to that resource. This field is used to find the in-tree representation of the claim parameters when the parameter reference of the claim refers to some unknown type. """
    metadata: meta.ObjectMeta
    """ Standard object metadata """
    shareable: bool
    """ Shareable indicates whether the allocated claim is meant to be shareable by multiple consumers at the same time. """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        driver_requests: list[DriverRequests] = None,
        generated_from: ResourceClaimParametersReference = None,
        metadata: meta.ObjectMeta = None,
        shareable: bool = None,
    ):
        super().__init__(
            name, namespace, driver_requests=driver_requests, generated_from=generated_from, metadata=metadata, shareable=shareable
        )


class ResourceClaimStatus(KubernetesObject):
    """ResourceClaimStatus tracks whether the resource has been allocated and what the resulting attributes are."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    allocation: AllocationResult
    """ Allocation is set by the resource driver once a resource or set of resources has been allocated successfully. If this is not specified, the resources have not been allocated yet. """
    deallocation_requested: bool
    """
    DeallocationRequested indicates that a ResourceClaim is to be deallocated.
    
    The driver then must deallocate this claim and reset the field together with clearing the Allocation field.
    
    While DeallocationRequested is set, no new consumers may be added to ReservedFor.
    """
    driver_name: str
    """ DriverName is a copy of the driver name from the ResourceClass at the time when allocation started. """
    reserved_for: list[ResourceClaimConsumerReference]
    """
    ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.
    
    There can be at most 32 such reservations. This may get increased in the future, but not reduced.
    """

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
    """ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ ObjectMeta may contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. """
    spec: ResourceClaimSpec
    """ Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here. """

    def __init__(self, metadata: meta.ObjectMeta = None, spec: ResourceClaimSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class ResourceClaimTemplate(KubernetesApiResource):
    """ResourceClaimTemplate is used to produce ResourceClaim objects."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClaimTemplate"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard object metadata """
    spec: ResourceClaimTemplateSpec
    """
    Describes the ResourceClaim that is to be generated.
    
    This field is immutable. A ResourceClaim will get created by the control plane for a Pod when needed and then not get updated anymore.
    """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: ResourceClaimTemplateSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class ResourceClassParametersReference(KubernetesObject):
    """ResourceClassParametersReference contains enough information to let you locate the parameters for a ResourceClass."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    _required_ = ["kind", "name"]

    api_group: str
    """ APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. """
    kind: str
    """ Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata. """
    name: str
    """ Name is the name of resource being referenced. """
    namespace: str
    """ Namespace that contains the referenced resource. Must be empty for cluster-scoped resources and non-empty for namespaced resources. """

    def __init__(self, api_group: str = None, kind: str = None, name: str = None, namespace: str = None):
        super().__init__(api_group=api_group, kind=kind, name=name, namespace=namespace)


class ResourceClass(KubernetesApiResource):
    """
    ResourceClass is used by administrators to influence how resources are allocated.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
    """

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClass"
    _scope_ = "namespace"

    _required_ = ["driver_name"]

    driver_name: str
    """
    DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.
    
    Resource drivers have a unique name in forward domain order (acme.example.com).
    """
    metadata: meta.ObjectMeta
    """ Standard object metadata """
    parameters_ref: ResourceClassParametersReference
    """ ParametersRef references an arbitrary separate object that may hold parameters that will be used by the driver when allocating a resource that uses this class. A dynamic resource driver can distinguish between parameters stored here and and those stored in ResourceClaimSpec. """
    structured_parameters: bool
    """ If and only if allocation of claims using this class is handled via structured parameters, then StructuredParameters must be set to true. """
    suitable_nodes: core.NodeSelector
    """
    Only nodes matching the selector will be considered by the scheduler when trying to find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.
    
    Setting this field is optional. If null, all nodes are candidates.
    """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        driver_name: str = None,
        metadata: meta.ObjectMeta = None,
        parameters_ref: ResourceClassParametersReference = None,
        structured_parameters: bool = None,
        suitable_nodes: core.NodeSelector = None,
    ):
        super().__init__(
            name,
            namespace,
            driver_name=driver_name,
            metadata=metadata,
            parameters_ref=parameters_ref,
            structured_parameters=structured_parameters,
            suitable_nodes=suitable_nodes,
        )


class ResourceFilter(KubernetesObject):
    """ResourceFilter is a filter for resources from one particular driver."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    driver_name: str
    """ DriverName is the name used by the DRA driver kubelet plugin. """
    named_resources: NamedResourcesFilter
    """ NamedResources describes a resource filter using the named resources model. """

    def __init__(self, driver_name: str = None, named_resources: NamedResourcesFilter = None):
        super().__init__(driver_name=driver_name, named_resources=named_resources)


class VendorParameters(KubernetesObject):
    """VendorParameters are opaque parameters for one particular driver."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"

    driver_name: str
    """ DriverName is the name used by the DRA driver kubelet plugin. """
    parameters: core.RawExtension
    """ Parameters can be arbitrary setup parameters. They are ignored while allocating a claim. """

    def __init__(self, driver_name: str = None, parameters: core.RawExtension = None):
        super().__init__(driver_name=driver_name, parameters=parameters)


class ResourceClassParameters(KubernetesApiResource):
    """ResourceClassParameters defines resource requests for a ResourceClass in an in-tree format understood by Kubernetes."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceClassParameters"
    _scope_ = "namespace"

    filters: list[ResourceFilter]
    """ Filters describes additional contraints that must be met when using the class. """
    generated_from: ResourceClassParametersReference
    """ If this object was created from some other resource, then this links back to that resource. This field is used to find the in-tree representation of the class parameters when the parameter reference of the class refers to some unknown type. """
    metadata: meta.ObjectMeta
    """ Standard object metadata """
    vendor_parameters: list[VendorParameters]
    """ VendorParameters are arbitrary setup parameters for all claims using this class. They are ignored while allocating the claim. There must not be more than one entry per driver. """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        filters: list[ResourceFilter] = None,
        generated_from: ResourceClassParametersReference = None,
        metadata: meta.ObjectMeta = None,
        vendor_parameters: list[VendorParameters] = None,
    ):
        super().__init__(
            name, namespace, filters=filters, generated_from=generated_from, metadata=metadata, vendor_parameters=vendor_parameters
        )


class ResourceSlice(KubernetesApiResource):
    """ResourceSlice provides information about available resources on individual nodes."""

    __slots__ = ()

    _api_version_ = "resource.k8s.io/v1alpha2"
    _api_group_ = "resource.k8s.io"
    _kind_ = "ResourceSlice"
    _scope_ = "namespace"

    _required_ = ["driver_name"]

    driver_name: str
    """ DriverName identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name. """
    metadata: meta.ObjectMeta
    """ Standard object metadata """
    named_resources: NamedResourcesResources
    """ NamedResources describes available resources using the named resources model. """
    node_name: str
    """
    NodeName identifies the node which provides the resources if they are local to a node.
    
    A field selector can be used to list only ResourceSlice objects with a certain node name.
    """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        driver_name: str = None,
        metadata: meta.ObjectMeta = None,
        named_resources: NamedResourcesResources = None,
        node_name: str = None,
    ):
        super().__init__(name, namespace, driver_name=driver_name, metadata=metadata, named_resources=named_resources, node_name=node_name)
