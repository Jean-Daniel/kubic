import typing as t
import unittest
from collections.abc import MutableSequence

import yaml

import kubic.api
import kubic.crds
from kubic import KubernetesApiResource, KubernetesObject
from kubic.api import apps
from kubic.api.apps import Deployment, DeploymentStrategy
from kubic.api.meta import LabelSelectorRequirement, ObjectMeta
from kubic.reader import create_api_resource, register_modules
from kubic.writer import KubernetesObjectDumper


class LeaveType(KubernetesObject):
    __slots__ = ()

    value: str | int


class SubType(KubernetesObject):
    __slots__ = ()

    value: str
    leave: LeaveType
    leaves: t.List[LeaveType]


class BaseType(KubernetesObject):
    __slots__ = ()

    spec: SubType


class SpecialProperty(KubernetesObject):
    __slots__ = ()

    from_: str
    load_urls: str
    my_property: int

    # _revfield_names_ are used when settings
    # values from a dictionary to convert camelCase names
    # into snake names. Only names that can be naively converted to
    # snake case are generated.
    _revfield_names_ = {"from": "from_", "loadURLs": "load_urls"}


class CustomResource(KubernetesApiResource):
    __slots__ = ()

    _api_version_ = "com.xenonium/v1"
    _api_group_ = "com.xenonium"
    _kind_ = "CustomResource"
    _scope_ = "namespace"


class ResourceTest(unittest.TestCase):
    def test_dir(self):
        obj = SpecialProperty()

        props = dir(obj)
        for prop in ("from_", "load_urls", "my_property"):
            self.assertIn(prop, props)

    def test_slots(self):
        obj = SpecialProperty()

        # assert does not raise on access internal property
        _ = obj.__annotations__
        with self.assertRaises(AttributeError):
            # make sure base class are properly defined to avoid creation of __dict__ (using __slots__)
            _ = obj.__dict__

    def test_get(self):
        obj = BaseType()

        # get should create value automatically
        self.assertIsInstance(obj.spec, SubType)
        self.assertIsInstance(obj.spec.leave, LeaveType)
        self.assertIsInstance(obj.spec.leaves, MutableSequence)

        # leave type should be None by default
        self.assertIsNone(obj.spec.value)
        # ditto for union
        self.assertIsNone(obj.spec.leave.value)

    def test_set(self):
        obj = BaseType()
        obj.spec = {}
        self.assertIsInstance(obj.spec, SubType)

        # list in KubernetesObjects ensure the object are of the right type
        # and support += with a single object.
        obj.spec.leaves = []
        obj.spec.leaves.append({})
        obj.spec.leaves += {}
        obj.spec.leaves += LeaveType()
        obj.spec.leaves += [LeaveType(), {}]
        for leave in obj.spec.leaves:
            self.assertIsInstance(leave, LeaveType)

        # when setting a list, its content should be converted in the expected object type.
        obj.spec.leaves = [{"value": "hello"}]
        self.assertTrue(len(obj.spec.leaves) == 1)
        self.assertIsInstance(obj.spec.leaves[0], LeaveType)
        self.assertEqual(obj.spec.leaves[0].value, "hello")

    def test_set_none(self):
        obj = BaseType()
        self.assertFalse("spec" in obj)
        obj.spec = None

        # accessing spec recreate it (after it was set to None)
        obj.spec.leaves += None
        self.assertTrue("spec" in obj)
        # but appending None to a Typed array is a noop
        self.assertEqual(0, len(obj.spec.leaves))

        # setting prop to None delete it
        obj.spec = None
        self.assertFalse("spec" in obj)

    def test_update(self):
        obj = BaseType()
        # merge supports using camelCase key name (and keyword without trailing '_')
        obj |= {"spec": {"value": "hello"}}
        self.assertEqual(obj.spec.value, "hello")

        obj.spec.update(leave={"value": "world"}, leaves=[{"value": 42}])
        self.assertEqual(obj.spec.leave.value, "world")
        self.assertEqual(obj.spec.leaves[0].value, 42)
        self.assertEqual(obj, obj.update({}))

    def test_update_camel(self):
        sp = SpecialProperty()
        # merge supports using camelCase key name (and keyword without trailing '_')
        sp.update({"from": "value"})
        self.assertEqual(sp.from_, "value")
        sp.update({"loadURLs": "urls", "myProperty": 25})
        self.assertEqual(sp.load_urls, "urls")
        self.assertEqual(sp.my_property, 25)

    def test_from_dict(self):
        # When initializing from a dict
        # it should be recursively converted to type safe objects.
        obj = BaseType.from_dict({"spec": {"value": "Hello", "leave": {"value": "leave"}, "leaves": [{"value": "or let die"}]}})
        self.assertIsInstance(obj, BaseType)
        self.assertIsInstance(obj.spec, SubType)
        self.assertIsInstance(obj.spec.leave, LeaveType)
        for leave in obj.spec.leaves:
            self.assertIsInstance(leave, LeaveType)

    # accessing and setting unknown attributes must raise
    def test_validation(self):
        base = BaseType()
        with self.assertRaises(AttributeError):
            _ = base.unknown

        with self.assertRaises(AttributeError):
            base.spec.unknown = ""

        with self.assertRaises(AttributeError):
            base.update({"unknown": "foo"})

    def test_read_only(self):
        dep = Deployment("myobj", namespace="default")
        # Make sure api_version and kind are read-only
        with self.assertRaises(AttributeError):
            dep.api_version = "youpi"

        with self.assertRaises(AttributeError):
            dep.group = "youpi"

        with self.assertRaises(AttributeError):
            dep.kind = "youpi"

        with self.assertRaises(AttributeError):
            dep.update({"apiVersion": "Anything"})

        with self.assertRaises(AttributeError):
            dep.update({"kind": "Something"})

        with self.assertRaises(AttributeError):
            dep.update({"group": "OK"})

        # And ensure status, and matching read-only fields are ignored
        dep.update({"status": {""}, "apiVersion": "apps/v1", "kind": "deployment"})

    def type_info(self):
        self.assertEqual(Deployment.api_version, "apps/v1")
        self.assertEqual(Deployment.group, "apps")
        self.assertEqual(Deployment.kind, "Deployment")


class LoaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        register_modules(kubic.api.__spec__)
        register_modules(kubic.crds.__spec__)

    def test_create(self):
        spec = {"apiVersion": "apps/v1", "kind": "Deployment", "spec": {}, "metadata": {"name": "myobject"}, "status": {}}
        rsrc = create_api_resource(spec)
        self.assertIsInstance(rsrc, Deployment)
        self.assertIsInstance(rsrc.metadata, ObjectMeta)
        self.assertEqual(rsrc.metadata.name, "myobject")
        self.assertEqual("apps/v1", rsrc.api_version)
        self.assertEqual("apps", rsrc.group)
        self.assertEqual("Deployment", rsrc.kind)

        # Test that kind is case insensitive
        spec["kind"] = "deployment"
        rsrc = create_api_resource(spec)
        self.assertIsInstance(rsrc, Deployment)
        self.assertIsInstance(rsrc.metadata, ObjectMeta)
        self.assertEqual(rsrc.metadata.name, "myobject")
        self.assertEqual("apps/v1", rsrc.api_version)
        self.assertEqual("apps", rsrc.group)
        self.assertEqual("Deployment", rsrc.kind)

    def test_create_any(self):
        spec = {"apiVersion": "apps/v3", "kind": "Deployment", "spec": {}, "metadata": {"name": "myobject"}, "status": {}}
        rsrc = create_api_resource(spec)
        self.assertIsInstance(rsrc, KubernetesApiResource)
        self.assertIsInstance(rsrc.metadata, ObjectMeta)
        self.assertEqual("myobject", rsrc.metadata.name)
        self.assertEqual("apps/v3", rsrc.api_version)
        self.assertEqual("Deployment", rsrc.kind)
        self.assertEqual("apps", rsrc.group)

    def test_metaclass(self):
        self.assertEqual("CustomResource", CustomResource.kind)
        self.assertEqual("com.xenonium", CustomResource.group)
        self.assertEqual("com.xenonium/v1", CustomResource.api_version)
        self.assertTrue(CustomResource.namespaced)


class WriterTest(unittest.TestCase):
    def test_writer(self):
        rsrc = apps.Deployment(name="myapp", namespace="default")
        rsrc.metadata.labels["foo"] = "bar"

        _ = rsrc.metadata.annotations
        rsrc.spec.paused = True
        rsrc.spec.template.spec.hostname = "example.com"
        _ = rsrc.spec.template.metadata.annotations
        rsrc.spec.template.metadata.labels["foo"] = "bar"
        rsrc.spec.selector.match_labels = {}
        rsrc.spec.selector.match_expressions = [LabelSelectorRequirement()]
        rsrc.spec.strategy = DeploymentStrategy()

        value = yaml.dump(rsrc, Dumper=KubernetesObjectDumper, sort_keys=True)
        data = yaml.load(value, yaml.CSafeLoader)

        self.assertEqual(data["metadata"]["labels"]["foo"], "bar")
        self.assertNotIn("annotations", data["metadata"])
        self.assertIn("template", data["spec"])

        self.assertNotIn("annotations", data["spec"]["template"]["metadata"])
        self.assertEqual(data["spec"]["template"]["metadata"]["labels"]["foo"], "bar")
        self.assertIn("strategy", data["spec"])
        self.assertIn("matchLabels", data["spec"]["selector"])
        self.assertEqual(1, len(data["spec"]["selector"]["matchExpressions"]))
        self.assertTrue(data["spec"]["paused"])
