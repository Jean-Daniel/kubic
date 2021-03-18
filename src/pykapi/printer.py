import sys
from typing import TextIO

# noinspection PyProtectedMember
from kubic import (
    snake_to_camel as naive_snake_to_camel,
    camel_to_snake as naive_camel_to_snake,
)
from .parser import ApiGroup
from .types import (
    ObjectType,
    TypeAlias,
    ApiResourceType,
)

BASE_OBJECT_TYPE = "KubernetesObject"
RESOURCE_OBJECT_TYPE = "KubernetesApiResource"


class TypePrinter:
    def __init__(self, api_module="."):
        self.api_module = api_module

    def print_group(self, group: ApiGroup, output: str):
        if output == "-":
            stream = sys.stdout
        else:
            stream = open(output, "w")

        try:
            self.print_imports(group, stream)
            stream.write("\n\n")

            self.print_types(group, stream)
        finally:
            if stream is not sys.stdout:
                stream.close()

    def print_imports(self, group: ApiGroup, stream: TextIO):
        if group.typing:
            stream.write("from typing import ")
            stream.write(", ".join(sorted(group.typing)))
            stream.write("\n\n")

        stream.write(
            f"from {self.api_module} import {BASE_OBJECT_TYPE}, {RESOURCE_OBJECT_TYPE}\n"
        )

        if group.refs:
            stream.write(f"from {self.api_module} import ")
            stream.write(", ".join(sorted(group.refs)))
            stream.write("\n\n")

    def print_types(self, group: ApiGroup, stream: TextIO):
        for ty in group.types:
            if isinstance(ty, TypeAlias):
                self.print_type_alias(ty, stream)
            else:
                assert isinstance(ty, ObjectType)
                self.print_type(group, ty, stream)
            stream.write("\n")

    @staticmethod
    def print_type_alias(ty: TypeAlias, stream: TextIO):
        stream.write(ty.name)
        if sys.version_info >= (3, 10):
            stream.write(": TypeAlias = ")
        else:
            stream.write(" = ")
        stream.write(str(ty.type))
        stream.write("\n\n")

    def print_type(self, group: ApiGroup, ty: ObjectType, stream: TextIO):
        stream.write("class ")
        stream.write(ty.name)
        if isinstance(ty, ApiResourceType):
            stream.write(f"({RESOURCE_OBJECT_TYPE})")
        else:
            stream.write(f"({BASE_OBJECT_TYPE})")
        stream.write(":\n")
        stream.write("    __slots__ = ()\n")

        if ty.group:
            stream.write(f'\n    _group_ = "{ty.group}"\n')
        if ty.version:
            stream.write(f'    _version_ = "{ty.version}"\n')

        required = [prop.snake_name for prop in ty.required_properties]
        if required:
            stream.write('\n    _required_ = ["')
            stream.write('", "'.join(required))
            stream.write('"]\n')

        # write fields mapping
        fields = {}
        revfields = {}
        for prop in ty.properties:
            snake = prop.snake_name
            if prop.name != naive_snake_to_camel(snake):
                fields[snake] = prop.name
            if naive_camel_to_snake(prop.name) != snake:
                revfields[prop.name] = snake

        if fields:
            stream.write("\n    _field_names_ = {\n")
            for snake, camel in fields.items():
                stream.write(f'        "{snake}": "{camel}",\n')
            stream.write("    }\n")

        if revfields:
            if not fields:
                stream.write("\n")
            stream.write("    _revfield_names_ = {\n")
            for camel, snake in revfields.items():
                stream.write(f'        "{camel}": "{snake}",\n')
            stream.write("    }\n")

        stream.write("\n")
        for prop in ty.properties:
            stream.write("    ")
            stream.write(prop.snake_name)
            stream.write(": ")
            stream.write(prop.type_name(group.name))
            stream.write("\n")

        stream.write("\n    def __init__(self")
        if isinstance(ty, ApiResourceType):
            stream.write(", name: str")
            if ty.scoped:
                stream.write(", namespace: str = None")
        for prop in ty.properties:
            stream.write(", ")
            stream.write(prop.snake_name)
            stream.write(": ")
            stream.write(prop.type_name(group.name))
            stream.write(" = None")
        stream.write("):\n")
        stream.write("        super().__init__(")
        if isinstance(ty, ApiResourceType):
            stream.write('"')
            if ty.group:
                stream.write(f"{ty.group}/")
            stream.write(f'{ty.version}"')
            stream.write(", ")
            stream.write(f'"{ty.kind}"')
            stream.write(", name")
            if ty.scoped:
                stream.write(", namespace")
            else:
                stream.write(', ""')
            if ty.properties:
                stream.write(", ")
        for idx, prop in enumerate(ty.properties):
            if idx != 0:
                stream.write(", ")
            stream.write(prop.snake_name)
            stream.write("=")
            stream.write(prop.snake_name)

        stream.write(")\n\n")
