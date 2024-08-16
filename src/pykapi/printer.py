import sys
import typing as t

# noinspection PyProtectedMember
from kubic import (
    snake_to_camel as naive_snake_to_camel,
    camel_to_snake as naive_camel_to_snake,
)
from .k8s import module_for_group
from .parser import ApiGroup
from .types import (
    ObjectType,
    TypeAlias,
    ApiResourceType,
    AnonymousType, ResourceType,
)


class TypePrinter:
    def __init__(self, api_module: str = ".", docstrings: bool = False):
        self.api_module = api_module
        self.docstrings = docstrings

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

    def print_imports(self, group: ApiGroup, stream: t.TextIO):
        if group.use_typing:
            stream.write("import typing as t")
            stream.write("\n\n")

        if group.base_types:
            stream.write(f"from kubic import ")
            stream.write(", ".join(sorted(group.base_types)))
            stream.write("\n")

        if group.refs:
            stream.write(f"from {self.api_module} import ")
            stream.write(", ".join(sorted(module_for_group(g) for g in group.refs)))
            stream.write("\n\n")

    def print_types(self, group: ApiGroup, stream: t.TextIO):
        for ty in group.types:
            if isinstance(ty, TypeAlias):
                self.print_type_alias(group, ty, stream)
            else:
                assert isinstance(ty, ObjectType)
                self.print_type(group, ty, stream)
            stream.write("\n")

    def print_type_alias(self, group: ApiGroup, ty: TypeAlias, stream: t.TextIO):
        stream.write(ty.name)
        stream.write(": t.TypeAlias = ")
        stream.write(group.qualified_name(ty.type))
        stream.write("\n")
        self.print_docstring(ty.description, stream)
        stream.write("\n")

    def print_docstring(self, description: str, stream: t.TextIO, indent=""):
        if not self.docstrings or not description:
            return

        stream.write(indent)
        stream.write('""" ')
        if "\n" in description:
            stream.write("\n")
            stream.write(indent)
            if indent:
                stream.write(description.replace("\n", f"\n{indent}"))
            else:
                stream.write(description)
            stream.write("\n")
            stream.write(indent)
        else:
            stream.write(description)
        stream.write(' """\n')

    def print_type(self, group: ApiGroup, ty: ObjectType, stream: t.TextIO):
        stream.write("class ")
        stream.write(ty.name)
        stream.write(f"({ty.kubic_type})")
        stream.write(":\n")

        if isinstance(ty, ResourceType):
            self.print_docstring(ty.description, stream, "    ")

        stream.write("    __slots__ = ()\n")

        if not isinstance(ty, AnonymousType):
            stream.write(f'\n    _api_version_ = "{ty.api_version}"\n')
            if isinstance(ty, ApiResourceType):
                stream.write(f'    _api_group_ = "{ty.api_group}"\n')
                stream.write(f'    _kind_ = "{ty.kind}"\n')
                scope = "namespace" if ty.scoped else "cluster"
                stream.write(f'    _scope_ = "{scope}"\n')
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
            stream.write(group.qualified_name(prop.type, ty))
            stream.write("\n")
            # docstring
            self.print_docstring(prop.description, stream, "    ")

        stream.write("\n    def __init__(self")
        if isinstance(ty, ApiResourceType):
            stream.write(", name: str")
            if ty.scoped:
                stream.write(", namespace: str = None")
        for prop in ty.properties:
            stream.write(", ")
            stream.write(prop.snake_name)
            stream.write(": ")
            stream.write(group.qualified_name(prop.type, ty))
            stream.write(" = None")
        stream.write("):\n")
        stream.write("        super().__init__(")
        if isinstance(ty, ApiResourceType):
            stream.write("name")
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
