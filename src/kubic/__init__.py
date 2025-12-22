import types
import typing as t
from collections.abc import Iterable, Mapping
from functools import cache

__all__ = ["KubernetesObject", "KubernetesApiResource"]

import yaml


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


R = t.TypeVar("R", bound="KubernetesObject")


class _TypedList(list):
    __slots__ = ("type", "__dirty")

    def __init__(self, ty: t.Type[R], dirty: bool, values: Iterable | None = None):
        super().__init__()
        self.type: t.Type[R] = ty
        self.__dirty = dirty
        if values:
            self.extend(values)

    @property
    def is_dirty(self):
        return self.__dirty

    def _cast(self, obj):
        if isinstance(obj, self.type):
            return obj
        # required to workaround dubious StatefulSet persistent volume claim declaration.
        if issubclass(self.type, KubernetesApiResource):
            return self.type("").update(obj)
        try:
            return self.type().update(obj)
        except ValueError as e:
            raise TypeError(f"cannot convert value of type {type(obj)} to expected type {self.type}") from e

    def append(self, obj):
        if obj is not None:
            super().append(self._cast(obj))

    def insert(self, index: int, obj):
        # do not create null entries
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
        # do not create null entries
        if value is not None:
            super().__setitem__(key, self._cast(value))

    def __add__(self, other: list):
        result = _TypedList(self.type, True)
        result.extend(self)
        result.extend(other)
        return result

    def __iadd__(self, other):
        if other is None:
            return None

        # convenient method to add a single item
        if isinstance(other, self.type):
            super().append(other)
        elif isinstance(other, dict):
            self.append(other)
        else:
            for item in other:
                self.append(item)
        return self


# RawDict is used to define if a dict has been implicitly created by __get__ access, or explicitly set by the user.
class RawDict(dict): ...


class RawList(list): ...


def _create_generic_type(hint):
    origin = _get_generic_origin(hint)
    if not origin or origin is t.Union:
        return None

    if origin is list:
        if hint.__args__:
            param = hint.__args__[0]
            if not _is_generic_type(param) and issubclass(param, KubernetesObject):
                lst = _TypedList(param, False)
                return lst
        return RawList()

    if origin is dict:
        # assumes all parameters are base types
        return RawDict()

    return None


class KubernetesObject(dict, metaclass=_K8SResourceMeta):
    __slots__ = ("__dirty",)
    _field_names_ = {}

    def __init__(self, **kwargs):
        super().__init__()
        # defaults to True, to not have to handle all case where the objet is created by the API user.
        self.__dirty = True
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
        if item == "__dirty":
            return self.__dirty

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
            value = hint(name="")
            value.__dirty = False
            self[camel_name] = value
        # handle resource instances
        elif issubclass(hint, KubernetesObject):
            value = hint()
            value.__dirty = False
            self[camel_name] = value

        return value

    def __setattr__(self, key, value):
        try:
            # do not interfere with existing attributes
            return super().__setattr__(key, value)
        except AttributeError:
            pass

        self.__dirty = True
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
                    value = _TypedList(param, True, value)
        elif issubclass(hint, KubernetesObject) and not isinstance(value, hint):
            # assume this is a dict and convert it into object
            value = hint.from_dict(value)
        else:
            # TODO: check base type ?
            pass

        camel_name = self._field_names_.get(key) or snake_to_camel(key)
        self[camel_name] = value
        return None

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
        self.__dirty = True
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


# Read-Only API Class Members
class _K8SApiResourceMeta(_K8SResourceMeta):
    __slots__ = ()

    @property
    def api_version(cls):
        # noinspection PyUnresolvedReferences
        return cls._api_version_

    @property
    def group(cls):
        # noinspection PyUnresolvedReferences
        return cls._api_group_

    @property
    def kind(cls):
        # noinspection PyUnresolvedReferences
        return cls._kind_

    @property
    def namespaced(cls):
        return getattr(cls, "_scope_", None) == "namespace"


