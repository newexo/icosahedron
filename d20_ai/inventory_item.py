class InventoryItem:
    def __init__(self, name, weight, description="", condition="new", value=0):
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
            "value": self.value
        }

    @classmethod
    def from_dict(cls, dict_data):
        return cls(
            name=dict_data.get("name", ""),
            weight=dict_data.get("weight", 0),
            description=dict_data.get("description", ""),
            condition=dict_data.get("condition", "new"),
            value=dict_data.get("value", 0)
        )


class ArmorItem(InventoryItem):
    def __init__(self, name, weight, value, armor_class, max_dex_bonus, check_penalty, spell_failure, speed_reduction,
                 condition="new"):
        super().__init__(name, weight, value, condition)
        self.armor_class = armor_class
        self.max_dex_bonus = max_dex_bonus
        self.check_penalty = check_penalty
        self.spell_failure = spell_failure
        self.speed_reduction = speed_reduction

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict.update({
            'armor_class': self.armor_class,
            'max_dex_bonus': self.max_dex_bonus,
            'check_penalty': self.check_penalty,
            'spell_failure': self.spell_failure,
            'speed_reduction': self.speed_reduction
        })
        return item_dict

    @classmethod
    def from_dict(cls, item_dict):
        return cls(
            item_dict['name'], item_dict['weight'], item_dict['value'], item_dict['armor_class'],
            item_dict['max_dex_bonus'], item_dict['check_penalty'], item_dict['spell_failure'],
            item_dict['speed_reduction'], item_dict['condition']
        )

class WeaponItem(InventoryItem):
    def __init__(self, name, weight, value, damage, damage_type, range, crit_range, crit_multiplier, special_properties=None, condition=None):
        super().__init__(name, weight, value, condition)
        self.damage = damage
        self.damage_type = damage_type
        self.range = range
        self.crit_range = crit_range
        self.crit_multiplier = crit_multiplier
        self.special_properties = special_properties or []

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'damage': self.damage,
            'damage_type': self.damage_type,
            'range': self.range,
            'crit_range': self.crit_range,
            'crit_multiplier': self.crit_multiplier,
            'special_properties': self.special_properties
        })
        return data

    @classmethod
    def from_dict(cls, data):
        special_properties = data.get('special_properties', [])
        return cls(
            data['name'],
            data['weight'],
            data['value'],
            data['damage'],
            data['damage_type'],
            data['range'],
            data['crit_range'],
            data['crit_multiplier'],
            special_properties,
            data.get('condition', None)
        )

class MagicRing(InventoryItem):
    def __init__(self, name: str, weight: float, value: float, condition: str, magic_bonus: int, effect: str):
        super().__init__(name, weight, value, condition)
        self.magic_bonus = magic_bonus
        self.effect = effect

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict.update({
            "magic_bonus": self.magic_bonus,
            "effect": self.effect
        })
        return item_dict

    @classmethod
    def from_dict(cls, item_dict):
        return cls(
            item_dict['name'],
            item_dict['weight'],
            item_dict['value'],
            item_dict['condition'],
            item_dict['magic_bonus'],
            item_dict['effect']
        )

