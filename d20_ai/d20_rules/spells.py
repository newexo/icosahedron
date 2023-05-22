import json

class Spell:
    def __init__(self, name, school, level, casting_time, range_, duration, saving_throw, spell_resistance, components, description):
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
            "description": self.description
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
            dict_obj["description"]
        )

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)