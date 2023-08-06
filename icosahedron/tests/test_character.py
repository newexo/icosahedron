import unittest

from icosahedron.d20_rules.character_class import CharacterClass, Character


class TestCharacter(unittest.TestCase):
    def test_compute_hit_points(self):
        char_class = CharacterClass(
            hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2
        )
        character = Character(
            level=1, character_class=char_class, constitution_modifier=2, intelligence_modifier=1
        )

        expected_hit_points = 12
        actual_hit_points = character.compute_hit_points()

        self.assertEqual(actual_hit_points, expected_hit_points)

    def test_compute_base_attack_bonus(self):
        char_class = CharacterClass(
            hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2
        )
        character = Character(
            level=3, character_class=char_class, constitution_modifier=2, intelligence_modifier=1
        )

        expected_bab = 2.5
        actual_bab = character.compute_base_attack_bonus()

        self.assertEqual(actual_bab, expected_bab)

    def test_compute_skill_points(self):
        char_class = CharacterClass(
            hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2
        )
        character = Character(
            level=5, character_class=char_class, constitution_modifier=2, intelligence_modifier=1
        )

        expected_skill_points = 15
        actual_skill_points = character.compute_skill_points()

        self.assertEqual(actual_skill_points, expected_skill_points)


if __name__ == "__main__":
    unittest.main()
