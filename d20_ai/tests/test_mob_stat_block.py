import unittest
import json

from d20_ai.mob_stat_block import MobStatBlock


class TestMobStatBlock(unittest.TestCase):
    def setUp(self):
        self.iggy_json = '{"name": "Iggy", "hit_points": 12, "armor_class": 14, "attack_bonus": 4, "damage": "1d6+2", "speed": 30, "abilities": {"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6}, "skills": {"stealth": 6}, "special_abilities": {"nimbleEscape": true}, "equipment": ["Shortsword", "Shortbow", "Leather Armor"], "alignment": "Chaotic Evil", "description": "Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord."}'

    def test_from_json(self):
        iggy_obj = MobStatBlock.from_json(self.iggy_json)

        self.assertEqual(iggy_obj.name, "Iggy")
        self.assertEqual(iggy_obj.hit_points, 12)
        self.assertEqual(iggy_obj.armor_class, 14)
        self.assertEqual(iggy_obj.attack_bonus, 4)
        self.assertEqual(iggy_obj.damage, "1d6+2")
        self.assertEqual(iggy_obj.speed, 30)
        self.assertEqual(
            iggy_obj.abilities,
            {"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6},
        )
        self.assertEqual(iggy_obj.skills, {"stealth": 6})
        self.assertEqual(iggy_obj.special_abilities, {"nimbleEscape": True})
        self.assertEqual(
            iggy_obj.equipment, ["Shortsword", "Shortbow", "Leather Armor"]
        )
        self.assertEqual(iggy_obj.alignment, "Chaotic Evil")
        self.assertEqual(
            iggy_obj.description,
            "Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord.",
        )

    def test_to_json(self):
        expected = json.loads(self.iggy_json)
        iggy_obj = MobStatBlock.from_json(self.iggy_json)
        new_iggy_json = iggy_obj.to_json()
        actual = json.loads(new_iggy_json)
        self.assertEqual(expected, actual)

    def test_init(self):
        npc = MobStatBlock(
            "Iggy",
            10,
            12,
            3,
            "1d6+1",
            30,
            {"str": 8, "dex": 14, "con": 12, "int": 6, "wis": 10, "cha": 6},
            {"stealth": 4, "sleight_of_hand": 2},
            {"darkvision": True},
            ["dagger", "shortbow"],
            "Chaotic Evil",
            "Iggy is a sneaky goblin who loves nothing more than causing chaos.",
        )

        self.assertEqual(npc.name, "Iggy")
        self.assertEqual(npc.hit_points, 10)
        self.assertEqual(npc.armor_class, 12)
        self.assertEqual(npc.attack_bonus, 3)
        self.assertEqual(npc.damage, "1d6+1")
        self.assertEqual(npc.speed, 30)
        self.assertEqual(
            npc.abilities,
            {"str": 8, "dex": 14, "con": 12, "int": 6, "wis": 10, "cha": 6},
        )
        self.assertEqual(npc.skills, {"stealth": 4, "sleight_of_hand": 2})
        self.assertEqual(npc.special_abilities, {"darkvision": True})
        self.assertEqual(npc.equipment, ["dagger", "shortbow"])
        self.assertEqual(npc.alignment, "Chaotic Evil")
        self.assertEqual(
            npc.description,
            "Iggy is a sneaky goblin who loves nothing more than causing chaos.",
        )

    def test_to_dict(self):
        npc = MobStatBlock(
            "Iggy",
            10,
            12,
            3,
            "1d6+1",
            30,
            {"str": 8, "dex": 14, "con": 12, "int": 6, "wis": 10, "cha": 6},
            {"stealth": 4, "sleight_of_hand": 2},
            {"darkvision": True},
            ["dagger", "shortbow"],
            "Chaotic Evil",
            "Iggy is a sneaky goblin who loves nothing more than causing chaos.",
        )
        expected_dict = {
            "name": "Iggy",
            "hit_points": 10,
            "armor_class": 12,
            "attack_bonus": 3,
            "damage": "1d6+1",
            "speed": 30,
            "abilities": {
                "str": 8,
                "dex": 14,
                "con": 12,
                "int": 6,
                "wis": 10,
                "cha": 6,
            },
            "skills": {"stealth": 4, "sleight_of_hand": 2},
            "special_abilities": {"darkvision": True},
            "equipment": ["dagger", "shortbow"],
            "alignment": "Chaotic Evil",
            "description": "Iggy is a sneaky goblin who loves nothing more than causing chaos.",
        }

        self.assertEqual(npc.to_dict(), expected_dict)
