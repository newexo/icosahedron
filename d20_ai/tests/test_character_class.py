import unittest

from d20_ai.d20_rules.character_class import CharacterClass

class TestCharacterClass(unittest.TestCase):
    def test_character_class_init(self):
        hit_dice = 10
        base_attack_bonus = 1
        bab_progression = 0.75
        skill_points = 2

        char_class = CharacterClass(hit_dice, base_attack_bonus, bab_progression, skill_points)

        self.assertEqual(char_class.hit_dice, hit_dice)
        self.assertEqual(char_class.base_attack_bonus, base_attack_bonus)
        self.assertEqual(char_class.bab_progression, bab_progression)
        self.assertEqual(char_class.skill_points, skill_points)

if __name__ == '__main__':
    unittest.main()