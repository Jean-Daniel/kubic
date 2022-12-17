import types
import typing as t
from collections.abc import Iterable, Mapping
from functools import cache

__all__ = ["KubernetesObject", "KubernetesApiResource"]


class _K8SResourceMeta(type):
    __slots__ = ()

    def __new__(mcs, clsname, superclasses, attributedict):
        # merge fields from all parent classes
        fields = attributedict.get("_field_names_") or {}
        revfields = attributedict.get("_revfield_names_") or {}
        for parent in superclasses:
            if hasattr(parent, "_field_names_"):
                fields.update(getattr(parent, "_field_names_"))
            if hasattr(parent, "_revfield_names_"):
                fields.update(getattr(parent, "_field_names_"))

        attributedict["_hints"] = None
        attributedict["_field_names_"] = fields
        attributedict["_revfield_names_"] = revfields

        return type.__new__(mcs, clsname, superclasses, attributedict)


@cache
def snake_to_camel(name: str) -> str:
    components = name.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


# naive implementation that miss lots of edge cases
def camel_to_snake(name: str) -> str:
    return "".join("_" + i.lower() if i.isupper() else i for i in name)


R = t.TypeVar("R", bound="K8SResource")


class _TypedList(list):
    __slots__ = ("type",)

    def __init__(self, ty: t.Type[R], values: Iterable | None = None):
        super().__init__()
        self.type: t.Type[R] = ty
        if values:
            self.extend(values)

    def _cast(self, obj):
        if isinstance(obj, self.type):
            return obj
        # required to workaround dubious StatefulSet persistent volume claim declaration.
        if issubclass(self.type, KubernetesApiResource):
            return self.type("").update(obj)
        return self.type().update(obj)

    def append(self, obj):
        if obj is not None:
            super().append(self._cast(obj))

    def insert(self, index: int, obj):
        if obj is not None:
            super().insert(index, self._cast(obj))

    def extend(self, values: Iterable):
        if not values:
            return
        if isinstance(values, _TypedList) and values.type == self.type:
            super().extend(values)
        else:
            for item in values:
                self.append(item)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __add__(self, other: list):
        result = _TypedList(self.type)
        result.extend(self)
        result.extend(other)
        return result

    def __iadd__(self, other):
        if other is None:
            return

        # convenient method to add a single item
        if isinstance(other, self.type):
            super().append(other)
        elif isinstance(other, dict):
            self.append(other)
        else:
            for item in other:
                self.append(item)
        return self


def _create_generic_type(hint):
    origin = _get_generic_origin(hint)
    if not origin or origin is t.Union:
        return None

    if origin is list:
        if hint.__args__:
            param = hint.__args__[0]
            if not _is_generic_type(param) and issubclass(param, KubernetesObject):
                return _TypedList(param)
        return list()

    if origin is dict:
        # assumes all parameters are base types
        return dict()


