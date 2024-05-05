import pytest
import json
from icosahedron.d20_rules.mob_stat_block import MobStatBlock
from icosahedron.directories import test_data


@pytest.fixture
def mob_stat_block():
    return MobStatBlock(
        name="Iggy",
        hit_points=12,
        armor_class=14,
        attack_bonus=4,
        damage="1d6+2",
        speed=30,
        abilities={"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6},
        skills={"stealth": 6},
        special_abilities=["nimbleEscape"],
        equipment=["Shortsword", "Shortbow", "Leather Armor"],
        alignment="Chaotic Evil",
        description="Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord.",
    )


@pytest.fixture
def instance_dict():
    with open(test_data("iggy.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(mob_stat_block):
    assert mob_stat_block.name == "Iggy"
    assert mob_stat_block.hit_points == 12
    assert mob_stat_block.armor_class == 14
    assert mob_stat_block.attack_bonus == 4
    assert mob_stat_block.damage == "1d6+2"
    assert mob_stat_block.speed == 30
    assert mob_stat_block.abilities == {
        "str": 12,
        "dex": 16,
        "con": 10,
        "int": 8,
        "wis": 8,
        "cha": 6,
    }
    assert mob_stat_block.skills == {"stealth": 6}
    assert mob_stat_block.special_abilities == ["nimbleEscape"]
    assert mob_stat_block.equipment == ["Shortsword", "Shortbow", "Leather Armor"]
    assert mob_stat_block.alignment == "Chaotic Evil"
    assert (
        mob_stat_block.description
        == "Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord."
    )


def test_from_dict(instance_dict):
    mob_stat_block = MobStatBlock.parse_obj(instance_dict)
    assert mob_stat_block.name == "Iggy"
    assert mob_stat_block.hit_points == 12
    assert mob_stat_block.armor_class == 14
    assert mob_stat_block.attack_bonus == 4
    assert mob_stat_block.damage == "1d6+2"
    assert mob_stat_block.speed == 30
    assert mob_stat_block.abilities == {
        "str": 12,
        "dex": 16,
        "con": 10,
        "int": 8,
        "wis": 8,
        "cha": 6,
    }
    assert mob_stat_block.skills == {"stealth": 6}
    assert mob_stat_block.special_abilities == ["nimbleEscape"]
    assert mob_stat_block.equipment == ["Shortsword", "Shortbow", "Leather Armor"]
    assert mob_stat_block.alignment == "Chaotic Evil"
    assert (
        mob_stat_block.description
        == "Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord."
    )
