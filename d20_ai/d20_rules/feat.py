from d20_ai.utils.dictable import Dictable


class Feat(Dictable):
    def __init__(
        self, name, prerequisites, benefit, description, usage, normal_use=None
    ):
        self.name = name
        self.prerequisites = prerequisites
        self.benefit = benefit
        self.description = description
        self.usage = usage
        self.normal_use = normal_use

    def to_dict(self):
        feat_dict = {
            "name": self.name,
            "prerequisites": self.prerequisites,
            "benefit": self.benefit,
            "description": self.description,
            "usage": self.usage,
        }
        if self.normal_use is not None:
            feat_dict["normal_use"] = self.normal_use
        return feat_dict

    @classmethod
    def from_dict(cls, feat_dict):
        return cls(
            feat_dict["name"],
            feat_dict["prerequisites"],
            feat_dict["benefit"],
            feat_dict["description"],
            feat_dict["usage"],
            feat_dict.get("normal_use"),
        )
