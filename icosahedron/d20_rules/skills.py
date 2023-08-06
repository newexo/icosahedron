from icosahedron.utils.dictable import Dictable


class Skill(Dictable):
    """
    Represents a skill object with various attributes.
    """

    def __init__(
        self, name, description, ability_score, class_skill, synergy, retry, special
    ):
        """
        Initialize a Skill object.

        Args:
            name (str): The name of the skill.
            description (str): A brief description of the skill.
            ability_score (str): The ability score associated with the skill.
            class_skill (bool): Indicates if the skill is a class skill for certain character classes.
            synergy (list): A list of dictionaries representing skill synergies.
            retry (bool): Indicates whether retries are allowed for the skill.
            special (list): A list of strings providing additional information about the skill.
        """
        self.name = name
        self.description = description
        self.ability_score = ability_score
        self.class_skill = class_skill
        self.synergy = synergy
        self.retry = retry
        self.special = special

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "abilityScore": self.ability_score,
            "classSkill": self.class_skill,
            "synergy": self.synergy,
            "retry": self.retry,
            "special": self.special,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["description"],
            data["abilityScore"],
            data["classSkill"],
            data["synergy"],
            data["retry"],
            data["special"],
        )
