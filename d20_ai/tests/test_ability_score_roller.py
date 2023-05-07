import unittest
from d20_ai.ability_score_roller import (
    StandardAbilityScoreRoller,
    ClassicAbilityScoreRoller,
    HeroicAbilityScoreRoller,
)


class TestAbilityScoreRoller(unittest.TestCase):
    def roll_ability_scores_range_test(self, roller, msg):
        scores = roller.roll_ability_scores()

        self.assertEqual(len(scores), 6)
        for score in scores:
            self.assertGreaterEqual(score, 3, msg="score >= 3 {}".format(msg))
            self.assertLessEqual(score, 18, msg="score <= 18 {}".format(msg))

    def test_ability_score_ranges(self):
        self.roll_ability_scores_range_test(
            StandardAbilityScoreRoller(), "standard ability score roller"
        )

    def test_classic_ability_score_ranges(self):
        self.roll_ability_scores_range_test(
            ClassicAbilityScoreRoller(), "classic ability score roller"
        )

    def test_heroic_ability_score_ranges(self):
        self.roll_ability_scores_range_test(
            HeroicAbilityScoreRoller(), "heroic ability score roller"
        )

    def test_standard_roll_ability_scores(self):
        # regression test of classical ability score rolling
        roller = StandardAbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()

        expected_scores = [14, 11, 12, 15, 16, 11]
        self.assertEqual(scores, expected_scores)

    def test_classic_roll_ability_scores(self):
        # regression test of classical ability score rolling
        roller = ClassicAbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()

        expected_scores = [12, 12, 9, 12, 13, 16]
        self.assertEqual(scores, expected_scores)

    def test_heroic_roll_ability_scores(self):
        # regression test of classical ability score rolling
        roller = HeroicAbilityScoreRoller(seed=42)
        scores = roller.roll_ability_scores()

        expected_scores = [16, 14, 17, 18, 15, 14]
        self.assertEqual(scores, expected_scores)


if __name__ == "__main__":
    unittest.main()
