from typing import List
from icosahedron.d20_rules.inventory_items.inventory_item import InventoryItem


class WeaponItem(InventoryItem):
    damage: str
    damage_type: str
    range: float
    crit_range: int
    crit_multiplier: str
    special_properties: List[str] = []
