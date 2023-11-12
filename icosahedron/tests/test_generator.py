import unittest

import json

from icosahedron.generate.generate_from_example import (
    GeneratorArmor,
    GeneratorGenericItem,
    GeneratorMagicRing,
    GeneratorWeapon,
)


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.item = GeneratorArmor(self.get_item_name())

    def tearDown(self):
        pass

    def get_item_name(self):
        return "Scale Mail"

    def test_init_armor_generator_default(self):
        self.assertEqual(0, self.item.temperature)
        self.assertEqual(500, self.item.max_tokens)
        self.assertEqual("gpt-3.5-turbo", self.item.model)
        self.assertEqual("####", self.item.delimiter)
        self.assertEqual(self.get_item_name(), self.item.name)

    def test_init_armor_generator(self):
        item = GeneratorArmor(
            self.get_item_name(),
            temperature=0.5,
            max_tokens=100,
            model="fancy-model",
            delimiter="***",
        )
        self.assertEqual(0.5, item.temperature)
        self.assertEqual(100, item.max_tokens)
        self.assertEqual("fancy-model", item.model)
        self.assertEqual("***", item.delimiter)
        self.assertEqual(self.get_item_name(), item.name)

    def test_system_message(self):
        expected = """You are a developer for software implementation of a fantasy RPG. \
You are adding entries to database of adventuring equipment. \
The name of the equipment item to implement will be delimited with \
#### characters.
Output a JSON objects, where each object is like the following example: \
{
    "name": "Chain Mail",
    "weight": 40,
    "description": "Chain Mail Armor is made up of thousands of interlinked metal rings, forming a flexible mesh-like \
structure that drapes over your body to provide protection. The intricate web of these interlocking rings not only \
absorbs the impact of attacks but also allows for some degree of movement and flexibility, despite its weight and \
bulkiness.",
    "condition": "new",
    "value": 75,
    "armor_class": 16,
    "max_dex_bonus": 2,
    "check_penalty": -5,
    "spell_failure": 30,
    "speed_reduction": 10
}  \
Only JSON objects, with nothing else."""
        actual = self.item.system_message
        self.assertEqual(expected, actual)

    def test_user_message(self):
        expected = "Write a JSON object for ####Scale Mail####."
        actual = self.item.user_message
        self.assertEqual(expected, actual)

    def test_messages(self):
        expected = [
            {"role": "system", "content": self.item.system_message},
            {"role": "user", "content": self.item.user_message},
        ]
        actual = self.item.messages
        self.assertEqual(expected, actual)

    def test_armor_json_sample(self):
        expected = {
            "name": "Chain Mail",
            "weight": 40,
            "description": "Chain Mail Armor is made up of thousands of interlinked metal rings, forming a flexible mesh-like structure that drapes over your body to provide protection. The intricate web of these interlocking rings not only absorbs the impact of attacks but also allows for some degree of movement and flexibility, despite its weight and bulkiness.",
            "condition": "new",
            "value": 75,
            "armor_class": 16,
            "max_dex_bonus": 2,
            "check_penalty": -5,
            "spell_failure": 30,
            "speed_reduction": 10,
        }

        actual = self.item.json_sample
        actual = json.loads(actual)
        self.assertEqual(expected, actual)

    def test_weapon_json_sample(self):
        item = GeneratorWeapon("Mace")
        expected = {
            "name": "Mace",
            "weight": 8.0,
            "description": "A mace is a blunt weapon with a heavy, metal head mounted on a sturdy wooden or metal shaft, designed for delivering powerful and crushing blows in close combat.",
            "condition": "Good",
            "value": 308.0,
            "damage": "1d6",
            "damage_type": "Bludgeoning",
            "range": 0,
            "crit_range": 2,
            "crit_multiplier": "2x",
            "special_properties": [],
        }
        actual = item.json_sample
        actual = json.loads(actual)
        self.assertEqual(expected, actual)

    def test_magic_ring(self):
        item = GeneratorMagicRing("Ring of Protection")
        expected = {
            "name": "Ring of Protection",
            "weight": 0,
            "description": "A Ring of Protection is a magical ring that, when worn, enhances the wearer's defense and increases their chances of avoiding harm by bolstering their armor class.",
            "condition": "Good",
            "value": 100,
            "magic_bonus": 2,
            "effect": "protection",
        }
        actual = item.json_sample
        actual = json.loads(actual)
        self.assertEqual(expected, actual)

    def test_generic_item(self):
        item = GeneratorGenericItem("Spellbook")
        expected = {
            "name": "Spellbook",
            "weight": 3,
            "description": "A spellbook is a leather-bound or parchment-covered tome filled with meticulously inscribed arcane symbols, incantations, and diagrams, often adorned with mystical sigils, used by wizards and spellcasters to record and study their magical spells.",
            "condition": "good",
            "value": 100,
        }
        actual = item.json_sample
        actual = json.loads(actual)
        self.assertEqual(expected, actual)
