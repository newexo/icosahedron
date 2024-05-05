import pytest
import json
from icosahedron.d20_rules.inventory_items.magic_ring_item import MagicRing
from icosahedron.directories import test_data


@pytest.fixture
def magic_ring():
    return MagicRing(
        name="Ring of Protection",
        weight=0,
        value=100,
        condition="Good",
        effect="protection",
        magic_bonus=2,
    )


@pytest.fixture
def instance_dict():
    with open(test_data("magic_ring.json")) as f:
        instance_str = f.read()
    return json.loads(instance_str)


def test_instance_test(magic_ring):
    assert magic_ring.name == "Ring of Protection"
    assert magic_ring.value == 100
    assert magic_ring.condition == "Good"
    assert magic_ring.effect == "protection"
    assert magic_ring.magic_bonus == 2


def test_from_dict(instance_dict):
    magic_ring = MagicRing.parse_obj(instance_dict)
    assert magic_ring.name == "Ring of Protection"
    assert magic_ring.value == 100
    assert magic_ring.condition == "Good"
    assert magic_ring.effect == "protection"
    assert magic_ring.magic_bonus == 2
