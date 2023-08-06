from icosahedron.utils.dictable import Dictable


class CharacterSheet(Dictable):
    def __init__(
        self,
        name,
        race,
        char_class,
        level,
        alignment,
        ability_scores,
        skills,
        feats,
        equipment,
        spells_known,
        background,
    ):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        self.alignment = alignment
        self.ability_scores = ability_scores
        self.skills = skills
        self.feats = feats
        self.equipment = equipment
        self.spells_known = spells_known
        self.background = background

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            race=data["race"],
            char_class=data["class"],
            level=data["level"],
            alignment=data["alignment"],
            ability_scores=data["ability_scores"],
            skills=data["skills"],
            feats=data["feats"],
            equipment=data["equipment"],
            spells_known=data["spells_known"],
            background=data["background"],
        )

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "level": self.level,
            "alignment": self.alignment,
            "ability_scores": self.ability_scores,
            "skills": self.skills,
            "feats": self.feats,
            "equipment": self.equipment,
            "spells_known": self.spells_known,
            "background": self.background,
        }
