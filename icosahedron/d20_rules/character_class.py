from pydantic import BaseModel


class CharacterClass(BaseModel):
    """
    Represents a character class in the d20 system.

    Attributes:
        hit_dice (int): The hit dice value for the character class.
        base_attack_bonus (int): The base attack bonus for the character class.
        bab_progression (float): The progression rate of the base attack bonus per level.
        skill_points (int): The number of skill points gained per level.
    """

    hit_dice: int
    base_attack_bonus: int
    bab_progression: float
    skill_points: int
