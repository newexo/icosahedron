import pytest
from ..d20v2.dice_roller import (
    DiceRoller,
)  # Assuming the DiceRoller class is in a file named dice_roller.py


# Fixture to create a DiceRoller instance with a fixed seed for deterministic results
@pytest.fixture
def dice_roller():
    return DiceRoller(seed=42)


# Helper function to check if the result of a dice roll is within a valid range
def is_within_range(rolls, sides):
    return all(1 <= roll <= sides for roll in rolls)


# Test d4 method with n=1 and modifier=0
def test_d4_single_roll(dice_roller):
    rolls, total = dice_roller.d4(n=1, modifier=0)
    assert len(rolls) == 1
    assert is_within_range(rolls, 4)
    assert 1 <= total <= 4


# Test d6 method with n=1 and modifier=0
def test_d6_single_roll(dice_roller):
    rolls, total = dice_roller.d6(n=1, modifier=0)
    assert len(rolls) == 1
    assert is_within_range(rolls, 6)
    assert 1 <= total <= 6


# Test d8 method with n=1 and modifier=0
def test_d8_single_roll(dice_roller):
    rolls, total = dice_roller.d8(n=1, modifier=0)
    assert len(rolls) == 1
    assert is_within_range(rolls, 8)
    assert 1 <= total <= 8


# Test d10 method with n=1 and modifier=0
def test_d10_single_roll(dice_roller):
    rolls, total = dice_roller.d10(n=1, modifier=0)
    assert len(rolls) == 1
    assert is_within_range(rolls, 10)
    assert 1 <= total <= 10


# Test d12 method with n=1 and modifier=0
def test_d12_single_roll(dice_roller):
    rolls, total = dice_roller.d12(n=1, modifier=0)
    assert len(rolls) == 1
    assert is_within_range(rolls, 12)
    assert 1 <= total <= 12


# Test d20 method with n=1 and modifier=0
def test_d20_single_roll(dice_roller):
    rolls, total = dice_roller.d20(n=1, modifier=0)
    assert len(rolls) == 1
    assert is_within_range(rolls, 20)
    assert 1 <= total <= 20


# Test d00 method with n=1 and modifier=0
def test_d00_single_roll(dice_roller):
    rolls, total = dice_roller.d00(n=1, modifier=0)
    assert len(rolls) == 1
    assert 0 <= rolls[0] < 100  # Percentile rolls should be between 0 and 99
    assert 0 <= total < 100


# Test dice rolls with n=2 and different modifiers for d4
@pytest.mark.parametrize(
    "modifier, expected_total_range",
    [
        (1, (3, 9)),
        (3, (5, 11)),
        (-1, (1, 7)),
    ],
)
def test_d4_multiple_rolls_with_modifier(dice_roller, modifier, expected_total_range):
    rolls, total = dice_roller.d4(n=2, modifier=modifier)
    assert len(rolls) == 2
    assert is_within_range(rolls, 4)
    assert expected_total_range[0] <= total <= expected_total_range[1]


# Test dice rolls with n=2 and different modifiers for d6
@pytest.mark.parametrize(
    "modifier, expected_total_range",
    [
        (1, (3, 13)),
        (3, (5, 15)),
        (-1, (1, 11)),
    ],
)
def test_d6_multiple_rolls_with_modifier(dice_roller, modifier, expected_total_range):
    rolls, total = dice_roller.d6(n=2, modifier=modifier)
    assert len(rolls) == 2
    assert is_within_range(rolls, 6)
    assert expected_total_range[0] <= total <= expected_total_range[1]


# Repeat similar tests for d8, d10, d12, d20, d00 (not shown here for brevity)
