import unittest
from d20_ai.ability_score_roller import AbilityScoreRoller, ClassicAbilityScoreRoller, HeroicAbilityScoreRoller

class TestAbilityScoreRoller(unittest.TestCase):
    def test_roll_ability_scores(self):
        roller = AbilityScoreRoller()
        scores = roller.roll_ability_scores()

        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3)
            self.assertLessEqual(score, 18)

class TestAbilityScoreRoller(unittest.TestCase):
    def test_roll_ability_scores(self):
        # test standard ability score rolling
        roller = AbilityScoreRoller()
        scores = roller.roll_ability_scores()

        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3)
            self.assertLessEqual(score, 18)

        # test classic ability score rolling with seed=42
        roller = ClassicAbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()

        expected_scores = [15, 14, 13, 12, 10, 8]
        self.assertEqual(scores, expected_scores)

if __name__ == '__main__':
    unittest.main()