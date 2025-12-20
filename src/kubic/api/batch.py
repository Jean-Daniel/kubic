from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class PodFailurePolicyOnExitCodesRequirement(KubernetesObject):
    """PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app container and init container status, represented by the .status.containerStatuses and .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with success (exit code 0) are excluded from the requirement check."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["operator", "values"]

    container_name: str
    """ Restricts the check for exit codes to the container with the specified name. When null, the rule applies to all containers. When specified, it should match one the container or initContainer names in the pod template. """
    operator: str
    """
    Represents the relationship between the container exit code(s) and the specified values. Containers completed with success (exit code 0) are excluded from the requirement check. Possible values are:
    
    - In: the requirement is satisfied if at least one container exit code
      (might be multiple if there are multiple containers not restricted
      by the 'containerName' field) is in the set of specified values.
    - NotIn: the requirement is satisfied if at least one container exit code
      (might be multiple if there are multiple containers not restricted
      by the 'containerName' field) is not in the set of specified values.
    Additional values are considered to be added in the future. Clients should react to an unknown operator by assuming the requirement is not satisfied.
    """
    values: list[int]
    """ Specifies the set of values. Each returned container exit code (might be multiple in case of multiple containers) is checked against this set of values with respect to the operator. The list of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In operator. At least one element is required. At most 255 elements are allowed. """

    def __init__(self, container_name: str = None, operator: str = None, values: list[int] = None):
        super().__init__(container_name=container_name, operator=operator, values=values)


class PodFailurePolicyOnPodConditionsPattern(KubernetesObject):
    """PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["status", "type"]

    status: str
    """ Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. """
    type: str
    """ Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. """

    def __init__(self, status: str = None, type: str = None):
        super().__init__(status=status, type=type)


class PodFailurePolicyRule(KubernetesObject):
    """PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["action"]

    action: str
    """
    Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:
    
    - FailJob: indicates that the pod's job is marked as Failed and all
      running pods are terminated.
    - FailIndex: indicates that the pod's index is marked as Failed and will
      not be restarted.
    - Ignore: indicates that the counter towards the .backoffLimit is not
      incremented and a replacement pod is created.
    - Count: indicates that the pod is handled in the default way - the
      counter towards the .backoffLimit is incremented.
    Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.
    """
    on_exit_codes: PodFailurePolicyOnExitCodesRequirement
    """ Represents the requirement on the container exit codes. """
    on_pod_conditions: list[PodFailurePolicyOnPodConditionsPattern]
    """ Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed. """

    def __init__(
        self,
        action: str = None,
        on_exit_codes: PodFailurePolicyOnExitCodesRequirement = None,
        on_pod_conditions: list[PodFailurePolicyOnPodConditionsPattern] = None,
    ):
        super().__init__(action=action, on_exit_codes=on_exit_codes, on_pod_conditions=on_pod_conditions)


class PodFailurePolicy(KubernetesObject):
    """PodFailurePolicy describes how failed pods influence the backoffLimit."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["rules"]

    rules: list[PodFailurePolicyRule]
    """ A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed. """

    def __init__(self, rules: list[PodFailurePolicyRule] = None):
        super().__init__(rules=rules)


class SuccessPolicyRule(KubernetesObject):
    """SuccessPolicyRule describes rule for declaring a Job as succeeded. Each rule must have at least one of the "succeededIndexes" or "succeededCount" specified."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    succeeded_count: int
    """ succeededCount specifies the minimal required size of the actual set of the succeeded indexes for the Job. When succeededCount is used along with succeededIndexes, the check is constrained only to the set of indexes specified by succeededIndexes. For example, given that succeededIndexes is "1-4", succeededCount is "3", and completed indexes are "1", "3", and "5", the Job isn't declared as succeeded because only "1" and "3" indexes are considered in that rules. When this field is null, this doesn't default to any value and is never evaluated at any time. When specified it needs to be a positive integer. """
    succeeded_indexes: str
    """ succeededIndexes specifies the set of indexes which need to be contained in the actual set of the succeeded indexes for the Job. The list of indexes must be within 0 to ".spec.completions-1" and must not contain duplicates. At least one element is required. The indexes are represented as intervals separated by commas. The intervals can be a decimal integer or a pair of decimal integers separated by a hyphen. The number are listed in represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7". When this field is null, this field doesn't default to any value and is never evaluated at any time. """

    def __init__(self, succeeded_count: int = None, succeeded_indexes: str = None):
        super().__init__(succeeded_count=succeeded_count, succeeded_indexes=succeeded_indexes)


