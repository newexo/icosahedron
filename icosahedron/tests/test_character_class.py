import json
import pytest
from icosahedron.d20_rules.character_class import CharacterClass
from icosahedron.directories import test_data


@pytest.fixture
def character_class():
    hit_dice = 10
    base_attack_bonus = 1
    bab_progression = 0.75
    skill_points = 2

    return CharacterClass(
        hit_dice=hit_dice,
        base_attack_bonus=base_attack_bonus,
        bab_progression=bab_progression,
        skill_points=skill_points,
    )


@pytest.fixture
def instance_dict():
    with open(test_data("fighter_class.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(character_class):
    assert character_class.hit_dice == 10
    assert character_class.base_attack_bonus == 1
    assert character_class.bab_progression == 0.75
    assert character_class.skill_points == 2


def test_from_dict(instance_dict):
    character_class = CharacterClass.parse_obj(instance_dict)
    assert character_class.hit_dice == 10
    assert character_class.base_attack_bonus == 1
    assert character_class.bab_progression == 0.75
    assert character_class.skill_points == 2
