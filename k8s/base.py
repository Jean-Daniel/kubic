import typing
from functools import cache


class ResourceMeta(type):
    def __new__(mcs, clsname, superclasses, attributedict):
        # merge fields from all parent classes
        fields = attributedict.get("_field_names_") or {}
        for parent in superclasses:
            if hasattr(parent, "_field_names_"):
                fields.update(getattr(parent, "_field_names_"))
        attributedict["_field_names_"] = fields
        cls = type.__new__(mcs, clsname, superclasses, attributedict)
        cls._hints_ = typing.get_type_hints(cls)
        return cls


@cache
def snake_to_camel(name: str) -> str:
    components = name.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


class Resource(dict, metaclass=ResourceMeta):
    __slots__ = ()
    _field_names_ = {}

    def __init__(self, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def __getattr__(self, item):
        # check if this is a managed field.
        factory = self._item_hint(item)

        # convert the python field name into kubernetes name
        camel_name = self._field_names_.get(item) or snake_to_camel(item)

        # fetch the stored value
        value = self.get(camel_name)
        if value is None:
            # if not value found -> try to create one using default type constructor
            try:
                # generic aliases -> __origin__ is list, dict, …
                if hasattr(factory, "__origin__"):
                    factory = factory.__origin__
                elif repr(factory).startswith("typing.Union"):
                    raise ValueError(
                        f"field {item} is an union and must be set before use."
                    )
                self[camel_name] = value = factory()
            except TypeError as e:
                # the constructor has required parameters
                raise ValueError(
                    f"field {item} has required parameter and must be set before use."
                ) from e

        return value

    def __setattr__(self, key, value):
        factory = self._item_hint(key)  # check key validity

        try:
            # convert dict into object automatically
            if issubclass(factory, Resource) and not isinstance(value, factory):
                value = factory.from_dict(value)
        except TypeError:
            pass

        camel_name = self._field_names_.get(key) or snake_to_camel(key)
        # TODO: type check ?
        self[camel_name] = value

    def __delattr__(self, item):
        self._item_hint(item)  # check key validity

        camel_name = self._field_names_.get(item) or snake_to_camel(item)
        del self[camel_name]

    def merge(self, values: dict):
        if not values:
            return
        for key, value in values.items():
            factory = self._item_hint(key)
            try:
                if issubclass(factory, Resource):
                    value = factory.from_dict(value)
            except TypeError:
                pass
            setattr(self, key, value)
        return self

    @classmethod
    def _item_hint(cls, key: str):
        try:
            return cls._hints_[key]
        except KeyError:
            # if not -> raise an attribute error
            raise AttributeError(f"{cls.__name__} does not has attribute {key}. Available attributes are: {', '.join(cls._hints_.keys())}")

    @classmethod
    def from_dict(cls, values: dict):
        if values is None:
            return None

        return cls().merge(values)


class ApiResource(Resource):
    __slots__ = ()

    def __init__(
            self, version: str, kind: str, name: str, namespace: str = None, **kwargs
    ):
        super().__init__(**kwargs)
        self["apiVersion"] = version
        self["kind"] = kind

        self.metadata.name = name
        # Cluster objects don't need namespace.
        if namespace:
            self.metadata.namespace = namespace
