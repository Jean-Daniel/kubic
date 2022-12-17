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


_rsrc_index: t.Dict[_ObjID, t.Type] = {}


# Must be called before trying to use the reader API.
# Module must be the module containing the Kubernetes API
def _register_any(object_meta):
    global AnyApiResource
    global AnyResourceList
    assert not AnyApiResource and not AnyResourceList

    class _AnyApiResource(KubernetesApiResource):
        __slots__ = ()

        spec: t.Dict[str, t.Any]
        metadata: object_meta

        def __init__(self, version: str, kind: str, name: str, namespace: str = None, **kwargs):
            super().__init__(version, kind, name, namespace)
            self.spec = {}
            self.spec.update(kwargs)

    AnyApiResource = _AnyApiResource

    class _AnyResourceList(KubernetesApiResource):
        __slots__ = ()

        _revfield_names_ = {
            "items": "items_",
        }

        items_: list
        metadata: object_meta

        def __init__(self, version: str, kind: str, name: str, namespace: str = None, items: t.List[KubernetesApiResource] = None):
            super().__init__(version, kind, name, namespace)
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
            oid = _ObjID(cls._api_version_, cls._kind_)
            _rsrc_index[oid] = cls
        elif name == "ObjectMeta" and getattr(cls, "_api_version_", None) == "meta/v1":
            _register_any(cls)


# Call with all modules containing CRD objects to register them.
def register_modules(spec: ModuleSpec):
    for pkg in pkgutil.iter_modules(spec.submodule_search_locations, prefix=spec.name + "."):
        mod = importlib.import_module(pkg.name)
        register_module(mod)


K = t.TypeVar("K", bound=KubernetesApiResource)


def create_api_resource(obj: dict) -> K:
    if isinstance(obj, KubernetesApiResource):
        return obj

    api_version = obj.get("apiVersion")
    kind = obj.get("kind")
    if not api_version or not kind:
        raise ValueError("K8S resource must have 'apiVersion' and 'kind'")

    obj.pop("status", None)
    rsrc = _rsrc_index.get(_ObjID(api_version, kind))
    if not rsrc:
        # assuming that object that contains items instead of spec is a ResourceList (ConfigMapList, …)
        items = obj.pop("items", None)
        if items:
            return AnyResourceList(api_version, kind, "", items=[create_api_resource(item) for item in items])
        return AnyApiResource(api_version, kind, "").update(obj)
    return rsrc("").update(obj)
