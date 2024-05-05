import json
import pytest
from ..directories import test_data
from ..d20_rules.inventory_items.armor_item import (
    ArmorItem,
)  # Import your ArmorItem class


@pytest.fixture
def armor_item():
    return ArmorItem(
        name="Chain Mail",
        armor_class=16,
        max_dex_bonus=2,
        check_penalty=-5,
        spell_failure=30,
        speed_reduction=10,
        weight=40,
        value=75,
        condition="new",
    )


@pytest.fixture
def instance_dict():
    with open(test_data("chain_mail.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(armor_item):
    assert armor_item.name == "Chain Mail"
    assert armor_item.armor_class == 16
    assert armor_item.max_dex_bonus == 2
    assert armor_item.check_penalty == -5
    assert armor_item.spell_failure == 30
    assert armor_item.speed_reduction == 10
    assert armor_item.weight == 40
    assert armor_item.value == 75
    assert armor_item.condition == "new"


def test_to_dict(armor_item, instance_dict):
    expected = instance_dict
    actual = armor_item.dict()
    assert expected == actual


def test_from_dict(instance_dict):
    armor_item = ArmorItem.parse_obj(instance_dict)
    assert armor_item.name == "Chain Mail"
    assert armor_item.armor_class == 16
    assert armor_item.max_dex_bonus == 2
    assert armor_item.check_penalty == -5
    assert armor_item.spell_failure == 30
    assert armor_item.speed_reduction == 10
    assert armor_item.weight == 40
    assert armor_item.value == 75
    assert armor_item.condition == "new"