class SuccessPolicy(KubernetesObject):
    """SuccessPolicy describes when a Job can be declared as succeeded based on the success of some indexes."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["rules"]

    rules: list[SuccessPolicyRule]
    """ rules represents the list of alternative rules for the declaring the Jobs as successful before `.status.succeeded >= .spec.completions`. Once any of the rules are met, the "SucceededCriteriaMet" condition is added, and the lingering pods are removed. The terminal state for such a Job has the "Complete" condition. Additionally, these rules are evaluated in order; Once the Job meets one of the rules, other rules are ignored. At most 20 elements are allowed. """

    def __init__(self, rules: list[SuccessPolicyRule] = None):
        super().__init__(rules=rules)


class JobSpec(KubernetesObject):
    """JobSpec describes how the job execution will look like."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["template"]

    active_deadline_seconds: int
    """ Specifies the duration in seconds relative to the startTime that the job may be continuously active before the system tries to terminate it; value must be positive integer. If a Job is suspended (at creation or through an update), this timer will effectively be stopped and reset when the Job is resumed again. """
    backoff_limit: int
    """ Specifies the number of retries before marking this job failed. Defaults to 6 """
    backoff_limit_per_index: int
    """ Specifies the limit for the number of retries within an index before marking this index as failed. When enabled the number of failures per index is kept in the pod's batch.kubernetes.io/job-index-failure-count annotation. It can only be set when Job's completionMode=Indexed, and the Pod's restart policy is Never. The field is immutable. """
    completion_mode: str
    """
    completionMode specifies how Pod completions are tracked. It can be `NonIndexed` (default) or `Indexed`.
    
    `NonIndexed` means that the Job is considered complete when there have been .spec.completions successfully completed Pods. Each Pod completion is homologous to each other.
    
    `Indexed` means that the Pods of a Job get an associated completion index from 0 to (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The Job is considered complete when there is one successfully completed Pod for each index. When value is `Indexed`, .spec.completions must be specified and `.spec.parallelism` must be less than or equal to 10^5. In addition, The Pod name takes the form `$(job-name)-$(index)-$(random-string)`, the Pod hostname takes the form `$(job-name)-$(index)`.
    
    More completion modes can be added in the future. If the Job controller observes a mode that it doesn't recognize, which is possible during upgrades due to version skew, the controller skips updates for the Job.
    """
    completions: int
    """ Specifies the desired number of successfully finished pods the job should be run with.  Setting to null means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """
    managed_by: str
    """
    ManagedBy field indicates the controller that manages a Job. The k8s Job controller reconciles jobs which don't have this field at all or the field value is the reserved string `kubernetes.io/job-controller`, but skips reconciling Jobs with a custom value for this field. The value must be a valid domain-prefixed path (e.g. acme.io/foo) - all characters before the first "/" must be a valid subdomain as defined by RFC 1123. All characters trailing the first "/" must be valid HTTP Path characters as defined by RFC 3986. The value cannot exceed 63 characters. This field is immutable.
    
    This field is beta-level. The job controller accepts setting the field when the feature gate JobManagedBy is enabled (enabled by default).
    """
    manual_selector: bool
    """ manualSelector controls generation of pod labels and pod selectors. Leave `manualSelector` unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector """
    max_failed_indexes: int
    """ Specifies the maximal number of failed indexes before marking the Job as failed, when backoffLimitPerIndex is set. Once the number of failed indexes exceeds this number the entire Job is marked as Failed and its execution is terminated. When left as null the job continues execution of all of its indexes and is marked with the `Complete` Job condition. It can only be specified when backoffLimitPerIndex is set. It can be null or up to completions. It is required and must be less than or equal to 10^4 when is completions greater than 10^5. """
    parallelism: int
    """ Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """
    pod_failure_policy: PodFailurePolicy
    """ Specifies the policy of handling failed pods. In particular, it allows to specify the set of actions and conditions which need to be satisfied to take the associated action. If empty, the default behaviour applies - the counter of failed pods, represented by the jobs's .status.failed field, is incremented and it is checked against the backoffLimit. This field cannot be used in combination with restartPolicy=OnFailure. """
    pod_replacement_policy: str
    """
    podReplacementPolicy specifies when to create replacement Pods. Possible values are: - TerminatingOrFailed means that we recreate pods
      when they are terminating (has a metadata.deletionTimestamp) or failed.
    - Failed means to wait until a previously created Pod is fully terminated (has phase
      Failed or Succeeded) before creating a replacement Pod.
    
    When using podFailurePolicy, Failed is the the only allowed value. TerminatingOrFailed and Failed are allowed values when podFailurePolicy is not in use. This is an beta field. To use this, enable the JobPodReplacementPolicy feature toggle. This is on by default.
    """
    selector: meta.LabelSelector
    """ A label query over pods that should match the pod count. Normally, the system sets this field for you. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors """
    success_policy: SuccessPolicy
    """ successPolicy specifies the policy when the Job can be declared as succeeded. If empty, the default behavior applies - the Job is declared as succeeded only when the number of succeeded pods equals to the completions. When the field is specified, it must be immutable and works only for the Indexed Jobs. Once the Job meets the SuccessPolicy, the lingering pods are terminated. """
    suspend: bool
    """ suspend specifies whether the Job controller should create Pods or not. If a Job is created with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods associated with this Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds timer too. Defaults to false. """
    template: core.PodTemplateSpec
    """ Describes the pod that will be created when executing a job. The only allowed template.spec.restartPolicy values are "Never" or "OnFailure". More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ """
    ttl_seconds_after_finished: int
    """ ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. """

    def __init__(
        self,
        active_deadline_seconds: int = None,
        backoff_limit: int = None,
        backoff_limit_per_index: int = None,
        completion_mode: str = None,
        completions: int = None,
        managed_by: str = None,
        manual_selector: bool = None,
        max_failed_indexes: int = None,
        parallelism: int = None,
        pod_failure_policy: PodFailurePolicy = None,
        pod_replacement_policy: str = None,
        selector: meta.LabelSelector = None,
        success_policy: SuccessPolicy = None,
        suspend: bool = None,
        template: core.PodTemplateSpec = None,
        ttl_seconds_after_finished: int = None,
    ):
        super().__init__(
            active_deadline_seconds=active_deadline_seconds,
            backoff_limit=backoff_limit,
            backoff_limit_per_index=backoff_limit_per_index,
            completion_mode=completion_mode,
            completions=completions,
            managed_by=managed_by,
            manual_selector=manual_selector,
            max_failed_indexes=max_failed_indexes,
            parallelism=parallelism,
            pod_failure_policy=pod_failure_policy,
            pod_replacement_policy=pod_replacement_policy,
            selector=selector,
            success_policy=success_policy,
            suspend=suspend,
            template=template,
            ttl_seconds_after_finished=ttl_seconds_after_finished,
        )


