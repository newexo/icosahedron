import unittest

from icosahedron.tests.base_test_case import BaseTestCase
from icosahedron.d20_rules.character_class import CharacterClass


class TestCharacterClass(unittest.TestCase, BaseTestCase):
    def setUp(self):
        hit_dice = 10
        base_attack_bonus = 1
        bab_progression = 0.75
        skill_points = 2

        self.instance = CharacterClass(
            hit_dice, base_attack_bonus, bab_progression, skill_points
        )
        self.load_data("fighter_class.json")

    def instance_test(self, instance):
        self.assertEqual(instance.hit_dice, 10)
        self.assertEqual(instance.base_attack_bonus, 1)
        self.assertEqual(instance.bab_progression, 0.75)
        self.assertEqual(instance.skill_points, 2)

    def from_dict(self):
        return CharacterClass.from_dict(self.instance_dict)


if __name__ == "__main__":
    unittest.main()
