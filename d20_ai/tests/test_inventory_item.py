import unittest
from d20_ai.inventory_item import InventoryItem, ArmorItem, WeaponItem, MagicRing

bedroll = {
    "name": "Bedroll",
    "weight": 7,
    "condition": "Good",
    "value": 1,
    "properties": "A bedroll is a simple but essential item for adventurers who need to sleep outdoors. It provides a soft and comfortable surface to sleep on, as well as some insulation against the cold or damp ground. When rolled up, it is compact and easy to carry, making it a convenient addition to any adventurer's gear.",
}
spellbook = {
    "name": "Spellbook",
    "weight": 3,
    "condition": "Good",
    "value": 50,
    "properties": "A spellbook is a wizard's most important possession, containing all of the spells they have learned and the formulae to prepare them. Alice's spellbook contains a variety of spells, including some that she has prepared for the day and others that she has yet to learn. The spellbook is carefully maintained and protected, as its loss would be a serious setback for Alice's magical studies.",
}

wand_of_magic_missiles = {
    "name": "Wand of Magic Missiles",
    "weight": 1,
    "condition": "Good",
    "value": 375,
    "properties": "A wand of magic missiles is a powerful arcane device that can unleash bolts of magical force at its target. Alice's wand can cast the magic missile spell, which automatically hits its target and deals force damage. The wand has a limited number of charges, and can be recharged by spending gold and time at a wizard's workshop.",
}

ring_of_protection = {
    "name": "Ring of Protection",
    "weight": 0,
    "condition": "Good",
    "value": 2000,
    "properties": "A ring of protection is a magical item that enhances the wearer's defenses. Alice's ring provides a +1 bonus to her Armor Class and all saving throws, making her harder to hit and more resilient to spells and other attacks. The ring is a valuable and sought-after item, and would be a valuable asset to any adventurer.",
}

rations = {
    "name": "Rations",
    "weight": 2,
    "condition": "Good",
    "value": 5,
    "properties": "Rations are a basic food supply that adventurers carry with them on their journeys. Alice's rations consist of dried meat, bread, and fruit, and are enough to sustain her for several days. They are carefully stored and packed to prevent spoilage, and are an essential part of Alice's survival kit.",
}

waterskin = {
    "name": "Waterskin",
    "weight": 5,
    "condition": "Good",
    "value": 1,
    "properties": "A waterskin is a container used to carry drinking water on long journeys. Alice's waterskin is made of sturdy leather and can hold up to a gallon of water. It is carefully filled and stored to prevent spills and leaks, and is an essential part of Alice's survival kit.",
}

alice_items = [
    spellbook,
    wand_of_magic_missiles,
    ring_of_protection,
    rations,
    waterskin,
]

chain_mail = {
    "name": "Chain Mail",
    "armor_class": 16,
    "strength_requirement": 13,
    "stealth_disadvantage": True,
    "weight": 55,
}

mace = {
    "name": "Mace",
    "damage": "1d6 bludgeoning",
    "properties": ["Versatile (1d8)", "Light"],
    "weight": 4,
}

shield = {"name": "Shield", "armor_class": 2, "weight": 6}

holy_symbol = {
    "name": "Holy Symbol",
    "description": "A silver amulet depicting a sunburst",
    "weight": 1,
}

eve_items = [chain_mail, mace, shield, holy_symbol]

mace = {
    "name": "Mace",
    "type": "Weapon",
    "subtype": "Bludgeoning",
    "damage": "1d8",
    "critical": "x2",
    "weight": 8.0,
    "value": 308.0,
    "condition": "Good",
}

quarterstaff = {
    "name": "Quarterstaff",
    "type": "Weapon",
    "subtype": "Bludgeoning",
    "damage": "1d6",
    "critical": "x2",
    "weight": 4.0,
    "value": 0.0,
    "condition": "Excellent",
}

chain_mail = ArmorItem(
    name="Chain mail",
    weight=40,
    value=150,
    armor_class=5,
    max_dex_bonus=2,
    check_penalty=-5,
    spell_failure=30,
    speed_reduction=10,
)

crossbow = {
    "name": "Heavy Crossbow",
    "type": "ranged",
    "subtype": "crossbow",
    "damage": "1d10",
    "critical": "19-20/x2",
    "range": "120 ft.",
    "weight": 8,
    "value": 50,
    "condition": "new",
}

ring_of_protection_dict = {
    "name": "Ring of Protection",
    "weight": 0.1,
    "value": 200,
    "condition": "Good",
    "magic_bonus": 1,
    "effect": "This ring grants a +1 deflection bonus to AC.",
}


