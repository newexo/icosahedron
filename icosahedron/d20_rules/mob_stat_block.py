from pydantic import BaseModel
from typing import Dict, List


class MobStatBlock(BaseModel):
    """
    A class representing the stat block of a non-player character (NPC) or monster in a role-playing game.

    Attributes:
        name (str): The name of the NPC/monster.
        hit_points (int): The amount of damage the NPC/monster can sustain before being defeated.
        armor_class (int): The difficulty of hitting the NPC/monster with an attack.
        attack_bonus (int): The bonus added to the NPC/monster's attack roll.
        damage (str): The type and amount of damage the NPC/monster deals with a successful attack.
        speed (int): The NPC/monster's speed in feet per round.
        abilities (dict): A dictionary of the NPC/monster's abilities (e.g. Strength, Dexterity, etc.).
        skills (dict): A dictionary of the NPC/monster's skills and their bonuses.
        special_abilities (list): A list of the NPC/monster's special abilities.
        equipment (list): A list of the NPC/monster's equipment.
        alignment (str): The NPC/monster's moral and ethical alignment.
        description (str): A brief description of the NPC/monster's appearance and behavior.
    """

    name: str
    hit_points: int
    armor_class: int
    attack_bonus: int
    damage: str
    speed: int
    abilities: Dict[str, int]
    skills: Dict[str, int]
    special_abilities: List[str]
    equipment: List[str]
    alignment: str
    description: str
