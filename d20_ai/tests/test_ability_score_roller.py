import unittest
from d20_ai.ability_score_roller import AbilityScoreRoller, ClassicAbilityScoreRoller, HeroicAbilityScoreRoller

class TestAbilityScoreRoller(unittest.TestCase):
    def roll_ability_scores_range_test(self, roller, msg):
        scores = roller.roll_ability_scores()

        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3, msg="score >= 3 {}".format(msg))
            self.assertLessEqual(score, 18, msg="score <= 18 {}".format(msg))

    def test_ability_score_ranges(self):
        self.roll_ability_scores_range_test(AbilityScoreRoller(), "standard ability score roller")

    def test_classic_ability_score_ranges(self):
        self.roll_ability_scores_range_test(ClassicAbilityScoreRoller(), "classic ability score roller")

    def test_heroic_ability_score_ranges(self):
        self.roll_ability_scores_range_test(HeroicAbilityScoreRoller(), "heroic ability score roller")

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