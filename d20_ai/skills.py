class Skill:
    def __init__(self, name, description, ability_score, class_skill, synergy, retry, special):
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
            "special": self.special
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
            data["special"]
        )