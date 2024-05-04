import pytest
from icosahedron.d20_rules.character_class import CharacterClass, Character


@pytest.fixture
def char_class():
    return CharacterClass(
        hit_dice=10, base_attack_bonus=1, bab_progression=0.75, skill_points=2
    )


@pytest.fixture
def character(char_class):
    return Character(
        level=1,
        character_class=char_class,
        constitution_modifier=2,
        intelligence_modifier=1,
    )


def test_compute_hit_points(character):
    expected_hit_points = 12
    actual_hit_points = character.compute_hit_points()
    assert actual_hit_points == expected_hit_points


def test_compute_base_attack_bonus(char_class):
    character = Character(
        level=3,
        character_class=char_class,
        constitution_modifier=2,
        intelligence_modifier=1,
    )
    expected_bab = 2.5
    actual_bab = character.compute_base_attack_bonus()
    assert actual_bab == expected_bab


def test_compute_skill_points(char_class):
    character = Character(
        level=5,
        character_class=char_class,
        constitution_modifier=2,
        intelligence_modifier=1,
    )
    expected_skill_points = 15
    actual_skill_points = character.compute_skill_points()
    assert actual_skill_points == expected_skill_points
