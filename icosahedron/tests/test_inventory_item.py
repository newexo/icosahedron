import json
import pytest
from ..directories import test_data
from ..d20_rules.inventory_items.inventory_item import (
    InventoryItem,
)  # Import your InventoryItem class


@pytest.fixture
def inventory_item():
    return InventoryItem(
        name="Spellbook",
        weight=3,
        description="A book of spells.",
        condition="good",
        value=100,
    )


@pytest.fixture
def instance_dict():
    with open(test_data("spellbook.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(inventory_item):
    assert inventory_item.name == "Spellbook"
    assert inventory_item.weight == 3
    assert inventory_item.description == "A book of spells."
    assert inventory_item.condition == "good"
    assert inventory_item.value == 100


def test_to_dict(inventory_item, instance_dict):
    expected = instance_dict
    actual = inventory_item.to_dict()
    assert expected == actual


def test_from_dict(instance_dict):
    inventory_item = InventoryItem.from_dict(instance_dict)
    assert inventory_item.name == "Spellbook"
    assert inventory_item.weight == 3
    assert inventory_item.description == "A book of spells."
    assert inventory_item.condition == "good"
    assert inventory_item.value == 100
