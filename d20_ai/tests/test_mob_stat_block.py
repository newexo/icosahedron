import unittest
from d20_ai.mob_stat_block import NPC


class TestNPC(unittest.TestCase):
    def test_from_json(self):
        iggy_json = '{"name": "Iggy", "hit_points": 12, "armor_class": 14, "attack_bonus": 4, "damage": "1d6+2", "speed": 30, "abilities": {"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6}, "skills": {"stealth": 6}, "special_abilities": {"nimbleEscape": true}, "equipment": ["Shortsword", "Shortbow", "Leather Armor"], "alignment": "Chaotic Evil", "description": "Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord."}'
        iggy_obj = NPC.from_json(iggy_json)

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
