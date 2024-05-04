import pytest
from icosahedron.d20_rules.dice import DiceRoller, DiceRoll


def test_roll():
    roller = DiceRoller(random_seed=42)

    for _ in range(1000):
        roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
        result = roller.roll(roll)
        assert 1 <= result <= 20

        # Test rolling a single D20
        roll = DiceRoll(dice_type=20)
        result = roller.roll(roll)
        assert 1 <= result <= 20

        # Test rolling multiple dice with modifiers
        roll = DiceRoll(dice_type=6, num_dice=3, modifier=-2)
        result = roller.roll(roll)
        assert 1 <= result <= 16


def test_roll_invalid_roll():
    with pytest.raises(ValueError):
        invalid_roll = DiceRoll(dice_type=0, num_dice=1, modifier=0)
