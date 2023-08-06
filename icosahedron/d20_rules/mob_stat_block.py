from icosahedron.utils.dictable import Dictable


class MobStatBlock(Dictable):
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

    def __init__(
        self,
        name,
        hit_points,
        armor_class,
        attack_bonus,
        damage,
        speed,
        abilities,
        skills,
        special_abilities,
        equipment,
        alignment,
        description,
    ):
        """
        Initializes a new instance of the MobStatBlock class.

        Args:
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
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attack_bonus = attack_bonus
        self.damage = damage
        self.speed = speed
        self.abilities = abilities
        self.skills = skills
        self.special_abilities = special_abilities
        self.equipment = equipment
        self.alignment = alignment
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "hit_points": self.hit_points,
            "armor_class": self.armor_class,
            "attack_bonus": self.attack_bonus,
            "damage": self.damage,
            "speed": self.speed,
            "abilities": self.abilities,
            "skills": self.skills,
            "special_abilities": self.special_abilities,
            "equipment": self.equipment,
            "alignment": self.alignment,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
