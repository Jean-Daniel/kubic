from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class ServiceReference(KubernetesObject):
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    name: str
    """ Name is the name of the service """
    namespace: str
    """ Namespace is the namespace of the service """
    port: int
    """ If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive). """

    def __init__(self, name: str = None, namespace: str = None, port: int = None):
        super().__init__(name=name, namespace=namespace, port=port)


class APIServiceSpec(KubernetesObject):
    """APIServiceSpec contains information for locating and communicating with a server. Only https is supported, though you are able to disable certificate verification."""

    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    _required_ = ["group_priority_minimum", "version_priority"]

    _field_names_ = {
        "insecure_skip_tls_verify": "insecureSkipTLSVerify",
    }
    _revfield_names_ = {
        "insecureSkipTLSVerify": "insecure_skip_tls_verify",
    }

    ca_bundle: core.Base64
    """ CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used. """
    group: str
    """ Group is the API group name this server hosts """
    group_priority_minimum: int
    """ GroupPriorityMinimum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMinimum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s """
    insecure_skip_tls_verify: bool
    """ InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead. """
    service: ServiceReference
    """ Service is a reference to the service for this API server.  It must communicate on port 443. If the Service is nil, that means the handling for the API groupversion is handled locally on this server. The call will simply delegate to the normal handler chain to be fulfilled. """
    version: str
    """ Version is the API version this server hosts.  For example, "v1" """
    version_priority: int
    """ VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. """

    def __init__(
        self,
        ca_bundle: core.Base64 = None,
        group: str = None,
        group_priority_minimum: int = None,
        insecure_skip_tls_verify: bool = None,
        service: ServiceReference = None,
        version: str = None,
        version_priority: int = None,
    ):
        super().__init__(
            ca_bundle=ca_bundle,
            group=group,
            group_priority_minimum=group_priority_minimum,
            insecure_skip_tls_verify=insecure_skip_tls_verify,
            service=service,
            version=version,
            version_priority=version_priority,
        )


class APIService(KubernetesApiResource):
    """APIService represents a server for a particular GroupVersion. Name must be "version.group"."""

    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"
    _api_group_ = "apiregistration.k8s.io"
    _kind_ = "APIService"
    _scope_ = "cluster"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: APIServiceSpec
    """ Spec contains information for locating and communicating with a server """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: APIServiceSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class APIServiceCondition(KubernetesObject):
    """APIServiceCondition describes the state of an APIService at a particular point"""

    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ Last time the condition transitioned from one status to another. """
    message: str
    """ Human-readable message indicating details about last transition. """
    reason: str
    """ Unique, one-word, CamelCase reason for the condition's last transition. """
    status: str
    """ Status is the status of the condition. Can be True, False, Unknown. """
    type: str
    """ Type is the type of the condition. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class APIServiceStatus(KubernetesObject):
    """APIServiceStatus contains derived information about an API server"""

    __slots__ = ()

    _api_version_ = "apiregistration.k8s.io/v1"

    conditions: list[APIServiceCondition]
    """ Current service state of apiService. """

    def __init__(self, conditions: list[APIServiceCondition] = None):
        super().__init__(conditions=conditions)
