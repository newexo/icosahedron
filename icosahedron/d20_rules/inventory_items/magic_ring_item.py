from icosahedron.d20_rules.inventory_items.inventory_item import InventoryItem


class MagicRing(InventoryItem):
    magic_bonus: int
    effect: str
