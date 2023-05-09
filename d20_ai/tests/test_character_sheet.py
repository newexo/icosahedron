import unittest


import unittest

class TestD20CharacterSheet(unittest.TestCase):
    def test_init(self):
        # Test valid inputs
        alice = D20CharacterSheet(
            name="Alice",
            race="Human",
            char_class="Wizard",
            level=3,
            alignment="Neutral Good",
            ability_scores={
                "strength": 8,
                "dexterity": 14,
                "constitution": 12,
                "intelligence": 16,
                "wisdom": 10,
                "charisma": 10
            },
            skills={
                "arcana": 6,
                "history": 6,
                "investigation": 6,
                "nature": 6,
                "religion": 6
            },
            feats=[
                {
                    "name": "Alert",
                    "description": "+5 initiative and cannot be surprised"
                },
                {
                    "name": "Magic Initiate",
                    "description": "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)"
                }
            ],
            equipment=[
                "Spellbook",
                "Wand",
                "Backpack",
                "Bedroll",
                "Rations (5 days)",
                "Waterskin",
                "20 gold pieces"
            ],
            spells_known={
                "cantrips": [
                    "Mage Hand",
                    "Prestidigitation",
                    "Ray of Frost"
                ],
                "1st_level_spells": [
                    "Magic Missile",
                    "Shield",
                    "Cure Wounds"
                ]
            },
            background="Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and"

        )

        self.assertEqual(alice.name, "Alice")
        self.assertEqual(alice.race, "Human")
        self.assertEqual(alice.char_class, "Wizard")
        self.assertEqual(alice.level, 3)
        self.assertEqual(alice.alignment, "Neutral Good")
        self.assertEqual(alice.ability_scores, {
            "strength": 8,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 16,
            "wisdom": 10,
            "charisma": 10
        })
        self.assertEqual(alice.skills, {
            "arcana": 6,
            "history": 6,
            "investigation": 6,
            "nature": 6,
            "religion": 6
        })
        self.assertEqual(len(alice.feats), 2)
        self.assertEqual(alice.feats[0]["name"], "Alert")
        self.assertEqual(alice.feats[0]["description"], "+5 initiative and cannot be surprised")
        self.assertEqual(alice.feats[1]["name"], "Magic Initiate")
        self.assertEqual(alice.feats[1]["description"], "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)")
        self.assertEqual(len(alice.equipment), 7)
        self.assertEqual(alice.equipment[0], "Spellbook")
        self.assertEqual(alice.equipment[1], "Wand")
        self.assertEqual(alice.equipment[2], "Backpack")
        # self.assertEqual(al
        # test is incomplete

import unittest

class TestD20CharacterSheet(unittest.TestCase):
    def test_to_dict(self):
        # Create a D20CharacterSheet object
        alice = D20CharacterSheet(
            name="Alice",
            race="Human",
            char_class="Wizard",
            level=3,
            alignment="Neutral Good",
            ability_scores={
                "strength": 8,
                "dexterity": 14,
                "constitution": 12,
                "intelligence": 16,
                "wisdom": 10,
                "charisma": 10
            },
            skills={
                "arcana": 6,
                "history": 6,
                "investigation": 6,
                "nature": 6,
                "religion": 6
            },
            feats=[
                {
                    "name": "Alert",
                    "description": "+5 initiative and cannot be surprised"
                },
                {
                    "name": "Magic Initiate",
                    "description": "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)"
                }
            ],
            equipment=[
                "Spellbook",
                "Wand",
                "Backpack",
                "Bedroll",
                "Rations (5 days)",
                "Waterskin",
                "20 gold pieces"
            ],
            spells_known={
                "cantrips": [
                    "Mage Hand",
                    "Prestidigitation",
                    "Ray of Frost"
                ],
                "1st_level_spells": [
                    "Magic Missile",
                    "Shield",
                    "Cure Wounds"
                ]
            },
            background="Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and"
        )

        # Convert the object to a dictionary
        alice_dict = alice.to_dict()

        # Check that the dictionary has the correct values
        self.assertEqual(alice_dict["name"], "Alice")
        self.assertEqual(alice_dict["race"], "Human")
        self.assertEqual(alice_dict["char_class"], "Wizard")
        self.assertEqual(alice_dict["level"], 3)
        self.assertEqual(alice_dict["alignment"], "Neutral Good")
        self.assertEqual(alice_dict["ability_scores"], {
            "strength": 8,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 16,
            "wisdom": 10,
            "charisma": 10
        })
        self.assertEqual(alice_dict["skills"], {
            "arcana": 6,
            "history": 6,
            "investigation": 6,
            "nature": 6,
            "religion": 6
        })
        self.assertEqual(len(alice_dict["feats"]), 2)
        self.assertEqual(alice_dict["feats"][0]["name"], "Alert")
        self.assertEqual(alice_dict["feats"][0]["description"], "+5 initiative and cannot be surprised")
        self.assertEqual(alice_dict["feats"][1]["name"], "Magic Initiate")
        self.assertEqual(alice_dict["feats"][1]["description"], "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)")
        # self.assertEqual(len
        # test is incomplete

import unittest

class TestD20CharacterSheet(unittest.TestCase):
    def test_from_dict(self):
        # Create a dictionary representing a D20CharacterSheet
        alice_dict = {
            "name": "Alice",
            "race": "Human",
            "char_class": "Wizard",
            "level": 3,
            "alignment": "Neutral Good",
            "ability_scores": {
                "strength": 8,
                "dexterity": 14,
                "constitution": 12,
                "intelligence": 16,
                "wisdom": 10,
                "charisma": 10
            },
            "skills": {
                "arcana": 6,
                "history": 6,
                "investigation": 6,
                "nature": 6,
                "religion": 6
            },
            "feats": [
                {
                    "name": "Alert",
                    "description": "+5 initiative and cannot be surprised"
                },
                {
                    "name": "Magic Initiate",
                    "description": "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)"
                }
            ],
            "equipment": [
                "Spellbook",
                "Wand",
                "Backpack",
                "Bedroll",
                "Rations (5 days)",
                "Waterskin",
                "20 gold pieces"
            ],
            "spells_known": {
                "cantrips": [
                    "Mage Hand",
                    "Prestidigitation",
                    "Ray of Frost"
                ],
                "1st_level_spells": [
                    "Magic Missile",
                    "Shield",
                    "Cure Wounds"
                ]
            },
            "background": "Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and"
        }

        # Create a D20CharacterSheet object from the dictionary
        alice = D20CharacterSheet.from_dict(alice_dict)

        # Check that the object has the correct values
        self.assertEqual(alice.name, "Alice")
        self.assertEqual(alice.race, "Human")
        self.assertEqual(alice.char_class, "Wizard")
        self.assertEqual(alice.level, 3)
        self.assertEqual(alice.alignment, "Neutral Good")
        self.assertEqual(alice.ability_scores, {
            "strength": 8,
            "dexterity": 14,
            "constitution": 12,
            "intelligence": 16,
            "wisdom": 10,
            "charisma": 10
        })
        self.assertEqual(alice.skills, {
            "arcana": 6,
            "history": 6,
            "investigation": 6,
            "nature": 6,
            "religion": 6
        })
        self.assertEqual(len(alice.feats), 2)
        self.assertEqual(alice.feats[0].name, "Alert")
        self.assertEqual(alice.feats[0].description, "+5 initiative and cannot be surprised")
        self.assertEqual(alice.feats[1].name, "Magic Initiate")
        # self.assertEqual(alice.feats[1].description, "Can cast two cantrips and one 1st-leve
        # test is incomplete


if __name__ == '__main__':
    unittest.main()
