class D20Character:
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


# Example usage:
character = D20Character(level=1, character_class=FighterClass(), constitution_modifier=2, intelligence_modifier=1)

hit_points = character.compute_hit_points()
print("Hit Points:", hit_points)

base_attack_bonus = character.compute_base_attack_bonus()
print("Base Attack Bonus:", base_attack_bonus)

available_skill_points = character.compute_skill_points()
print("Available Skill Points:", available_skill_points)