class TestInventoryItem(unittest.TestCase):
    def test_init(self):
        item = InventoryItem(
            name="Spellbook", weight=3, description="A book of spells."
        )
        self.assertEqual(item.name, "Spellbook")
        self.assertEqual(item.weight, 3)
        self.assertEqual(item.description, "A book of spells.")
        self.assertEqual(item.condition, "new")
        self.assertEqual(item.value, 0)

        item = InventoryItem(
            name="Wand of Magic Missiles",
            weight=1,
            description="A wand that shoots magic missiles.",
        )
        self.assertEqual(item.name, "Wand of Magic Missiles")
        self.assertEqual(item.weight, 1)
        self.assertEqual(item.description, "A wand that shoots magic missiles.")
        self.assertEqual(item.condition, "new")
        self.assertEqual(item.value, 0)

    def test_to_dict(self):
        item = InventoryItem(
            name="Spellbook", weight=3, description="A book of spells."
        )
        expected_dict = {
            "name": "Spellbook",
            "weight": 3,
            "description": "A book of spells.",
            "condition": "new",
            "value": 0,
        }
        self.assertDictEqual(item.to_dict(), expected_dict)

        item = InventoryItem(
            name="Wand of Magic Missiles",
            weight=1,
            description="A wand that shoots magic missiles.",
            value=100,
        )
        expected_dict = {
            "name": "Wand of Magic Missiles",
            "weight": 1,
            "description": "A wand that shoots magic missiles.",
            "condition": "new",
            "value": 100,
        }
        self.assertDictEqual(item.to_dict(), expected_dict)

    def test_from_dict(self):
        dict_data = {
            "name": "Spellbook",
            "weight": 3,
            "description": "A book of spells.",
            "condition": "used",
            "value": 50,
        }
        item = InventoryItem.from_dict(dict_data)
        self.assertEqual(item.name, "Spellbook")
        self.assertEqual(item.weight, 3)
        self.assertEqual(item.description, "A book of spells.")
        self.assertEqual(item.condition, "used")
        self.assertEqual(item.value, 50)

        dict_data = {
            "name": "Wand of Magic Missiles",
            "weight": 1,
            "description": "A wand that shoots magic missiles.",
            "value": 100,
        }
        item = InventoryItem.from_dict(dict_data)
        self.assertEqual(item.name, "Wand of Magic Missiles")
        self.assertEqual(item.weight, 1)
        self.assertEqual(item.description, "A wand that shoots magic missiles.")
        self.assertEqual(item.condition, "new")
        self.assertEqual(item.value, 100)


class TestArmorItem(unittest.TestCase):
    def test_init(self):
        # create an instance of ArmorItem
        armor = ArmorItem(
            name="Chain Mail",
            armor_class=16,
            max_dex_bonus=2,
            check_penalty=-5,
            spell_failure=30,
            speed_reduction=10,
            weight=40,
            value=75,
            condition="new",
        )

        # check that the properties are correctly set
        self.assertEqual(armor.name, "Chain Mail")
        self.assertEqual(armor.armor_class, 16)
        self.assertEqual(armor.max_dex_bonus, 2)
        self.assertEqual(armor.check_penalty, -5)
        self.assertEqual(armor.spell_failure, 30)
        self.assertEqual(armor.speed_reduction, 10)
        self.assertEqual(armor.weight, 40)
        self.assertEqual(armor.value, 75)
        self.assertEqual(armor.condition, "new")

    def test_from_dict(self):
        item_dict = {
            "name": "Chain mail",
            "item_type": "armor",
            "armor_type": "medium",
            "armor_class": 5,
            "max_dex_bonus": 2,
            "check_penalty": -5,
            "spell_failure": 30,
            "speed_reduction": -5,
            "weight": 40,
            "value": 150,
            "condition": "new",
        }

        item = ArmorItem.from_dict(item_dict)

        self.assertEqual(item.name, "Chain mail")
        # self.assertEqual(item.armor_type, "medium")
        self.assertEqual(item.armor_class, 5)
        self.assertEqual(item.max_dex_bonus, 2)
        self.assertEqual(item.check_penalty, -5)
        self.assertEqual(item.spell_failure, 30)
        self.assertEqual(item.speed_reduction, -5)
        self.assertEqual(item.weight, 40)
        self.assertEqual(item.value, 150)
        self.assertEqual(item.condition, "new")

    def test_to_dict(self):
        item = ArmorItem("Chain mail", 40, 150, 5, 2, -5, 30, -5)

        item_dict = item.to_dict()

        self.assertEqual(item_dict["name"], "Chain mail")
        self.assertEqual(item_dict["armor_class"], 5)
        self.assertEqual(item_dict["max_dex_bonus"], 2)
        self.assertEqual(item_dict["check_penalty"], -5)
        self.assertEqual(item_dict["spell_failure"], 30)
        self.assertEqual(item_dict["speed_reduction"], -5)
        self.assertEqual(item_dict["weight"], 40)
        self.assertEqual(item_dict["value"], 150)
        self.assertEqual(item_dict["condition"], "new")


