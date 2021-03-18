from typing import Union, List, Any, NamedTuple

from .k8s import QualifiedName, camel_to_snake


class GenericType(NamedTuple):
    base_type: str
    value_type: Any

    def qualified_name(self, group: str) -> str:
        if hasattr(self.value_type, "qualified_name"):
            value = self.value_type.qualified_name(group)
        else:
            value = str(self.value_type)
        return f"{self.base_type}[{value}]"

    def __str__(self):
        return f"{self.base_type}[{str(self.value_type)}]"

    def __repr__(self):
        return str(self)


class ApiType:
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
    def version(self) -> str:
        return self.fqn.version

    def qualified_name(self, group: str) -> str:
        if self.group and self.group != group:
            return f"{self.group}.{self.name}"
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Type: {self.fqn}"


class TypeAlias(ApiType):
    def __init__(self, fqn: QualifiedName, ty: "Type"):
        super().__init__(fqn)
        self.type = ty

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type


class Property(NamedTuple):
    name: str
    type: "Type"
    required: bool

    def type_name(self, group) -> str:
        if hasattr(self.type, "qualified_name"):
            return self.type.qualified_name(group)
        return str(self.type)

    @property
    def snake_name(self):
        return camel_to_snake(self.name)


class ObjectType(ApiType):
    def __init__(self, fqn: QualifiedName):
        super().__init__(fqn)
        self.properties: List[Property] = []

    def __eq__(self, other):
        return self.name == other.name and self.properties == other.properties

    @property
    def required_properties(self):
        return (prop for prop in self.properties if prop.required)

    @property
    def optional_properties(self):
        return (prop for prop in self.properties if not prop.required)


class ApiResourceType(ObjectType):
    def __init__(self, name: QualifiedName, scoped: bool):
        super().__init__(name)
        self.scoped = scoped

    @property
    def kind(self):
        return self.fqn.name


class AnonymousType(ObjectType):
    def __init__(self, fqn: QualifiedName, parent: ObjectType):
        super().__init__(fqn)
        self.parent = parent
        # freeze parent name
        self.parent_name: str = self.parent.name

    def __eq__(self, other):
        return self.name == other.name and super().__eq__(other)

    def __str__(self):
        return self.name


Type = Union[str, ApiType, GenericType]
