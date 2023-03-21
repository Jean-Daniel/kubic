from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta



class EventSeries(KubernetesObject):
    __slots__ = ()

    _api_version_ = "events.k8s.io/v1"

    _required_ = ["count", "last_observed_time"]

    count: int
    last_observed_time: meta.MicroTime

    def __init__(self, count: int = None, last_observed_time: meta.MicroTime = None):
        super().__init__(count=count, last_observed_time=last_observed_time)


class Event(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "events.k8s.io/v1"
    _api_group_ = "events.k8s.io"
    _kind_ = "Event"
    _scope_ = "namespace"

    _required_ = ["event_time"]

    action: str
    deprecated_count: int
    deprecated_first_timestamp: meta.Time
    deprecated_last_timestamp: meta.Time
    deprecated_source: core.EventSource
    event_time: meta.MicroTime
    metadata: meta.ObjectMeta
    note: str
    reason: str
    regarding: core.ObjectReference
    related: core.ObjectReference
    reporting_controller: str
    reporting_instance: str
    series: EventSeries
    type: str

    def __init__(self, name: str, namespace: str = None, action: str = None, deprecated_count: int = None, deprecated_first_timestamp: meta.Time = None, deprecated_last_timestamp: meta.Time = None, deprecated_source: core.EventSource = None, event_time: meta.MicroTime = None, metadata: meta.ObjectMeta = None, note: str = None, reason: str = None, regarding: core.ObjectReference = None, related: core.ObjectReference = None, reporting_controller: str = None, reporting_instance: str = None, series: EventSeries = None, type: str = None):
        super().__init__(name, namespace, action=action, deprecated_count=deprecated_count, deprecated_first_timestamp=deprecated_first_timestamp, deprecated_last_timestamp=deprecated_last_timestamp, deprecated_source=deprecated_source, event_time=event_time, metadata=metadata, note=note, reason=reason, regarding=regarding, related=related, reporting_controller=reporting_controller, reporting_instance=reporting_instance, series=series, type=type)


class EventList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "events.k8s.io/v1"
    _api_group_ = "events.k8s.io"
    _kind_ = "EventList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Event]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Event] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


