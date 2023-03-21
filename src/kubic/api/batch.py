from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class PodFailurePolicyOnExitCodesRequirement(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["operator", "values"]

    container_name: str
    operator: str
    values: list[int]

    def __init__(self, container_name: str = None, operator: str = None, values: list[int] = None):
        super().__init__(container_name=container_name, operator=operator, values=values)


class PodFailurePolicyOnPodConditionsPattern(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["status", "type"]

    status: str
    type: str

    def __init__(self, status: str = None, type: str = None):
        super().__init__(status=status, type=type)


class PodFailurePolicyRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["action", "on_pod_conditions"]

    action: str
    on_exit_codes: PodFailurePolicyOnExitCodesRequirement
    on_pod_conditions: list[PodFailurePolicyOnPodConditionsPattern]

    def __init__(
        self,
        action: str = None,
        on_exit_codes: PodFailurePolicyOnExitCodesRequirement = None,
        on_pod_conditions: list[PodFailurePolicyOnPodConditionsPattern] = None,
    ):
        super().__init__(action=action, on_exit_codes=on_exit_codes, on_pod_conditions=on_pod_conditions)


class PodFailurePolicy(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["rules"]

    rules: list[PodFailurePolicyRule]

    def __init__(self, rules: list[PodFailurePolicyRule] = None):
        super().__init__(rules=rules)


class JobSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["template"]

    active_deadline_seconds: int
    backoff_limit: int
    completion_mode: str
    completions: int
    manual_selector: bool
    parallelism: int
    pod_failure_policy: PodFailurePolicy
    selector: meta.LabelSelector
    suspend: bool
    template: core.PodTemplateSpec
    ttl_seconds_after_finished: int

    def __init__(
        self,
        active_deadline_seconds: int = None,
        backoff_limit: int = None,
        completion_mode: str = None,
        completions: int = None,
        manual_selector: bool = None,
        parallelism: int = None,
        pod_failure_policy: PodFailurePolicy = None,
        selector: meta.LabelSelector = None,
        suspend: bool = None,
        template: core.PodTemplateSpec = None,
        ttl_seconds_after_finished: int = None,
    ):
        super().__init__(
            active_deadline_seconds=active_deadline_seconds,
            backoff_limit=backoff_limit,
            completion_mode=completion_mode,
            completions=completions,
            manual_selector=manual_selector,
            parallelism=parallelism,
            pod_failure_policy=pod_failure_policy,
            selector=selector,
            suspend=suspend,
            template=template,
            ttl_seconds_after_finished=ttl_seconds_after_finished,
        )


class JobTemplateSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    metadata: meta.ObjectMeta
    spec: JobSpec

    def __init__(self, metadata: meta.ObjectMeta = None, spec: JobSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class CronJobSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["job_template", "schedule"]

    concurrency_policy: str
    failed_jobs_history_limit: int
    job_template: JobTemplateSpec
    schedule: str
    starting_deadline_seconds: int
    successful_jobs_history_limit: int
    suspend: bool
    time_zone: str

    def __init__(
        self,
        concurrency_policy: str = None,
        failed_jobs_history_limit: int = None,
        job_template: JobTemplateSpec = None,
        schedule: str = None,
        starting_deadline_seconds: int = None,
        successful_jobs_history_limit: int = None,
        suspend: bool = None,
        time_zone: str = None,
    ):
        super().__init__(
            concurrency_policy=concurrency_policy,
            failed_jobs_history_limit=failed_jobs_history_limit,
            job_template=job_template,
            schedule=schedule,
            starting_deadline_seconds=starting_deadline_seconds,
            successful_jobs_history_limit=successful_jobs_history_limit,
            suspend=suspend,
            time_zone=time_zone,
        )


class CronJob(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "batch/v1"
    _api_group_ = "batch"
    _kind_ = "CronJob"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: CronJobSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CronJobSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class CronJobList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "batch/v1"
    _api_group_ = "batch"
    _kind_ = "CronJobList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[CronJob]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[CronJob] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class CronJobStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    active: list[core.ObjectReference]
    last_schedule_time: meta.Time
    last_successful_time: meta.Time

    def __init__(
        self, active: list[core.ObjectReference] = None, last_schedule_time: meta.Time = None, last_successful_time: meta.Time = None
    ):
        super().__init__(active=active, last_schedule_time=last_schedule_time, last_successful_time=last_successful_time)


class Job(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "batch/v1"
    _api_group_ = "batch"
    _kind_ = "Job"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    spec: JobSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: JobSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class JobCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["status", "type"]

    last_probe_time: meta.Time
    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self,
        last_probe_time: meta.Time = None,
        last_transition_time: meta.Time = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        super().__init__(
            last_probe_time=last_probe_time,
            last_transition_time=last_transition_time,
            message=message,
            reason=reason,
            status=status,
            type=type,
        )


class JobList(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "batch/v1"
    _api_group_ = "batch"
    _kind_ = "JobList"
    _scope_ = "namespace"

    _required_ = ["items"]

    items: list[Job]
    metadata: meta.ListMeta

    def __init__(self, name: str, namespace: str = None, items: list[Job] = None, metadata: meta.ListMeta = None):
        super().__init__(name, namespace, items=items, metadata=metadata)


class UncountedTerminatedPods(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    failed: list[str]
    succeeded: list[str]

    def __init__(self, failed: list[str] = None, succeeded: list[str] = None):
        super().__init__(failed=failed, succeeded=succeeded)


class JobStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "batch/v1"

    active: int
    completed_indexes: str
    completion_time: meta.Time
    conditions: list[JobCondition]
    failed: int
    ready: int
    start_time: meta.Time
    succeeded: int
    uncounted_terminated_pods: UncountedTerminatedPods

    def __init__(
        self,
        active: int = None,
        completed_indexes: str = None,
        completion_time: meta.Time = None,
        conditions: list[JobCondition] = None,
        failed: int = None,
        ready: int = None,
        start_time: meta.Time = None,
        succeeded: int = None,
        uncounted_terminated_pods: UncountedTerminatedPods = None,
    ):
        super().__init__(
            active=active,
            completed_indexes=completed_indexes,
            completion_time=completion_time,
            conditions=conditions,
            failed=failed,
            ready=ready,
            start_time=start_time,
            succeeded=succeeded,
            uncounted_terminated_pods=uncounted_terminated_pods,
        )
