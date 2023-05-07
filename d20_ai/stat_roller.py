import numpy as np
from abc import ABC, abstractmethod


class BaseAbilityScoreRoller(ABC):
    def __init__(self, seed=None):
        self.scores = []
        self.seed = seed

    @abstractmethod
    def roll_ability_scores(self):
        pass


class AbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_scores(self):
        rand_state = np.random.RandomState(seed=self.seed)
        for i in range(6):
            dice_rolls = rand_state.randint(1, 7, size=4)
            dropped_die = np.min(dice_rolls)
            score = np.sum(dice_rolls) - dropped_die
            self.scores.append(score)
        return self.scores


class ClassicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_scores(self):
        rand_state = np.random.RandomState(seed=self.seed)
        for i in range(6):
            dice_rolls = rand_state.randint(3, 19, size=3)
            score = np.sum(dice_rolls)
            self.scores.append(score)
        return self.scores


class HeroicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_scores(self):
        rand_state = np.random.RandomState(seed=self.seed)
        for i in range(6):
            dice_rolls = rand_state.randint(4, 7, size=3)
            score = np.sum(dice_rolls)
            self.scores.append(score)
        return self.scores

