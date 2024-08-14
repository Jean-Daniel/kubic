import typing as t
from collections.abc import Iterable

from .k8s import QualifiedName, camel_to_snake, type_name_from_property_name


class GenericType(t.NamedTuple):
    base_type: str
    parameters: Iterable[t.Any]

    def __str__(self):
        return f"{self.base_type}[{str(self.parameters)}]"

    def __repr__(self):
        return str(self)


class ApiType:
    __slots__ = ("fqn",)

    def __init__(self, fqn: QualifiedName):
        super().__init__()
        self.fqn = fqn

    @property
    def name(self) -> str:
        return self.fqn.name

    @property
    def group(self) -> str:
        return self.fqn.group

    @property
    def api_group(self) -> str:
        return self.fqn.group if self.fqn.group != "core" else ""

    @property
    def version(self) -> str:
        return self.fqn.version

    @property
    def api_version(self) -> str:
        if self.group and self.group != "core":
            return f"{self.group}/{self.version}"
        return self.version

    def __eq__(self, other):
        return self.name == other.name if other else False

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Type: {self.fqn}"


# use distinct class to be able to use isinstance on ref
class ApiTypeRef(ApiType):
    pass


class TypeAlias(ApiType):
    __slots__ = ("type", "description")

    def __init__(self, fqn: QualifiedName, ty: "Type", description: str):
        super().__init__(fqn)
        self.type = ty
        self.description = description

    def __eq__(self, other):
        return super().__eq__(other) and self.type == other.type


class Property(t.NamedTuple):
    name: str
    type: "Type"
    required: bool
    description: str

    @property
    def snake_name(self):
        return camel_to_snake(self.name)


class NamedProperty(t.NamedTuple):
    name: str
    type: "Type"
    required: bool
    description: str
    snake_name: str


class ObjectType(ApiType):
    __slots__ = ("properties",)

    def __init__(self, fqn: QualifiedName):
        super().__init__(fqn)
        self.properties: list[Property] = []

    def __eq__(self, other):
        return self.name == other.name and self.properties == other.properties

    @property
    def kubic_type(self):
        return "KubernetesObject"

    @property
    def required_properties(self):
        return (prop for prop in self.properties if prop.required)

    @property
    def optional_properties(self):
        return (prop for prop in self.properties if not prop.required)


class ResourceType(ObjectType):
    __slots__ = ("description",)

    def __init__(self, name: QualifiedName, description: str):
        super().__init__(name)
        self.description = description


class ApiResourceType(ResourceType):
    __slots__ = ("scoped",)

    def __init__(self, name: QualifiedName, description: str, scoped: bool):
        super().__init__(name, description)
        self.scoped = scoped

    @property
    def kubic_type(self):
        return "KubernetesApiResource"

    @property
    def kind(self):
        return self.fqn.name


class AnonymousType(ObjectType):
    __slots__ = ("parent", "_basename", "prop_name")

    def __init__(self, fqn: QualifiedName, parent: ObjectType, prop_name: str):
        super().__init__(fqn)
        self.parent = parent
        self._basename = fqn.name
        self.prop_name = prop_name

    @property
    def fullname(self) -> str:
        if isinstance(self.parent, AnonymousType):
            return self.parent._basename + self._basename
        return self.parent.fqn.name + self._basename

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name and super().__eq__(other)

    def __str__(self):
        return self.name

    @classmethod
    def with_property(cls, prop_name: str, parent: ObjectType) -> "AnonymousType":
        base_name = type_name_from_property_name(prop_name)
        # Spec is a commonly used name.
        # To avoid having a lot of conflicting Spec types -> use fullname by default.
        if base_name == "Spec":
            base_name = parent.name + base_name
        return AnonymousType(QualifiedName(base_name, parent.group, parent.version), parent, prop_name)


Type: t.TypeAlias = str | ApiType | GenericType
