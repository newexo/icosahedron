from pydantic import BaseModel

from icosahedron.d20_rules.character_class import CharacterClass


class Character(BaseModel):
    """
    Represents a character in the d20 system.

    Attributes:
        level (int): The level of the character.
        character_class (CharacterClass): The character's class.
        constitution_modifier (int): The modifier based on the character's constitution.
        intelligence_modifier (int): The modifier based on the character's intelligence.
    """

    level: int
    character_class: CharacterClass
    constitution_modifier: int
    intelligence_modifier: int

    def compute_hit_points(self) -> int:
        """
        Computes the hit points of the character based on their class and level.

        Returns:
            int: The calculated hit points of the character.
        """
        hit_dice = self.character_class.hit_dice
        hit_points = hit_dice + self.constitution_modifier
        for _ in range(2, self.level + 1):
            hit_points += max(1, (hit_dice // 2 + 1)) + self.constitution_modifier
        return hit_points

    def compute_base_attack_bonus(self) -> float:
        """
        Computes the base attack bonus of the character based on their class and level.

        Returns:
            float: The calculated base attack bonus of the character.
        """
        bab = (
            self.character_class.base_attack_bonus
            + (self.level - 1) * self.character_class.bab_progression
        )
        return bab

    def compute_skill_points(self) -> int:
        """
        Computes the skill points of the character based on their class, level, and intelligence.

        Returns:
            int: The calculated skill points of the character.
        """
        skill_points = self.character_class.skill_points + self.intelligence_modifier
        for _ in range(2, self.level + 1):
            skill_points += (
                max(1, (self.character_class.skill_points // 2 + 1))
                + self.intelligence_modifier
            )
        return skill_points
