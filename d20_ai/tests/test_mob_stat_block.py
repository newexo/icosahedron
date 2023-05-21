import unittest

from d20_ai.tests.base_test_case import BaseTestCase
from d20_ai.d20_rules.mob_stat_block import MobStatBlock


class TestMobStatBlock(unittest.TestCase, BaseTestCase):
    def setUp(self):
        self.instance = MobStatBlock(
            name="Iggy",
            hit_points=12,
            armor_class=14,
            attack_bonus=4,
            damage="1d6+2",
            speed=30,
            abilities={"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6},
            skills={"stealth": 6},
            special_abilities=["nimbleEscape"],
            equipment=["Shortsword", "Shortbow", "Leather Armor"],
            alignment="Chaotic Evil",
            description="Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord.",
        )

        self.load_data("iggy.json")

    def instance_test(self, instance):
        self.assertEqual(instance.name, "Iggy")
        self.assertEqual(instance.hit_points, 12)
        self.assertEqual(instance.armor_class, 14)
        self.assertEqual(instance.attack_bonus, 4)
        self.assertEqual(instance.damage, "1d6+2")
        self.assertEqual(instance.speed, 30)
        self.assertEqual(
            instance.abilities,
            {"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6},
        )
        self.assertEqual(instance.skills, {"stealth": 6})
        self.assertEqual(instance.special_abilities, ["nimbleEscape"])
        self.assertEqual(
            instance.equipment, ["Shortsword", "Shortbow", "Leather Armor"]
        )
        self.assertEqual(instance.alignment, "Chaotic Evil")
        self.assertEqual(
            instance.description,
            "Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord.",
        )

    def from_dict(self):
        return MobStatBlock.from_dict(self.instance_dict)
