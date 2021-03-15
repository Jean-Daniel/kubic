import unittest
from collections.abc import MutableSequence
from typing import List, Union

from k8s.base import K8SResource


class LeaveType(K8SResource):
    value: Union[str, int]


class SubType(K8SResource):
    value: str
    leave: LeaveType
    leaves: List[LeaveType]


class BaseType(K8SResource):
    spec: SubType


class SpecialProperty(K8SResource):
    from_: str
    load_urls: str
    my_property: int

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

        # leave type should be none by default
        self.assertIsNone(obj.spec.value)
        # ditto for union
        self.assertIsNone(obj.spec.leave.value)

    def test_set(self):
        obj = BaseType()
        obj.spec = {}
        self.assertIsInstance(obj.spec, SubType)

        obj.spec.leaves = []
        obj.spec.leaves.append({})
        obj.spec.leaves += {}
        obj.spec.leaves += LeaveType()
        obj.spec.leaves += [LeaveType(), {}]
        for leave in obj.spec.leaves:
            self.assertIsInstance(leave, LeaveType)

        obj.spec.leaves = [{
            "value": "hello"
        }]
        self.assertTrue(len(obj.spec.leaves) == 1)
        self.assertIsInstance(obj.spec.leaves[0], LeaveType)
        self.assertEqual(obj.spec.leaves[0].value, "hello")

    def test_merge(self):
        sp = SpecialProperty()
        sp.merge({"from": "value"})
        self.assertEqual(sp.from_, "value")
        sp.merge({"loadURLs": "urls", "myProperty": 25})
        self.assertEqual(sp.load_urls, "urls")
        self.assertEqual(sp.my_property, 25)

    def test_from_dict(self):
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
