import importlib.util
import inspect
import pkgutil
import typing as t
from importlib.machinery import ModuleSpec
from types import ModuleType

from . import KubernetesObject, KubernetesApiResource, _TypedList

R = t.TypeVar("R", bound=KubernetesApiResource)

# noinspection PyTypeChecker
AnyApiResource: t.Type[R] = None
# noinspection PyTypeChecker
AnyResourceList: t.Type[R] = None


class _ObjID(t.NamedTuple):
    api_version: str
    kind: str


_rsrc_index: dict[_ObjID, t.Type] = {}


# Must be called before trying to use the reader API.
# Module must be the module containing the Kubernetes API
def _register_any(object_meta):
    global AnyApiResource
    global AnyResourceList
    assert not AnyApiResource and not AnyResourceList

    class _AnyApiResource(KubernetesApiResource):
        __slots__ = ("_api_version_", "_api_group_", "_kind_")

        spec: dict[str, t.Any]
        metadata: object_meta

        def __init__(self, version: str, kind: str, name: str, namespace: str = None, **kwargs):
            self._api_version_ = version
            self._api_group_, _, _ = version.rpartition("/")
            self._kind_ = kind

            super().__init__(name, namespace)
            self.spec = {}
            self.spec.update(kwargs)

        # Cannot guess unknown resource scope
        @property
        def is_namespaced(self) -> bool:
            if self.metadata.namespace:
                return True

            raise ValueError("try to access is_namespaced on unknown resource type: " + self._kind_)

    AnyApiResource = _AnyApiResource

    class _AnyResourceList(KubernetesApiResource):
        __slots__ = ("_api_version_", "_api_group_", "_kind_")

        _revfield_names_ = {
            "items": "items_",
        }

        items_: list
        metadata: object_meta

        def __init__(self, version: str, kind: str, name: str, namespace: str = None, items: list[KubernetesApiResource] = None):
            self._api_version_ = version
            self._api_group_, _, _ = version.rpartition("/")
            self._kind_ = kind
            super().__init__(name, namespace)
            if items and isinstance(items[0], KubernetesObject):
                self.items_ = _TypedList(type(items[0]), items)
            else:
                self.items_ = list(items)

    AnyResourceList = _AnyResourceList


def register_module(module: ModuleType):
    for name, cls in inspect.getmembers(module):
        if not inspect.isclass(cls):
            continue
        if hasattr(cls, "_kind_"):
            oid = _ObjID(cls._api_version_, cls._kind_.lower())
            _rsrc_index[oid] = cls
        elif name == "ObjectMeta" and getattr(cls, "_api_version_", None) == "meta/v1":
            _register_any(cls)


# Call with all modules containing CRD objects to register them.
def register_modules(spec: ModuleSpec):
    for pkg in pkgutil.iter_modules(spec.submodule_search_locations, prefix=spec.name + "."):
        mod = importlib.import_module(pkg.name)
        register_module(mod)


KubernetesApiResourceTy = t.TypeVar("KubernetesApiResourceTy", bound=KubernetesApiResource)


def create_api_resource(obj: dict) -> KubernetesApiResourceTy:
    if isinstance(obj, KubernetesApiResource):
        return obj

    api_version: str = obj.get("apiVersion")
    kind: str = obj.get("kind")
    if not api_version or not kind:
        raise ValueError("K8S resource must have 'apiVersion' and 'kind'")

    rsrc = _rsrc_index.get(_ObjID(api_version, kind.lower()))
    if not rsrc:
        # assuming that object that contains items instead of spec is a ResourceList (ConfigMapList, …)
        items = obj.pop("items", None)
        if items:
            return AnyResourceList(api_version, kind, "", items=[create_api_resource(item) for item in items])
        return AnyApiResource(api_version, kind, "").update(obj)
    return rsrc("").update(obj)
