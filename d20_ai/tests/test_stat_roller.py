import unittest
from d20_ai.stat_roller import AbilityScoreRoller, ClassicAbilityScoreRoller, HeroicAbilityScoreRoller


class TestAbilityScoreRoller(unittest.TestCase):
    def test_roll_standard_ability_scores_ranges(self):
        for seed in range(1,1000):
            roller = AbilityScoreRoller(seed=seed)
            scores = roller.roll_ability_scores()

            self.assertEqual(len(scores), 6)
            for score in scores:
                self.assertGreaterEqual(score, 3)
                self.assertLessEqual(score, 18)

    def test_roll_classic_ability_scores_ranges(self):
        for seed in range(1,1000):
            roller = ClassicAbilityScoreRoller(seed=seed)
            scores = roller.roll_ability_scores()

            self.assertEqual(len(scores), 6)
            for score in scores:
                self.assertGreaterEqual(score, 3)
                self.assertLessEqual(score, 18)

    def test_roll_heroic_ability_scores_ranges(self):
        for seed in range(1,1000):
            roller = HeroicAbilityScoreRoller(seed=seed)
            scores = roller.roll_ability_scores()
            print(scores)

            self.assertEqual(len(scores), 6)
            for score in scores:
                self.assertGreaterEqual(score, 3)
                self.assertLessEqual(score, 18)

    def test_roll_standard_ability_scores(self):
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