class JobTemplateSpec(KubernetesObject):
    """JobTemplateSpec describes the data a Job should have when created from a template"""

    __slots__ = ()

    _api_version_ = "batch/v1"

    metadata: meta.ObjectMeta
    """ Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: JobSpec
    """ Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, metadata: meta.ObjectMeta = None, spec: JobSpec = None):
        super().__init__(metadata=metadata, spec=spec)


class CronJobSpec(KubernetesObject):
    """CronJobSpec describes how the job execution will look like and when it will actually run."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["job_template", "schedule"]

    concurrency_policy: str
    """
    Specifies how to treat concurrent executions of a Job. Valid values are:
    
    - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - "Replace": cancels currently running job and replaces it with a new one
    """
    failed_jobs_history_limit: int
    """ The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1. """
    job_template: JobTemplateSpec
    """ Specifies the job that will be created when executing a CronJob. """
    schedule: str
    """ The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron. """
    starting_deadline_seconds: int
    """ Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones. """
    successful_jobs_history_limit: int
    """ The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3. """
    suspend: bool
    """ This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false. """
    time_zone: str
    """ The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones """

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
    """CronJob represents the configuration of a single cron job."""

    __slots__ = ()

    _api_version_ = "batch/v1"
    _api_group_ = "batch"
    _kind_ = "CronJob"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: CronJobSpec
    """ Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: CronJobSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class CronJobStatus(KubernetesObject):
    """CronJobStatus represents the current state of a cron job."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    active: list[core.ObjectReference]
    """ A list of pointers to currently running jobs. """
    last_schedule_time: meta.Time
    """ Information when was the last time the job was successfully scheduled. """
    last_successful_time: meta.Time
    """ Information when was the last time the job successfully completed. """

    def __init__(
        self, active: list[core.ObjectReference] = None, last_schedule_time: meta.Time = None, last_successful_time: meta.Time = None
    ):
        super().__init__(active=active, last_schedule_time=last_schedule_time, last_successful_time=last_successful_time)


class Job(KubernetesApiResource):
    """Job represents the configuration of a single job."""

    __slots__ = ()

    _api_version_ = "batch/v1"
    _api_group_ = "batch"
    _kind_ = "Job"
    _scope_ = "namespace"

    metadata: meta.ObjectMeta
    """ Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: JobSpec
    """ Specification of the desired behavior of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status """

    def __init__(self, name: str, namespace: str = None, metadata: meta.ObjectMeta = None, spec: JobSpec = None):
        super().__init__(name, namespace, metadata=metadata, spec=spec)


