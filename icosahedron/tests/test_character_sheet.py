import json
import pytest
from icosahedron.d20_rules.character_sheet import CharacterSheet
from icosahedron.directories import test_data


@pytest.fixture
def character_sheet():
    return CharacterSheet(
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


@pytest.fixture
def instance_dict():
    with open(test_data("alice.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(character_sheet):
    assert character_sheet.name == "Alice"
    assert character_sheet.race == "Human"
    assert character_sheet.char_class == "Wizard"
    assert character_sheet.level == 3
    assert character_sheet.alignment == "Neutral Good"
    assert character_sheet.ability_scores == {
        "strength": 8,
        "dexterity": 14,
        "constitution": 12,
        "intelligence": 16,
        "wisdom": 10,
        "charisma": 10,
    }
    assert character_sheet.skills == {
        "arcana": 6,
        "history": 6,
        "investigation": 6,
        "nature": 6,
        "religion": 6,
    }
    assert len(character_sheet.feats) == 2
    assert character_sheet.feats[0]["name"] == "Alert"
    assert (
        character_sheet.feats[0]["description"]
        == "+5 initiative and cannot be surprised"
    )
    assert character_sheet.feats[1]["name"] == "Magic Initiate"
    assert (
        character_sheet.feats[1]["description"]
        == "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)"
    )
    assert len(character_sheet.equipment) == 7
    assert character_sheet.equipment == [
        "Spellbook",
        "Wand",
        "Backpack",
        "Bedroll",
        "Rations (5 days)",
        "Waterskin",
        "20 gold pieces",
    ]
    assert character_sheet.spells_known == {
        "cantrips": ["Mage Hand", "Prestidigitation", "Ray of Frost"],
        "1st_level_spells": ["Magic Missile", "Shield", "Cure Wounds"],
    }
    assert (
        character_sheet.background
        == "Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and"
    )


def test_from_dict(instance_dict):
    character_sheet = CharacterSheet.from_dict(instance_dict)
    assert character_sheet.name == "Alice"
    assert character_sheet.race == "Human"
    assert character_sheet.char_class == "Wizard"
    assert character_sheet.level == 3
    assert character_sheet.alignment == "Neutral Good"
    assert character_sheet.ability_scores == {
        "strength": 8,
        "dexterity": 14,
        "constitution": 12,
        "intelligence": 16,
        "wisdom": 10,
        "charisma": 10,
    }
    assert character_sheet.skills == {
        "arcana": 6,
        "history": 6,
        "investigation": 6,
        "nature": 6,
        "religion": 6,
    }
    assert len(character_sheet.feats) == 2
    assert character_sheet.feats[0]["name"] == "Alert"
    assert (
        character_sheet.feats[0]["description"]
        == "+5 initiative and cannot be surprised"
    )
    assert character_sheet.feats[1]["name"] == "Magic Initiate"
    assert (
        character_sheet.feats[1]["description"]
        == "Can cast two cantrips and one 1st-level spell from a chosen spellcasting class (cleric)"
    )
    assert len(character_sheet.equipment) == 7
    assert character_sheet.equipment == [
        "Spellbook",
        "Wand",
        "Backpack",
        "Bedroll",
        "Rations (5 days)",
        "Waterskin",
        "20 gold pieces",
    ]
    assert character_sheet.spells_known == {
        "cantrips": ["Mage Hand", "Prestidigitation", "Ray of Frost"],
        "1st_level_spells": ["Magic Missile", "Shield", "Cure Wounds"],
    }
    assert (
        character_sheet.background
        == "Alice grew up in a small village where she was fascinated by the natural world and the secrets of the arcane. She left her village to study magic at a nearby wizard academy, where she excelled in her studies and gained a reputation as a diligent and creative student. After graduating, she set out on a journey to explore the world and use her magic to help others. Alice is driven by a desire to uncover new knowledge and"
    )
