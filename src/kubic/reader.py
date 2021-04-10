import importlib.util
import inspect
import os
import pkgutil
import typing
from typing import NamedTuple

from . import meta, KubernetesApiResource


class AnyApiResource(KubernetesApiResource):
    __slots__ = ()

    spec: typing.Dict[str, typing.Any]
    metadata: meta.ObjectMeta

    def __init__(self, version: str, kind: str, name: str, namespace: str = None, **kwargs):
        super().__init__(version, kind, name, namespace)
        self.spec = {}
        self.spec.update(kwargs)


class _ObjID(NamedTuple):
    api_version: str
    kind: str


_rsrc_index: typing.Dict[_ObjID, typing.Type] = {}


def create_api_resource(obj: dict) -> KubernetesApiResource:
    if not _rsrc_index:
        modulepath = os.path.dirname(__file__)
        module, _ = __name__.rsplit(".", maxsplit=1)
        for pkg in pkgutil.walk_packages([modulepath], prefix=module + "."):
            mod = importlib.import_module(pkg.name)
            for name, cls in inspect.getmembers(mod):
                if not inspect.isclass(cls) or not hasattr(cls, "_kind_"):
                    continue
                oid = _ObjID(cls._api_version_, cls._kind_)
                _rsrc_index[oid] = cls

    api_version = obj.get("apiVersion")
    kind = obj.get("kind")
    obj.pop("status", None)
    rsrc = _rsrc_index.get(_ObjID(api_version, kind))
    if not rsrc:
        return AnyApiResource(api_version, kind, "").update(obj)
    return rsrc("").update(obj)
