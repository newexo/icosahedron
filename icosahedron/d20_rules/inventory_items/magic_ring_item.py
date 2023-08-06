from icosahedron.d20_rules.inventory_items.inventory_item import InventoryItem


class MagicRing(InventoryItem):
    def __init__(
        self,
        name: str,
        weight: float,
        value: float,
        condition: str,
        magic_bonus: int,
        effect: str,
    ):
        super().__init__(name, weight=weight, value=value, condition=condition)
        self.magic_bonus = magic_bonus
        self.effect = effect

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict.update({"magic_bonus": self.magic_bonus, "effect": self.effect})
        return item_dict

    @classmethod
    def from_dict(cls, item_dict):
        return cls(
            name=item_dict["name"],
            weight=item_dict["weight"],
            value=item_dict["value"],
            condition=item_dict["condition"],
            magic_bonus=item_dict["magic_bonus"],
            effect=item_dict["effect"],
        )
