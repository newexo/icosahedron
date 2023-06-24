import unittest

class CharacterClass:
    def __init__(self, hit_dice, base_attack_bonus, bab_progression, skill_points):
        self.hit_dice = hit_dice
        self.base_attack_bonus = base_attack_bonus
        self.bab_progression = bab_progression
        self.skill_points = skill_points

class D20Character:
    def __init__(self, level, character_class, constitution_modifier):
        self.level = level
        self.character_class = character_class
        self.constitution_modifier = constitution_modifier

    def compute_hit_points(self):
        hit_dice = self.character_class.hit_dice
        hit_points = hit_dice + self.constitution_modifier
        for _ in range(2, self.level + 1):
            hit_points += max(1, (hit_dice // 2 + 1)) + self.constitution_modifier
        return hit_points

    def compute_base_attack_bonus(self):
        bab = self.character_class.base_attack_bonus + (self.level - 1) * self.character_class.bab_progression
        return bab

    def compute_skill_points(self):
        skill_points = self.character_class.skill_points
        for _ in range(2, self.level + 1):
            skill_points += max(1, (self.character_class.skill_points // 2 + 1))
        return skill_points


class D20CharacterTestCase(unittest.TestCase):
    def test_compute_hit_points(self):
        char_class = CharacterClass(hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2)
        character = D20Character(level=1, character_class=char_class, constitution_modifier=2)

        expected_hit_points = 12
        actual_hit_points = character.compute_hit_points()

        self.assertEqual(actual_hit_points, expected_hit_points)

    def test_compute_base_attack_bonus(self):
        char_class = CharacterClass(hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2)
        character = D20Character(level=3, character_class=char_class, constitution_modifier=2)

        expected_bab = 2.5
        actual_bab = character.compute_base_attack_bonus()

        self.assertEqual(actual_bab, expected_bab)

    def test_compute_skill_points(self):
        char_class = CharacterClass(hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2)
        character = D20Character(level=5, character_class=char_class, constitution_modifier=2)

        expected_skill_points = 9
        actual_skill_points = character.compute_skill_points()

        self.assertEqual(actual_skill_points, expected_skill_points)


if __name__ == '__main__':
    unittest.main()