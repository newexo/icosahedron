import unittest

from icosahedron.d20_rules.inventory_items.weapon_item import WeaponItem
from icosahedron.tests.base_test_case import BaseTestCase


class TestWeaponItem(unittest.TestCase, BaseTestCase):
    def setUp(self):
        self.instance = WeaponItem(
            name="Mace",
            weight=8.0,
            value=308.0,
            description="nothing special",
            condition="Good",
            range=0,
            damage="1d6",
            damage_type="Bludgeoning",
            crit_range=2,
            crit_multiplier="2x",
        )
        self.load_data("mace.json")

    def instance_test(self, instance):
        self.assertEqual(instance.name, "Mace")
        self.assertEqual(instance.value, 308)
        self.assertEqual(instance.condition, "Good")
        self.assertEqual(instance.value, 308.0)
        self.assertEqual(instance.weight, 8)
        self.assertEqual(instance.damage, "1d6")
        self.assertEqual(instance.damage_type, "Bludgeoning")
        self.assertEqual(instance.description, "nothing special")

    def from_dict(self):
        return WeaponItem.from_dict(self.instance_dict)


if __name__ == "__main__":
    unittest.main()
