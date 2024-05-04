from icosahedron.d20_rules.ability_score_roller import (
    StandardAbilityScoreRoller,
    ClassicAbilityScoreRoller,
    HeroicAbilityScoreRoller,
)
import pytest


@pytest.fixture
def standard_roller():
    return StandardAbilityScoreRoller(seed=42)


@pytest.fixture
def classic_roller():
    return ClassicAbilityScoreRoller(seed=42)


@pytest.fixture
def heroic_roller():
    return HeroicAbilityScoreRoller(seed=42)


def roll_ability_scores_range_test(roller):
    scores = roller.roll_ability_scores()
    assert len(scores) == 6
    for score in scores:
        assert 3 <= score <= 18


def test_ability_score_ranges_standard(standard_roller):
    roll_ability_scores_range_test(standard_roller)


def test_ability_score_ranges_classic(classic_roller):
    roll_ability_scores_range_test(classic_roller)


def test_ability_score_ranges_heroic(heroic_roller):
    roll_ability_scores_range_test(heroic_roller)


def no_repeat_test(roller):
    first = roller.roll_ability_scores()
    second = roller.roll_ability_scores()
    assert first != second


def test_standard_ability_score_roller_no_repeat(standard_roller):
    no_repeat_test(standard_roller)


def test_classic_ability_score_roller_no_repeat(classic_roller):
    no_repeat_test(classic_roller)


def test_heroic_ability_score_roller_no_repeat(heroic_roller):
    no_repeat_test(heroic_roller)


def test_standard_roll_ability_scores():
    roller = StandardAbilityScoreRoller(seed=42)
    scores = roller.roll_ability_scores()
    expected_scores = [14, 11, 12, 15, 16, 11]
    assert scores == expected_scores


def test_classic_roll_ability_scores():
    roller = ClassicAbilityScoreRoller(seed=42)
    scores = roller.roll_ability_scores()
    expected_scores = [12, 12, 9, 12, 13, 16]
    assert scores == expected_scores


def test_heroic_roll_ability_scores():
    roller = HeroicAbilityScoreRoller(seed=42)
    scores = roller.roll_ability_scores()
    expected_scores = [16, 14, 17, 18, 15, 14]
    assert scores == expected_scores
