import pytest
from ..d20v2.treasure_generator import DungeonTreasureGenerator
from ..d20v2.dice_roller import DiceRoller


@pytest.fixture
def dice_roller():
    # Create a DiceRoller instance with a fixed seed for predictable results
    return DiceRoller(seed=42)


@pytest.fixture
def treasure_generator(dice_roller):
    # Create a DungeonTreasureGenerator with the provided dice_roller
    return DungeonTreasureGenerator(dice_roller)


# Test treasure generation for a low CR (0-4) with random rolls
def test_treasure_generation_low_cr_random(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=3, use_average=False)

    # Expected results based on a CR of 3 with random dice rolls:
    # Coins: {cp: random from d6 * 100, sp: random from d6, gp: random from d6}
    # Gems: 1d6 gems worth 10gp each
    # Magic items: Common magic item (e.g., "Potion of Healing")

    assert "coins" in treasure
    assert "gems" in treasure
    assert "magic_items" in treasure

    # Example values, check ranges rather than exact values since it's random
    assert 4 <= treasure["coins"]["cp"] <= 600
    assert 1 <= treasure["coins"]["sp"] <= 6
    assert 1 <= treasure["coins"]["gp"] <= 6
    assert 1 <= len(treasure["gems"]) <= 6
    assert all(gem == 10 for gem in treasure["gems"])
    assert "Potion of Healing" in treasure["magic_items"]


# Test treasure generation for a low CR (0-4) with average values
def test_treasure_generation_low_cr_average(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=3, use_average=True)

    # Expected average results:
    # Coins: {cp: 100, sp: 10, gp: 1}
    # Gems: 1 gem worth 10gp
    # Magic items: Common magic item (e.g., "Potion of Healing", "Scroll of Light")

    assert treasure["coins"] == {"cp": 100, "sp": 10, "gp": 1}
    assert treasure["gems"] == [10]
    assert "Potion of Healing" in treasure["magic_items"]
    assert "Scroll of Light" in treasure["magic_items"]


# Test treasure generation for a mid CR (5-10) with random rolls
def test_treasure_generation_mid_cr_random(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=7, use_average=False)

    # Expected results based on a CR of 7 with random dice rolls:
    # Coins: {gp: random from d6 * 10, pp: random from d6}
    # Gems: 1d6 gems worth 50gp each
    # Magic items: Uncommon magic item (e.g., "+1 Weapon")

    assert "coins" in treasure
    assert "gems" in treasure
    assert "magic_items" in treasure

    assert 40 <= treasure["coins"]["gp"] <= 600
    assert 1 <= treasure["coins"]["pp"] <= 6
    assert 1 <= len(treasure["gems"]) <= 6
    assert all(gem == 50 for gem in treasure["gems"])
    assert "+1 Weapon" in treasure["magic_items"]


# Test treasure generation for a mid CR (5-10) with average values
def test_treasure_generation_mid_cr_average(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=7, use_average=True)

    # Expected average results:
    # Coins: {gp: 100, pp: 10}
    # Gems: 3 gems worth 50gp each
    # Magic items: Uncommon magic item (e.g., "+1 Weapon", "Bag of Holding")

    assert treasure["coins"] == {"gp": 100, "pp": 10}
    assert treasure["gems"] == [50, 50, 50]
    assert "+1 Weapon" in treasure["magic_items"]
    assert "Bag of Holding" in treasure["magic_items"]


# Test treasure generation for a high CR (11-16) with random rolls
def test_treasure_generation_high_cr_random(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=12, use_average=False)

    # Expected results based on a CR of 12 with random dice rolls:
    # Coins: {gp: random from d6 * 100, pp: random from d6 * 2}
    # Gems: 1d6 gems worth 100gp each
    # Magic items: Rare magic item (e.g., "+2 Weapon")

    assert "coins" in treasure
    assert "gems" in treasure
    assert "magic_items" in treasure

    assert 100 <= treasure["coins"]["gp"] <= 600
    assert 2 <= treasure["coins"]["pp"] <= 12
    assert 1 <= len(treasure["gems"]) <= 6
    assert all(gem == 100 for gem in treasure["gems"])
    assert "+2 Weapon" in treasure["magic_items"]


# Test treasure generation for a high CR (11-16) with average values
def test_treasure_generation_high_cr_average(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=12, use_average=True)

    # Expected average results:
    # Coins: {gp: 500, pp: 20}
    # Gems: 5 gems worth 100gp each
    # Magic items: Rare magic item (e.g., "+2 Weapon", "Cloak of Protection")

    assert treasure["coins"] == {"gp": 500, "pp": 20}
    assert treasure["gems"] == [100, 100, 100, 100, 100]
    assert "+2 Weapon" in treasure["magic_items"]
    assert "Cloak of Protection" in treasure["magic_items"]


# Test treasure generation for a very high CR (17+) with random rolls
def test_treasure_generation_very_high_cr_random(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=18, use_average=False)

    # Expected results based on a CR of 18 with random dice rolls:
    # Coins: {gp: random from d6 * 500, pp: random from d6 * 5}
    # Gems: 1d6 gems worth 500gp each
    # Magic items: Very rare or legendary magic item (e.g., "+3 Weapon")

    assert "coins" in treasure
    assert "gems" in treasure
    assert "magic_items" in treasure

    assert 500 <= treasure["coins"]["gp"] <= 3000
    assert 5 <= treasure["coins"]["pp"] <= 30
    assert 1 <= len(treasure["gems"]) <= 6
    assert all(gem == 500 for gem in treasure["gems"])
    assert "+3 Weapon" in treasure["magic_items"]


# Test treasure generation for a very high CR (17+) with average values
def test_treasure_generation_very_high_cr_average(treasure_generator):
    treasure = treasure_generator.generate_treasure(cr=18, use_average=True)

    # Expected average results:
    # Coins: {gp: 1000, pp: 50}
    # Gems: 6 gems worth 500gp each
    # Magic items: Very rare or legendary magic item (e.g., "+3 Weapon", "Staff of Power")

    assert treasure["coins"] == {"gp": 1000, "pp": 50}
    assert treasure["gems"] == [500, 500, 500, 500, 500, 500]
    assert "+3 Weapon" in treasure["magic_items"]
    assert "Staff of Power" in treasure["magic_items"]
