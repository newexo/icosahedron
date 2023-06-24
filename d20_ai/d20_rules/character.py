class CharacterClass:
    def __init__(self, hit_dice, base_attack_bonus, bab_progression, skill_points):
        self.hit_dice = hit_dice
        self.base_attack_bonus = base_attack_bonus
        self.bab_progression = bab_progression
        self.skill_points = skill_points

    def to_dict(self):
        return {
            "hit_dice": self.hit_dice,
            "base_attack_bonus": self.base_attack_bonus,
            "bab_progression": self.bab_progression,
            "skill_points": self.skill_points
        }

    @classmethod
    def from_dict(cls, class_dict):
        return cls(
            hit_dice=class_dict["hit_dice"],
            base_attack_bonus=class_dict["base_attack_bonus"],
            bab_progression=class_dict["bab_progression"],
            skill_points=class_dict["skill_points"]
        )


# Example usage:
fighter_dict = {
    "hit_dice": 10,
    "base_attack_bonus": 1,
    "bab_progression": 0.75,
    "skill_points": 2
}

fighter_class = CharacterClass.from_dict(fighter_dict)

print(fighter_class.to_dict())

class FighterClass(CharacterClass):
    def __init__(self):
        super().__init__(hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2)


class WizardClass(CharacterClass):
    def __init__(self):
        super().__init__(hit_dice=6, base_attack_bonus=0, bab_progression=0.5, skill_points=2)


# Example usage:
character = D20Character(level=1, character_class=FighterClass(), constitution_modifier=2, intelligence_modifier=1)

hit_points = character.compute_hit_points()
print("Hit Points:", hit_points)

base_attack_bonus = character.compute_base_attack_bonus()
print("Base Attack Bonus:", base_attack_bonus)

available_skill_points = character.compute_skill_points()
print("Available Skill Points:", available_skill_points)
