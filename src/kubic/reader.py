import importlib.util
import inspect
import pkgutil
import typing
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import NamedTuple

from . import KubernetesApiResource
from . import api
from .api import meta


class AnyApiResource(KubernetesApiResource):
    __slots__ = ()

    spec: typing.Dict[str, typing.Any]
    metadata: api.meta.ObjectMeta

    def __init__(self, version: str, kind: str, name: str, namespace: str = None, **kwargs):
        super().__init__(version, kind, name, namespace)
        self.spec = {}
        self.spec.update(kwargs)


class _ObjID(NamedTuple):
    api_version: str
    kind: str


_rsrc_index: typing.Dict[_ObjID, typing.Type] = {}


def register_module(module: ModuleType):
    for name, cls in inspect.getmembers(module):
        if not inspect.isclass(cls) or not hasattr(cls, "_kind_"):
            continue
        oid = _ObjID(cls._api_version_, cls._kind_)
        _rsrc_index[oid] = cls


def register_modules(spec: ModuleSpec):
    for pkg in pkgutil.iter_modules(spec.submodule_search_locations, prefix=spec.name + "."):
        mod = importlib.import_module(pkg.name)
        register_module(mod)


def create_api_resource(obj: dict) -> KubernetesApiResource:
    if isinstance(obj, KubernetesApiResource):
        return obj

    api_version = obj.get("apiVersion")
    kind = obj.get("kind")
    obj.pop("status", None)
    rsrc = _rsrc_index.get(_ObjID(api_version, kind))
    if not rsrc:
        return AnyApiResource(api_version, kind, "").update(obj)
    return rsrc("").update(obj)


register_modules(api.__spec__)
