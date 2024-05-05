import pytest
import json
from icosahedron.d20_rules.skills import Skill
from icosahedron.directories import test_data


@pytest.fixture
def skill_data():
    return {
        "name": "Spellcraft",
        "description": "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting.",
        "ability_score": "Intelligence",
        "class_skill": True,
        "synergy": [
            {
                "skill": "Knowledge (Arcana)",
                "bonus": 2,
                "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
            },
            {
                "skill": "Use Magic Device",
                "bonus": 2,
                "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
            },
        ],
        "retry": True,
        "special": [
            "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
            "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
            "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
            "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
        ],
    }


@pytest.fixture
def skill():
    skill_data = {
        "name": "Spellcraft",
        "description": "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting.",
        "ability_score": "Intelligence",
        "class_skill": True,
        "synergy": [
            {
                "skill": "Knowledge (Arcana)",
                "bonus": 2,
                "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
            },
            {
                "skill": "Use Magic Device",
                "bonus": 2,
                "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
            },
        ],
        "retry": True,
        "special": [
            "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
            "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
            "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
            "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
        ],
    }
    return Skill.parse_obj(skill_data)


def test_init(skill):
    assert skill.name == "Spellcraft"
    assert (
        skill.description
        == "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting."
    )
    assert skill.ability_score == "Intelligence"
    assert skill.class_skill is True
    assert skill.synergy == [
        {
            "skill": "Knowledge (Arcana)",
            "bonus": 2,
            "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
        },
        {
            "skill": "Use Magic Device",
            "bonus": 2,
            "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
        },
    ]
    assert skill.retry is True
    assert skill.special == [
        "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
        "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
        "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
        "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
    ]


def test_to_dict(skill):
    skill_dict = skill.dict()
    assert skill_dict["name"] == "Spellcraft"
    assert (
        skill_dict["description"]
        == "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting."
    )
    assert skill_dict["ability_score"] == "Intelligence"
    assert skill_dict["class_skill"] is True
    assert skill_dict["synergy"] == [
        {
            "skill": "Knowledge (Arcana)",
            "bonus": 2,
            "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
        },
        {
            "skill": "Use Magic Device",
            "bonus": 2,
            "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
        },
    ]
    assert skill_dict["retry"] is True
    assert skill_dict["special"] == [
        "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
        "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
        "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
        "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
    ]


def test_from_dict(skill_data):
    skill = Skill.parse_obj(skill_data)
    assert skill.name == "Spellcraft"
    assert (
        skill.description
        == "Spellcraft represents knowledge and understanding of spells, magical items, and the intricacies of spellcasting."
    )
    assert skill.ability_score == "Intelligence"
    assert skill.class_skill is True
    assert skill.synergy == [
        {
            "skill": "Knowledge (Arcana)",
            "bonus": 2,
            "description": "Having ranks in Knowledge (Arcana) provides a +2 synergy bonus to Spellcraft checks.",
        },
        {
            "skill": "Use Magic Device",
            "bonus": 2,
            "description": "Having ranks in Use Magic Device provides a +2 synergy bonus to Spellcraft checks.",
        },
    ]
    assert skill.retry is True
    assert skill.special == [
        "Identify Spell: A successful Spellcraft check allows the character to identify a spell as it is being cast or a magic item as it is being used.",
        "Decipher Magical Writings: Spellcraft can be used to understand and interpret magical writings, including scrolls, spellbooks, and magical inscriptions.",
        "Recognize Spells: A character with Spellcraft can identify and recognize spells being cast, allowing them to understand the potential effects and countermeasures.",
        "Determine Magic Item Properties: By examining a magic item, Spellcraft can help determine its properties, functions, and limitations.",
    ]
