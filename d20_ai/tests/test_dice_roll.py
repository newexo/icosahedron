import unittest
import json

from d20_ai.d20_rules.dice import DiceRoll
from d20_ai.directories import test_data


class TestDiceRoll(unittest.TestCase):
    def test_init(self):
        # Test initializing a D20Roll with no arguments
        roll = DiceRoll(dice_type=20)
        self.assertEqual(roll.dice_type, 20)
        self.assertEqual(roll.num_dice, 1)
        self.assertEqual(roll.modifier, 0)

        # Test initializing a D20Roll with all arguments
        roll = DiceRoll(dice_type=6, num_dice=3, modifier=-2)
        self.assertEqual(roll.dice_type, 6)
        self.assertEqual(roll.num_dice, 3)
        self.assertEqual(roll.modifier, -2)

    def test_all_valid_dice_types(self):
        d4 = DiceRoll(dice_type=4)
        self.assertEqual(4, d4.dice_type)
        self.assertEqual(1, d4.num_dice)
        self.assertEqual(0, d4.modifier)

        d6 = DiceRoll(dice_type=6)
        self.assertEqual(6, d6.dice_type)

        d8 = DiceRoll(dice_type=8)
        self.assertEqual(8, d8.dice_type)

        d10 = DiceRoll(dice_type=10)
        self.assertEqual(10, d10.dice_type)

        d12 = DiceRoll(dice_type=12)
        self.assertEqual(12, d12.dice_type)

        d20 = DiceRoll(dice_type=20)
        self.assertEqual(20, d20.dice_type)

        d00 = DiceRoll(dice_type=100)
        self.assertEqual(100, d00.dice_type)

    def test_init_valid_dice_type(self):
        roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
        self.assertEqual(roll.dice_type, 20)

    def test_init_invalid_dice_type(self):
        with self.assertRaises(ValueError):
            DiceRoll(dice_type=0, num_dice=1, modifier=0)
        with self.assertRaises(ValueError):
            DiceRoll(dice_type=-1, num_dice=1, modifier=0)
        with self.assertRaises(ValueError):
            DiceRoll(dice_type=3, num_dice=1, modifier=0)
        with self.assertRaises(ValueError):
            DiceRoll(dice_type=10067, num_dice=1, modifier=0)

    def test_init_negative_num_dice(self):
        with self.assertRaises(ValueError):
            DiceRoll(dice_type=20, num_dice=-1, modifier=0)

    def test_to_json(self):
        roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
        expected = {"dice_type": 20, "num_dice": 1, "modifier": 0}
        result = roll.to_json()
        self.assertDictEqual(json.loads(result), expected)

    def test_from_json(self):
        json_data = '{"dice_type": 20, "num_dice": 1, "modifier": 0}'
        roll = DiceRoll.from_json(json_data)
        self.assertEqual(roll.dice_type, 20)
        self.assertEqual(roll.num_dice, 1)
        self.assertEqual(roll.modifier, 0)

    def test_to_dict(self):
        roll = DiceRoll(dice_type=20, num_dice=1, modifier=0)
        expected = {"dice_type": 20, "num_dice": 1, "modifier": 0}
        self.assertDictEqual(roll.to_dict(), expected)

    def test_from_dict(self):
        data = {"dice_type": 20, "num_dice": 1, "modifier": 0}
        roll = DiceRoll.from_dict(data)
        self.assertEqual(roll.dice_type, 20)
        self.assertEqual(roll.num_dice, 1)
        self.assertEqual(roll.modifier, 0)

    def test_load_roll(self):
        with open(test_data("1d20plus5.json")) as f:
            roll = DiceRoll.from_json(f.read())
            self.assertEqual(20, roll.dice_type)
            self.assertEqual(1, roll.num_dice)
            self.assertEqual(5, roll.modifier)

    def test_load_rolls(self):
        with open(test_data("dice_rolls.json")) as f:
            rolls = DiceRoll.list_from_json(f.read())

            roll = rolls[0]
            self.assertEqual(20, roll.dice_type)
            self.assertEqual(1, roll.num_dice)
            self.assertEqual(5, roll.modifier)

            roll = rolls[1]
            self.assertEqual(6, roll.dice_type)
            self.assertEqual(3, roll.num_dice)
            self.assertEqual(0, roll.modifier)

            roll = rolls[2]
            self.assertEqual(12, roll.dice_type)
            self.assertEqual(6, roll.num_dice)
            self.assertEqual(2, roll.modifier)


if __name__ == "__main__":
    unittest.main()
