import unittest
from d20_ai.dice import D20Roller, D20Roll


# class TestD20Roll(unittest.TestCase):
#     def test_init(self):
#         # Test initializing a D20Roll with no arguments
#         roll = D20Roll(dice_type=20)
#         self.assertEqual(roll.dice_type, 20)
#         self.assertEqual(roll.num_dice, 1)
#         self.assertEqual(roll.modifier, 0)
#
#         # Test initializing a D20Roll with all arguments
#         roll = D20Roll(dice_type=6, num_dice=3, modifier=-2)
#         self.assertEqual(roll.dice_type, 6)
#         self.assertEqual(roll.num_dice, 3)
#         self.assertEqual(roll.modifier, -2)
#
#         # Test initializing a D20Roll with invalid arguments (should not raise exceptions)
#         roll = D20Roll(dice_type=8, modifier="foo")
#
#
# class TestD20Roller(unittest.TestCase):
#     def test_roll(self):
#         roller = D20Roller()
#
#         # Test rolling a single D20
#         roll = D20Roll(dice_type=20)
#         result = roller.roll(roll)
#         self.assertGreaterEqual(result, 1)
#         self.assertLessEqual(result, 20)
#
#         # Test rolling multiple dice with modifiers
#         roll = D20Roll(dice_type=6, num_dice=3, modifier=-2)
#         result = roller.roll(roll)
#         self.assertGreaterEqual(result, 1)
#         self.assertLessEqual(result, 16)
#
#         # Test rolling with invalid dice types (should raise ValueError)
#         with self.assertRaises(ValueError):
#             roll = D20Roll(dice_type=0)
#             roller.roll(roll)
#         with self.assertRaises(ValueError):
#             roll = D20Roll(dice_type=-4, num_dice=2)
#             roller.roll(roll)
#
#         # Test rolling with invalid arguments (should raise TypeError)
#         with self.assertRaises(TypeError):
#             roll = D20Roll(dice_type=12, num_dice="-3")
#             roller.roll(roll)
#
#
# import unittest
# from d20_ai.dice import D20Roll, D20Roller

class TestD20Roll(unittest.TestCase):
    def test_init_valid_dice_type(self):
        roll = D20Roll(dice_type=20, num_dice=1, modifier=0)
        self.assertEqual(roll.dice_type, 20)

    def test_init_invalid_dice_type(self):
        with self.assertRaises(ValueError):
            D20Roll(dice_type=0, num_dice=1, modifier=0)

    def test_init_negative_num_dice(self):
        with self.assertRaises(ValueError):
            D20Roll(dice_type=20, num_dice=-1, modifier=0)

    def test_init_negative_modifier(self):
        with self.assertRaises(ValueError):
            D20Roll(dice_type=20, num_dice=1, modifier=-1)

    def test_to_json(self):
        roll = D20Roll(dice_type=20, num_dice=1, modifier=0)
        expected = {"dice_type": 20, "num_dice": 1, "modifier": 0}
        self.assertDictEqual(roll.to_json(), expected)

    def test_from_json(self):
        json_data = {"dice_type": 20, "num_dice": 1, "modifier": 0}
        roll = D20Roll.from_json(json_data)
        self.assertEqual(roll.dice_type, 20)
        self.assertEqual(roll.num_dice, 1)
        self.assertEqual(roll.modifier, 0)


class TestD20Roller(unittest.TestCase):
    def test_roll(self):
        roller = D20Roller(random_seed=42)
        roll = D20Roll(dice_type=20, num_dice=1, modifier=0)
        result = roller.roll(roll)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 20)

    def test_roll_invalid_roll(self):
        roller = D20Roller(random_seed=42)
        invalid_roll = D20Roll(dice_type=0, num_dice=1, modifier=0)
        with self.assertRaises(ValueError):
            roller.roll(invalid_roll)

    def test_roll_invalid_roll_type(self):
        roller = D20Roller(random_seed=42)
        invalid_roll = "not a D20Roll object"
        with self.assertRaises(TypeError):
            roller.roll(invalid_roll)


if __name__ == "__main__":
    unittest.main()
