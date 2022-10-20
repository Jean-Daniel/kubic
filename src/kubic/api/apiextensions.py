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
    conversion_review_versions: t.List[str]

    def __init__(self, client_config: WebhookClientConfig = None, conversion_review_versions: t.List[str] = None):
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

    categories: t.List[str]
    kind: str
    list_kind: str
    plural: str
    short_names: t.List[str]
    singular: str

    def __init__(
        self,
        categories: t.List[str] = None,
        kind: str = None,
        list_kind: str = None,
        plural: str = None,
        short_names: t.List[str] = None,
        singular: str = None,
    ):
        super().__init__(categories=categories, kind=kind, list_kind=list_kind, plural=plural, short_names=short_names, singular=singular)


class ExternalDocumentation(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    description: str
    url: str

    def __init__(self, description: str = None, url: str = None):
        super().__init__(description=description, url=url)


class ValidationRule(KubernetesObject):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["rule"]

    message: str
    rule: str

    def __init__(self, message: str = None, rule: str = None):
        super().__init__(message=message, rule=rule)


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
    additional_items: Any
    additional_properties: Any
    all_of: t.List["JSONSchemaProps"]
    any_of: t.List["JSONSchemaProps"]
    default: Any
    definitions: t.Dict[str, "JSONSchemaProps"]
    dependencies: t.Dict[str, Any]
    description: str
    enum: t.List[Any]
    example: Any
    exclusive_maximum: bool
    exclusive_minimum: bool
    external_docs: ExternalDocumentation
    format: str
    id: str
    items: Any
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
    one_of: t.List["JSONSchemaProps"]
    pattern: str
    pattern_properties: t.Dict[str, "JSONSchemaProps"]
    properties: t.Dict[str, "JSONSchemaProps"]
    required: t.List[str]
    title: str
    type: str
    unique_items: bool
    x_kubernetes_embedded_resource: bool
    x_kubernetes_int_or_string: bool
    x_kubernetes_list_map_keys: t.List[str]
    x_kubernetes_list_type: str
    x_kubernetes_map_type: str
    x_kubernetes_preserve_unknown_fields: bool
    x_kubernetes_validations: t.List[ValidationRule]

    def __init__(
        self,
        ref_: str = None,
        schema_: str = None,
        additional_items: Any = None,
        additional_properties: Any = None,
        all_of: t.List["JSONSchemaProps"] = None,
        any_of: t.List["JSONSchemaProps"] = None,
        default: Any = None,
        definitions: t.Dict[str, "JSONSchemaProps"] = None,
        dependencies: t.Dict[str, Any] = None,
        description: str = None,
        enum: t.List[Any] = None,
        example: Any = None,
        exclusive_maximum: bool = None,
        exclusive_minimum: bool = None,
        external_docs: ExternalDocumentation = None,
        format: str = None,
        id: str = None,
        items: Any = None,
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
        one_of: t.List["JSONSchemaProps"] = None,
        pattern: str = None,
        pattern_properties: t.Dict[str, "JSONSchemaProps"] = None,
        properties: t.Dict[str, "JSONSchemaProps"] = None,
        required: t.List[str] = None,
        title: str = None,
        type: str = None,
        unique_items: bool = None,
        x_kubernetes_embedded_resource: bool = None,
        x_kubernetes_int_or_string: bool = None,
        x_kubernetes_list_map_keys: t.List[str] = None,
        x_kubernetes_list_type: str = None,
        x_kubernetes_map_type: str = None,
        x_kubernetes_preserve_unknown_fields: bool = None,
        x_kubernetes_validations: t.List[ValidationRule] = None,
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


CustomResourceSubresourceStatus: t.TypeAlias = t.Dict[str, Any]


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

    additional_printer_columns: t.List[CustomResourceColumnDefinition]
    deprecated: bool
    deprecation_warning: str
    name: str
    schema: CustomResourceValidation
    served: bool
    storage: bool
    subresources: CustomResourceSubresources

    def __init__(
        self,
        additional_printer_columns: t.List[CustomResourceColumnDefinition] = None,
        deprecated: bool = None,
        deprecation_warning: str = None,
        name: str = None,
        schema: CustomResourceValidation = None,
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
    versions: t.List[CustomResourceDefinitionVersion]

    def __init__(
        self,
        conversion: CustomResourceConversion = None,
        group: str = None,
        names: CustomResourceDefinitionNames = None,
        preserve_unknown_fields: bool = None,
        scope: str = None,
        versions: t.List[CustomResourceDefinitionVersion] = None,
    ):
        super().__init__(
            conversion=conversion, group=group, names=names, preserve_unknown_fields=preserve_unknown_fields, scope=scope, versions=versions
        )


class CustomResourceDefinition(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"
    _kind_ = "CustomResourceDefinition"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    spec: CustomResourceDefinitionSpec

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CustomResourceDefinitionSpec = None):
        super().__init__("apiextensions.k8s.io/v1", "CustomResourceDefinition", name, "", metadata=metadata, spec=spec)
