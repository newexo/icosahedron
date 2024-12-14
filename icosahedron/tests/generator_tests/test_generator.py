import json

from icosahedron.tests.generator_tests.conftest import MockOpenAI
from icosahedron.generate.generate_from_example import (
    GeneratorFromExample,
    ExampleItemType,
)
from icosahedron.generate.model_context import ModelContext


def test_generator(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.ARMOR, "Scale Mail", context=context
    )

    assert context == item.context
    assert "Scale Mail" == item.name


def test_system_message(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.ARMOR, "Scale Mail", context=context
    )
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
    assert expected == item.system_message


def test_user_message(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.ARMOR, "Scale Mail", context=context
    )
    expected = "Write a JSON object for ####Scale Mail####. Do produce any other output besides the JSON."
    assert expected == item.user_message


def test_messages(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.ARMOR, "Scale Mail", context=context
    )
    expected = [
        {"role": "system", "content": item.system_message},
        {"role": "user", "content": item.user_message},
    ]
    assert expected == item.messages


def test_armor_json_sample(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.ARMOR, "Scale Mail", context=context
    )
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
    actual = json.loads(item.json_sample)
    assert expected == actual


def test_weapon_json_sample(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.WEAPON, "Mace", context=context
    )
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
    actual = json.loads(item.json_sample)
    assert expected == actual


def test_magic_ring(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.MAGIC_RING, "Ring of Protection", context=context
    )
    expected = {
        "name": "Ring of Protection",
        "weight": 0,
        "description": "A Ring of Protection is a magical ring that, when worn, enhances the wearer's defense and increases their chances of avoiding harm by bolstering their armor class.",
        "condition": "Good",
        "value": 100,
        "magic_bonus": 2,
        "effect": "protection",
    }
    actual = json.loads(item.json_sample)
    assert expected == actual


def test_generic_item(context):
    item = GeneratorFromExample.get_generator(
        ExampleItemType.GENERIC_ITEM, "Spellbook", context=context
    )
    expected = {
        "name": "Spellbook",
        "weight": 3,
        "description": "A spellbook is a leather-bound or parchment-covered tome filled with meticulously inscribed arcane symbols, incantations, and diagrams, often adorned with mystical sigils, used by wizards and spellcasters to record and study their magical spells.",
        "condition": "good",
        "value": 100,
    }
    actual = json.loads(item.json_sample)
    assert expected == actual
