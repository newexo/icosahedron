import numpy as np
from abc import ABC, abstractmethod


class BaseAbilityScoreRoller(ABC):
    def __init__(self, seed=None):
        self.seed = seed
        self.rand_state = np.random.RandomState(seed=self.seed)

    @abstractmethod
    def roll_ability_score(self):
        pass

    def roll_ability_scores(self):
        return [self.roll_ability_score() for _ in range(6)]


class StandardAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_score(self):
        dice_rolls = self.rand_state.randint(1, 7, size=4)
        dropped_die = np.min(dice_rolls)
        return np.sum(dice_rolls) - dropped_die


class ClassicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_score(self):
        dice_rolls = self.rand_state.randint(1, 7, size=3)
        return np.sum(dice_rolls)


class HeroicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_score(self):
        dice_rolls = self.rand_state.randint(4, 7, size=3)
        return np.sum(dice_rolls)
