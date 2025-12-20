import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from ..api import core, meta


class AWS(KubernetesObject):
    __slots__ = ()

    labels: dict[str, str]
    region: str
    security_groups_ids: list[str]
    security_groups_names: list[str]

    def __init__(
        self,
        labels: dict[str, str] = None,
        region: str = None,
        security_groups_ids: list[str] = None,
        security_groups_names: list[str] = None,
    ):
        super().__init__(labels=labels, region=region, security_groups_ids=security_groups_ids, security_groups_names=security_groups_names)


class Addresse(KubernetesObject):
    __slots__ = ()

    ip: str
    """ IP is an IP of a node """
    type: str
    """ Type is the type of the node address """

    def __init__(self, ip: str = None, type: str = None):
        super().__init__(ip=ip, type=type)


class Addressing(KubernetesObject):
    __slots__ = ()

    ipv4: str
    ipv6: str

    def __init__(self, ipv4: str = None, ipv6: str = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6)


class Communities(KubernetesObject):
    __slots__ = ()

    large: list[str]
    """ Large holds a list of the BGP Large Communities Attribute (RFC 8092) values. """
    standard: list[str]
    """ Standard holds a list of "standard" 32-bit BGP Communities Attribute (RFC 1997) values defined as numeric values. """
    well_known: list[str]
    """
    WellKnown holds a list "standard" 32-bit BGP Communities Attribute (RFC 1997) values defined as
    well-known string aliases to their numeric values.
    """

    def __init__(self, large: list[str] = None, standard: list[str] = None, well_known: list[str] = None):
        super().__init__(large=large, standard=standard, well_known=well_known)


class AdvertisedPathAttribute(KubernetesObject):
    __slots__ = ()

    _required_ = ["selector_type"]

    communities: Communities
    """
    Communities defines a set of community values advertised in the supported BGP Communities path attributes.
    If nil / not set, no BGP Communities path attribute will be advertised.
    """
    local_preference: int
    """
    LocalPreference defines the preference value advertised in the BGP Local Preference path attribute.
    As Local Preference is only valid for iBGP peers, this value will be ignored for eBGP peers
    (no Local Preference path attribute will be advertised).
    If nil / not set, the default Local Preference of 100 will be advertised in
    the Local Preference path attribute for iBGP peers.
    """
    selector: meta.LabelSelector
    """
    Selector selects a group of objects of the SelectorType
    resulting into routes that will be announced with the configured Attributes.
    If nil / not set, all objects of the SelectorType are selected.
    """
    selector_type: str
    """
    SelectorType defines the object type on which the Selector applies:
    - For "PodCIDR" the Selector matches k8s CiliumNode resources
      (path attributes apply to routes announced for PodCIDRs of selected CiliumNodes.
      Only affects routes of cluster scope / Kubernetes IPAM CIDRs, not Multi-Pool IPAM CIDRs.
    - For "CiliumLoadBalancerIPPool" the Selector matches CiliumLoadBalancerIPPool custom resources
      (path attributes apply to routes announced for selected CiliumLoadBalancerIPPools).
    - For "CiliumPodIPPool" the Selector matches CiliumPodIPPool custom resources
      (path attributes apply to routes announced for allocated CIDRs of selected CiliumPodIPPools).
    """

    def __init__(
        self, communities: Communities = None, local_preference: int = None, selector: meta.LabelSelector = None, selector_type: str = None
    ):
        super().__init__(communities=communities, local_preference=local_preference, selector=selector, selector_type=selector_type)


class Attributes(KubernetesObject):
    __slots__ = ()

    communities: Communities
    """
    Communities sets the community attributes in the route.
    If not specified, no community attribute is set.
    """
    local_preference: int
    """
    LocalPreference sets the local preference attribute in the route.
    If not specified, no local preference attribute is set.
    """

    def __init__(self, communities: Communities = None, local_preference: int = None):
        super().__init__(communities=communities, local_preference=local_preference)


class AdvertisementService(KubernetesObject):
    __slots__ = ()

    _required_ = ["addresses"]

    addresses: list[str]
    """ Addresses is a list of service address types which needs to be advertised via BGP. """

    def __init__(self, addresses: list[str] = None):
        super().__init__(addresses=addresses)


class Advertisement(KubernetesObject):
    __slots__ = ()

    _required_ = ["advertisement_type"]

    advertisement_type: str
    """ AdvertisementType defines type of advertisement which has to be advertised. """
    attributes: Attributes
    """
    Attributes defines additional attributes to set to the advertised routes.
    If not specified, no additional attributes are set.
    """
    selector: meta.LabelSelector
    """
    Selector is a label selector to select objects of the type specified by AdvertisementType.
    If not specified, no objects of the type specified by AdvertisementType are selected for advertisement.
    """
    service: AdvertisementService
    """ Service defines configuration options for advertisementType service. """

    def __init__(
        self,
        advertisement_type: str = None,
        attributes: Attributes = None,
        selector: meta.LabelSelector = None,
        service: AdvertisementService = None,
    ):
        super().__init__(advertisement_type=advertisement_type, attributes=attributes, selector=selector, service=service)


class AlibabaCloud(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "availability_zone": "availability-zone",
        "cidr_block": "cidr-block",
        "instance_type": "instance-type",
        "security_group_tags": "security-group-tags",
        "security_groups": "security-groups",
        "vpc_id": "vpc-id",
        "vswitch_tags": "vswitch-tags",
    }
    _revfield_names_ = {
        "availability-zone": "availability_zone",
        "cidr-block": "cidr_block",
        "instance-type": "instance_type",
        "security-group-tags": "security_group_tags",
        "security-groups": "security_groups",
        "vpc-id": "vpc_id",
        "vswitch-tags": "vswitch_tags",
    }

    availability_zone: str
    """
    AvailabilityZone is the availability zone to use when allocating
    ENIs.
    """
    cidr_block: str
    """ CIDRBlock is vpc ipv4 CIDR """
    instance_type: str
    """ InstanceType is the ECS instance type, e.g. "ecs.g6.2xlarge" """
    security_group_tags: dict[str, str]
    """
    SecurityGroupTags is the list of tags to use when evaluating which
    security groups to use for the ENI.
    """
    security_groups: list[str]
    """
    SecurityGroups is the list of security groups to attach to any ENI
    that is created and attached to the instance.
    """
    vpc_id: str
    """ VPCID is the VPC ID to use when allocating ENIs. """
    vswitch_tags: dict[str, str]
    """
    VSwitchTags is the list of tags to use when evaluating which
    vSwitch to use for the ENI.
    """
    vswitches: list[str]
    """ VSwitches is the ID of vSwitch available for ENI """

    def __init__(
        self,
        availability_zone: str = None,
        cidr_block: str = None,
        instance_type: str = None,
        security_group_tags: dict[str, str] = None,
        security_groups: list[str] = None,
        vpc_id: str = None,
        vswitch_tags: dict[str, str] = None,
        vswitches: list[str] = None,
    ):
        super().__init__(
            availability_zone=availability_zone,
            cidr_block=cidr_block,
            instance_type=instance_type,
            security_group_tags=security_group_tags,
            security_groups=security_groups,
            vpc_id=vpc_id,
            vswitch_tags=vswitch_tags,
            vswitches=vswitches,
        )


CIDR: t.TypeAlias = str


class Allocated(KubernetesObject):
    __slots__ = ()

    _required_ = ["pool"]

    cidrs: list[CIDR]
    """ CIDRs contains a list of pod CIDRs currently allocated from this pool """
    pool: str
    """ Pool is the name of the IPAM pool backing this allocation """

    def __init__(self, cidrs: list[CIDR] = None, pool: str = None):
        super().__init__(cidrs=cidrs, pool=pool)


class Authentication(KubernetesObject):
    __slots__ = ()

    _required_ = ["mode"]

    mode: str
    """ Mode is the required authentication mode for the allowed traffic, if any. """

    def __init__(self, mode: str = None):
        super().__init__(mode=mode)


class Azure(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "interface_name": "interface-name",
    }
    _revfield_names_ = {
        "interface-name": "interface_name",
    }

    interface_name: str
    """
    InterfaceName is the name of the interface the cilium-operator
    will use to allocate all the IPs on
    """

    def __init__(self, interface_name: str = None):
        super().__init__(interface_name=interface_name)


