import unittest
from collections.abc import MutableSequence
from typing import List, Union

from k8s.base import KubernetesObject


class LeaveType(KubernetesObject):
    value: Union[str, int]


class SubType(KubernetesObject):
    value: str
    leave: LeaveType
    leaves: List[LeaveType]


class BaseType(KubernetesObject):
    spec: SubType


class SpecialProperty(KubernetesObject):
    from_: str
    load_urls: str
    my_property: int

    # _revfield_names_ are used when settings
    # values from a dictionary to convert camelCase names
    # into snake names. Only names that can be naively converted to
    # snake case are generated.
    _revfield_names_ = {
        "from": "from_",
        "loadURLs": "load_urls"
    }


class ResourceTest(unittest.TestCase):

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
        obj.spec.leaves = [{
            "value": "hello"
        }]
        self.assertTrue(len(obj.spec.leaves) == 1)
        self.assertIsInstance(obj.spec.leaves[0], LeaveType)
        self.assertEqual(obj.spec.leaves[0].value, "hello")

    def test_merge(self):
        sp = SpecialProperty()
        # merge supports using camelCase key name (and keyword without trailing '_')
        sp.merge({"from": "value"})
        self.assertEqual(sp.from_, "value")
        sp.merge({"loadURLs": "urls", "myProperty": 25})
        self.assertEqual(sp.load_urls, "urls")
        self.assertEqual(sp.my_property, 25)

    def test_from_dict(self):
        # When initializing from a dict
        # it should be recursively converted to type safe objects.
        obj = BaseType.from_dict({
            "spec": {
                "value": "Hello",
                "leave": {
                    "value": "leave"
                },
                "leaves": [{
                    "value": "or let die"
                }]
            }
        })
        self.assertIsInstance(obj, BaseType)
        self.assertIsInstance(obj.spec, SubType)
        self.assertIsInstance(obj.spec.leave, LeaveType)
        for leave in obj.spec.leaves:
            self.assertIsInstance(leave, LeaveType)

    # accessing and setting unknown attributes must raise
    def test_validation(self):
        base = BaseType()
        with self.assertRaises(AttributeError):
            a = base.unknown

        with self.assertRaises(AttributeError):
            base.spec.unknown = ""

        with self.assertRaises(AttributeError):
            base.merge({"unknown": "foo"})
