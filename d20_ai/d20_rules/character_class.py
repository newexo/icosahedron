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


class Character:
    def __init__(self, level, character_class, constitution_modifier, intelligence_modifier):
        self.level = level
        self.character_class = character_class
        self.constitution_modifier = constitution_modifier
        self.intelligence_modifier = intelligence_modifier

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
        skill_points = self.character_class.skill_points + self.intelligence_modifier
        for _ in range(2, self.level + 1):
            skill_points += max(1, (self.character_class.skill_points // 2 + 1)) + self.intelligence_modifier
        return skill_points

