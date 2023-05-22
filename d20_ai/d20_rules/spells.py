from d20_ai.utils.dictable import Dictable


class Spell(Dictable):
    """
    A class representing a spell in the D20 system.
    """

    def __init__(
        self,
        name,
        school,
        level,
        casting_time,
        range_,
        duration,
        saving_throw,
        spell_resistance,
        components,
        description,
    ):
        """
        Initializes a new instance of the Spell class.

        Args:
            name (str): The name of the spell.
            school (str): The school of magic the spell belongs to.
            level (int): The level of the spell.
            casting_time (str): The time required to cast the spell.
            range_ (str): The range of the spell.
            duration (str): The duration of the spell.
            saving_throw (str): The type of saving throw, if any, required to resist the spell.
            spell_resistance (bool): Indicates whether the spell can be resisted by spell resistance.
            components (list[str]): The components required to cast the spell.
            description (str): A description of the spell.
        """
        self.name = name
        self.school = school
        self.level = level
        self.casting_time = casting_time
        self.range = range_
        self.duration = duration
        self.saving_throw = saving_throw
        self.spell_resistance = spell_resistance
        self.components = components
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "school": self.school,
            "level": self.level,
            "casting_time": self.casting_time,
            "range": self.range,
            "duration": self.duration,
            "saving_throw": self.saving_throw,
            "spell_resistance": self.spell_resistance,
            "components": self.components,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj["name"],
            dict_obj["school"],
            dict_obj["level"],
            dict_obj["casting_time"],
            dict_obj["range"],
            dict_obj["duration"],
            dict_obj["saving_throw"],
            dict_obj["spell_resistance"],
            dict_obj["components"],
            dict_obj["description"],
        )
