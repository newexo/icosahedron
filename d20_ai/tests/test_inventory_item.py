import unittest

from d20_ai.tests.base_test_case import BaseTestCase
from d20_ai.inventory_item import InventoryItem


class TestInventoryItem(unittest.TestCase, BaseTestCase):
    def setUp(self):
        self.instance = InventoryItem(
            name="Spellbook",
            weight=3,
            description="A book of spells.",
            condition="good",
            value=100,
        )
        self.load_data("spellbook.json")

    def instance_test(self, instance):
        self.assertEqual(instance.name, "Spellbook")
        self.assertEqual(instance.weight, 3)
        self.assertEqual(instance.description, "A book of spells.")
        self.assertEqual(instance.condition, "good")
        self.assertEqual(instance.value, 100)

    def from_dict(self):
        return InventoryItem.from_dict(self.instance_dict)


if __name__ == "__main__":
    unittest.main()
