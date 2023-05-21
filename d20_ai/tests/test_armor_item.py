import unittest

from d20_ai.d20_rules.inventory_items.armor_item import ArmorItem
from d20_ai.tests.base_test_case import BaseTestCase


class TestArmorItem(unittest.TestCase, BaseTestCase):
    def setUp(self):
        self.instance = ArmorItem(
            name="Chain Mail",
            armor_class=16,
            max_dex_bonus=2,
            check_penalty=-5,
            spell_failure=30,
            speed_reduction=10,
            weight=40,
            value=75,
            condition="new",
        )
        self.load_data("chain_mail.json")

    def instance_test(self, instance):
        self.assertEqual(instance.name, "Chain Mail")
        self.assertEqual(instance.armor_class, 16)
        self.assertEqual(instance.max_dex_bonus, 2)
        self.assertEqual(instance.check_penalty, -5)
        self.assertEqual(instance.spell_failure, 30)
        self.assertEqual(instance.speed_reduction, 10)
        self.assertEqual(instance.weight, 40)
        self.assertEqual(instance.value, 75)
        self.assertEqual(instance.condition, "new")

    def from_dict(self):
        return ArmorItem.from_dict(self.instance_dict)


if __name__ == "__main__":
    unittest.main()
