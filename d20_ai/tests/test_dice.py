import unittest
from d20_ai.dice import D20Roller, D20Roll


class TestD20Roller(unittest.TestCase):
    def setUp(self):
        self.d20roller = D20Roller()

    def test_roll(self):
        # Test rolling 1d20 with no modifier
        roll = D20Roll(20)
        result = self.d20roller.roll(roll)
        self.assertTrue(1 <= result <= 20)

        # Test rolling 3d6 with a +2 modifier
        roll = D20Roll(6, num_dice=3, modifier=2)
        result = self.d20roller.roll(roll)
        self.assertTrue(5 <= result <= 20)

        # Test rolling 1d12 with a -1 modifier
        roll = D20Roll(12, modifier=-1)
        result = self.d20roller.roll(roll)
        self.assertTrue(0 <= result <= 11)


class TestD20Roll(unittest.TestCase):
    def test_init(self):
        # Test initializing a D20Roll with no arguments
        roll = D20Roll()
        self.assertEqual(roll.die_type, 20)
        self.assertEqual(roll.num_dice, 1)
        self.assertEqual(roll.modifier, 0)

        # Test initializing a D20Roll with all arguments
        roll = D20Roll(6, num_dice=3, modifier=-2)
        self.assertEqual(roll.die_type, 6)
        self.assertEqual(roll.num_dice, 3)
        self.assertEqual(roll.modifier, -2)

        # Test initializing a D20Roll with invalid arguments
        with self.assertRaises(ValueError):
            roll = D20Roll(0)
        with self.assertRaises(ValueError):
            roll = D20Roll(-4, num_dice=2)
        with self.assertRaises(ValueError):
            roll = D20Roll(12, num_dice=-3)
        with self.assertRaises(TypeError):
            roll = D20Roll(8, modifier="foo")


if __name__ == "__main__":
    unittest.main()
