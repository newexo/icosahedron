from d20_ai.d20_rules.inventory_items.inventory_item import InventoryItem


class WeaponItem(InventoryItem):
    def __init__(
        self,
        name,
        weight,
        value,
        damage,
        damage_type,
        range,
        crit_range,
        crit_multiplier,
        special_properties=None,
        condition=None,
        description=None,
    ):
        super().__init__(
            name=name,
            weight=weight,
            value=value,
            condition=condition,
            description=description,
        )
        self.damage = damage
        self.damage_type = damage_type
        self.range = range
        self.crit_range = crit_range
        self.crit_multiplier = crit_multiplier
        self.special_properties = special_properties or []

    def to_dict(self):
        data = super().to_dict()
        data.update(
            {
                "damage": self.damage,
                "damage_type": self.damage_type,
                "range": self.range,
                "crit_range": self.crit_range,
                "crit_multiplier": self.crit_multiplier,
                "special_properties": self.special_properties,
            }
        )
        return data

    @classmethod
    def from_dict(cls, data):
        special_properties = data.get("special_properties", [])
        return cls(
            name=data["name"],
            weight=data["weight"],
            value=data["value"],
            damage=data["damage"],
            damage_type=data["damage_type"],
            range=data["range"],
            crit_range=data["crit_range"],
            crit_multiplier=data["crit_multiplier"],
            special_properties=special_properties,
            condition=data.get("condition", None),
            description=data.get("description", None),
        )