class KubernetesObject(dict, metaclass=_K8SResourceMeta):
    __slots__ = ()
    _field_names_ = {}

    def __init__(self, **kwargs):
        super().__init__()
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def __contains__(self, item):
        if super().__contains__(item):
            return True
        # check if this is a managed field.
        self._item_hint(item)
        # convert the python field name into kubernetes name
        camel_name = self._field_names_.get(item) or snake_to_camel(item)
        return super().__contains__(camel_name)

    def __getattr__(self, item):
        # check if this is a managed field.
        hint = self._item_hint(item)
        # convert the python field name into kubernetes name
        camel_name = self._field_names_.get(item) or snake_to_camel(item)
        # fetch the stored value
        try:
            return self[camel_name]
        except KeyError:
            # value not set yet
            pass

        value = None
        # Handle generic types
        if _is_generic_type(hint):
            value = _create_generic_type(hint)
            if value is not None:
                self[camel_name] = value
            return value

        # workaround broken PersistentVolumeClaim used as subresource.
        if issubclass(hint, KubernetesApiResource):
            self[camel_name] = value = hint(name="")
        # handle resource instances
        elif issubclass(hint, KubernetesObject):
            self[camel_name] = value = hint()

        return value

    def __setattr__(self, key, value):
        # kubernetes does not uses the concept of null value.
        # So instead of setting to None, remove the entry.
        if value is None:
            return self.__delattr__(key)

        hint = self._item_hint(key)  # check key validity

        if _is_generic_type(hint):
            origin = _get_generic_origin(hint)
            if (origin is list) and hint.__args__:
                param = hint.__args__[0]
                if issubclass(param, KubernetesObject):
                    value = _TypedList(param, value)
        elif issubclass(hint, KubernetesObject) and not isinstance(value, hint):
            # assume this is a dict and convert it into object
            value = hint.from_dict(value)
        else:
            # TODO: check base type ?
            pass

        camel_name = self._field_names_.get(key) or snake_to_camel(key)
        self[camel_name] = value

    def __delattr__(self, item):
        self._item_hint(item)  # check key validity

        camel_name = self._field_names_.get(item) or snake_to_camel(item)
        super().pop(camel_name, None)

    def __dir__(self):
        return dir(type(self)) + list(self._hints_().keys())

    def _hints_(self) -> dict:
        cls = type(self)
        if cls._hints is None:
            cls._hints = t.get_type_hints(cls)
        return cls._hints

    def _item_hint(self, key: str):
        hint = self._hints_().get(key)
        if not hint:
            # if not -> raise an attribute error
            self._attribute_error(key)
        return hint

    def _update(self, key, value):
        # Dict accepts keys in both python syntax and using the kubernetes case
        # it also accepts keyword properties with or without the trailing '_'.
        factory = self._hints_().get(key)
        if factory is None:
            snake_name = self._revfield_names_.get(key) or camel_to_snake(key)
            factory = self._hints_().get(snake_name)
            if factory:
                key = snake_name
            else:
                self._attribute_error(key)

        if not _is_generic_type(factory):
            if issubclass(factory, KubernetesObject):
                # merge recursively
                getattr(self, key).update(value)
                return
            elif issubclass(factory, dict):
                # merge recursively
                getattr(self, key).update(value)
                return
        # else set the value
        setattr(self, key, value)

    def update(self, values: dict = None, **kwargs):
        if values:
            # assume iterable of pairs if not a dict
            items = values.items() if isinstance(values, Mapping) else values
            for key, value in items:
                self._update(key, value)

        if kwargs:
            for key, value in kwargs.items():
                self._update(key, value)

        return self

    def __or__(self, other):
        # copy self, bypassing type checking
        copy = type(self)()
        dict.update(copy, self)
        # merge with other
        copy.update(other)
        return copy

    def __ior__(self, other):
        self.update(other)
        return self

    def _attribute_error(self, attr: str):
        raise AttributeError(
            f"{type(self).__name__} does not have attribute {attr}. Available attributes are: {', '.join(self._hints_().keys())}"
        )

    @classmethod
    def from_dict(cls, values: dict):
        if values is None:
            return None

        return cls().update(values)


# Wrapper to properly handle types.UnionType which is not a generic type but should behave like one
def _get_generic_origin(ty: t.Type) -> t.Type | None:
    if isinstance(ty, types.UnionType):
        return None
    return getattr(ty, "__origin__")


def _is_generic_type(ty: t.Type) -> bool:
    return isinstance(ty, types.UnionType) or hasattr(ty, "__origin__")


class KubernetesApiResource(KubernetesObject):
    __slots__ = ()

    api_version: str
    kind: str

    def __init__(self, version: str, kind: str, name: str, namespace: str = None, **kwargs):
        super().__init__(**kwargs)
        self["apiVersion"] = version
        self["kind"] = kind

        self.metadata.name = name
        # Cluster objects don't need namespace.
        if namespace:
            self.metadata.namespace = namespace

    @property
    def has_namespace(self) -> bool:
        return getattr(type(self), "_scope_", None) == "namespace"
