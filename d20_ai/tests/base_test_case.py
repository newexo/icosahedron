import json
from abc import ABCMeta, abstractmethod

from d20_ai.directories import test_data


class BaseTestCase(metaclass=ABCMeta):
    def __init__(self):
        self.instance_str = None
        self.instance = None
        self.instance_dict = None

    @abstractmethod
    def instance_test(self, instance):
        pass

    @abstractmethod
    def from_dict(self):
        pass

    @abstractmethod
    def assertEqual(self, expected, actual):
        pass

    def load_data(self, filename):
        with open(test_data(filename)) as f:
            self.instance_str = f.read()

        self.instance_dict = json.loads(self.instance_str)

    def test_init(self):
        self.instance_test(self.instance)

    def test_to_dict(self):
        expected = self.instance_dict
        actual = self.instance.to_dict()
        self.assertEqual(expected, actual)

    def test_from_dict(self):
        # verify that we can change from dict to Character and back
        instance_from_dict = self.from_dict()
        self.instance_test(instance_from_dict)

        expected = self.instance_dict
        actual = instance_from_dict.to_dict()
        self.assertEqual(expected, actual)
