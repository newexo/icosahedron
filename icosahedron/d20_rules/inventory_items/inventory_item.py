from icosahedron.utils.dictable import Dictable


class InventoryItem(Dictable):
    def __init__(self, name, weight, description="", condition="new", value: float = 0):
        self.name = name
        self.weight = weight
        self.description = description
        self.condition = condition
        self.value = value

    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "description": self.description,
            "condition": self.condition,
            "value": self.value,
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            name=dict_data.get("name", ""),
            weight=dict_data.get("weight", 0),
            description=dict_data.get("description", ""),
            condition=dict_data.get("condition", "new"),
            value=dict_data.get("value", 0),
        )
