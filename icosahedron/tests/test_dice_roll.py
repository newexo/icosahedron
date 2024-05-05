import pytest
import json
from icosahedron.d20_rules.dice import DiceRoll
from icosahedron.directories import test_data


def test_init():
    # Test initializing a D20Roll with no arguments
    roll = DiceRoll(dice_type=20)
    assert roll.dice_type == 20
    assert roll.num_dice == 1
    assert roll.modifier == 0

    # Test initializing a D20Roll with all arguments
    roll = DiceRoll(dice_type=6, num_dice=3, modifier=-2)
    assert roll.dice_type == 6
    assert roll.num_dice == 3
    assert roll.modifier == -2


def test_all_valid_dice_types():
    d4 = DiceRoll(dice_type=4)
    assert d4.dice_type == 4
    assert d4.num_dice == 1
    assert d4.modifier == 0

    d6 = DiceRoll(dice_type=6)
    assert d6.dice_type == 6

    d8 = DiceRoll(dice_type=8)
    assert d8.dice_type == 8

    d10 = DiceRoll(dice_type=10)
    assert d10.dice_type == 10

    d12 = DiceRoll(dice_type=12)
    assert d12.dice_type == 12

    d20 = DiceRoll(dice_type=20)
    assert d20.dice_type == 20

    d00 = DiceRoll(dice_type=100)
    assert d00.dice_type == 100


def test_init_valid_dice_type():
    roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
    assert roll.dice_type == 20


def test_init_invalid_dice_type():
    with pytest.raises(ValueError):
        DiceRoll(dice_type=0, num_dice=1, modifier=0)
    with pytest.raises(ValueError):
        DiceRoll(dice_type=-1, num_dice=1, modifier=0)
    with pytest.raises(ValueError):
        DiceRoll(dice_type=3, num_dice=1, modifier=0)
    with pytest.raises(ValueError):
        DiceRoll(dice_type=10067, num_dice=1, modifier=0)


def test_init_negative_num_dice():
    with pytest.raises(ValueError):
        DiceRoll(dice_type=20, num_dice=-1, modifier=0)


def test_to_json():
    roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
    expected = {"dice_type": 20, "num_dice": 1, "modifier": 0}
    result = roll.model_dump_json()
    assert json.loads(result) == expected


def test_from_json():
    json_data = '{"dice_type": 20, "num_dice": 1, "modifier": 0}'
    roll = DiceRoll.model_validate_json(json_data)
    assert roll.dice_type == 20
    assert roll.num_dice == 1
    assert roll.modifier == 0


def test_to_dict():
    roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
    expected = {"dice_type": 20, "num_dice": 1, "modifier": 0}
    assert roll.dict() == expected


def test_from_dict():
    data = {"dice_type": 20, "num_dice": 1, "modifier": 0}
    roll = DiceRoll.parse_obj(data)
    assert roll.dice_type == 20
    assert roll.num_dice == 1
    assert roll.modifier == 0


def test_load_roll():
    with open(test_data("1d20plus5.json")) as f:
        roll = DiceRoll.model_validate_json(f.read())
        assert roll.dice_type == 20
        assert roll.num_dice == 1
        assert roll.modifier == 5
