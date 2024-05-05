import pytest
import json
from icosahedron.d20_rules.inventory_items.weapon_item import WeaponItem
from icosahedron.directories import test_data


@pytest.fixture
def weapon_item():
    return WeaponItem(
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


@pytest.fixture
def instance_dict():
    with open(test_data("mace.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(weapon_item):
    assert weapon_item.name == "Mace"
    assert weapon_item.value == 308
    assert weapon_item.condition == "Good"
    assert weapon_item.value == 308.0
    assert weapon_item.weight == 8
    assert weapon_item.damage == "1d6"
    assert weapon_item.damage_type == "Bludgeoning"
    assert weapon_item.description == "nothing special"


def test_from_dict(instance_dict):
    weapon_item = WeaponItem.parse_obj(instance_dict)
    assert weapon_item.name == "Mace"
    assert weapon_item.value == 308
    assert weapon_item.condition == "Good"
    assert weapon_item.value == 308.0
    assert weapon_item.weight == 8
    assert weapon_item.damage == "1d6"
    assert weapon_item.damage_type == "Bludgeoning"
    assert weapon_item.description == "nothing special"