class JobCondition(KubernetesObject):
    """JobCondition describes current state of a job."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    _required_ = ["status", "type"]

    last_probe_time: meta.Time
    """ Last time the condition was checked. """
    last_transition_time: meta.Time
    """ Last time the condition transit from one status to another. """
    message: str
    """ Human readable message indicating details about last transition. """
    reason: str
    """ (brief) reason for the condition's last transition. """
    status: str
    """ Status of the condition, one of True, False, Unknown. """
    type: str
    """ Type of job condition, Complete or Failed. """

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


class UncountedTerminatedPods(KubernetesObject):
    """UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    failed: list[str]
    """ failed holds UIDs of failed Pods. """
    succeeded: list[str]
    """ succeeded holds UIDs of succeeded Pods. """

    def __init__(self, failed: list[str] = None, succeeded: list[str] = None):
        super().__init__(failed=failed, succeeded=succeeded)


class JobStatus(KubernetesObject):
    """JobStatus represents the current state of a Job."""

    __slots__ = ()

    _api_version_ = "batch/v1"

    active: int
    """ The number of pending and running pods which are not terminating (without a deletionTimestamp). The value is zero for finished jobs. """
    completed_indexes: str
    """ completedIndexes holds the completed indexes when .spec.completionMode = "Indexed" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7". """
    completion_time: meta.Time
    """ Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is set when the job finishes successfully, and only then. The value cannot be updated or removed. The value indicates the same or later point in time as the startTime field. """
    conditions: list[JobCondition]
    """
    The latest available observations of an object's current state. When a Job fails, one of the conditions will have type "Failed" and status true. When a Job is suspended, one of the conditions will have type "Suspended" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type "Complete" and status true.
    
    A job is considered finished when it is in a terminal condition, either "Complete" or "Failed". A Job cannot have both the "Complete" and "Failed" conditions. Additionally, it cannot be in the "Complete" and "FailureTarget" conditions. The "Complete", "Failed" and "FailureTarget" conditions cannot be disabled.
    
    More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/
    """
    failed: int
    """ The number of pods which reached phase Failed. The value increases monotonically. """
    failed_indexes: str
    """ FailedIndexes holds the failed indexes when spec.backoffLimitPerIndex is set. The indexes are represented in the text format analogous as for the `completedIndexes` field, ie. they are kept as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the failed indexes are 1, 3, 4, 5 and 7, they are represented as "1,3-5,7". The set of failed indexes cannot overlap with the set of completed indexes. """
    ready: int
    """ The number of active pods which have a Ready condition and are not terminating (without a deletionTimestamp). """
    start_time: meta.Time
    """
    Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.
    
    Once set, the field can only be removed when the job is suspended. The field cannot be modified while the job is unsuspended or finished.
    """
    succeeded: int
    """ The number of pods which reached phase Succeeded. The value increases monotonically for a given spec. However, it may decrease in reaction to scale down of elastic indexed jobs. """
    terminating: int
    """
    The number of pods which are terminating (in phase Pending or Running and have a deletionTimestamp).
    
    This field is beta-level. The job controller populates the field when the feature gate JobPodReplacementPolicy is enabled (enabled by default).
    """
    uncounted_terminated_pods: UncountedTerminatedPods
    """
    uncountedTerminatedPods holds the UIDs of Pods that have terminated but the job controller hasn't yet accounted for in the status counters.
    
    The job controller creates pods with a finalizer. When a pod terminates (succeeded or failed), the controller does three steps to account for it in the job status:
    
    1. Add the pod UID to the arrays in this field. 2. Remove the pod finalizer. 3. Remove the pod UID from the arrays while increasing the corresponding
        counter.
    
    Old jobs might not be tracked using this field, in which case the field remains null. The structure is empty for finished jobs.
    """

    def __init__(
        self,
        active: int = None,
        completed_indexes: str = None,
        completion_time: meta.Time = None,
        conditions: list[JobCondition] = None,
        failed: int = None,
        failed_indexes: str = None,
        ready: int = None,
        start_time: meta.Time = None,
        succeeded: int = None,
        terminating: int = None,
        uncounted_terminated_pods: UncountedTerminatedPods = None,
    ):
        super().__init__(
            active=active,
            completed_indexes=completed_indexes,
            completion_time=completion_time,
            conditions=conditions,
            failed=failed,
            failed_indexes=failed_indexes,
            ready=ready,
            start_time=start_time,
            succeeded=succeeded,
            terminating=terminating,
            uncounted_terminated_pods=uncounted_terminated_pods,
        )
