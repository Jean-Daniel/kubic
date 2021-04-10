import typing

from kubic import meta, KubernetesApiResource


class AnyApiResource(KubernetesApiResource):
    __slots__ = ()

    spec: typing.Dict[str, typing.Any]
    metadata: meta.ObjectMeta

    def __init__(self, version: str, kind: str, name: str, namespace: str = None, **kwargs):
        super().__init__(version, kind, name, namespace)
        self.spec = {}
        self.spec.update(kwargs)
