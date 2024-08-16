import typing as t

from kubic import KubernetesApiResource, KubernetesObject
from . import core, meta


class CustomResourceColumnDefinition(KubernetesObject):
    """CustomResourceColumnDefinition specifies a column for server side printing."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["json_path", "name", "type"]

    description: str
    """ description is a human readable description of this column. """
    format: str
    """ format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """
    json_path: str
    """ jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column. """
    name: str
    """ name is a human readable name for the column. """
    priority: int
    """ priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0. """
    type: str
    """ type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. """

    def __init__(
        self, description: str = None, format: str = None, json_path: str = None, name: str = None, priority: int = None, type: str = None
    ):
        super().__init__(description=description, format=format, json_path=json_path, name=name, priority=priority, type=type)


class ServiceReference(KubernetesObject):
    """ServiceReference holds a reference to Service.legacy.k8s.io"""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["name", "namespace"]

    name: str
    """ name is the name of the service. Required """
    namespace: str
    """ namespace is the namespace of the service. Required """
    path: str
    """ path is an optional URL path at which the webhook will be contacted. """
    port: int
    """ port is an optional service port at which the webhook will be contacted. `port` should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility. """

    def __init__(self, name: str = None, namespace: str = None, path: str = None, port: int = None):
        super().__init__(name=name, namespace=namespace, path=path, port=port)


class WebhookClientConfig(KubernetesObject):
    """WebhookClientConfig contains the information to make a TLS connection with the webhook."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    ca_bundle: core.Base64
    """ caBundle is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. """
    service: ServiceReference
    """
    service is a reference to the service for this webhook. Either service or url must be specified.
    
    If the webhook is running within the cluster, then you should use `service`.
    """
    url: str
    """
    url gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.
    
    The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.
    
    Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.
    
    The scheme must be "https"; the URL must begin with "https://".
    
    A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.
    
    Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.
    """

    def __init__(self, ca_bundle: core.Base64 = None, service: ServiceReference = None, url: str = None):
        super().__init__(ca_bundle=ca_bundle, service=service, url=url)


class WebhookConversion(KubernetesObject):
    """WebhookConversion describes how to call a conversion webhook"""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["conversion_review_versions"]

    client_config: WebhookClientConfig
    """ clientConfig is the instructions for how to call the webhook if strategy is `Webhook`. """
    conversion_review_versions: list[str]
    """ conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. """

    def __init__(self, client_config: WebhookClientConfig = None, conversion_review_versions: list[str] = None):
        super().__init__(client_config=client_config, conversion_review_versions=conversion_review_versions)


