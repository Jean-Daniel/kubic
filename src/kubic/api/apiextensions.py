import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class CustomResourceColumnDefinition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["json_path", "name", "type"]

    description: str
    format: str
    json_path: str
    name: str
    priority: int
    type: str

    def __init__(
        self, description: str = None, format: str = None, json_path: str = None, name: str = None, priority: int = None, type: str = None
    ):
        super().__init__(description=description, format=format, json_path=json_path, name=name, priority=priority, type=type)


class ServiceReference(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["name", "namespace"]

    name: str
    namespace: str
    path: str
    port: int

    def __init__(self, name: str = None, namespace: str = None, path: str = None, port: int = None):
        super().__init__(name=name, namespace=namespace, path=path, port=port)


class WebhookClientConfig(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    ca_bundle: core.Base64
    service: ServiceReference
    url: str

    def __init__(self, ca_bundle: core.Base64 = None, service: ServiceReference = None, url: str = None):
        super().__init__(ca_bundle=ca_bundle, service=service, url=url)


class WebhookConversion(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["conversion_review_versions"]

    client_config: WebhookClientConfig
    conversion_review_versions: list[str]

    def __init__(self, client_config: WebhookClientConfig = None, conversion_review_versions: list[str] = None):
        super().__init__(client_config=client_config, conversion_review_versions=conversion_review_versions)


class CustomResourceConversion(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["strategy"]

    strategy: str
    webhook: WebhookConversion

    def __init__(self, strategy: str = None, webhook: WebhookConversion = None):
        super().__init__(strategy=strategy, webhook=webhook)


class CustomResourceDefinitionNames(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["kind", "plural"]

    categories: list[str]
    kind: str
    list_kind: str
    plural: str
    short_names: list[str]
    singular: str

    def __init__(
        self,
        categories: list[str] = None,
        kind: str = None,
        list_kind: str = None,
        plural: str = None,
        short_names: list[str] = None,
        singular: str = None,
    ):
        super().__init__(categories=categories, kind=kind, list_kind=list_kind, plural=plural, short_names=short_names, singular=singular)


JSONSchemaPropsOrBool: t.TypeAlias = "JSONSchemaProps" | bool


JSON: t.TypeAlias = bool | int | float | str | list["JSON"], dict[str, "JSON"] | None


JSONSchemaPropsOrStringArray: t.TypeAlias = "JSONSchemaProps" | list[str]


class ExternalDocumentation(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    description: str
    url: str

    def __init__(self, description: str = None, url: str = None):
        super().__init__(description=description, url=url)


JSONSchemaPropsOrArray: t.TypeAlias = "JSONSchemaProps" | list["JSONSchemaProps"]


class ValidationRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["rule"]

    field_path: str
    message: str
    message_expression: str
    optional_old_self: bool
    reason: str
    rule: str

    def __init__(
        self,
        field_path: str = None,
        message: str = None,
        message_expression: str = None,
        optional_old_self: bool = None,
        reason: str = None,
        rule: str = None,
    ):
        super().__init__(
            field_path=field_path,
            message=message,
            message_expression=message_expression,
            optional_old_self=optional_old_self,
            reason=reason,
            rule=rule,
        )


class JSONSchemaProps(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _field_names_ = {
        "ref_": "$ref",
        "schema_": "$schema",
        "x_kubernetes_embedded_resource": "x-kubernetes-embedded-resource",
        "x_kubernetes_int_or_string": "x-kubernetes-int-or-string",
        "x_kubernetes_list_map_keys": "x-kubernetes-list-map-keys",
        "x_kubernetes_list_type": "x-kubernetes-list-type",
        "x_kubernetes_map_type": "x-kubernetes-map-type",
        "x_kubernetes_preserve_unknown_fields": "x-kubernetes-preserve-unknown-fields",
        "x_kubernetes_validations": "x-kubernetes-validations",
    }
    _revfield_names_ = {
        "$ref": "ref_",
        "$schema": "schema_",
        "not": "not_",
        "x-kubernetes-embedded-resource": "x_kubernetes_embedded_resource",
        "x-kubernetes-int-or-string": "x_kubernetes_int_or_string",
        "x-kubernetes-list-map-keys": "x_kubernetes_list_map_keys",
        "x-kubernetes-list-type": "x_kubernetes_list_type",
        "x-kubernetes-map-type": "x_kubernetes_map_type",
        "x-kubernetes-preserve-unknown-fields": "x_kubernetes_preserve_unknown_fields",
        "x-kubernetes-validations": "x_kubernetes_validations",
    }

    ref_: str
    schema_: str
    additional_items: JSONSchemaPropsOrBool
    additional_properties: JSONSchemaPropsOrBool
    all_of: list["JSONSchemaProps"]
    any_of: list["JSONSchemaProps"]
    default: JSON
    definitions: dict[str, "JSONSchemaProps"]
    dependencies: dict[str, JSONSchemaPropsOrStringArray]
    description: str
    enum: list[JSON]
    example: JSON
    exclusive_maximum: bool
    exclusive_minimum: bool
    external_docs: ExternalDocumentation
    format: str
    id: str
    items: JSONSchemaPropsOrArray
    max_items: int
    max_length: int
    max_properties: int
    maximum: float
    min_items: int
    min_length: int
    min_properties: int
    minimum: float
    multiple_of: float
    not_: "JSONSchemaProps"
    nullable: bool
    one_of: list["JSONSchemaProps"]
    pattern: str
    pattern_properties: dict[str, "JSONSchemaProps"]
    properties: dict[str, "JSONSchemaProps"]
    required: list[str]
    title: str
    type: str
    unique_items: bool
    x_kubernetes_embedded_resource: bool
    x_kubernetes_int_or_string: bool
    x_kubernetes_list_map_keys: list[str]
    x_kubernetes_list_type: str
    x_kubernetes_map_type: str
    x_kubernetes_preserve_unknown_fields: bool
    x_kubernetes_validations: list[ValidationRule]

    def __init__(
        self,
        ref_: str = None,
        schema_: str = None,
        additional_items: JSONSchemaPropsOrBool = None,
        additional_properties: JSONSchemaPropsOrBool = None,
        all_of: list["JSONSchemaProps"] = None,
        any_of: list["JSONSchemaProps"] = None,
        default: JSON = None,
        definitions: dict[str, "JSONSchemaProps"] = None,
        dependencies: dict[str, JSONSchemaPropsOrStringArray] = None,
        description: str = None,
        enum: list[JSON] = None,
        example: JSON = None,
        exclusive_maximum: bool = None,
        exclusive_minimum: bool = None,
        external_docs: ExternalDocumentation = None,
        format: str = None,
        id: str = None,
        items: JSONSchemaPropsOrArray = None,
        max_items: int = None,
        max_length: int = None,
        max_properties: int = None,
        maximum: float = None,
        min_items: int = None,
        min_length: int = None,
        min_properties: int = None,
        minimum: float = None,
        multiple_of: float = None,
        not_: "JSONSchemaProps" = None,
        nullable: bool = None,
        one_of: list["JSONSchemaProps"] = None,
        pattern: str = None,
        pattern_properties: dict[str, "JSONSchemaProps"] = None,
        properties: dict[str, "JSONSchemaProps"] = None,
        required: list[str] = None,
        title: str = None,
        type: str = None,
        unique_items: bool = None,
        x_kubernetes_embedded_resource: bool = None,
        x_kubernetes_int_or_string: bool = None,
        x_kubernetes_list_map_keys: list[str] = None,
        x_kubernetes_list_type: str = None,
        x_kubernetes_map_type: str = None,
        x_kubernetes_preserve_unknown_fields: bool = None,
        x_kubernetes_validations: list[ValidationRule] = None,
    ):
        super().__init__(
            ref_=ref_,
            schema_=schema_,
            additional_items=additional_items,
            additional_properties=additional_properties,
            all_of=all_of,
            any_of=any_of,
            default=default,
            definitions=definitions,
            dependencies=dependencies,
            description=description,
            enum=enum,
            example=example,
            exclusive_maximum=exclusive_maximum,
            exclusive_minimum=exclusive_minimum,
            external_docs=external_docs,
            format=format,
            id=id,
            items=items,
            max_items=max_items,
            max_length=max_length,
            max_properties=max_properties,
            maximum=maximum,
            min_items=min_items,
            min_length=min_length,
            min_properties=min_properties,
            minimum=minimum,
            multiple_of=multiple_of,
            not_=not_,
            nullable=nullable,
            one_of=one_of,
            pattern=pattern,
            pattern_properties=pattern_properties,
            properties=properties,
            required=required,
            title=title,
            type=type,
            unique_items=unique_items,
            x_kubernetes_embedded_resource=x_kubernetes_embedded_resource,
            x_kubernetes_int_or_string=x_kubernetes_int_or_string,
            x_kubernetes_list_map_keys=x_kubernetes_list_map_keys,
            x_kubernetes_list_type=x_kubernetes_list_type,
            x_kubernetes_map_type=x_kubernetes_map_type,
            x_kubernetes_preserve_unknown_fields=x_kubernetes_preserve_unknown_fields,
            x_kubernetes_validations=x_kubernetes_validations,
        )


class CustomResourceValidation(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _field_names_ = {
        "openapi_v3_schema": "openAPIV3Schema",
    }
    _revfield_names_ = {
        "openAPIV3Schema": "openapi_v3_schema",
    }

    openapi_v3_schema: JSONSchemaProps

    def __init__(self, openapi_v3_schema: JSONSchemaProps = None):
        super().__init__(openapi_v3_schema=openapi_v3_schema)


class SelectableField(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["json_path"]

    json_path: str

    def __init__(self, json_path: str = None):
        super().__init__(json_path=json_path)


class CustomResourceSubresourceScale(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["spec_replicas_path", "status_replicas_path"]

    label_selector_path: str
    spec_replicas_path: str
    status_replicas_path: str

    def __init__(self, label_selector_path: str = None, spec_replicas_path: str = None, status_replicas_path: str = None):
        super().__init__(
            label_selector_path=label_selector_path, spec_replicas_path=spec_replicas_path, status_replicas_path=status_replicas_path
        )


CustomResourceSubresourceStatus: t.TypeAlias = dict[str, t.Any]


class CustomResourceSubresources(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    scale: CustomResourceSubresourceScale
    status: CustomResourceSubresourceStatus

    def __init__(self, scale: CustomResourceSubresourceScale = None, status: CustomResourceSubresourceStatus = None):
        super().__init__(scale=scale, status=status)


class CustomResourceDefinitionVersion(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["name", "served", "storage"]

    additional_printer_columns: list[CustomResourceColumnDefinition]
    deprecated: bool
    deprecation_warning: str
    name: str
    schema: CustomResourceValidation
    selectable_fields: list[SelectableField]
    served: bool
    storage: bool
    subresources: CustomResourceSubresources

    def __init__(
        self,
        additional_printer_columns: list[CustomResourceColumnDefinition] = None,
        deprecated: bool = None,
        deprecation_warning: str = None,
        name: str = None,
        schema: CustomResourceValidation = None,
        selectable_fields: list[SelectableField] = None,
        served: bool = None,
        storage: bool = None,
        subresources: CustomResourceSubresources = None,
    ):
        super().__init__(
            additional_printer_columns=additional_printer_columns,
            deprecated=deprecated,
            deprecation_warning=deprecation_warning,
            name=name,
            schema=schema,
            selectable_fields=selectable_fields,
            served=served,
            storage=storage,
            subresources=subresources,
        )


class CustomResourceDefinitionSpec(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["group", "names", "scope", "versions"]

    conversion: CustomResourceConversion
    group: str
    names: CustomResourceDefinitionNames
    preserve_unknown_fields: bool
    scope: str
    versions: list[CustomResourceDefinitionVersion]

    def __init__(
        self,
        conversion: CustomResourceConversion = None,
        group: str = None,
        names: CustomResourceDefinitionNames = None,
        preserve_unknown_fields: bool = None,
        scope: str = None,
        versions: list[CustomResourceDefinitionVersion] = None,
    ):
        super().__init__(
            conversion=conversion, group=group, names=names, preserve_unknown_fields=preserve_unknown_fields, scope=scope, versions=versions
        )


class CustomResourceDefinition(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"
    _api_group_ = "apiextensions.k8s.io"
    _kind_ = "CustomResourceDefinition"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CustomResourceDefinitionSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CustomResourceDefinitionSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CustomResourceDefinitionCondition(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    message: str
    reason: str
    status: str
    type: str

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class CustomResourceDefinitionStatus(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    accepted_names: CustomResourceDefinitionNames
    conditions: list[CustomResourceDefinitionCondition]
    stored_versions: list[str]

    def __init__(
        self,
        accepted_names: CustomResourceDefinitionNames = None,
        conditions: list[CustomResourceDefinitionCondition] = None,
        stored_versions: list[str] = None,
    ):
        super().__init__(accepted_names=accepted_names, conditions=conditions, stored_versions=stored_versions)
