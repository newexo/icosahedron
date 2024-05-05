from icosahedron.d20_rules.inventory_items.inventory_item import InventoryItem


class ArmorItem(InventoryItem):
    armor_class: int
    max_dex_bonus: int
    check_penalty: int
    spell_failure: int
    speed_reduction: int