class CustomResourceConversion(KubernetesObject):
    """CustomResourceConversion describes how to convert different versions of a CR."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["strategy"]

    strategy: str
    """
    strategy specifies how custom resources are converted between versions. Allowed values are: - `"None"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `"Webhook"`: API Server will call to an external webhook to do the conversion. Additional information
      is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set.
    """
    webhook: WebhookConversion
    """ webhook describes how to call the conversion webhook. Required when `strategy` is set to `"Webhook"`. """

    def __init__(self, strategy: str = None, webhook: WebhookConversion = None):
        super().__init__(strategy=strategy, webhook=webhook)


class CustomResourceDefinitionNames(KubernetesObject):
    """CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition"""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["kind", "plural"]

    categories: list[str]
    """ categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`. """
    kind: str
    """ kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls. """
    list_kind: str
    """ listKind is the serialized kind of the list for this resource. Defaults to "`kind`List". """
    plural: str
    """ plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase. """
    short_names: list[str]
    """ shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase. """
    singular: str
    """ singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`. """

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


JSONSchemaPropsOrBool: t.TypeAlias = t.Union["JSONSchemaProps", bool]
""" Represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. """


JSON: t.TypeAlias = bool | int | float | str | list["JSON"], dict[str, "JSON"] | None
""" Represents any valid JSON value. """


JSONSchemaPropsOrStringArray: t.TypeAlias = t.Union["JSONSchemaProps", list[str]]
""" Represents a JSONSchemaProps or a string array. """


class ExternalDocumentation(KubernetesObject):
    """ExternalDocumentation allows referencing an external resource for extended documentation."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    description: str
    url: str

    def __init__(self, description: str = None, url: str = None):
        super().__init__(description=description, url=url)


JSONSchemaPropsOrArray: t.TypeAlias = t.Union["JSONSchemaProps", list["JSONSchemaProps"]]
""" Represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes. """


class ValidationRule(KubernetesObject):
    """ValidationRule describes a validation rule written in the CEL expression language."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["rule"]

    field_path: str
    """ fieldPath represents the field path returned when the validation fails. It must be a relative JSON path (i.e. with array notation) scoped to the location of this x-kubernetes-validations extension in the schema and refer to an existing field. e.g. when validation checks if a specific attribute `foo` under a map `testMap`, the fieldPath could be set to `.testMap.foo` If the validation checks two lists must have unique attributes, the fieldPath could be set to either of the list: e.g. `.testList` It does not support list numeric index. It supports child operation to refer to an existing field currently. Refer to [JSONPath support in Kubernetes](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for more info. Numeric index of array is not supported. For field name which contains special characters, use `['specialName']` to refer the field name. e.g. for attribute `foo.34$` appears in a list `testList`, the fieldPath could be set to `.testList['foo.34$']` """
    message: str
    """ Message represents the message displayed when validation fails. The message is required if the Rule contains line breaks. The message must not contain line breaks. If unset, the message is "failed rule: {Rule}". e.g. "must be a URL with the host matching spec.host" """
    message_expression: str
    """ MessageExpression declares a CEL expression that evaluates to the validation failure message that is returned when this rule fails. Since messageExpression is used as a failure message, it must evaluate to a string. If both message and messageExpression are present on a rule, then messageExpression will be used if validation fails. If messageExpression results in a runtime error, the runtime error is logged, and the validation failure message is produced as if the messageExpression field were unset. If messageExpression evaluates to an empty string, a string with only spaces, or a string that contains line breaks, then the validation failure message will also be produced as if the messageExpression field were unset, and the fact that messageExpression produced an empty string/string with only spaces/string with line breaks will be logged. messageExpression has access to all the same variables as the rule; the only difference is the return type. Example: "x must be less than max ("+string(self.max)+")" """
    optional_old_self: bool
    """
    optionalOldSelf is used to opt a transition rule into evaluation even when the object is first created, or if the old object is missing the value.
    
    When enabled `oldSelf` will be a CEL optional whose value will be `None` if there is no old value, or when the object is initially created.
    
    You may check for presence of oldSelf using `oldSelf.hasValue()` and unwrap it after checking using `oldSelf.value()`. Check the CEL documentation for Optional types for more information: https://pkg.go.dev/github.com/google/cel-go/cel#OptionalTypes
    
    May not be set unless `oldSelf` is used in `rule`.
    """
    reason: str
    """ reason provides a machine-readable validation failure reason that is returned to the caller when a request fails this validation rule. The HTTP status code returned to the caller will match the reason of the reason of the first failed validation rule. The currently supported reasons are: "FieldValueInvalid", "FieldValueForbidden", "FieldValueRequired", "FieldValueDuplicate". If not set, default to use "FieldValueInvalid". All future added reasons must be accepted by clients when reading this value and unknown reasons should be treated as FieldValueInvalid. """
    rule: str
    """
    Rule represents the expression which will be evaluated by CEL. ref: https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-validations extension in the schema. The `self` variable in the CEL expression is bound to the scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {"rule": "self.status.actual <= self.spec.maxDesired"}
    
    If the Rule is scoped to an object with properties, the accessible properties of the object are field selectable via `self.field` and field presence can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self` and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value. Examples: - Rule scoped to a map of objects: {"rule": "self.components['Widget'].priority < 10"} - Rule scoped to a list of integers: {"rule": "self.values.all(value, value >= 0 && value < 100)"} - Rule scoped to a string value: {"rule": "self.startsWith('kube')"}
    
    The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the root of the object and from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are accessible.
    
    Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property schema is of an "unknown type". An "unknown type" is recursively defined as:
      - A schema with no type and x-kubernetes-preserve-unknown-fields set to true
      - An array where the items schema is of an "unknown type"
      - An object where the additionalProperties schema is of an "unknown type"
    
    Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:
    	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if",
    	  "import", "let", "loop", "package", "namespace", "return".
    Examples:
      - Rule accessing a property named "namespace": {"rule": "self.__namespace__ > 0"}
      - Rule accessing a property named "x-prop": {"rule": "self.x__dash__prop > 0"}
      - Rule accessing a property named "redact__d": {"rule": "self.redact__underscores__d > 0"}
    
    Equality on arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:
      - 'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and
        non-intersecting elements in `Y` are appended, retaining their partial order.
      - 'map': `X + Y` performs a merge where the array positions of all keys in `X` are preserved but the values
        are overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with
        non-intersecting keys are appended, retaining their partial order.
    
    If `rule` makes use of the `oldSelf` variable it is implicitly a `transition rule`.
    
    By default, the `oldSelf` variable is the same type as `self`. When `optionalOldSelf` is true, the `oldSelf` variable is a CEL optional
     variable whose value() is the same type as `self`.
    See the documentation for the `optionalOldSelf` field for details.
    
    Transition rules by default are applied only on UPDATE requests and are skipped if an old value could not be found. You can opt a transition rule into unconditional evaluation by setting `optionalOldSelf` to true.
    """

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
    """JSONSchemaProps is a JSON-Schema following Specification Draft 4 (http://json-schema.org/)."""

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
    """ default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false. """
    definitions: dict[str, "JSONSchemaProps"]
    dependencies: dict[str, JSONSchemaPropsOrStringArray]
    description: str
    enum: list[JSON]
    example: JSON
    exclusive_maximum: bool
    exclusive_minimum: bool
    external_docs: ExternalDocumentation
    format: str
    """
    format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:
    
    - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like "0321751043" or "978-0321751041" - isbn10: an ISBN10 number string like "0321751043" - isbn13: an ISBN13 number string like "978-0321751041" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: an hexadecimal color code like "#FFFFFF: following the regex ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like "rgb(255,255,2559" - byte: base64 encoded binary data - password: any kind of string - date: a date string like "2006-01-02" as defined by full-date in RFC3339 - duration: a duration string like "22 ns" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like "2014-12-15T19:30:20.000Z" as defined by date-time in RFC3339.
    """
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
    """ x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata). """
    x_kubernetes_int_or_string: bool
    """
    x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:
    
    1) anyOf:
       - type: integer
       - type: string
    2) allOf:
       - anyOf:
         - type: integer
         - type: string
       - ... zero or more
    """
    x_kubernetes_list_map_keys: list[str]
    """
    x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type `map` by specifying the keys used as the index of the map.
    
    This tag MUST only be used on lists that have the "x-kubernetes-list-type" extension set to "map". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).
    
    The properties specified must either be required or have a default value, to ensure those properties are present for all list items.
    """
    x_kubernetes_list_type: str
    """
    x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:
    
    1) `atomic`: the list is treated as a single entity, like a scalar.
         Atomic lists will be entirely replaced when updated. This extension
         may be used on any type of list (struct, scalar, ...).
    2) `set`:
         Sets are lists that must not have multiple items with the same value. Each
         value must be a scalar, an object with x-kubernetes-map-type `atomic` or an
         array with x-kubernetes-list-type `atomic`.
    3) `map`:
         These lists are like maps in that their elements have a non-index key
         used to identify them. Order is preserved upon merge. The map tag
         must only be used on a list with elements of type object.
    Defaults to atomic for arrays.
    """
    x_kubernetes_map_type: str
    """
    x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:
    
    1) `granular`:
         These maps are actual maps (key-value pairs) and each fields are independent
         from each other (they can each be manipulated by separate actors). This is
         the default behaviour for all maps.
    2) `atomic`: the list is treated as a single entity, like a scalar.
         Atomic maps will be entirely replaced when updated.
    """
    x_kubernetes_preserve_unknown_fields: bool
    """ x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. """
    x_kubernetes_validations: list[ValidationRule]
    """ x-kubernetes-validations describes a list of validation rules written in the CEL expression language. This field is an alpha-level. Using this field requires the feature gate `CustomResourceValidationExpressions` to be enabled. """

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
    """CustomResourceValidation is a list of validation methods for CustomResources."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _field_names_ = {
        "openapi_v3_schema": "openAPIV3Schema",
    }
    _revfield_names_ = {
        "openAPIV3Schema": "openapi_v3_schema",
    }

    openapi_v3_schema: JSONSchemaProps
    """ openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning. """

    def __init__(self, openapi_v3_schema: JSONSchemaProps = None):
        super().__init__(openapi_v3_schema=openapi_v3_schema)


class SelectableField(KubernetesObject):
    """SelectableField specifies the JSON path of a field that may be used with field selectors."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["json_path"]

    json_path: str
    """ jsonPath is a simple JSON path which is evaluated against each custom resource to produce a field selector value. Only JSON paths without the array notation are allowed. Must point to a field of type string, boolean or integer. Types with enum values and strings with formats are allowed. If jsonPath refers to absent field in a resource, the jsonPath evaluates to an empty string. Must not point to metdata fields. Required. """

    def __init__(self, json_path: str = None):
        super().__init__(json_path=json_path)


class CustomResourceSubresourceScale(KubernetesObject):
    """CustomResourceSubresourceScale defines how to serve the scale subresource for CustomResources."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["spec_replicas_path", "status_replicas_path"]

    label_selector_path: str
    """ labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource If there is no value under the given path in the custom resource, the `status.selector` value in the `/scale` subresource will default to the empty string. """
    spec_replicas_path: str
    """ specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale` subresource will return an error on GET. """
    status_replicas_path: str
    """ statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status`. If there is no value under the given path in the custom resource, the `status.replicas` value in the `/scale` subresource will default to 0. """

    def __init__(self, label_selector_path: str = None, spec_replicas_path: str = None, status_replicas_path: str = None):
        super().__init__(
            label_selector_path=label_selector_path, spec_replicas_path=spec_replicas_path, status_replicas_path=status_replicas_path
        )


CustomResourceSubresourceStatus: t.TypeAlias = dict[str, t.Any]
""" CustomResourceSubresourceStatus defines how to serve the status subresource for CustomResources. Status is represented by the `.status` JSON path inside of a CustomResource. When set, * exposes a /status subresource for the custom resource * PUT requests to the /status subresource take a custom resource object, and ignore changes to anything except the status stanza * PUT/POST/PATCH requests to the custom resource ignore changes to the status stanza """


class CustomResourceSubresources(KubernetesObject):
    """CustomResourceSubresources defines the status and scale subresources for CustomResources."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    scale: CustomResourceSubresourceScale
    """ scale indicates the custom resource should serve a `/scale` subresource that returns an `autoscaling/v1` Scale object. """
    status: CustomResourceSubresourceStatus
    """ status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object. """

    def __init__(self, scale: CustomResourceSubresourceScale = None, status: CustomResourceSubresourceStatus = None):
        super().__init__(scale=scale, status=status)


class CustomResourceDefinitionVersion(KubernetesObject):
    """CustomResourceDefinitionVersion describes a version for CRD."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["name", "served", "storage"]

    additional_printer_columns: list[CustomResourceColumnDefinition]
    """ additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. """
    deprecated: bool
    """ deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. """
    deprecation_warning: str
    """ deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. """
    name: str
    """ name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true. """
    schema: CustomResourceValidation
    """ schema describes the schema used for validation, pruning, and defaulting of this version of the custom resource. """
    selectable_fields: list[SelectableField]
    """ selectableFields specifies paths to fields that may be used as field selectors. A maximum of 8 selectable fields are allowed. See https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors """
    served: bool
    """ served is a flag enabling/disabling this version from being served via REST APIs """
    storage: bool
    """ storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true. """
    subresources: CustomResourceSubresources
    """ subresources specify what subresources this version of the defined custom resource have. """

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
    """CustomResourceDefinitionSpec describes how a user wants their resource to appear"""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["group", "names", "scope", "versions"]

    conversion: CustomResourceConversion
    """ conversion defines conversion settings for the CRD. """
    group: str
    """ group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). """
    names: CustomResourceDefinitionNames
    """ names specify the resource and kind names for the custom resource. """
    preserve_unknown_fields: bool
    """ preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#field-pruning for details. """
    scope: str
    """ scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`. """
    versions: list[CustomResourceDefinitionVersion]
    """ versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. """

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
    """CustomResourceDefinition represents a resource that should be exposed on the API server.  Its name MUST be in the format <.spec.name>.<.spec.group>."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"
    _api_group_ = "apiextensions.k8s.io"
    _kind_ = "CustomResourceDefinition"
    _scope_ = "cluster"

    _required_ = ["spec"]

    metadata: meta.ObjectMeta
    """ Standard object's metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata """
    spec: CustomResourceDefinitionSpec
    """ spec describes how the user wants the resources to appear """

    def __init__(self, name: str, metadata: meta.ObjectMeta = None, spec: CustomResourceDefinitionSpec = None):
        super().__init__(name, "", metadata=metadata, spec=spec)


