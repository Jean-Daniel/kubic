from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class EventSeries(KubernetesObject):
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations."""

    __slots__ = ()

    _api_version_ = "events.k8s.io/v1"

    _required_ = ["count", "last_observed_time"]

    count: int
    """ count is the number of occurrences in this series up to the last heartbeat time. """
    last_observed_time: meta.MicroTime
    """ lastObservedTime is the time when last Event from the series was seen before last heartbeat. """

    def __init__(self, count: int = None, last_observed_time: meta.MicroTime = None):
        super().__init__(count=count, last_observed_time=last_observed_time)


class Event(KubernetesApiResource):
    """Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data."""

    __slots__ = ()

    _api_version_ = "events.k8s.io/v1"
    _api_group_ = "events.k8s.io"
    _kind_ = "Event"
    _scope_ = "namespace"

    _required_ = ["event_time"]

    action: str
    """ action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters. """
    deprecated_count: int
    """ deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type. """
    deprecated_first_timestamp: meta.Time
    """ deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. """
    deprecated_last_timestamp: meta.Time
    """ deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type. """
    deprecated_source: core.EventSource
    """ deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type. """
    event_time: meta.MicroTime
    """ eventTime is the time when this Event was first observed. It is required. """
    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    note: str
    """ note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB. """
    reason: str
    """ reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters. """
    regarding: core.ObjectReference
    """ regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object. """
    related: core.ObjectReference
    """ related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object. """
    reporting_controller: str
    """ reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events. """
    reporting_instance: str
    """ reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters. """
    series: EventSeries
    """ series is data about the Event series this event represents or nil if it's a singleton Event. """
    type: str
    """ type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events. """

    def __init__(
        self,
        name: str,
        namespace: str = None,
        action: str = None,
        deprecated_count: int = None,
        deprecated_first_timestamp: meta.Time = None,
        deprecated_last_timestamp: meta.Time = None,
        deprecated_source: core.EventSource = None,
        event_time: meta.MicroTime = None,
        metadata: meta.ObjectMeta = None,
        note: str = None,
        reason: str = None,
        regarding: core.ObjectReference = None,
        related: core.ObjectReference = None,
        reporting_controller: str = None,
        reporting_instance: str = None,
        series: EventSeries = None,
        type: str = None,
    ):
        super().__init__(
            name,
            namespace,
            action=action,
            deprecated_count=deprecated_count,
            deprecated_first_timestamp=deprecated_first_timestamp,
            deprecated_last_timestamp=deprecated_last_timestamp,
            deprecated_source=deprecated_source,
            event_time=event_time,
            metadata=metadata,
            note=note,
            reason=reason,
            regarding=regarding,
            related=related,
            reporting_controller=reporting_controller,
            reporting_instance=reporting_instance,
            series=series,
            type=type,
        )
