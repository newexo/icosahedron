import unittest

from d20_ai.d20_rules.inventory_items.magic_ring_item import MagicRing
from d20_ai.tests.base_test_case import BaseTestCase


class TestMagicRing(unittest.TestCase, BaseTestCase):
    def setUp(self):
        self.instance = MagicRing(
            name="Ring of Protection",
            weight=0,
            value=100,
            condition="Good",
            effect="protection",
            magic_bonus=2,
        )
        self.load_data("magic_ring.json")

    def instance_test(self, instance):
        instance = MagicRing(
            name="Ring of Protection",
            weight=0,
            value=100,
            condition="Good",
            effect="protection",
            magic_bonus=2,
        )
        self.assertEqual(instance.name, "Ring of Protection")
        self.assertEqual(instance.value, 100)
        self.assertEqual(instance.condition, "Good")
        self.assertEqual(instance.effect, "protection")
        self.assertEqual(instance.magic_bonus, 2)

    def from_dict(self):
        return MagicRing.from_dict(self.instance_dict)


if __name__ == "__main__":
    unittest.main()
