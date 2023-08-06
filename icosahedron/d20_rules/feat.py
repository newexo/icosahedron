from icosahedron.utils.dictable import Dictable


class Feat(Dictable):
    """
    Class representing a feat in a role-playing game.
    """

    def __init__(
        self, name, prerequisites, benefit, description, usage, normal_use=None
    ):
        """
        Initialize a Feat object.

        Args:
            name (str): The name of the feat.
            prerequisites (str): The prerequisites for the feat.
            benefit (str): The benefit provided by the feat.
            description (str): A description of the feat.
            usage (str): Instructions on how to use the feat.
            normal_use (str, optional): The description of the normal use without the feat.

        Returns:
            Feat: A Feat object.

        """
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
