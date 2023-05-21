import unittest
import json

from d20_ai.directories import test_data
from d20_ai.character_sheet import D20CharacterSheet


class TestD20CharacterSheet(unittest.TestCase):
    def setUp(self):
        self.instance = D20CharacterSheet(
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
                "charisma": 10,
            },
            skills={
                "arcana": 6,
                "history": 6,
                "investigation": 6,
                "nature": 6,
                "religion": 6,
            },
            feats=[
                {
                    "name": "Alert",
                    "description": "+5 initiative and cannot be surprised",
                },
                {
                    "name": "Magic Initiate",
                    "description": "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)",
                },
            ],
            equipment=[
                "Spellbook",
                "Wand",
                "Backpack",
                "Bedroll",
                "Rations (5 days)",
                "Waterskin",
                "20 gold pieces",
            ],
            spells_known={
                "cantrips": ["Mage Hand", "Prestidigitation", "Ray of Frost"],
                "1st_level_spells": ["Magic Missile", "Shield", "Cure Wounds"],
            },
            background="Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and",
        )

        with open(test_data("alice.json")) as f:
            self.instance_str = f.read()

        self.instance_dict = json.loads(self.instance_str)

    def instance_test(self, instance):
        self.assertEqual(instance.name, "Alice")
        self.assertEqual(instance.race, "Human")
        self.assertEqual(instance.char_class, "Wizard")
        self.assertEqual(instance.level, 3)
        self.assertEqual(instance.alignment, "Neutral Good")
        self.assertEqual(
            instance.ability_scores,
            {
                "strength": 8,
                "dexterity": 14,
                "constitution": 12,
                "intelligence": 16,
                "wisdom": 10,
                "charisma": 10,
            },
        )
        self.assertEqual(
            instance.skills,
            {"arcana": 6, "history": 6, "investigation": 6, "nature": 6, "religion": 6},
        )
        self.assertEqual(len(instance.feats), 2)
        self.assertEqual(instance.feats[0]["name"], "Alert")
        self.assertEqual(
            instance.feats[0]["description"], "+5 initiative and cannot be surprised"
        )
        self.assertEqual(instance.feats[1]["name"], "Magic Initiate")
        self.assertEqual(
            instance.feats[1]["description"],
            "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)",
        )
        self.assertEqual(len(instance.equipment), 7)
        self.assertEqual(
            instance.equipment,
            [
                "Spellbook",
                "Wand",
                "Backpack",
                "Bedroll",
                "Rations (5 days)",
                "Waterskin",
                "20 gold pieces",
            ],
        )
        self.assertEqual(
            instance.spells_known,
            {
                "cantrips": ["Mage Hand", "Prestidigitation", "Ray of Frost"],
                "1st_level_spells": ["Magic Missile", "Shield", "Cure Wounds"],
            },
        )
        self.assertEqual(
            instance.background,
            "Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and",
        )

    def from_dict(self, d):
        return D20CharacterSheet.from_dict(d)
    def test_init(self):
        self.instance_test(self.instance)

    def test_to_dict(self):
        expected = self.instance_dict
        actual = self.instance.to_dict()
        self.assertEqual(expected, actual)

    def test_from_dict(self):
        # verify that we can change from dict to Character and back
        instance_from_dict = self.from_dict(self.instance_dict)
        self.instance_test(instance_from_dict)

        expected = self.instance_dict
        actual = instance_from_dict.to_dict()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
