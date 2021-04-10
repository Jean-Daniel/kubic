from . import KubernetesApiResource, KubernetesObject
from . import core, meta


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

    _api_version_ = "batch/v1"
    _kind_ = "CronJob"

    metadata: meta.ObjectMeta
    spec: CronJobSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CronJobSpec = None):
        super().__init__("batch/v1", "CronJob", name, namespace, metadata=metadata, spec=spec)


class Job(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "batch/v1"
    _kind_ = "Job"

    metadata: meta.ObjectMeta
    spec: JobSpec

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: JobSpec = None):
        super().__init__("batch/v1", "Job", name, namespace, metadata=metadata, spec=spec)