class TestWeaponItem(unittest.TestCase):
    def setUp(self):
        self.mace = WeaponItem(
            name="Mace",
            weight=8.0,
            value=308.0,
            description="nothing special",
            condition="Good",
            range=0,
            damage="1d6",
            damage_type="Bludgeoning",
            crit_range=2,
            crit_multiplier="2x",
        )

    def test_init(self):
        self.assertEqual(self.mace.name, "Mace")
        self.assertEqual(self.mace.value, 308)
        self.assertEqual(self.mace.condition, "Good")
        self.assertEqual(self.mace.value, 308.0)
        self.assertEqual(self.mace.weight, 8)
        self.assertEqual(self.mace.damage, "1d6")
        self.assertEqual(self.mace.damage_type, "Bludgeoning")
        self.assertEqual(self.mace.description, "nothing special")

    def test_to_dict(self):
        expected = {
            "name": "Mace",
            "weight": 8.0,
            "description": "nothing special",
            "condition": "Good",
            "value": 308.0,
            "damage": "1d6",
            "damage_type": "Bludgeoning",
            "range": 0,
            "crit_range": 2,
            "crit_multiplier": "2x",
            "special_properties": [],
        }
        actual = self.mace.to_dict()
        self.assertEqual(actual, expected)

    def test_from_dict(self):
        data = {
            "name": "Mace",
            "weight": 8.0,
            "description": "nothing special",
            "condition": "Good",
            "value": 20,
            "damage": "1d6",
            "damage_type": "Bludgeoning",
            "range": 0,
            "crit_range": 2,
            "crit_multiplier": "2x",
            "special_properties": [],
        }
        mace = WeaponItem.from_dict(data)
        self.assertEqual(mace.name, "Mace")
        self.assertEqual(mace.value, 20)
        self.assertEqual(mace.condition, "Good")
        self.assertEqual(mace.weight, 8.0)
        self.assertEqual(mace.damage, "1d6")
        self.assertEqual(mace.damage_type, "Bludgeoning")
        self.assertEqual(mace.description, "nothing special")


class TestMagicRing(unittest.TestCase):
    def test_init(self):
        # Test initialization of MagicRing object
        ring = MagicRing(
            name="Ring of Protection",
            weight=0,
            value=100,
            condition="Good",
            effect="protection",
            magic_bonus=2,
        )
        self.assertEqual(ring.name, "Ring of Protection")
        self.assertEqual(ring.value, 100)
        self.assertEqual(ring.condition, "Good")
        self.assertEqual(ring.effect, "protection")
        self.assertEqual(ring.magic_bonus, 2)

    def test_to_dict(self):
        # Test conversion of MagicRing object to dictionary
        ring = MagicRing(
            name="Ring of Protection",
            weight=0,
            value=100,
            condition="Good",
            magic_bonus=2,
            effect="protection",
        )
        ring_dict = ring.to_dict()
        expected_dict = {
            "name": "Ring of Protection",
            "weight": 0,
            "description": "",
            "condition": "Good",
            "value": 100,
            "magic_bonus": 2,
            "effect": "protection",
        }
        self.assertDictEqual(ring_dict, expected_dict)

    def test_from_dict(self):
        # Test conversion of dictionary to MagicRing object
        ring_dict = {
            "name": "Ring of Protection",
            "weight": 0,
            "value": 100,
            "condition": "Good",
            "effect": "protection",
            "magic_bonus": 2,
        }
        ring = MagicRing.from_dict(ring_dict)
        self.assertEqual(ring.name, "Ring of Protection")
        self.assertEqual(ring.value, 100)
        self.assertEqual(ring.condition, "Good")
        self.assertEqual(ring.effect, "protection")
        self.assertEqual(ring.magic_bonus, 2)


if __name__ == "__main__":
    unittest.main()
