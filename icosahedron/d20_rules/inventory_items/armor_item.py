from icosahedron.d20_rules.inventory_items.inventory_item import InventoryItem


class ArmorItem(InventoryItem):
    def __init__(
        self,
        name,
        weight,
        value,
        armor_class,
        max_dex_bonus,
        check_penalty,
        spell_failure,
        speed_reduction,
        condition="new",
    ):
        super().__init__(name, weight=weight, value=value, condition=condition)
        self.armor_class = armor_class
        self.max_dex_bonus = max_dex_bonus
        self.check_penalty = check_penalty
        self.spell_failure = spell_failure
        self.speed_reduction = speed_reduction

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict.update(
            {
                "armor_class": self.armor_class,
                "max_dex_bonus": self.max_dex_bonus,
                "check_penalty": self.check_penalty,
                "spell_failure": self.spell_failure,
                "speed_reduction": self.speed_reduction,
            }
        )
        return item_dict

    @classmethod
    def from_dict(cls, item_dict):
        return cls(
            item_dict["name"],
            item_dict["weight"],
            item_dict["value"],
            item_dict["armor_class"],
            item_dict["max_dex_bonus"],
            item_dict["check_penalty"],
            item_dict["spell_failure"],
            item_dict["speed_reduction"],
            item_dict["condition"],
        )