class KubernetesApiResource(KubernetesObject, metaclass=_K8SApiResourceMeta):
    __slots__ = ()

    # === read-only class members ===
    # api_version: str
    # group: str
    # kind: str

    def __init__(self, name: str, namespace: str = None, **kwargs):
        super().__init__(**kwargs)
        self["apiVersion"] = self._api_version_
        self["kind"] = self._kind_

        self.metadata.name = name
        # Cluster objects don't need namespace.
        if namespace:
            self.metadata.namespace = namespace

    @property
    def api_version(self) -> str:
        return self._api_version_

    @property
    def group(self) -> str:
        return self._api_group_

    @property
    def kind(self) -> str:
        return self._kind_

    @property
    def name(self) -> str:
        return self.metadata.name

    @property
    def is_namespaced(self) -> bool:
        return getattr(type(self), "_scope_", None) == "namespace"

    # Special case to be able to pass a whole object dict and don't have to worry about ignored fields
    def _update(self, key, value):
        if key == "api_version" or key == "apiVersion":
            if value.lower() != self.api_version.lower():
                raise AttributeError(f"apiVersion is a read-only attribute ({self.api_version} ≠ {value})")
            return None

        if key == "kind":
            if value.lower() != self.kind.lower():
                raise AttributeError(f"kind is a read-only attribute ({self.kind} ≠ {value})")
            return None

        if key == "status":
            return None

        if key == "metadata" and isinstance(value, dict) and "managedFields" in value:
            value = dict(value)
            del value["managedFields"]

        return super()._update(key, value)


# ================================================
#              YAML Representation
# ================================================

yaml.SafeDumper.add_representer(_TypedList, yaml.SafeDumper.represent_list)
yaml.SafeDumper.add_representer(RawList, yaml.SafeDumper.represent_list)
yaml.SafeDumper.add_representer(RawDict, yaml.SafeDumper.represent_dict)

yaml.CSafeDumper.add_representer(_TypedList, yaml.SafeDumper.represent_list)
yaml.CSafeDumper.add_representer(RawList, yaml.SafeDumper.represent_list)
yaml.CSafeDumper.add_representer(RawDict, yaml.SafeDumper.represent_dict)


# see represent_dict()
def represent_k8s_object(dumper, obj: KubernetesObject):
    value = []
    node = yaml.MappingNode("tag:yaml.org,2002:map", value)
    if dumper.alias_key is not None:
        dumper.represented_objects[dumper.alias_key] = node
    best_style = True
    mapping = obj.items()
    if dumper.sort_keys:
        try:
            mapping = sorted(mapping)
        except TypeError:
            pass
    for item_key, item_value in mapping:
        # Skipping objets generated by __get__ accessor, but never updated.
        if isinstance(item_value, KubernetesObject) and not _is_dirty(item_value):
            continue

        if isinstance(item_value, _TypedList) and not item_value and not _is_dirty(item_value):
            continue

        # Skipping empty dict if it was generated by __get__ accessor.
        if isinstance(item_value, RawDict) and not item_value:
            continue

        # Skipping empty list if it was generated by __get__ accessor.
        if isinstance(item_value, RawList) and not item_value:
            continue

        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        if not (isinstance(node_key, yaml.ScalarNode) and not node_key.style):
            best_style = False
        if not (isinstance(node_value, yaml.ScalarNode) and not node_value.style):
            best_style = False
        value.append((node_key, node_value))

    if dumper.default_flow_style is not None:
        node.flow_style = dumper.default_flow_style
    else:
        node.flow_style = best_style
    return node


def _is_dirty(rsrc: object):
    if isinstance(rsrc, KubernetesObject):
        if rsrc.__dirty:
            return True
        for v in rsrc.values():
            if _is_dirty(v):
                return True
    elif isinstance(rsrc, _TypedList):
        if len(rsrc) > 0 or rsrc.is_dirty:
            return True
    elif isinstance(rsrc, RawDict):
        if len(rsrc) > 0:
            return True
    elif isinstance(rsrc, list):
        if len(rsrc) > 0:
            return True
    return False


yaml.SafeDumper.add_multi_representer(KubernetesObject, represent_k8s_object)
yaml.CSafeDumper.add_multi_representer(KubernetesObject, represent_k8s_object)