class BackendService(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    name: str
    """ Name is the name of a destination Kubernetes service that identifies traffic to be redirected. """
    namespace: str
    """ Namespace is the Kubernetes service namespace. In CiliumEnvoyConfig namespace defaults to the namespace of the CEC, In CiliumClusterwideEnvoyConfig namespace defaults to "default". """
    number: list[str]
    """ Ports is a set of port numbers, which can be used for filtering in case of underlying is exposing multiple port numbers. """

    def __init__(self, name: str = None, namespace: str = None, number: list[str] = None):
        super().__init__(name=name, namespace=namespace, number=number)


class PeerConfigRef(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    group: str
    """
    Group is the group of the peer config resource.
    If not specified, the default of "cilium.io" is used.
    """
    kind: str
    """
    Kind is the kind of the peer config resource.
    If not specified, the default of "CiliumBGPPeerConfig" is used.
    """
    name: str
    """
    Name is the name of the peer config resource.
    Name refers to the name of a Kubernetes object (typically a CiliumBGPPeerConfig).
    """

    def __init__(self, group: str = None, kind: str = None, name: str = None):
        super().__init__(group=group, kind=kind, name=name)


class BgpInstancePeer(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    _field_names_ = {
        "peer_asn": "peerASN",
    }
    _revfield_names_ = {
        "peerASN": "peer_asn",
    }

    local_address: str
    """
    LocalAddress is the IP address of the local interface to use for the peering session.
    This configuration is derived from CiliumBGPNodeConfigOverride resource. If not specified, the local address will be used for setting up peering.
    """
    name: str
    """ Name is the name of the BGP peer. This name is used to identify the BGP peer for the BGP instance. """
    peer_asn: int
    """
    PeerASN is the ASN of the peer BGP router.
    Supports extended 32bit ASNs
    """
    peer_address: str
    """
    PeerAddress is the IP address of the neighbor.
    Supports IPv4 and IPv6 addresses.
    """
    peer_config_ref: PeerConfigRef
    """
    PeerConfigRef is a reference to a peer configuration resource.
    If not specified, the default BGP configuration is used for this peer.
    """

    def __init__(
        self,
        local_address: str = None,
        name: str = None,
        peer_asn: int = None,
        peer_address: str = None,
        peer_config_ref: PeerConfigRef = None,
    ):
        super().__init__(
            local_address=local_address, name=name, peer_asn=peer_asn, peer_address=peer_address, peer_config_ref=peer_config_ref
        )


class BgpInstancePeer1(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    local_address: str
    """ LocalAddress is the IP address to use for connecting to this peer. """
    local_port: int
    """ LocalPort is source port to use for connecting to this peer. """
    name: str
    """ Name is the name of the peer for which the configuration is overridden. """

    def __init__(self, local_address: str = None, local_port: int = None, name: str = None):
        super().__init__(local_address=local_address, local_port=local_port, name=name)


class BgpInstancePeer2(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    _field_names_ = {
        "peer_asn": "peerASN",
    }
    _revfield_names_ = {
        "peerASN": "peer_asn",
    }

    name: str
    """ Name is the name of the BGP peer. It is a unique identifier for the peer within the BGP instance. """
    peer_asn: int
    """
    PeerASN is the ASN of the peer BGP router.
    Supports extended 32bit ASNs.
    
    If peerASN is 0, the BGP OPEN message validation of ASN will be disabled and
    ASN will be determined based on peer's OPEN message.
    """
    peer_address: str
    """
    PeerAddress is the IP address of the neighbor.
    Supports IPv4 and IPv6 addresses.
    """
    peer_config_ref: PeerConfigRef
    """
    PeerConfigRef is a reference to a peer configuration resource.
    If not specified, the default BGP configuration is used for this peer.
    """

    def __init__(self, name: str = None, peer_asn: int = None, peer_address: str = None, peer_config_ref: PeerConfigRef = None):
        super().__init__(name=name, peer_asn=peer_asn, peer_address=peer_address, peer_config_ref=peer_config_ref)


class Block(KubernetesObject):
    __slots__ = ()

    cidr: CIDR
    start: str
    stop: str

    def __init__(self, cidr: CIDR = None, start: str = None, stop: str = None):
        super().__init__(cidr=cidr, start=start, stop=stop)


class CiliumBGPAdvertisementSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["advertisements"]

    advertisements: list[Advertisement]
    """ Advertisements is a list of BGP advertisements. """

    def __init__(self, advertisements: list[Advertisement] = None):
        super().__init__(advertisements=advertisements)


class CiliumBGPAdvertisement(KubernetesApiResource):
    """CiliumBGPAdvertisement is the Schema for the ciliumbgpadvertisements API"""

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumBGPAdvertisement"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumBGPAdvertisementSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumBGPAdvertisementSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumBGPClusterConfigSpecBgpInstance(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    _field_names_ = {
        "local_asn": "localASN",
    }
    _revfield_names_ = {
        "localASN": "local_asn",
    }

    local_asn: int
    """
    LocalASN is the ASN of this BGP instance.
    Supports extended 32bit ASNs.
    """
    name: str
    """
    Name is the name of the BGP instance. It is a unique identifier for the BGP instance
    within the cluster configuration.
    """
    peers: list[BgpInstancePeer2]
    """ Peers is a list of neighboring BGP peers for this virtual router """

    def __init__(self, local_asn: int = None, name: str = None, peers: list[BgpInstancePeer2] = None):
        super().__init__(local_asn=local_asn, name=name, peers=peers)


class CiliumBGPClusterConfigSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["bgp_instances"]

    bgp_instances: list[CiliumBGPClusterConfigSpecBgpInstance]
    """
    A list of CiliumBGPInstance(s) which instructs
    the BGP control plane how to instantiate virtual BGP routers.
    """
    node_selector: meta.LabelSelector
    """
    NodeSelector selects a group of nodes where this BGP Cluster
    config applies.
    If empty / nil this config applies to all nodes.
    """

    def __init__(self, bgp_instances: list[CiliumBGPClusterConfigSpecBgpInstance] = None, node_selector: meta.LabelSelector = None):
        super().__init__(bgp_instances=bgp_instances, node_selector=node_selector)


class CiliumBGPClusterConfig(KubernetesApiResource):
    """CiliumBGPClusterConfig is the Schema for the CiliumBGPClusterConfig API"""

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumBGPClusterConfig"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumBGPClusterConfigSpec
    """ Spec defines the desired cluster configuration of the BGP control plane. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumBGPClusterConfigSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


Ipv4: t.TypeAlias = str


class CiliumBGPNodeConfigSpecBgpInstance(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    _field_names_ = {
        "local_asn": "localASN",
        "router_id": "routerID",
    }
    _revfield_names_ = {
        "localASN": "local_asn",
        "routerID": "router_id",
    }

    local_asn: int
    """
    LocalASN is the ASN of this virtual router.
    Supports extended 32bit ASNs.
    """
    local_port: int
    """
    LocalPort is the port on which the BGP daemon listens for incoming connections.
    
    If not specified, BGP instance will not listen for incoming connections.
    """
    name: str
    """ Name is the name of the BGP instance. This name is used to identify the BGP instance on the node. """
    peers: list[BgpInstancePeer]
    """ Peers is a list of neighboring BGP peers for this virtual router """
    router_id: Ipv4
    """
    RouterID is the BGP router ID of this virtual router.
    This configuration is derived from CiliumBGPNodeConfigOverride resource.
    
    If not specified, the router ID will be derived from the node local address.
    """

    def __init__(
        self, local_asn: int = None, local_port: int = None, name: str = None, peers: list[BgpInstancePeer] = None, router_id: Ipv4 = None
    ):
        super().__init__(local_asn=local_asn, local_port=local_port, name=name, peers=peers, router_id=router_id)


class CiliumBGPNodeConfigSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["bgp_instances"]

    bgp_instances: list[CiliumBGPNodeConfigSpecBgpInstance]
    """ BGPInstances is a list of BGP router instances on the node. """

    def __init__(self, bgp_instances: list[CiliumBGPNodeConfigSpecBgpInstance] = None):
        super().__init__(bgp_instances=bgp_instances)


class CiliumBGPNodeConfig(KubernetesApiResource):
    """
    CiliumBGPNodeConfig is node local configuration for BGP agent. Name of the object should be node name.
    This resource will be created by Cilium operator and is read-only for the users.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumBGPNodeConfig"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumBGPNodeConfigSpec
    """ Spec is the specification of the desired behavior of the CiliumBGPNodeConfig. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumBGPNodeConfigSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumBGPNodeConfigOverrideSpecBgpInstance(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    _field_names_ = {
        "router_id": "routerID",
    }
    _revfield_names_ = {
        "routerID": "router_id",
    }

    local_port: int
    """ LocalPort is port to use for this BGP instance. """
    name: str
    """ Name is the name of the BGP instance for which the configuration is overridden. """
    peers: list[BgpInstancePeer1]
    """ Peers is a list of peer configurations to override. """
    router_id: Ipv4
    """ RouterID is BGP router id to use for this instance. It must be unique across all BGP instances. """

    def __init__(self, local_port: int = None, name: str = None, peers: list[BgpInstancePeer1] = None, router_id: Ipv4 = None):
        super().__init__(local_port=local_port, name=name, peers=peers, router_id=router_id)


class CiliumBGPNodeConfigOverrideSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["bgp_instances"]

    bgp_instances: list[CiliumBGPNodeConfigOverrideSpecBgpInstance]
    """ BGPInstances is a list of BGP instances to override. """

    def __init__(self, bgp_instances: list[CiliumBGPNodeConfigOverrideSpecBgpInstance] = None):
        super().__init__(bgp_instances=bgp_instances)


class CiliumBGPNodeConfigOverride(KubernetesApiResource):
    """
    CiliumBGPNodeConfigOverride specifies configuration overrides for a CiliumBGPNodeConfig.
    It allows fine-tuning of BGP behavior on a per-node basis. For the override to be effective,
    the names in CiliumBGPNodeConfigOverride and CiliumBGPNodeConfig must match exactly. This
    matching ensures that specific node configurations are applied correctly and only where intended.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumBGPNodeConfigOverride"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumBGPNodeConfigOverrideSpec
    """ Spec is the specification of the desired behavior of the CiliumBGPNodeConfigOverride. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumBGPNodeConfigOverrideSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumBGPPeerConfigSpecFamily(KubernetesObject):
    __slots__ = ()

    _required_ = ["afi", "safi"]

    advertisements: meta.LabelSelector
    """
    Advertisements selects group of BGP Advertisement(s) to advertise for this family.
    
    If not specified, no advertisements are sent for this family.
    
    This field is ignored in CiliumBGPNeighbor which is used in CiliumBGPPeeringPolicy.
    Use CiliumBGPPeeringPolicy advertisement options instead.
    """
    afi: str
    """ Afi is the Address Family Identifier (AFI) of the family. """
    safi: str
    """ Safi is the Subsequent Address Family Identifier (SAFI) of the family. """

    def __init__(self, advertisements: meta.LabelSelector = None, afi: str = None, safi: str = None):
        super().__init__(advertisements=advertisements, afi=afi, safi=safi)


class GracefulRestart(KubernetesObject):
    __slots__ = ()

    _required_ = ["enabled"]

    enabled: bool
    """ Enabled flag, when set enables graceful restart capability. """
    restart_time_seconds: int
    """
    RestartTimeSeconds is the estimated time it will take for the BGP
    session to be re-established with peer after a restart.
    After this period, peer will remove stale routes. This is
    described RFC 4724 section 4.2.
    """

    def __init__(self, enabled: bool = None, restart_time_seconds: int = None):
        super().__init__(enabled=enabled, restart_time_seconds=restart_time_seconds)


class Timers(KubernetesObject):
    __slots__ = ()

    connect_retry_time_seconds: int
    """
    ConnectRetryTimeSeconds defines the initial value for the BGP ConnectRetryTimer (RFC 4271, Section 8).
    
    If not specified, defaults to 120 seconds.
    """
    hold_time_seconds: int
    """
    HoldTimeSeconds defines the initial value for the BGP HoldTimer (RFC 4271, Section 4.2).
    Updating this value will cause a session reset.
    
    If not specified, defaults to 90 seconds.
    """
    keep_alive_time_seconds: int
    """
    KeepaliveTimeSeconds defines the initial value for the BGP KeepaliveTimer (RFC 4271, Section 8).
    It can not be larger than HoldTimeSeconds. Updating this value will cause a session reset.
    
    If not specified, defaults to 30 seconds.
    """

    def __init__(self, connect_retry_time_seconds: int = None, hold_time_seconds: int = None, keep_alive_time_seconds: int = None):
        super().__init__(
            connect_retry_time_seconds=connect_retry_time_seconds,
            hold_time_seconds=hold_time_seconds,
            keep_alive_time_seconds=keep_alive_time_seconds,
        )


class Transport(KubernetesObject):
    __slots__ = ()

    local_port: int
    """
    Deprecated
    LocalPort is the local port to be used for the BGP session.
    
    If not specified, ephemeral port will be picked to initiate a connection.
    
    This field is deprecated and will be removed in a future release.
    Local port configuration is unnecessary and is not recommended.
    """
    peer_port: int
    """
    PeerPort is the peer port to be used for the BGP session.
    
    If not specified, defaults to TCP port 179.
    """

    def __init__(self, local_port: int = None, peer_port: int = None):
        super().__init__(local_port=local_port, peer_port=peer_port)


class CiliumBGPPeerConfigSpec(KubernetesObject):
    __slots__ = ()

    auth_secret_ref: str
    """
    AuthSecretRef is the name of the secret to use to fetch a TCP
    authentication password for this peer.
    
    If not specified, no authentication is used.
    """
    ebgp_multihop: int
    """
    EBGPMultihopTTL controls the multi-hop feature for eBGP peers.
    Its value defines the Time To Live (TTL) value used in BGP
    packets sent to the peer.
    
    If not specified, EBGP multihop is disabled. This field is ignored for iBGP neighbors.
    """
    families: list[CiliumBGPPeerConfigSpecFamily]
    """
    Families, if provided, defines a set of AFI/SAFIs the speaker will
    negotiate with it's peer.
    
    If not specified, the default families of IPv6/unicast and IPv4/unicast will be created.
    """
    graceful_restart: GracefulRestart
    """
    GracefulRestart defines graceful restart parameters which are negotiated
    with this peer.
    
    If not specified, the graceful restart capability is disabled.
    """
    timers: Timers
    """
    Timers defines the BGP timers for the peer.
    
    If not specified, the default timers are used.
    """
    transport: Transport
    """
    Transport defines the BGP transport parameters for the peer.
    
    If not specified, the default transport parameters are used.
    """

    def __init__(
        self,
        auth_secret_ref: str = None,
        ebgp_multihop: int = None,
        families: list[CiliumBGPPeerConfigSpecFamily] = None,
        graceful_restart: GracefulRestart = None,
        timers: Timers = None,
        transport: Transport = None,
    ):
        super().__init__(
            auth_secret_ref=auth_secret_ref,
            ebgp_multihop=ebgp_multihop,
            families=families,
            graceful_restart=graceful_restart,
            timers=timers,
            transport=transport,
        )


class CiliumBGPPeerConfig(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumBGPPeerConfig"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumBGPPeerConfigSpec
    """ Spec is the specification of the desired behavior of the CiliumBGPPeerConfig. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumBGPPeerConfigSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class NeighborFamily(KubernetesObject):
    __slots__ = ()

    _required_ = ["afi", "safi"]

    afi: str
    """ Afi is the Address Family Identifier (AFI) of the family. """
    safi: str
    """ Safi is the Subsequent Address Family Identifier (SAFI) of the family. """

    def __init__(self, afi: str = None, safi: str = None):
        super().__init__(afi=afi, safi=safi)


class Neighbor(KubernetesObject):
    __slots__ = ()

    _required_ = ["peer_asn", "peer_address"]

    _field_names_ = {
        "e_bgp_multihop_ttl": "eBGPMultihopTTL",
        "peer_asn": "peerASN",
    }
    _revfield_names_ = {
        "eBGPMultihopTTL": "e_bgp_multihop_ttl",
        "peerASN": "peer_asn",
    }

    advertised_path_attributes: list[AdvertisedPathAttribute]
    """
    AdvertisedPathAttributes can be used to apply additional path attributes
    to selected routes when advertising them to the peer.
    If empty / nil, no additional path attributes are advertised.
    """
    auth_secret_ref: str
    """
    AuthSecretRef is the name of the secret to use to fetch a TCP
    authentication password for this peer.
    """
    connect_retry_time_seconds: int
    """ ConnectRetryTimeSeconds defines the initial value for the BGP ConnectRetryTimer (RFC 4271, Section 8). """
    e_bgp_multihop_ttl: int
    """
    EBGPMultihopTTL controls the multi-hop feature for eBGP peers.
    Its value defines the Time To Live (TTL) value used in BGP packets sent to the neighbor.
    The value 1 implies that eBGP multi-hop feature is disabled (only a single hop is allowed).
    This field is ignored for iBGP peers.
    """
    families: list[NeighborFamily]
    """
    Families, if provided, defines a set of AFI/SAFIs the speaker will
    negotiate with it's peer.
    
    If this slice is not provided the default families of IPv6 and IPv4 will
    be provided.
    """
    graceful_restart: GracefulRestart
    """
    GracefulRestart defines graceful restart parameters which are negotiated
    with this neighbor. If empty / nil, the graceful restart capability is disabled.
    """
    hold_time_seconds: int
    """
    HoldTimeSeconds defines the initial value for the BGP HoldTimer (RFC 4271, Section 4.2).
    Updating this value will cause a session reset.
    """
    keep_alive_time_seconds: int
    """
    KeepaliveTimeSeconds defines the initial value for the BGP KeepaliveTimer (RFC 4271, Section 8).
    It can not be larger than HoldTimeSeconds. Updating this value will cause a session reset.
    """
    peer_asn: int
    """
    PeerASN is the ASN of the peer BGP router.
    Supports extended 32bit ASNs
    """
    peer_address: CIDR
    """
    PeerAddress is the IP address of the peer.
    This must be in CIDR notation and use a /32 to express
    a single host.
    """
    peer_port: int
    """
    PeerPort is the TCP port of the peer. 1-65535 is the range of
    valid port numbers that can be specified. If unset, defaults to 179.
    """

    def __init__(
        self,
        advertised_path_attributes: list[AdvertisedPathAttribute] = None,
        auth_secret_ref: str = None,
        connect_retry_time_seconds: int = None,
        e_bgp_multihop_ttl: int = None,
        families: list[NeighborFamily] = None,
        graceful_restart: GracefulRestart = None,
        hold_time_seconds: int = None,
        keep_alive_time_seconds: int = None,
        peer_asn: int = None,
        peer_address: CIDR = None,
        peer_port: int = None,
    ):
        super().__init__(
            advertised_path_attributes=advertised_path_attributes,
            auth_secret_ref=auth_secret_ref,
            connect_retry_time_seconds=connect_retry_time_seconds,
            e_bgp_multihop_ttl=e_bgp_multihop_ttl,
            families=families,
            graceful_restart=graceful_restart,
            hold_time_seconds=hold_time_seconds,
            keep_alive_time_seconds=keep_alive_time_seconds,
            peer_asn=peer_asn,
            peer_address=peer_address,
            peer_port=peer_port,
        )


class VirtualRouter(KubernetesObject):
    __slots__ = ()

    _required_ = ["local_asn", "neighbors"]

    _field_names_ = {
        "export_pod_cidr": "exportPodCIDR",
        "local_asn": "localASN",
        "pod_ip_pool_selector": "podIPPoolSelector",
    }
    _revfield_names_ = {
        "exportPodCIDR": "export_pod_cidr",
        "localASN": "local_asn",
        "podIPPoolSelector": "pod_ip_pool_selector",
    }

    export_pod_cidr: bool
    """
    ExportPodCIDR determines whether to export the Node's private CIDR block
    to the configured neighbors.
    """
    local_asn: int
    """
    LocalASN is the ASN of this virtual router.
    Supports extended 32bit ASNs
    """
    neighbors: list[Neighbor]
    """ Neighbors is a list of neighboring BGP peers for this virtual router """
    pod_ip_pool_selector: meta.LabelSelector
    """
    PodIPPoolSelector selects CiliumPodIPPools based on labels. The virtual
    router will announce allocated CIDRs of matching CiliumPodIPPools.
    
    If empty / nil no CiliumPodIPPools will be announced.
    """
    service_advertisements: list[str]
    """
    ServiceAdvertisements selects a group of BGP Advertisement(s) to advertise
    for the selected services.
    """
    service_selector: meta.LabelSelector
    """
    ServiceSelector selects a group of load balancer services which this
    virtual router will announce. The loadBalancerClass for a service must
    be nil or specify a class supported by Cilium, e.g. "io.cilium/bgp-control-plane".
    Refer to the following document for additional details regarding load balancer
    classes:
    
      https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class
    
    If empty / nil no services will be announced.
    """

    def __init__(
        self,
        export_pod_cidr: bool = None,
        local_asn: int = None,
        neighbors: list[Neighbor] = None,
        pod_ip_pool_selector: meta.LabelSelector = None,
        service_advertisements: list[str] = None,
        service_selector: meta.LabelSelector = None,
    ):
        super().__init__(
            export_pod_cidr=export_pod_cidr,
            local_asn=local_asn,
            neighbors=neighbors,
            pod_ip_pool_selector=pod_ip_pool_selector,
            service_advertisements=service_advertisements,
            service_selector=service_selector,
        )


class CiliumBGPPeeringPolicySpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["virtual_routers"]

    node_selector: meta.LabelSelector
    """
    NodeSelector selects a group of nodes where this BGP Peering
    Policy applies.
    
    If empty / nil this policy applies to all nodes.
    """
    virtual_routers: list[VirtualRouter]
    """
    A list of CiliumBGPVirtualRouter(s) which instructs
    the BGP control plane how to instantiate virtual BGP routers.
    """

    def __init__(self, node_selector: meta.LabelSelector = None, virtual_routers: list[VirtualRouter] = None):
        super().__init__(node_selector=node_selector, virtual_routers=virtual_routers)


class CiliumBGPPeeringPolicy(KubernetesApiResource):
    """
    CiliumBGPPeeringPolicy is a Kubernetes third-party resource for instructing
    Cilium's BGP control plane to create virtual BGP routers.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumBGPPeeringPolicy"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumBGPPeeringPolicySpec
    """ Spec is a human readable description of a BGP peering policy """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumBGPPeeringPolicySpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumCIDRGroupSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["external_cidrs"]

    _field_names_ = {
        "external_cidrs": "externalCIDRs",
    }
    _revfield_names_ = {
        "externalCIDRs": "external_cidrs",
    }

    external_cidrs: list[CIDR]
    """ ExternalCIDRs is a list of CIDRs selecting peers outside the clusters. """

    def __init__(self, external_cidrs: list[CIDR] = None):
        super().__init__(external_cidrs=external_cidrs)


class CiliumCIDRGroup(KubernetesApiResource):
    """
    CiliumCIDRGroup is a list of external CIDRs (i.e: CIDRs selecting peers
    outside the clusters) that can be referenced as a single entity from
    CiliumNetworkPolicies.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumCIDRGroup"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CiliumCIDRGroupSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumCIDRGroupSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class Service(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    listener: str
    """
    Listener specifies the name of the Envoy listener the service traffic is redirected to. The listener must be specified in the Envoy 'resources' of the same CiliumEnvoyConfig. 
     If omitted, the first listener specified in 'resources' is used.
    """
    name: str
    """ Name is the name of a destination Kubernetes service that identifies traffic to be redirected. """
    namespace: str
    """ Namespace is the Kubernetes service namespace. In CiliumEnvoyConfig namespace this is overridden to the namespace of the CEC, In CiliumClusterwideEnvoyConfig namespace defaults to "default". """
    ports: list[int]
    """ Ports is a set of service's frontend ports that should be redirected to the Envoy listener. By default all frontend ports of the service are redirected. """

    def __init__(self, listener: str = None, name: str = None, namespace: str = None, ports: list[int] = None):
        super().__init__(listener=listener, name=name, namespace=namespace, ports=ports)


class CiliumClusterwideEnvoyConfigSpec(KubernetesObject):
    __slots__ = ()

    backend_services: list[BackendService]
    """ BackendServices specifies Kubernetes services whose backends are automatically synced to Envoy using EDS.  Traffic for these services is not forwarded to an Envoy listener. This allows an Envoy listener load balance traffic to these backends while normal Cilium service load balancing takes care of balancing traffic for these services at the same time. """
    node_selector: meta.LabelSelector
    """ NodeSelector is a label selector that determines to which nodes this configuration applies. If nil, then this config applies to all nodes. """
    resources: list[dict[str, t.Any]]
    """ Envoy xDS resources, a list of the following Envoy resource types: type.googleapis.com/envoy.config.listener.v3.Listener, type.googleapis.com/envoy.config.route.v3.RouteConfiguration, type.googleapis.com/envoy.config.cluster.v3.Cluster, type.googleapis.com/envoy.config.endpoint.v3.ClusterLoadAssignment, and type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.Secret. """
    services: list[Service]
    """ Services specifies Kubernetes services for which traffic is forwarded to an Envoy listener for L7 load balancing. Backends of these services are automatically synced to Envoy usign EDS. """

    def __init__(
        self,
        backend_services: list[BackendService] = None,
        node_selector: meta.LabelSelector = None,
        resources: list[dict[str, t.Any]] = None,
        services: list[Service] = None,
    ):
        super().__init__(backend_services=backend_services, node_selector=node_selector, resources=resources, services=services)


class CiliumClusterwideEnvoyConfig(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumClusterwideEnvoyConfig"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumClusterwideEnvoyConfigSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumClusterwideEnvoyConfigSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class Field(KubernetesObject):
    __slots__ = ()

    _required_ = ["type"]

    family: str
    """
    Family is a IP address version.
    Currently, we support `IPv4` and `IPv6`.
    `IPv4` is set as default.
    """
    type: core.IntOrString
    """
    Type is a ICMP-type.
    It should be an 8bit code (0-255), or it's CamelCase name (for example, "EchoReply").
    Allowed ICMP types are:
        Ipv4: EchoReply | DestinationUnreachable | Redirect | Echo | EchoRequest |
    		     RouterAdvertisement | RouterSelection | TimeExceeded | ParameterProblem |
    			 Timestamp | TimestampReply | Photuris | ExtendedEcho Request | ExtendedEcho Reply
        Ipv6: DestinationUnreachable | PacketTooBig | TimeExceeded | ParameterProblem |
    			 EchoRequest | EchoReply | MulticastListenerQuery| MulticastListenerReport |
    			 MulticastListenerDone | RouterSolicitation | RouterAdvertisement | NeighborSolicitation |
    			 NeighborAdvertisement | RedirectMessage | RouterRenumbering | ICMPNodeInformationQuery |
    			 ICMPNodeInformationResponse | InverseNeighborDiscoverySolicitation | InverseNeighborDiscoveryAdvertisement |
    			 HomeAgentAddressDiscoveryRequest | HomeAgentAddressDiscoveryReply | MobilePrefixSolicitation |
    			 MobilePrefixAdvertisement | DuplicateAddressRequestCodeSuffix | DuplicateAddressConfirmationCodeSuffix |
    			 ExtendedEchoRequest | ExtendedEchoReply
    """

    def __init__(self, family: str = None, type: core.IntOrString = None):
        super().__init__(family=family, type=type)


class Icmp(KubernetesObject):
    __slots__ = ()

    fields: list[Field]
    """ Fields is a list of ICMP fields. """

    def __init__(self, fields: list[Field] = None):
        super().__init__(fields=fields)


class ToCIDRSet(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "except": "except_",
    }

    cidr: CIDR
    """ CIDR is a CIDR prefix / IP Block. """
    cidr_group_ref: str
    """
    CIDRGroupRef is a reference to a CiliumCIDRGroup object.
    A CiliumCIDRGroup contains a list of CIDRs that the endpoint, subject to
    the rule, can (Ingress/Egress) or cannot (IngressDeny/EgressDeny) receive
    connections from.
    """
    cidr_group_selector: meta.LabelSelector
    """
    CIDRGroupSelector selects CiliumCIDRGroups by their labels,
    rather than by name.
    """
    except_: list[CIDR]
    """
    ExceptCIDRs is a list of IP blocks which the endpoint subject to the rule
    is not allowed to initiate connections to. These CIDR prefixes should be
    contained within Cidr, using ExceptCIDRs together with CIDRGroupRef is not
    supported yet.
    These exceptions are only applied to the Cidr in this CIDRRule, and do not
    apply to any other CIDR prefixes in any other CIDRRules.
    """

    def __init__(
        self, cidr: CIDR = None, cidr_group_ref: str = None, cidr_group_selector: meta.LabelSelector = None, except_: list[CIDR] = None
    ):
        super().__init__(cidr=cidr, cidr_group_ref=cidr_group_ref, cidr_group_selector=cidr_group_selector, except_=except_)


class ToFQDN(KubernetesObject):
    __slots__ = ()

    match_name: str
    """
    MatchName matches literal DNS names. A trailing "." is automatically added
    when missing.
    """
    match_pattern: str
    """
    MatchPattern allows using wildcards to match DNS names. All wildcards are
    case insensitive. The wildcards are:
    - "*" matches 0 or more DNS valid characters, and may occur anywhere in
    the pattern. As a special case a "*" as the leftmost character, without a
    following "." matches all subdomains as well as the name to the right.
    A trailing "." is automatically added when missing.
    
    Examples:
    `*.cilium.io` matches subomains of cilium at that level
      www.cilium.io and blog.cilium.io match, cilium.io and google.com do not
    `*cilium.io` matches cilium.io and all subdomains ends with "cilium.io"
      except those containing "." separator, subcilium.io and sub-cilium.io match,
      www.cilium.io and blog.cilium.io does not
    sub*.cilium.io matches subdomains of cilium where the subdomain component
    begins with "sub"
      sub.cilium.io and subdomain.cilium.io match, www.cilium.io,
      blog.cilium.io, cilium.io and google.com do not
    """

    def __init__(self, match_name: str = None, match_pattern: str = None):
        super().__init__(match_name=match_name, match_pattern=match_pattern)


class ToGroup(KubernetesObject):
    __slots__ = ()

    aws: AWS
    """ AWSGroup is an structure that can be used to whitelisting information from AWS integration """

    def __init__(self, aws: AWS = None):
        super().__init__(aws=aws)


class EnvoyConfig(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    kind: str
    """
    Kind is the resource type being referred to. Defaults to CiliumEnvoyConfig or
    CiliumClusterwideEnvoyConfig for CiliumNetworkPolicy and CiliumClusterwideNetworkPolicy,
    respectively. The only case this is currently explicitly needed is when referring to a
    CiliumClusterwideEnvoyConfig from CiliumNetworkPolicy, as using a namespaced listener
    from a cluster scoped policy is not allowed.
    """
    name: str
    """
    Name is the resource name of the CiliumEnvoyConfig or CiliumClusterwideEnvoyConfig where
    the listener is defined in.
    """

    def __init__(self, kind: str = None, name: str = None):
        super().__init__(kind=kind, name=name)


class Listener(KubernetesObject):
    __slots__ = ()

    _required_ = ["envoy_config", "name"]

    envoy_config: EnvoyConfig
    """
    EnvoyConfig is a reference to the CEC or CCEC resource in which
    the listener is defined.
    """
    name: str
    """ Name is the name of the listener. """
    priority: int
    """
    Priority for this Listener that is used when multiple rules would apply different
    listeners to a policy map entry. Behavior of this is implementation dependent.
    """

    def __init__(self, envoy_config: EnvoyConfig = None, name: str = None, priority: int = None):
        super().__init__(envoy_config=envoy_config, name=name, priority=priority)


class OriginatingTLS(KubernetesObject):
    __slots__ = ()

    _required_ = ["secret"]

    _field_names_ = {
        "trusted_ca": "trustedCA",
    }
    _revfield_names_ = {
        "trustedCA": "trusted_ca",
    }

    certificate: str
    """
    Certificate is the file name or k8s secret item name for the certificate
    chain. If omitted, 'tls.crt' is assumed, if it exists. If given, the
    item must exist.
    """
    private_key: str
    """
    PrivateKey is the file name or k8s secret item name for the private key
    matching the certificate chain. If omitted, 'tls.key' is assumed, if it
    exists. If given, the item must exist.
    """
    secret: core.SecretReference
    """
    Secret is the secret that contains the certificates and private key for
    the TLS context.
    By default, Cilium will search in this secret for the following items:
     - 'ca.crt'  - Which represents the trusted CA to verify remote source.
     - 'tls.crt' - Which represents the public key certificate.
     - 'tls.key' - Which represents the private key matching the public key
                   certificate.
    """
    trusted_ca: str
    """
    TrustedCA is the file name or k8s secret item name for the trusted CA.
    If omitted, 'ca.crt' is assumed, if it exists. If given, the item must
    exist.
    """

    def __init__(self, certificate: str = None, private_key: str = None, secret: core.SecretReference = None, trusted_ca: str = None):
        super().__init__(certificate=certificate, private_key=private_key, secret=secret, trusted_ca=trusted_ca)


class Port(KubernetesObject):
    __slots__ = ()

    _required_ = ["port"]

    end_port: int
    """ EndPort can only be an L4 port number. """
    port: str
    """
    Port can be an L4 port number, or a name in the form of "http"
    or "http-8080".
    """
    protocol: str
    """
    Protocol is the L4 protocol. If omitted or empty, any protocol
    matches. Accepted values: "TCP", "UDP", "SCTP", "ANY"
    
    Matching on ICMP is not supported.
    
    Named port specified for a container may narrow this down, but may not
    contradict this.
    """

    def __init__(self, end_port: int = None, port: str = None, protocol: str = None):
        super().__init__(end_port=end_port, port=port, protocol=protocol)


class DNS(KubernetesObject):
    __slots__ = ()

    match_name: str
    """
    MatchName matches literal DNS names. A trailing "." is automatically added
    when missing.
    """
    match_pattern: str
    """
    MatchPattern allows using wildcards to match DNS names. All wildcards are
    case insensitive. The wildcards are:
    - "*" matches 0 or more DNS valid characters, and may occur anywhere in
    the pattern. As a special case a "*" as the leftmost character, without a
    following "." matches all subdomains as well as the name to the right.
    A trailing "." is automatically added when missing.
    
    Examples:
    `*.cilium.io` matches subomains of cilium at that level
      www.cilium.io and blog.cilium.io match, cilium.io and google.com do not
    `*cilium.io` matches cilium.io and all subdomains ends with "cilium.io"
      except those containing "." separator, subcilium.io and sub-cilium.io match,
      www.cilium.io and blog.cilium.io does not
    sub*.cilium.io matches subdomains of cilium where the subdomain component
    begins with "sub"
      sub.cilium.io and subdomain.cilium.io match, www.cilium.io,
      blog.cilium.io, cilium.io and google.com do not
    """

    def __init__(self, match_name: str = None, match_pattern: str = None):
        super().__init__(match_name=match_name, match_pattern=match_pattern)


class HeaderMatche(KubernetesObject):
    __slots__ = ()

    _required_ = ["name"]

    mismatch: str
    """
    Mismatch identifies what to do in case there is no match. The default is
    to drop the request. Otherwise the overall rule is still considered as
    matching, but the mismatches are logged in the access log.
    """
    name: str
    """ Name identifies the header. """
    secret: core.SecretReference
    """
    Secret refers to a secret that contains the value to be matched against.
    The secret must only contain one entry. If the referred secret does not
    exist, and there is no "Value" specified, the match will fail.
    """
    value: str
    """
    Value matches the exact value of the header. Can be specified either
    alone or together with "Secret"; will be used as the header value if the
    secret can not be found in the latter case.
    """

    def __init__(self, mismatch: str = None, name: str = None, secret: core.SecretReference = None, value: str = None):
        super().__init__(mismatch=mismatch, name=name, secret=secret, value=value)


IDNHostname: t.TypeAlias = str


class Http(KubernetesObject):
    __slots__ = ()

    header_matches: list[HeaderMatche]
    """
    HeaderMatches is a list of HTTP headers which must be
    present and match against the given values. Mismatch field can be used
    to specify what to do when there is no match.
    """
    headers: list[str]
    """
    Headers is a list of HTTP headers which must be present in the
    request. If omitted or empty, requests are allowed regardless of
    headers present.
    """
    host: IDNHostname
    """
    Host is an extended POSIX regex matched against the host header of a
    request. Examples:
    
    - foo.bar.com will match the host fooXbar.com or foo-bar.com
    - foo\\.bar\\.com will only match the host foo.bar.com
    
    If omitted or empty, the value of the host header is ignored.
    """
    method: str
    """
    Method is an extended POSIX regex matched against the method of a
    request, e.g. "GET", "POST", "PUT", "PATCH", "DELETE", ...
    
    If omitted or empty, all methods are allowed.
    """
    path: str
    """
    Path is an extended POSIX regex matched against the path of a
    request. Currently it can contain characters disallowed from the
    conventional "path" part of a URL as defined by RFC 3986.
    
    If omitted or empty, all paths are all allowed.
    """

    def __init__(
        self,
        header_matches: list[HeaderMatche] = None,
        headers: list[str] = None,
        host: IDNHostname = None,
        method: str = None,
        path: str = None,
    ):
        super().__init__(header_matches=header_matches, headers=headers, host=host, method=method, path=path)


class Kafka(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "client_id": "clientID",
    }
    _revfield_names_ = {
        "clientID": "client_id",
    }

    api_key: str
    """
    APIKey is a case-insensitive string matched against the key of a
    request, e.g. "produce", "fetch", "createtopic", "deletetopic", et al
    Reference: https://kafka.apache.org/protocol#protocol_api_keys
    
    If omitted or empty, and if Role is not specified, then all keys are allowed.
    """
    api_version: str
    """
    APIVersion is the version matched against the api version of the
    Kafka message. If set, it has to be a string representing a positive
    integer.
    
    If omitted or empty, all versions are allowed.
    """
    client_id: str
    """
    ClientID is the client identifier as provided in the request.
    
    From Kafka protocol documentation:
    This is a user supplied identifier for the client application. The
    user can use any identifier they like and it will be used when
    logging errors, monitoring aggregates, etc. For example, one might
    want to monitor not just the requests per second overall, but the
    number coming from each client application (each of which could
    reside on multiple servers). This id acts as a logical grouping
    across all requests from a particular client.
    
    If omitted or empty, all client identifiers are allowed.
    """
    role: str
    """
    Role is a case-insensitive string and describes a group of API keys
    necessary to perform certain higher-level Kafka operations such as "produce"
    or "consume". A Role automatically expands into all APIKeys required
    to perform the specified higher-level operation.
    
    The following values are supported:
     - "produce": Allow producing to the topics specified in the rule
     - "consume": Allow consuming from the topics specified in the rule
    
    This field is incompatible with the APIKey field, i.e APIKey and Role
    cannot both be specified in the same rule.
    
    If omitted or empty, and if APIKey is not specified, then all keys are
    allowed.
    """
    topic: str
    """
    Topic is the topic name contained in the message. If a Kafka request
    contains multiple topics, then all topics must be allowed or the
    message will be rejected.
    
    This constraint is ignored if the matched request message type
    doesn't contain any topic. Maximum size of Topic can be 249
    characters as per recent Kafka spec and allowed characters are
    a-z, A-Z, 0-9, -, . and _.
    
    Older Kafka versions had longer topic lengths of 255, but in Kafka 0.10
    version the length was changed from 255 to 249. For compatibility
    reasons we are using 255.
    
    If omitted or empty, all topics are allowed.
    """

    def __init__(self, api_key: str = None, api_version: str = None, client_id: str = None, role: str = None, topic: str = None):
        super().__init__(api_key=api_key, api_version=api_version, client_id=client_id, role=role, topic=topic)


class Rules(KubernetesObject):
    __slots__ = ()

    dns: list[DNS]
    """ DNS-specific rules. """
    http: list[Http]
    """ HTTP specific rules. """
    kafka: list[Kafka]
    """ Kafka-specific rules. """
    l7: list[dict[str, str]]
    """ Key-value pair rules. """
    l7proto: str
    """ Name of the L7 protocol for which the Key-value pair rules apply. """

    def __init__(
        self,
        dns: list[DNS] = None,
        http: list[Http] = None,
        kafka: list[Kafka] = None,
        l7: list[dict[str, str]] = None,
        l7proto: str = None,
    ):
        super().__init__(dns=dns, http=http, kafka=kafka, l7=l7, l7proto=l7proto)


class TerminatingTLS(KubernetesObject):
    __slots__ = ()

    _required_ = ["secret"]

    _field_names_ = {
        "trusted_ca": "trustedCA",
    }
    _revfield_names_ = {
        "trustedCA": "trusted_ca",
    }

    certificate: str
    """
    Certificate is the file name or k8s secret item name for the certificate
    chain. If omitted, 'tls.crt' is assumed, if it exists. If given, the
    item must exist.
    """
    private_key: str
    """
    PrivateKey is the file name or k8s secret item name for the private key
    matching the certificate chain. If omitted, 'tls.key' is assumed, if it
    exists. If given, the item must exist.
    """
    secret: core.SecretReference
    """
    Secret is the secret that contains the certificates and private key for
    the TLS context.
    By default, Cilium will search in this secret for the following items:
     - 'ca.crt'  - Which represents the trusted CA to verify remote source.
     - 'tls.crt' - Which represents the public key certificate.
     - 'tls.key' - Which represents the private key matching the public key
                   certificate.
    """
    trusted_ca: str
    """
    TrustedCA is the file name or k8s secret item name for the trusted CA.
    If omitted, 'ca.crt' is assumed, if it exists. If given, the item must
    exist.
    """

    def __init__(self, certificate: str = None, private_key: str = None, secret: core.SecretReference = None, trusted_ca: str = None):
        super().__init__(certificate=certificate, private_key=private_key, secret=secret, trusted_ca=trusted_ca)


class ToPort2(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "originating_tls": "originatingTLS",
        "terminating_tls": "terminatingTLS",
    }
    _revfield_names_ = {
        "originatingTLS": "originating_tls",
        "terminatingTLS": "terminating_tls",
    }

    listener: Listener
    """
    listener specifies the name of a custom Envoy listener to which this traffic should be
    redirected to.
    """
    originating_tls: OriginatingTLS
    """
    OriginatingTLS is the TLS context for the connections originated by
    the L7 proxy.  For egress policy this specifies the client-side TLS
    parameters for the upstream connection originating from the L7 proxy
    to the remote destination. For ingress policy this specifies the
    client-side TLS parameters for the connection from the L7 proxy to
    the local endpoint.
    """
    ports: list[Port]
    """ Ports is a list of L4 port/protocol """
    rules: Rules
    """
    Rules is a list of additional port level rules which must be met in
    order for the PortRule to allow the traffic. If omitted or empty,
    no layer 7 rules are enforced.
    """
    server_names: list[str]
    """
    ServerNames is a list of allowed TLS SNI values. If not empty, then
    TLS must be present and one of the provided SNIs must be indicated in the
    TLS handshake.
    """
    terminating_tls: TerminatingTLS
    """
    TerminatingTLS is the TLS context for the connection terminated by
    the L7 proxy.  For egress policy this specifies the server-side TLS
    parameters to be applied on the connections originated from the local
    endpoint and terminated by the L7 proxy. For ingress policy this specifies
    the server-side TLS parameters to be applied on the connections
    originated from a remote source and terminated by the L7 proxy.
    """

    def __init__(
        self,
        listener: Listener = None,
        originating_tls: OriginatingTLS = None,
        ports: list[Port] = None,
        rules: Rules = None,
        server_names: list[str] = None,
        terminating_tls: TerminatingTLS = None,
    ):
        super().__init__(
            listener=listener,
            originating_tls=originating_tls,
            ports=ports,
            rules=rules,
            server_names=server_names,
            terminating_tls=terminating_tls,
        )


class K8sService(KubernetesObject):
    __slots__ = ()

    namespace: str
    service_name: str

    def __init__(self, namespace: str = None, service_name: str = None):
        super().__init__(namespace=namespace, service_name=service_name)


class K8sServiceSelector(KubernetesObject):
    __slots__ = ()

    _required_ = ["selector"]

    namespace: str
    selector: meta.LabelSelector
    """ ServiceSelector is a label selector for k8s services """

    def __init__(self, namespace: str = None, selector: meta.LabelSelector = None):
        super().__init__(namespace=namespace, selector=selector)


class ToService(KubernetesObject):
    __slots__ = ()

    k8s_service: K8sService
    """ K8sService selects service by name and namespace pair """
    k8s_service_selector: K8sServiceSelector
    """ K8sServiceSelector selects services by k8s labels and namespace """

    def __init__(self, k8s_service: K8sService = None, k8s_service_selector: K8sServiceSelector = None):
        super().__init__(k8s_service=k8s_service, k8s_service_selector=k8s_service_selector)


class Egress(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "to_cidr": "toCIDR",
        "to_cidr_set": "toCIDRSet",
        "to_fqdns": "toFQDNs",
    }
    _revfield_names_ = {
        "toCIDR": "to_cidr",
        "toCIDRSet": "to_cidr_set",
        "toFQDNs": "to_fqdns",
    }

    authentication: Authentication
    """ Authentication is the required authentication type for the allowed traffic, if any. """
    icmps: list[Icmp]
    """
    ICMPs is a list of ICMP rule identified by type number
    which the endpoint subject to the rule is allowed to connect to.
    
    Example:
    Any endpoint with the label "app=httpd" is allowed to initiate
    type 8 ICMP connections.
    """
    to_cidr: list[CIDR]
    """
    ToCIDR is a list of IP blocks which the endpoint subject to the rule
    is allowed to initiate connections. Only connections destined for
    outside of the cluster and not targeting the host will be subject
    to CIDR rules.  This will match on the destination IP address of
    outgoing connections. Adding a prefix into ToCIDR or into ToCIDRSet
    with no ExcludeCIDRs is equivalent. Overlaps are allowed between
    ToCIDR and ToCIDRSet.
    
    Example:
    Any endpoint with the label "app=database-proxy" is allowed to
    initiate connections to 10.2.3.0/24
    """
    to_cidr_set: list[ToCIDRSet]
    """
    ToCIDRSet is a list of IP blocks which the endpoint subject to the rule
    is allowed to initiate connections to in addition to connections
    which are allowed via ToEndpoints, along with a list of subnets contained
    within their corresponding IP block to which traffic should not be
    allowed. This will match on the destination IP address of outgoing
    connections. Adding a prefix into ToCIDR or into ToCIDRSet with no
    ExcludeCIDRs is equivalent. Overlaps are allowed between ToCIDR and
    ToCIDRSet.
    
    Example:
    Any endpoint with the label "app=database-proxy" is allowed to
    initiate connections to 10.2.3.0/24 except from IPs in subnet 10.2.3.0/28.
    """
    to_endpoints: list[meta.LabelSelector]
    """
    ToEndpoints is a list of endpoints identified by an EndpointSelector to
    which the endpoints subject to the rule are allowed to communicate.
    
    Example:
    Any endpoint with the label "role=frontend" can communicate with any
    endpoint carrying the label "role=backend".
    """
    to_entities: list[str]
    """
    ToEntities is a list of special entities to which the endpoint subject
    to the rule is allowed to initiate connections. Supported entities are
    `world`, `cluster`,`host`,`remote-node`,`kube-apiserver`, `init`,
    `health`,`unmanaged` and `all`.
    """
    to_fqdns: list[ToFQDN]
    """
    ToFQDN allows whitelisting DNS names in place of IPs. The IPs that result
    from DNS resolution of `ToFQDN.MatchName`s are added to the same
    EgressRule object as ToCIDRSet entries, and behave accordingly. Any L4 and
    L7 rules within this EgressRule will also apply to these IPs.
    The DNS -> IP mapping is re-resolved periodically from within the
    cilium-agent, and the IPs in the DNS response are effected in the policy
    for selected pods as-is (i.e. the list of IPs is not modified in any way).
    Note: An explicit rule to allow for DNS traffic is needed for the pods, as
    ToFQDN counts as an egress rule and will enforce egress policy when
    PolicyEnforcment=default.
    Note: If the resolved IPs are IPs within the kubernetes cluster, the
    ToFQDN rule will not apply to that IP.
    Note: ToFQDN cannot occur in the same policy as other To* rules.
    """
    to_groups: list[ToGroup]
    """
    ToGroups is a directive that allows the integration with multiple outside
    providers. Currently, only AWS is supported, and the rule can select by
    multiple sub directives:
    
    Example:
    toGroups:
    - aws:
        securityGroupsIds:
        - 'sg-XXXXXXXXXXXXX'
    """
    to_nodes: list[meta.LabelSelector]
    """
    ToNodes is a list of nodes identified by an
    EndpointSelector to which endpoints subject to the rule is allowed to communicate.
    """
    to_ports: list[ToPort2]
    """
    ToPorts is a list of destination ports identified by port number and
    protocol which the endpoint subject to the rule is allowed to
    connect to.
    
    Example:
    Any endpoint with the label "role=frontend" is allowed to initiate
    connections to destination port 8080/tcp
    """
    to_requires: list[meta.LabelSelector]
    """
    ToRequires is a list of additional constraints which must be met
    in order for the selected endpoints to be able to connect to other
    endpoints. These additional constraints do no by itself grant access
    privileges and must always be accompanied with at least one matching
    ToEndpoints.
    
    Example:
    Any Endpoint with the label "team=A" requires any endpoint to which it
    communicates to also carry the label "team=A".
    """
    to_services: list[ToService]
    """
    ToServices is a list of services to which the endpoint subject
    to the rule is allowed to initiate connections.
    Currently Cilium only supports toServices for K8s services.
    """

    def __init__(
        self,
        authentication: Authentication = None,
        icmps: list[Icmp] = None,
        to_cidr: list[CIDR] = None,
        to_cidr_set: list[ToCIDRSet] = None,
        to_endpoints: list[meta.LabelSelector] = None,
        to_entities: list[str] = None,
        to_fqdns: list[ToFQDN] = None,
        to_groups: list[ToGroup] = None,
        to_nodes: list[meta.LabelSelector] = None,
        to_ports: list[ToPort2] = None,
        to_requires: list[meta.LabelSelector] = None,
        to_services: list[ToService] = None,
    ):
        super().__init__(
            authentication=authentication,
            icmps=icmps,
            to_cidr=to_cidr,
            to_cidr_set=to_cidr_set,
            to_endpoints=to_endpoints,
            to_entities=to_entities,
            to_fqdns=to_fqdns,
            to_groups=to_groups,
            to_nodes=to_nodes,
            to_ports=to_ports,
            to_requires=to_requires,
            to_services=to_services,
        )


class ToPort(KubernetesObject):
    __slots__ = ()

    ports: list[Port]
    """ Ports is a list of L4 port/protocol """

    def __init__(self, ports: list[Port] = None):
        super().__init__(ports=ports)


class EgressDeny(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "to_cidr": "toCIDR",
        "to_cidr_set": "toCIDRSet",
    }
    _revfield_names_ = {
        "toCIDR": "to_cidr",
        "toCIDRSet": "to_cidr_set",
    }

    icmps: list[Icmp]
    """
    ICMPs is a list of ICMP rule identified by type number
    which the endpoint subject to the rule is not allowed to connect to.
    
    Example:
    Any endpoint with the label "app=httpd" is not allowed to initiate
    type 8 ICMP connections.
    """
    to_cidr: list[CIDR]
    """
    ToCIDR is a list of IP blocks which the endpoint subject to the rule
    is allowed to initiate connections. Only connections destined for
    outside of the cluster and not targeting the host will be subject
    to CIDR rules.  This will match on the destination IP address of
    outgoing connections. Adding a prefix into ToCIDR or into ToCIDRSet
    with no ExcludeCIDRs is equivalent. Overlaps are allowed between
    ToCIDR and ToCIDRSet.
    
    Example:
    Any endpoint with the label "app=database-proxy" is allowed to
    initiate connections to 10.2.3.0/24
    """
    to_cidr_set: list[ToCIDRSet]
    """
    ToCIDRSet is a list of IP blocks which the endpoint subject to the rule
    is allowed to initiate connections to in addition to connections
    which are allowed via ToEndpoints, along with a list of subnets contained
    within their corresponding IP block to which traffic should not be
    allowed. This will match on the destination IP address of outgoing
    connections. Adding a prefix into ToCIDR or into ToCIDRSet with no
    ExcludeCIDRs is equivalent. Overlaps are allowed between ToCIDR and
    ToCIDRSet.
    
    Example:
    Any endpoint with the label "app=database-proxy" is allowed to
    initiate connections to 10.2.3.0/24 except from IPs in subnet 10.2.3.0/28.
    """
    to_endpoints: list[meta.LabelSelector]
    """
    ToEndpoints is a list of endpoints identified by an EndpointSelector to
    which the endpoints subject to the rule are allowed to communicate.
    
    Example:
    Any endpoint with the label "role=frontend" can communicate with any
    endpoint carrying the label "role=backend".
    """
    to_entities: list[str]
    """
    ToEntities is a list of special entities to which the endpoint subject
    to the rule is allowed to initiate connections. Supported entities are
    `world`, `cluster`,`host`,`remote-node`,`kube-apiserver`, `init`,
    `health`,`unmanaged` and `all`.
    """
    to_groups: list[ToGroup]
    """
    ToGroups is a directive that allows the integration with multiple outside
    providers. Currently, only AWS is supported, and the rule can select by
    multiple sub directives:
    
    Example:
    toGroups:
    - aws:
        securityGroupsIds:
        - 'sg-XXXXXXXXXXXXX'
    """
    to_nodes: list[meta.LabelSelector]
    """
    ToNodes is a list of nodes identified by an
    EndpointSelector to which endpoints subject to the rule is allowed to communicate.
    """
    to_ports: list[ToPort]
    """
    ToPorts is a list of destination ports identified by port number and
    protocol which the endpoint subject to the rule is not allowed to connect
    to.
    
    Example:
    Any endpoint with the label "role=frontend" is not allowed to initiate
    connections to destination port 8080/tcp
    """
    to_requires: list[meta.LabelSelector]
    """
    ToRequires is a list of additional constraints which must be met
    in order for the selected endpoints to be able to connect to other
    endpoints. These additional constraints do no by itself grant access
    privileges and must always be accompanied with at least one matching
    ToEndpoints.
    
    Example:
    Any Endpoint with the label "team=A" requires any endpoint to which it
    communicates to also carry the label "team=A".
    """
    to_services: list[ToService]
    """
    ToServices is a list of services to which the endpoint subject
    to the rule is allowed to initiate connections.
    Currently Cilium only supports toServices for K8s services.
    """

    def __init__(
        self,
        icmps: list[Icmp] = None,
        to_cidr: list[CIDR] = None,
        to_cidr_set: list[ToCIDRSet] = None,
        to_endpoints: list[meta.LabelSelector] = None,
        to_entities: list[str] = None,
        to_groups: list[ToGroup] = None,
        to_nodes: list[meta.LabelSelector] = None,
        to_ports: list[ToPort] = None,
        to_requires: list[meta.LabelSelector] = None,
        to_services: list[ToService] = None,
    ):
        super().__init__(
            icmps=icmps,
            to_cidr=to_cidr,
            to_cidr_set=to_cidr_set,
            to_endpoints=to_endpoints,
            to_entities=to_entities,
            to_groups=to_groups,
            to_nodes=to_nodes,
            to_ports=to_ports,
            to_requires=to_requires,
            to_services=to_services,
        )


class EnableDefaultDeny(KubernetesObject):
    __slots__ = ()

    egress: bool
    """
    Whether or not the endpoint should have a default-deny rule applied
    to egress traffic.
    """
    ingress: bool
    """
    Whether or not the endpoint should have a default-deny rule applied
    to ingress traffic.
    """

    def __init__(self, egress: bool = None, ingress: bool = None):
        super().__init__(egress=egress, ingress=ingress)


class FromCIDRSet(KubernetesObject):
    __slots__ = ()

    _revfield_names_ = {
        "except": "except_",
    }

    cidr: CIDR
    """ CIDR is a CIDR prefix / IP Block. """
    cidr_group_ref: str
    """
    CIDRGroupRef is a reference to a CiliumCIDRGroup object.
    A CiliumCIDRGroup contains a list of CIDRs that the endpoint, subject to
    the rule, can (Ingress/Egress) or cannot (IngressDeny/EgressDeny) receive
    connections from.
    """
    cidr_group_selector: meta.LabelSelector
    """
    CIDRGroupSelector selects CiliumCIDRGroups by their labels,
    rather than by name.
    """
    except_: list[CIDR]
    """
    ExceptCIDRs is a list of IP blocks which the endpoint subject to the rule
    is not allowed to initiate connections to. These CIDR prefixes should be
    contained within Cidr, using ExceptCIDRs together with CIDRGroupRef is not
    supported yet.
    These exceptions are only applied to the Cidr in this CIDRRule, and do not
    apply to any other CIDR prefixes in any other CIDRRules.
    """

    def __init__(
        self, cidr: CIDR = None, cidr_group_ref: str = None, cidr_group_selector: meta.LabelSelector = None, except_: list[CIDR] = None
    ):
        super().__init__(cidr=cidr, cidr_group_ref=cidr_group_ref, cidr_group_selector=cidr_group_selector, except_=except_)


class FromGroup(KubernetesObject):
    __slots__ = ()

    aws: AWS
    """ AWSGroup is an structure that can be used to whitelisting information from AWS integration """

    def __init__(self, aws: AWS = None):
        super().__init__(aws=aws)


class Ingress(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "from_cidr": "fromCIDR",
        "from_cidr_set": "fromCIDRSet",
    }
    _revfield_names_ = {
        "fromCIDR": "from_cidr",
        "fromCIDRSet": "from_cidr_set",
    }

    authentication: Authentication
    """ Authentication is the required authentication type for the allowed traffic, if any. """
    from_cidr: list[CIDR]
    """
    FromCIDR is a list of IP blocks which the endpoint subject to the
    rule is allowed to receive connections from. Only connections which
    do *not* originate from the cluster or from the local host are subject
    to CIDR rules. In order to allow in-cluster connectivity, use the
    FromEndpoints field.  This will match on the source IP address of
    incoming connections. Adding  a prefix into FromCIDR or into
    FromCIDRSet with no ExcludeCIDRs is  equivalent.  Overlaps are
    allowed between FromCIDR and FromCIDRSet.
    
    Example:
    Any endpoint with the label "app=my-legacy-pet" is allowed to receive
    connections from 10.3.9.1
    """
    from_cidr_set: list[FromCIDRSet]
    """
    FromCIDRSet is a list of IP blocks which the endpoint subject to the
    rule is allowed to receive connections from in addition to FromEndpoints,
    along with a list of subnets contained within their corresponding IP block
    from which traffic should not be allowed.
    This will match on the source IP address of incoming connections. Adding
    a prefix into FromCIDR or into FromCIDRSet with no ExcludeCIDRs is
    equivalent. Overlaps are allowed between FromCIDR and FromCIDRSet.
    
    Example:
    Any endpoint with the label "app=my-legacy-pet" is allowed to receive
    connections from 10.0.0.0/8 except from IPs in subnet 10.96.0.0/12.
    """
    from_endpoints: list[meta.LabelSelector]
    """
    FromEndpoints is a list of endpoints identified by an
    EndpointSelector which are allowed to communicate with the endpoint
    subject to the rule.
    
    Example:
    Any endpoint with the label "role=backend" can be consumed by any
    endpoint carrying the label "role=frontend".
    """
    from_entities: list[str]
    """
    FromEntities is a list of special entities which the endpoint subject
    to the rule is allowed to receive connections from. Supported entities are
    `world`, `cluster` and `host`
    """
    from_groups: list[FromGroup]
    """
    FromGroups is a directive that allows the integration with multiple outside
    providers. Currently, only AWS is supported, and the rule can select by
    multiple sub directives:
    
    Example:
    FromGroups:
    - aws:
        securityGroupsIds:
        - 'sg-XXXXXXXXXXXXX'
    """
    from_nodes: list[meta.LabelSelector]
    """
    FromNodes is a list of nodes identified by an
    EndpointSelector which are allowed to communicate with the endpoint
    subject to the rule.
    """
    from_requires: list[meta.LabelSelector]
    """
    FromRequires is a list of additional constraints which must be met
    in order for the selected endpoints to be reachable. These
    additional constraints do no by itself grant access privileges and
    must always be accompanied with at least one matching FromEndpoints.
    
    Example:
    Any Endpoint with the label "team=A" requires consuming endpoint
    to also carry the label "team=A".
    """
    icmps: list[Icmp]
    """
    ICMPs is a list of ICMP rule identified by type number
    which the endpoint subject to the rule is allowed to
    receive connections on.
    
    Example:
    Any endpoint with the label "app=httpd" can only accept incoming
    type 8 ICMP connections.
    """
    to_ports: list[ToPort2]
    """
    ToPorts is a list of destination ports identified by port number and
    protocol which the endpoint subject to the rule is allowed to
    receive connections on.
    
    Example:
    Any endpoint with the label "app=httpd" can only accept incoming
    connections on port 80/tcp.
    """

    def __init__(
        self,
        authentication: Authentication = None,
        from_cidr: list[CIDR] = None,
        from_cidr_set: list[FromCIDRSet] = None,
        from_endpoints: list[meta.LabelSelector] = None,
        from_entities: list[str] = None,
        from_groups: list[FromGroup] = None,
        from_nodes: list[meta.LabelSelector] = None,
        from_requires: list[meta.LabelSelector] = None,
        icmps: list[Icmp] = None,
        to_ports: list[ToPort2] = None,
    ):
        super().__init__(
            authentication=authentication,
            from_cidr=from_cidr,
            from_cidr_set=from_cidr_set,
            from_endpoints=from_endpoints,
            from_entities=from_entities,
            from_groups=from_groups,
            from_nodes=from_nodes,
            from_requires=from_requires,
            icmps=icmps,
            to_ports=to_ports,
        )


class IngressDeny(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "from_cidr": "fromCIDR",
        "from_cidr_set": "fromCIDRSet",
    }
    _revfield_names_ = {
        "fromCIDR": "from_cidr",
        "fromCIDRSet": "from_cidr_set",
    }

    from_cidr: list[CIDR]
    """
    FromCIDR is a list of IP blocks which the endpoint subject to the
    rule is allowed to receive connections from. Only connections which
    do *not* originate from the cluster or from the local host are subject
    to CIDR rules. In order to allow in-cluster connectivity, use the
    FromEndpoints field.  This will match on the source IP address of
    incoming connections. Adding  a prefix into FromCIDR or into
    FromCIDRSet with no ExcludeCIDRs is  equivalent.  Overlaps are
    allowed between FromCIDR and FromCIDRSet.
    
    Example:
    Any endpoint with the label "app=my-legacy-pet" is allowed to receive
    connections from 10.3.9.1
    """
    from_cidr_set: list[FromCIDRSet]
    """
    FromCIDRSet is a list of IP blocks which the endpoint subject to the
    rule is allowed to receive connections from in addition to FromEndpoints,
    along with a list of subnets contained within their corresponding IP block
    from which traffic should not be allowed.
    This will match on the source IP address of incoming connections. Adding
    a prefix into FromCIDR or into FromCIDRSet with no ExcludeCIDRs is
    equivalent. Overlaps are allowed between FromCIDR and FromCIDRSet.
    
    Example:
    Any endpoint with the label "app=my-legacy-pet" is allowed to receive
    connections from 10.0.0.0/8 except from IPs in subnet 10.96.0.0/12.
    """
    from_endpoints: list[meta.LabelSelector]
    """
    FromEndpoints is a list of endpoints identified by an
    EndpointSelector which are allowed to communicate with the endpoint
    subject to the rule.
    
    Example:
    Any endpoint with the label "role=backend" can be consumed by any
    endpoint carrying the label "role=frontend".
    """
    from_entities: list[str]
    """
    FromEntities is a list of special entities which the endpoint subject
    to the rule is allowed to receive connections from. Supported entities are
    `world`, `cluster` and `host`
    """
    from_groups: list[FromGroup]
    """
    FromGroups is a directive that allows the integration with multiple outside
    providers. Currently, only AWS is supported, and the rule can select by
    multiple sub directives:
    
    Example:
    FromGroups:
    - aws:
        securityGroupsIds:
        - 'sg-XXXXXXXXXXXXX'
    """
    from_nodes: list[meta.LabelSelector]
    """
    FromNodes is a list of nodes identified by an
    EndpointSelector which are allowed to communicate with the endpoint
    subject to the rule.
    """
    from_requires: list[meta.LabelSelector]
    """
    FromRequires is a list of additional constraints which must be met
    in order for the selected endpoints to be reachable. These
    additional constraints do no by itself grant access privileges and
    must always be accompanied with at least one matching FromEndpoints.
    
    Example:
    Any Endpoint with the label "team=A" requires consuming endpoint
    to also carry the label "team=A".
    """
    icmps: list[Icmp]
    """
    ICMPs is a list of ICMP rule identified by type number
    which the endpoint subject to the rule is not allowed to
    receive connections on.
    
    Example:
    Any endpoint with the label "app=httpd" can not accept incoming
    type 8 ICMP connections.
    """
    to_ports: list[ToPort]
    """
    ToPorts is a list of destination ports identified by port number and
    protocol which the endpoint subject to the rule is not allowed to
    receive connections on.
    
    Example:
    Any endpoint with the label "app=httpd" can not accept incoming
    connections on port 80/tcp.
    """

    def __init__(
        self,
        from_cidr: list[CIDR] = None,
        from_cidr_set: list[FromCIDRSet] = None,
        from_endpoints: list[meta.LabelSelector] = None,
        from_entities: list[str] = None,
        from_groups: list[FromGroup] = None,
        from_nodes: list[meta.LabelSelector] = None,
        from_requires: list[meta.LabelSelector] = None,
        icmps: list[Icmp] = None,
        to_ports: list[ToPort] = None,
    ):
        super().__init__(
            from_cidr=from_cidr,
            from_cidr_set=from_cidr_set,
            from_endpoints=from_endpoints,
            from_entities=from_entities,
            from_groups=from_groups,
            from_nodes=from_nodes,
            from_requires=from_requires,
            icmps=icmps,
            to_ports=to_ports,
        )


class Label(KubernetesObject):
    __slots__ = ()

    _required_ = ["key"]

    key: str
    source: str
    """ Source can be one of the above values (e.g.: LabelSourceContainer). """
    value: str

    def __init__(self, key: str = None, source: str = None, value: str = None):
        super().__init__(key=key, source=source, value=value)


class CiliumClusterwideNetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    description: str
    """
    Description is a free form string, it can be used by the creator of
    the rule to store human readable explanation of the purpose of this
    rule. Rules cannot be identified by comment.
    """
    egress: list[Egress]
    """
    Egress is a list of EgressRule which are enforced at egress.
    If omitted or empty, this rule does not apply at egress.
    """
    egress_deny: list[EgressDeny]
    """
    EgressDeny is a list of EgressDenyRule which are enforced at egress.
    Any rule inserted here will be denied regardless of the allowed egress
    rules in the 'egress' field.
    If omitted or empty, this rule does not apply at egress.
    """
    enable_default_deny: EnableDefaultDeny
    """
    EnableDefaultDeny determines whether this policy configures the
    subject endpoint(s) to have a default deny mode. If enabled,
    this causes all traffic not explicitly allowed by a network policy
    to be dropped.
    
    If not specified, the default is true for each traffic direction
    that has rules, and false otherwise. For example, if a policy
    only has Ingress or IngressDeny rules, then the default for
    ingress is true and egress is false.
    
    If multiple policies apply to an endpoint, that endpoint's default deny
    will be enabled if any policy requests it.
    
    This is useful for creating broad-based network policies that will not
    cause endpoints to enter default-deny mode.
    """
    endpoint_selector: meta.LabelSelector
    """
    EndpointSelector selects all endpoints which should be subject to
    this rule. EndpointSelector and NodeSelector cannot be both empty and
    are mutually exclusive.
    """
    ingress: list[Ingress]
    """
    Ingress is a list of IngressRule which are enforced at ingress.
    If omitted or empty, this rule does not apply at ingress.
    """
    ingress_deny: list[IngressDeny]
    """
    IngressDeny is a list of IngressDenyRule which are enforced at ingress.
    Any rule inserted here will be denied regardless of the allowed ingress
    rules in the 'ingress' field.
    If omitted or empty, this rule does not apply at ingress.
    """
    labels: list[Label]
    """
    Labels is a list of optional strings which can be used to
    re-identify the rule or to store metadata. It is possible to lookup
    or delete strings based on labels. Labels are not required to be
    unique, multiple rules can have overlapping or identical labels.
    """
    node_selector: meta.LabelSelector
    """
    NodeSelector selects all nodes which should be subject to this rule.
    EndpointSelector and NodeSelector cannot be both empty and are mutually
    exclusive. Can only be used in CiliumClusterwideNetworkPolicies.
    """

    def __init__(
        self,
        description: str = None,
        egress: list[Egress] = None,
        egress_deny: list[EgressDeny] = None,
        enable_default_deny: EnableDefaultDeny = None,
        endpoint_selector: meta.LabelSelector = None,
        ingress: list[Ingress] = None,
        ingress_deny: list[IngressDeny] = None,
        labels: list[Label] = None,
        node_selector: meta.LabelSelector = None,
    ):
        super().__init__(
            description=description,
            egress=egress,
            egress_deny=egress_deny,
            enable_default_deny=enable_default_deny,
            endpoint_selector=endpoint_selector,
            ingress=ingress,
            ingress_deny=ingress_deny,
            labels=labels,
            node_selector=node_selector,
        )


class CiliumClusterwideNetworkPolicy(KubernetesApiResource):
    """
    CiliumClusterwideNetworkPolicy is a Kubernetes third-party resource with an
    modified version of CiliumNetworkPolicy which is cluster scoped rather than
    namespace scoped.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumClusterwideNetworkPolicy"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumClusterwideNetworkPolicySpec
    """ Spec is the desired Cilium specific rule specification. """
    specs: list[CiliumClusterwideNetworkPolicySpec]
    """ Specs is a list of desired Cilium specific rule specification. """

    def __init__(
        self,
        name: str,
        metadata: meta.ObjectMeta = None,
        spec: CiliumClusterwideNetworkPolicySpec = None,
        specs: list[CiliumClusterwideNetworkPolicySpec] = None,
    ):
        super().__init__(name, "", metadata=metadata, spec=spec, specs=specs)


class CiliumEndpoint(KubernetesApiResource):
    """CiliumEndpoint is the status of a Cilium policy rule."""

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumEndpoint"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None):
        super().__init__(name, namespace, metadata=metadata)


class Encryption(KubernetesObject):
    __slots__ = ()

    key: int
    """ Key is the index to the key to use for encryption or 0 if encryption is disabled. """

    def __init__(self, key: int = None):
        super().__init__(key=key)


class NamedPort(KubernetesObject):
    __slots__ = ()

    name: str
    """ Optional layer 4 port name """
    port: int
    """ Layer 4 port number """
    protocol: str
    """ Layer 4 protocol Enum: [TCP UDP SCTP ICMP ICMPV6 ANY] """

    def __init__(self, name: str = None, port: int = None, protocol: str = None):
        super().__init__(name=name, port=port, protocol=protocol)


class Networking(KubernetesObject):
    __slots__ = ()

    _required_ = ["addressing"]

    addressing: list[Addressing]
    """ IP4/6 addresses assigned to this Endpoint """
    node: str
    """ NodeIP is the IP of the node the endpoint is running on. The IP must be reachable between nodes. """

    def __init__(self, addressing: list[Addressing] = None, node: str = None):
        super().__init__(addressing=addressing, node=node)


class Endpoint(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "named_ports": "named-ports",
    }
    _revfield_names_ = {
        "named-ports": "named_ports",
    }

    encryption: Encryption
    """ EncryptionSpec defines the encryption relevant configuration of a node. """
    id: int
    """ IdentityID is the numeric identity of the endpoint """
    name: str
    """ Name indicate as CiliumEndpoint name. """
    named_ports: list[NamedPort]
    """
    NamedPorts List of named Layer 4 port and protocol pairs which will be used in Network Policy specs. 
     swagger:model NamedPorts
    """
    networking: Networking
    """ EndpointNetworking is the addressing information of an endpoint. """

    def __init__(
        self,
        encryption: Encryption = None,
        id: int = None,
        name: str = None,
        named_ports: list[NamedPort] = None,
        networking: Networking = None,
    ):
        super().__init__(encryption=encryption, id=id, name=name, named_ports=named_ports, networking=networking)


class CiliumEndpointSlice(KubernetesApiResource):
    """CiliumEndpointSlice contains a group of CoreCiliumendpoints."""

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumEndpointSlice"
    _scope_ = "cluster"

    _required_ = ["endpoints", "metadata"]

    endpoints: list[Endpoint]
    """ Endpoints is a list of coreCEPs packed in a CiliumEndpointSlice """
    metadata: meta.ObjectMeta
    namespace: str
    """ Namespace indicate as CiliumEndpointSlice namespace. All the CiliumEndpoints within the same namespace are put together in CiliumEndpointSlice. """

    def __init__(self, name: str, endpoints: list[Endpoint] = None, metadata: meta.ObjectMeta = None, namespace: str = None):
        super().__init__(name, "", endpoints=endpoints, metadata=metadata, namespace=namespace)


class CiliumEnvoyConfigSpec(KubernetesObject):
    __slots__ = ()

    backend_services: list[BackendService]
    """ BackendServices specifies Kubernetes services whose backends are automatically synced to Envoy using EDS.  Traffic for these services is not forwarded to an Envoy listener. This allows an Envoy listener load balance traffic to these backends while normal Cilium service load balancing takes care of balancing traffic for these services at the same time. """
    node_selector: meta.LabelSelector
    """ NodeSelector is a label selector that determines to which nodes this configuration applies. If nil, then this config applies to all nodes. """
    resources: list[dict[str, t.Any]]
    """ Envoy xDS resources, a list of the following Envoy resource types: type.googleapis.com/envoy.config.listener.v3.Listener, type.googleapis.com/envoy.config.route.v3.RouteConfiguration, type.googleapis.com/envoy.config.cluster.v3.Cluster, type.googleapis.com/envoy.config.endpoint.v3.ClusterLoadAssignment, and type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.Secret. """
    services: list[Service]
    """ Services specifies Kubernetes services for which traffic is forwarded to an Envoy listener for L7 load balancing. Backends of these services are automatically synced to Envoy usign EDS. """

    def __init__(
        self,
        backend_services: list[BackendService] = None,
        node_selector: meta.LabelSelector = None,
        resources: list[dict[str, t.Any]] = None,
        services: list[Service] = None,
    ):
        super().__init__(backend_services=backend_services, node_selector=node_selector, resources=resources, services=services)


class CiliumEnvoyConfig(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumEnvoyConfig"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumEnvoyConfigSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CiliumEnvoyConfigSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class CiliumExternalWorkloadSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "ipv4_alloc_cidr": "ipv4-alloc-cidr",
        "ipv6_alloc_cidr": "ipv6-alloc-cidr",
    }
    _revfield_names_ = {
        "ipv4-alloc-cidr": "ipv4_alloc_cidr",
        "ipv6-alloc-cidr": "ipv6_alloc_cidr",
    }

    ipv4_alloc_cidr: str
    """
    IPv4AllocCIDR is the range of IPv4 addresses in the CIDR format that the external workload can
    use to allocate IP addresses for the tunnel device and the health endpoint.
    """
    ipv6_alloc_cidr: str
    """
    IPv6AllocCIDR is the range of IPv6 addresses in the CIDR format that the external workload can
    use to allocate IP addresses for the tunnel device and the health endpoint.
    """

    def __init__(self, ipv4_alloc_cidr: str = None, ipv6_alloc_cidr: str = None):
        super().__init__(ipv4_alloc_cidr=ipv4_alloc_cidr, ipv6_alloc_cidr=ipv6_alloc_cidr)


class CiliumExternalWorkload(KubernetesApiResource):
    """
    CiliumExternalWorkload is a Kubernetes Custom Resource that
    contains a specification for an external workload that can join the
    cluster.  The name of the CRD is the FQDN of the external workload,
    and it needs to match the name in the workload registration. The
    labels on the CRD object are the labels that will be used to
    allocate a Cilium Identity for the external workload. If
    'io.kubernetes.pod.namespace' or 'io.kubernetes.pod.name' labels
    are not explicitly specified, they will be defaulted to 'default'
    and <workload name>, respectively. 'io.cilium.k8s.policy.cluster'
    will always be defined as the name of the current cluster, which
    defaults to "default".
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumExternalWorkload"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumExternalWorkloadSpec
    """ Spec is the desired configuration of the external Cilium workload. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumExternalWorkloadSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumIdentity(KubernetesApiResource):
    """
    CiliumIdentity is a CRD that represents an identity managed by Cilium.
    It is intended as a backing store for identity allocation, acting as the
    global coordination backend, and can be used in place of a KVStore (such as
    etcd).
    The name of the CRD is the numeric identity and the labels on the CRD object
    are the kubernetes sourced labels seen by cilium. This is currently the
    only label source possible when running under kubernetes. Non-kubernetes
    labels are filtered but all labels, from all sources, are places in the
    SecurityLabels field. These also include the source and are used to define
    the identity.
    The labels under metav1.ObjectMeta can be used when searching for
    CiliumIdentity instances that include particular labels. This can be done
    with invocations such as:

        kubectl get ciliumid -l 'foo=bar'
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumIdentity"
    _scope_ = "cluster"

    _required_ = ["metadata", "security_labels"]

    _field_names_ = {
        "security_labels": "security-labels",
    }
    _revfield_names_ = {
        "security-labels": "security_labels",
    }

    metadata: meta.ObjectMeta
    security_labels: dict[str, str]
    """ SecurityLabels is the source-of-truth set of labels for this identity. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, security_labels: dict[str, str] = None):
        super().__init__(name, "", metadata=metadata, security_labels=security_labels)


class CiliumL2AnnouncementPolicySpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "external_ips": "externalIPs",
        "load_balancer_ips": "loadBalancerIPs",
    }
    _revfield_names_ = {
        "externalIPs": "external_ips",
        "loadBalancerIPs": "load_balancer_ips",
    }

    external_ips: bool
    """ If true, the external IPs of the services are announced """
    interfaces: list[str]
    """
    A list of regular expressions that express which network interface(s) should be used
    to announce the services over. If nil, all network interfaces are used.
    """
    load_balancer_ips: bool
    """
    If true, the loadbalancer IPs of the services are announced
    
    If nil this policy applies to all services.
    """
    node_selector: meta.LabelSelector
    """
    NodeSelector selects a group of nodes which will announce the IPs for
    the services selected by the service selector.
    
    If nil this policy applies to all nodes.
    """
    service_selector: meta.LabelSelector
    """
    ServiceSelector selects a set of services which will be announced over L2 networks.
    The loadBalancerClass for a service must be nil or specify a supported class, e.g.
    "io.cilium/l2-announcer". Refer to the following document for additional details
    regarding load balancer classes:
    
      https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-class
    
    If nil this policy applies to all services.
    """

    def __init__(
        self,
        external_ips: bool = None,
        interfaces: list[str] = None,
        load_balancer_ips: bool = None,
        node_selector: meta.LabelSelector = None,
        service_selector: meta.LabelSelector = None,
    ):
        super().__init__(
            external_ips=external_ips,
            interfaces=interfaces,
            load_balancer_ips=load_balancer_ips,
            node_selector=node_selector,
            service_selector=service_selector,
        )


class CiliumL2AnnouncementPolicy(KubernetesApiResource):
    """
    CiliumL2AnnouncementPolicy is a Kubernetes third-party resource which
    is used to defined which nodes should announce what services on the
    L2 network.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumL2AnnouncementPolicy"
    _scope_ = "cluster"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumL2AnnouncementPolicySpec
    """ Spec is a human readable description of a L2 announcement policy """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumL2AnnouncementPolicySpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumLoadBalancerIPPoolSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "allow_first_last_ips": "allowFirstLastIPs",
    }
    _revfield_names_ = {
        "allowFirstLastIPs": "allow_first_last_ips",
    }

    allow_first_last_ips: str
    """
    AllowFirstLastIPs, if set to `Yes` or undefined means that the first and last IPs of each CIDR will be allocatable.
    If `No`, these IPs will be reserved. This field is ignored for /{31,32} and /{127,128} CIDRs since
    reserving the first and last IPs would make the CIDRs unusable.
    """
    blocks: list[Block]
    """ Blocks is a list of CIDRs comprising this IP Pool """
    disabled: bool
    """
    Disabled, if set to true means that no new IPs will be allocated from this pool.
    Existing allocations will not be removed from services.
    """
    service_selector: meta.LabelSelector
    """ ServiceSelector selects a set of services which are eligible to receive IPs from this """

    def __init__(
        self,
        allow_first_last_ips: str = None,
        blocks: list[Block] = None,
        disabled: bool = None,
        service_selector: meta.LabelSelector = None,
    ):
        super().__init__(allow_first_last_ips=allow_first_last_ips, blocks=blocks, disabled=disabled, service_selector=service_selector)


class CiliumLoadBalancerIPPool(KubernetesApiResource):
    """
    CiliumLoadBalancerIPPool is a Kubernetes third-party resource which
    is used to defined pools of IPs which the operator can use to to allocate
    and advertise IPs for Services of type LoadBalancer.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumLoadBalancerIPPool"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumLoadBalancerIPPoolSpec
    """
    Spec is a human readable description for a BGP load balancer
    ip pool.
    """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumLoadBalancerIPPoolSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumNetworkPolicySpec(KubernetesObject):
    __slots__ = ()

    description: str
    """
    Description is a free form string, it can be used by the creator of
    the rule to store human readable explanation of the purpose of this
    rule. Rules cannot be identified by comment.
    """
    egress: list[Egress]
    """
    Egress is a list of EgressRule which are enforced at egress.
    If omitted or empty, this rule does not apply at egress.
    """
    egress_deny: list[EgressDeny]
    """
    EgressDeny is a list of EgressDenyRule which are enforced at egress.
    Any rule inserted here will be denied regardless of the allowed egress
    rules in the 'egress' field.
    If omitted or empty, this rule does not apply at egress.
    """
    enable_default_deny: EnableDefaultDeny
    """
    EnableDefaultDeny determines whether this policy configures the
    subject endpoint(s) to have a default deny mode. If enabled,
    this causes all traffic not explicitly allowed by a network policy
    to be dropped.
    
    If not specified, the default is true for each traffic direction
    that has rules, and false otherwise. For example, if a policy
    only has Ingress or IngressDeny rules, then the default for
    ingress is true and egress is false.
    
    If multiple policies apply to an endpoint, that endpoint's default deny
    will be enabled if any policy requests it.
    
    This is useful for creating broad-based network policies that will not
    cause endpoints to enter default-deny mode.
    """
    endpoint_selector: meta.LabelSelector
    """
    EndpointSelector selects all endpoints which should be subject to
    this rule. EndpointSelector and NodeSelector cannot be both empty and
    are mutually exclusive.
    """
    ingress: list[Ingress]
    """
    Ingress is a list of IngressRule which are enforced at ingress.
    If omitted or empty, this rule does not apply at ingress.
    """
    ingress_deny: list[IngressDeny]
    """
    IngressDeny is a list of IngressDenyRule which are enforced at ingress.
    Any rule inserted here will be denied regardless of the allowed ingress
    rules in the 'ingress' field.
    If omitted or empty, this rule does not apply at ingress.
    """
    labels: list[Label]
    """
    Labels is a list of optional strings which can be used to
    re-identify the rule or to store metadata. It is possible to lookup
    or delete strings based on labels. Labels are not required to be
    unique, multiple rules can have overlapping or identical labels.
    """
    node_selector: meta.LabelSelector
    """
    NodeSelector selects all nodes which should be subject to this rule.
    EndpointSelector and NodeSelector cannot be both empty and are mutually
    exclusive. Can only be used in CiliumClusterwideNetworkPolicies.
    """

    def __init__(
        self,
        description: str = None,
        egress: list[Egress] = None,
        egress_deny: list[EgressDeny] = None,
        enable_default_deny: EnableDefaultDeny = None,
        endpoint_selector: meta.LabelSelector = None,
        ingress: list[Ingress] = None,
        ingress_deny: list[IngressDeny] = None,
        labels: list[Label] = None,
        node_selector: meta.LabelSelector = None,
    ):
        super().__init__(
            description=description,
            egress=egress,
            egress_deny=egress_deny,
            enable_default_deny=enable_default_deny,
            endpoint_selector=endpoint_selector,
            ingress=ingress,
            ingress_deny=ingress_deny,
            labels=labels,
            node_selector=node_selector,
        )


class CiliumNetworkPolicy(KubernetesApiResource):
    """
    CiliumNetworkPolicy is a Kubernetes third-party resource with an extended
    version of NetworkPolicy.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumNetworkPolicy"
    _scope_ = "namespace"

    _required_ = ["metadata"]

    metadata: meta.ObjectMeta
    spec: CiliumNetworkPolicySpec
    """ Spec is the desired Cilium specific rule specification. """
    specs: list[CiliumNetworkPolicySpec]
    """ Specs is a list of desired Cilium specific rule specification. """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        metadata: meta.ObjectMeta = None,
        spec: CiliumNetworkPolicySpec = None,
        specs: list[CiliumNetworkPolicySpec] = None,
    ):
        super().__init__(name, namespace, metadata=metadata, spec=spec, specs=specs)


class ENI(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "availability_zone": "availability-zone",
        "delete_on_termination": "delete-on-termination",
        "disable_prefix_delegation": "disable-prefix-delegation",
        "exclude_interface_tags": "exclude-interface-tags",
        "first_interface_index": "first-interface-index",
        "instance_id": "instance-id",
        "instance_type": "instance-type",
        "max_above_watermark": "max-above-watermark",
        "min_allocate": "min-allocate",
        "node_subnet_id": "node-subnet-id",
        "pre_allocate": "pre-allocate",
        "security_group_tags": "security-group-tags",
        "security_groups": "security-groups",
        "subnet_ids": "subnet-ids",
        "subnet_tags": "subnet-tags",
        "use_primary_address": "use-primary-address",
        "vpc_id": "vpc-id",
    }
    _revfield_names_ = {
        "availability-zone": "availability_zone",
        "delete-on-termination": "delete_on_termination",
        "disable-prefix-delegation": "disable_prefix_delegation",
        "exclude-interface-tags": "exclude_interface_tags",
        "first-interface-index": "first_interface_index",
        "instance-id": "instance_id",
        "instance-type": "instance_type",
        "max-above-watermark": "max_above_watermark",
        "min-allocate": "min_allocate",
        "node-subnet-id": "node_subnet_id",
        "pre-allocate": "pre_allocate",
        "security-group-tags": "security_group_tags",
        "security-groups": "security_groups",
        "subnet-ids": "subnet_ids",
        "subnet-tags": "subnet_tags",
        "use-primary-address": "use_primary_address",
        "vpc-id": "vpc_id",
    }

    availability_zone: str
    """
    AvailabilityZone is the availability zone to use when allocating
    ENIs.
    """
    delete_on_termination: bool
    """
    DeleteOnTermination defines that the ENI should be deleted when the
    associated instance is terminated. If the parameter is not set the
    default behavior is to delete the ENI on instance termination.
    """
    disable_prefix_delegation: bool
    """
    DisablePrefixDelegation determines whether ENI prefix delegation should be
    disabled on this node.
    """
    exclude_interface_tags: dict[str, str]
    """
    ExcludeInterfaceTags is the list of tags to use when excluding ENIs for
    Cilium IP allocation. Any interface matching this set of tags will not
    be managed by Cilium.
    """
    first_interface_index: int
    """
    FirstInterfaceIndex is the index of the first ENI to use for IP
    allocation, e.g. if the node has eth0, eth1, eth2 and
    FirstInterfaceIndex is set to 1, then only eth1 and eth2 will be
    used for IP allocation, eth0 will be ignored for PodIP allocation.
    """
    instance_id: str
    """
    InstanceID is the AWS InstanceId of the node. The InstanceID is used
    to retrieve AWS metadata for the node.
    
    OBSOLETE: This field is obsolete, please use Spec.InstanceID
    """
    instance_type: str
    """ InstanceType is the AWS EC2 instance type, e.g. "m5.large" """
    max_above_watermark: int
    """
    MaxAboveWatermark is the maximum number of addresses to allocate
    beyond the addresses needed to reach the PreAllocate watermark.
    Going above the watermark can help reduce the number of API calls to
    allocate IPs, e.g. when a new ENI is allocated, as many secondary
    IPs as possible are allocated. Limiting the amount can help reduce
    waste of IPs.
    
    OBSOLETE: This field is obsolete, please use Spec.IPAM.MaxAboveWatermark
    """
    min_allocate: int
    """
    MinAllocate is the minimum number of IPs that must be allocated when
    the node is first bootstrapped. It defines the minimum base socket
    of addresses that must be available. After reaching this watermark,
    the PreAllocate and MaxAboveWatermark logic takes over to continue
    allocating IPs.
    
    OBSOLETE: This field is obsolete, please use Spec.IPAM.MinAllocate
    """
    node_subnet_id: str
    """
    NodeSubnetID is the subnet of the primary ENI the instance was brought up
    with. It is used as a sensible default subnet to create ENIs in.
    """
    pre_allocate: int
    """
    PreAllocate defines the number of IP addresses that must be
    available for allocation in the IPAMspec. It defines the buffer of
    addresses available immediately without requiring cilium-operator to
    get involved.
    
    OBSOLETE: This field is obsolete, please use Spec.IPAM.PreAllocate
    """
    security_group_tags: dict[str, str]
    """
    SecurityGroupTags is the list of tags to use when evaliating what
    AWS security groups to use for the ENI.
    """
    security_groups: list[str]
    """
    SecurityGroups is the list of security groups to attach to any ENI
    that is created and attached to the instance.
    """
    subnet_ids: list[str]
    """
    SubnetIDs is the list of subnet ids to use when evaluating what AWS
    subnets to use for ENI and IP allocation.
    """
    subnet_tags: dict[str, str]
    """
    SubnetTags is the list of tags to use when evaluating what AWS
    subnets to use for ENI and IP allocation.
    """
    use_primary_address: bool
    """
    UsePrimaryAddress determines whether an ENI's primary address
    should be available for allocations on the node
    """
    vpc_id: str
    """ VpcID is the VPC ID to use when allocating ENIs. """

    def __init__(
        self,
        availability_zone: str = None,
        delete_on_termination: bool = None,
        disable_prefix_delegation: bool = None,
        exclude_interface_tags: dict[str, str] = None,
        first_interface_index: int = None,
        instance_id: str = None,
        instance_type: str = None,
        max_above_watermark: int = None,
        min_allocate: int = None,
        node_subnet_id: str = None,
        pre_allocate: int = None,
        security_group_tags: dict[str, str] = None,
        security_groups: list[str] = None,
        subnet_ids: list[str] = None,
        subnet_tags: dict[str, str] = None,
        use_primary_address: bool = None,
        vpc_id: str = None,
    ):
        super().__init__(
            availability_zone=availability_zone,
            delete_on_termination=delete_on_termination,
            disable_prefix_delegation=disable_prefix_delegation,
            exclude_interface_tags=exclude_interface_tags,
            first_interface_index=first_interface_index,
            instance_id=instance_id,
            instance_type=instance_type,
            max_above_watermark=max_above_watermark,
            min_allocate=min_allocate,
            node_subnet_id=node_subnet_id,
            pre_allocate=pre_allocate,
            security_group_tags=security_group_tags,
            security_groups=security_groups,
            subnet_ids=subnet_ids,
            subnet_tags=subnet_tags,
            use_primary_address=use_primary_address,
            vpc_id=vpc_id,
        )


class Health(KubernetesObject):
    __slots__ = ()

    ipv4: str
    """ IPv4 is the IPv4 address of the IPv4 health endpoint. """
    ipv6: str
    """ IPv6 is the IPv6 address of the IPv4 health endpoint. """

    def __init__(self, ipv4: str = None, ipv6: str = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6)


class CiliumNodeSpecIngress(KubernetesObject):
    __slots__ = ()

    ipv4: str
    ipv6: str

    def __init__(self, ipv4: str = None, ipv6: str = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6)


class Ipv6Pool(KubernetesObject):
    __slots__ = ()

    owner: str
    """
    Owner is the owner of the IP. This field is set if the IP has been
    allocated. It will be set to the pod name or another identifier
    representing the usage of the IP
    
    The owner field is left blank for an entry in Spec.IPAM.Pool and
    filled out as the IP is used and also added to Status.IPAM.Used.
    """
    resource: str
    """
    Resource is set for both available and allocated IPs, it represents
    what resource the IP is associated with, e.g. in combination with
    AWS ENI, this will refer to the ID of the ENI
    """

    def __init__(self, owner: str = None, resource: str = None):
        super().__init__(owner=owner, resource=resource)


class Pool(KubernetesObject):
    __slots__ = ()

    owner: str
    """
    Owner is the owner of the IP. This field is set if the IP has been
    allocated. It will be set to the pod name or another identifier
    representing the usage of the IP
    
    The owner field is left blank for an entry in Spec.IPAM.Pool and
    filled out as the IP is used and also added to Status.IPAM.Used.
    """
    resource: str
    """
    Resource is set for both available and allocated IPs, it represents
    what resource the IP is associated with, e.g. in combination with
    AWS ENI, this will refer to the ID of the ENI
    """

    def __init__(self, owner: str = None, resource: str = None):
        super().__init__(owner=owner, resource=resource)


class Needed(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "ipv4_addrs": "ipv4-addrs",
        "ipv6_addrs": "ipv6-addrs",
    }
    _revfield_names_ = {
        "ipv4-addrs": "ipv4_addrs",
        "ipv6-addrs": "ipv6_addrs",
    }

    ipv4_addrs: int
    """
    IPv4Addrs contains the number of requested IPv4 addresses out of a given
    pool
    """
    ipv6_addrs: int
    """
    IPv6Addrs contains the number of requested IPv6 addresses out of a given
    pool
    """

    def __init__(self, ipv4_addrs: int = None, ipv6_addrs: int = None):
        super().__init__(ipv4_addrs=ipv4_addrs, ipv6_addrs=ipv6_addrs)


class Requested(KubernetesObject):
    __slots__ = ()

    _required_ = ["pool"]

    needed: Needed
    """
    Needed indicates how many IPs out of the above Pool this node requests
    from the operator. The operator runs a reconciliation loop to ensure each
    node always has enough PodCIDRs allocated in each pool to fulfill the
    requested number of IPs here.
    """
    pool: str
    """ Pool is the name of the IPAM pool backing this request """

    def __init__(self, needed: Needed = None, pool: str = None):
        super().__init__(needed=needed, pool=pool)


class Pools(KubernetesObject):
    __slots__ = ()

    allocated: list[Allocated]
    """
    Allocated contains the list of pooled CIDR assigned to this node. The
    operator will add new pod CIDRs to this field, whereas the agent will
    remove CIDRs it has released.
    """
    requested: list[Requested]
    """
    Requested contains a list of IPAM pool requests, i.e. indicates how many
    addresses this node requests out of each pool listed here. This field
    is owned and written to by cilium-agent and read by the operator.
    """

    def __init__(self, allocated: list[Allocated] = None, requested: list[Requested] = None):
        super().__init__(allocated=allocated, requested=requested)


class IPAM(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "ipv6_pool": "ipv6-pool",
        "max_above_watermark": "max-above-watermark",
        "max_allocate": "max-allocate",
        "min_allocate": "min-allocate",
        "pod_cidrs": "podCIDRs",
        "pre_allocate": "pre-allocate",
        "static_ip_tags": "static-ip-tags",
    }
    _revfield_names_ = {
        "ipv6-pool": "ipv6_pool",
        "max-above-watermark": "max_above_watermark",
        "max-allocate": "max_allocate",
        "min-allocate": "min_allocate",
        "podCIDRs": "pod_cidrs",
        "pre-allocate": "pre_allocate",
        "static-ip-tags": "static_ip_tags",
    }

    ipv6_pool: dict[str, Ipv6Pool]
    """
    IPv6Pool is the list of IPv6 addresses available to the node for allocation.
    When an IPv6 address is used, it will remain on this list but will be added to
    Status.IPAM.IPv6Used
    """
    max_above_watermark: int
    """
    MaxAboveWatermark is the maximum number of addresses to allocate
    beyond the addresses needed to reach the PreAllocate watermark.
    Going above the watermark can help reduce the number of API calls to
    allocate IPs, e.g. when a new ENI is allocated, as many secondary
    IPs as possible are allocated. Limiting the amount can help reduce
    waste of IPs.
    """
    max_allocate: int
    """
    MaxAllocate is the maximum number of IPs that can be allocated to the
    node. When the current amount of allocated IPs will approach this value,
    the considered value for PreAllocate will decrease down to 0 in order to
    not attempt to allocate more addresses than defined.
    """
    min_allocate: int
    """
    MinAllocate is the minimum number of IPs that must be allocated when
    the node is first bootstrapped. It defines the minimum base socket
    of addresses that must be available. After reaching this watermark,
    the PreAllocate and MaxAboveWatermark logic takes over to continue
    allocating IPs.
    """
    pod_cidrs: list[str]
    """
    PodCIDRs is the list of CIDRs available to the node for allocation.
    When an IP is used, the IP will be added to Status.IPAM.Used
    """
    pool: dict[str, Pool]
    """
    Pool is the list of IPv4 addresses available to the node for allocation.
    When an IPv4 address is used, it will remain on this list but will be added to
    Status.IPAM.Used
    """
    pools: Pools
    """ Pools contains the list of assigned IPAM pools for this node. """
    pre_allocate: int
    """
    PreAllocate defines the number of IP addresses that must be
    available for allocation in the IPAMspec. It defines the buffer of
    addresses available immediately without requiring cilium-operator to
    get involved.
    """
    static_ip_tags: dict[str, str]
    """
    StaticIPTags are used to determine the pool of IPs from which to
    attribute a static IP to the node. For example in AWS this is used to
    filter Elastic IP Addresses.
    """

    def __init__(
        self,
        ipv6_pool: dict[str, Ipv6Pool] = None,
        max_above_watermark: int = None,
        max_allocate: int = None,
        min_allocate: int = None,
        pod_cidrs: list[str] = None,
        pool: dict[str, Pool] = None,
        pools: Pools = None,
        pre_allocate: int = None,
        static_ip_tags: dict[str, str] = None,
    ):
        super().__init__(
            ipv6_pool=ipv6_pool,
            max_above_watermark=max_above_watermark,
            max_allocate=max_allocate,
            min_allocate=min_allocate,
            pod_cidrs=pod_cidrs,
            pool=pool,
            pools=pools,
            pre_allocate=pre_allocate,
            static_ip_tags=static_ip_tags,
        )


class CiliumNodeSpec(KubernetesObject):
    __slots__ = ()

    _field_names_ = {
        "alibaba_cloud": "alibaba-cloud",
        "instance_id": "instance-id",
    }
    _revfield_names_ = {
        "alibaba-cloud": "alibaba_cloud",
        "instance-id": "instance_id",
    }

    addresses: list[Addresse]
    """ Addresses is the list of all node addresses. """
    alibaba_cloud: AlibabaCloud
    """ AlibabaCloud is the AlibabaCloud IPAM specific configuration. """
    azure: Azure
    """ Azure is the Azure IPAM specific configuration. """
    bootid: str
    """ BootID is a unique node identifier generated on boot """
    encryption: Encryption
    """ Encryption is the encryption configuration of the node. """
    eni: ENI
    """ ENI is the AWS ENI specific configuration. """
    health: Health
    """
    HealthAddressing is the addressing information for health connectivity
    checking.
    """
    ingress: CiliumNodeSpecIngress
    """ IngressAddressing is the addressing information for Ingress listener. """
    instance_id: str
    """
    InstanceID is the identifier of the node. This is different from the
    node name which is typically the FQDN of the node. The InstanceID
    typically refers to the identifier used by the cloud provider or
    some other means of identification.
    """
    ipam: IPAM
    """
    IPAM is the address management specification. This section can be
    populated by a user or it can be automatically populated by an IPAM
    operator.
    """
    nodeidentity: int
    """ NodeIdentity is the Cilium numeric identity allocated for the node, if any. """

    def __init__(
        self,
        addresses: list[Addresse] = None,
        alibaba_cloud: AlibabaCloud = None,
        azure: Azure = None,
        bootid: str = None,
        encryption: Encryption = None,
        eni: ENI = None,
        health: Health = None,
        ingress: CiliumNodeSpecIngress = None,
        instance_id: str = None,
        ipam: IPAM = None,
        nodeidentity: int = None,
    ):
        super().__init__(
            addresses=addresses,
            alibaba_cloud=alibaba_cloud,
            azure=azure,
            bootid=bootid,
            encryption=encryption,
            eni=eni,
            health=health,
            ingress=ingress,
            instance_id=instance_id,
            ipam=ipam,
            nodeidentity=nodeidentity,
        )


class CiliumNode(KubernetesApiResource):
    """
    CiliumNode represents a node managed by Cilium. It contains a specification
    to control various node specific configuration aspects and a status section
    to represent the status of the node.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumNode"
    _scope_ = "cluster"

    _required_ = ["metadata", "spec"]

    metadata: meta.ObjectMeta
    spec: CiliumNodeSpec
    """ Spec defines the desired specification/configuration of the node. """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumNodeSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CiliumNodeConfigSpec(KubernetesObject):
    __slots__ = ()

    _required_ = ["defaults", "node_selector"]

    defaults: dict[str, str]
    """
    Defaults is treated the same as the cilium-config ConfigMap - a set
    of key-value pairs parsed by the agent and operator processes.
    Each key must be a valid config-map data field (i.e. a-z, A-Z, -, _, and .)
    """
    node_selector: meta.LabelSelector
    """
    NodeSelector is a label selector that determines to which nodes
    this configuration applies.
    If not supplied, then this config applies to no nodes. If
    empty, then it applies to all nodes.
    """

    def __init__(self, defaults: dict[str, str] = None, node_selector: meta.LabelSelector = None):
        super().__init__(defaults=defaults, node_selector=node_selector)


class CiliumNodeConfig(KubernetesApiResource):
    """
    CiliumNodeConfig is a list of configuration key-value pairs. It is applied to
    nodes indicated by a label selector.

    If multiple overrides apply to the same node, they will be ordered by name
    with later Overrides overwriting any conflicting keys.
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumNodeConfig"
    _scope_ = "namespace"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CiliumNodeConfigSpec
    """ Spec is the desired Cilium configuration overrides for a given node """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CiliumNodeConfigSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class Ipv6(KubernetesObject):
    __slots__ = ()

    _required_ = ["cidrs", "mask_size"]

    cidrs: list[CIDR]
    """ CIDRs is a list of IPv6 CIDRs that are part of the pool. """
    mask_size: int
    """ MaskSize is the mask size of the pool. """

    def __init__(self, cidrs: list[CIDR] = None, mask_size: int = None):
        super().__init__(cidrs=cidrs, mask_size=mask_size)


class CiliumPodIPPoolSpec(KubernetesObject):
    __slots__ = ()

    ipv4: Ipv4
    """ IPv4 specifies the IPv4 CIDRs and mask sizes of the pool """
    ipv6: Ipv6
    """ IPv6 specifies the IPv6 CIDRs and mask sizes of the pool """

    def __init__(self, ipv4: Ipv4 = None, ipv6: Ipv6 = None):
        super().__init__(ipv4=ipv4, ipv6=ipv6)


class CiliumPodIPPool(KubernetesApiResource):
    """
    CiliumPodIPPool defines an IP pool that can be used for pooled IPAM (i.e. the multi-pool IPAM
    mode).
    """

    __slots__ = ()

    _api_version_ = "cilium.io/v2alpha1"
    _api_group_ = "cilium.io"
    _kind_ = "CiliumPodIPPool"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CiliumPodIPPoolSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CiliumPodIPPoolSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)
