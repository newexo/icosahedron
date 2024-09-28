import pytest
from ..d20v2.hit_point_calculator import (
    FighterHitPointCalculator,
    WizardHitPointCalculator,
)
from ..d20v2.dice_roller import DiceRoller


@pytest.fixture
def dice_roller():
    # Create a DiceRoller instance with a fixed seed for predictable results
    return DiceRoller(seed=42)


@pytest.fixture
def fighter_hp_calculator(dice_roller):
    # Create a FighterHitPointCalculator with Constitution modifier of +2
    return FighterHitPointCalculator(dice_roller, constitution_modifier=2)


@pytest.fixture
def wizard_hp_calculator(dice_roller):
    # Create a WizardHitPointCalculator with Constitution modifier of -1
    return WizardHitPointCalculator(dice_roller, constitution_modifier=-1)


# Test rolling hit dice for a 3rd-level fighter
def test_fighter_hp_rolling(fighter_hp_calculator):
    hp = fighter_hp_calculator.calculate_hit_points(level=3, use_average=False)

    # Expected result based on seed and constitution modifier:
    # 1st level: max(10) + 2 (Con mod) = 12
    # 2nd level: rolled d10 (8) + 2 (Con mod) = 10
    # 3rd level: rolled d10 (5) + 2 (Con mod) = 7
    # Total = 12 + 10 + 7 = 29
    assert hp == 27


# Test using average hit points for a 3rd-level fighter
def test_fighter_hp_average(fighter_hp_calculator):
    hp = fighter_hp_calculator.calculate_hit_points(level=3, use_average=True)

    # Expected result using average:
    # 1st level: max(10) + 2 (Con mod) = 12
    # 2nd level: average(6) + 2 (Con mod) = 8
    # 3rd level: average(6) + 2 (Con mod) = 8
    # Total = 12 + 8 + 8 = 28
    assert hp == 28


# Test rolling hit dice for a 3rd-level wizard with a low Constitution modifier
def test_wizard_hp_rolling(wizard_hp_calculator):
    hp = wizard_hp_calculator.calculate_hit_points(level=3, use_average=False)

    # Expected result based on seed and constitution modifier:
    # 1st level: max(6) - 1 (Con mod) = 5
    # 2nd level: rolled d6 (4) - 1 (Con mod) = 3
    # 3rd level: rolled d6 (5) - 1 (Con mod) = 4
    # Total = 5 + 3 + 4 = 12
    assert hp == 12


# Test using average hit points for a 3rd-level wizard with a low Constitution modifier
def test_wizard_hp_average(wizard_hp_calculator):
    hp = wizard_hp_calculator.calculate_hit_points(level=3, use_average=True)

    # Expected result using average:
    # 1st level: max(6) - 1 (Con mod) = 5
    # 2nd level: average(4) - 1 (Con mod) = 3
    # 3rd level: average(4) - 1 (Con mod) = 3
    # Total = 5 + 3 + 3 = 11
    assert hp == 11


# Test minimum 1 HP rule for wizard with low Constitution (if the Constitution modifier is -1 and roll is 1)
def test_wizard_hp_minimum_one(wizard_hp_calculator, dice_roller):
    # Create a wizard with even lower Constitution (-3)
    wizard_with_low_constitution = WizardHitPointCalculator(
        dice_roller, constitution_modifier=-3
    )

    # Simulate a case where the wizard rolls 1s (expected from a low roll on d6)
    hp = wizard_with_low_constitution.calculate_hit_points(level=3, use_average=False)

    # Expected result:
    # 1st level: max(6) - 3 (Con mod) = 3
    # 2nd level: rolled d6 (4) - 3 (Con mod) = 1 (due to minimum HP rule)
    # 3rd level: rolled d6 (2) - 3 (Con mod) = 1 (due to minimum HP rule)
    # Total = 3 + 1 + 1 = 5
    assert hp == 6