class CustomResourceDefinitionCondition(KubernetesObject):
    """CustomResourceDefinitionCondition contains details for the current condition of this pod."""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    _required_ = ["status", "type"]

    last_transition_time: meta.Time
    """ lastTransitionTime last time the condition transitioned from one status to another. """
    message: str
    """ message is a human-readable message indicating details about last transition. """
    reason: str
    """ reason is a unique, one-word, CamelCase reason for the condition's last transition. """
    status: str
    """ status is the status of the condition. Can be True, False, Unknown. """
    type: str
    """ type is the type of the condition. Types include Established, NamesAccepted and Terminating. """

    def __init__(
        self, last_transition_time: meta.Time = None, message: str = None, reason: str = None, status: str = None, type: str = None
    ):
        super().__init__(last_transition_time=last_transition_time, message=message, reason=reason, status=status, type=type)


class CustomResourceDefinitionStatus(KubernetesObject):
    """CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition"""

    __slots__ = ()

    _api_version_ = "apiextensions.k8s.io/v1"

    accepted_names: CustomResourceDefinitionNames
    """ acceptedNames are the names that are actually being used to serve discovery. They may be different than the names in spec. """
    conditions: list[CustomResourceDefinitionCondition]
    """ conditions indicate state for particular aspects of a CustomResourceDefinition """
    stored_versions: list[str]
    """ storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list. """

    def __init__(
        self,
        accepted_names: CustomResourceDefinitionNames = None,
        conditions: list[CustomResourceDefinitionCondition] = None,
        stored_versions: list[str] = None,
    ):
        super().__init__(accepted_names=accepted_names, conditions=conditions, stored_versions=stored_versions)
