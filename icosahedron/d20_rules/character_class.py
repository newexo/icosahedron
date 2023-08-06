from icosahedron.utils.dictable import Dictable


class CharacterClass(Dictable):
    """
    Represents a character class in the d20 system.

    Attributes:
        hit_dice (int): The hit dice value for the character class.
        base_attack_bonus (int): The base attack bonus for the character class.
        bab_progression (float): The progression rate of the base attack bonus per level.
        skill_points (int): The number of skill points gained per level.

    Methods:
        to_dict(): Converts the CharacterClass instance to a dictionary.
        from_dict(class_dict): Creates a new CharacterClass instance from a dictionary.
    """

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
            "skill_points": self.skill_points,
        }

    @classmethod
    def from_dict(cls, class_dict):
        return cls(
            hit_dice=class_dict["hit_dice"],
            base_attack_bonus=class_dict["base_attack_bonus"],
            bab_progression=class_dict["bab_progression"],
            skill_points=class_dict["skill_points"],
        )


class Character:
    """
    Represents a character in the d20 system.

    Attributes:
        level (int): The level of the character.
        character_class (CharacterClass): The character's class.
        constitution_modifier (int): The modifier based on the character's constitution.
        intelligence_modifier (int): The modifier based on the character's intelligence.

    Methods:
        compute_hit_points(): Computes the hit points of the character based on their class and level.
        compute_base_attack_bonus(): Computes the base attack bonus of the character based on their class and level.
        compute_skill_points(): Computes the skill points of the character based on their class, level, and intelligence.

    """

    def __init__(
        self, level, character_class, constitution_modifier, intelligence_modifier
    ):
        """
        Initializes a new instance of the Character class.

        Args:
            level (int): The level of the character.
            character_class (CharacterClass): The character's class.
            constitution_modifier (int): The modifier based on the character's constitution.
            intelligence_modifier (int): The modifier based on the character's intelligence.
        """
        self.level = level
        self.character_class = character_class
        self.constitution_modifier = constitution_modifier
        self.intelligence_modifier = intelligence_modifier

    def compute_hit_points(self):
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

    def compute_base_attack_bonus(self):
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

    def compute_skill_points(self):
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
