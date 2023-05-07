import numpy as np
from abc import ABC, abstractmethod


class BaseAbilityScoreRoller(ABC):
    def __init__(self, rand_state=None, seed=None):
        self.scores = []
        if seed is None:
            seed = 48
        if rand_state is None:
            rand_state = np.random.RandomState(seed=seed)
        self.rand_state = rand_state

    @abstractmethod
    def roll_ability_scores(self):
        pass


class AbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_scores(self):
        for i in range(6):
            dice_rolls = self.rand_state.randint(1, 7, size=4)
            dropped_die = np.min(dice_rolls)
            score = np.sum(dice_rolls) - dropped_die
            self.scores.append(score)
        return self.scores


class ClassicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_scores(self):
        for i in range(6):
            dice_rolls = self.rand_state.randint(1, 7, size=3)
            score = np.sum(dice_rolls)
            self.scores.append(score)
        return self.scores


class HeroicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_scores(self):
        for i in range(6):
            dice_rolls = self.rand_state.randint(4, 7, size=3)
            score = np.sum(dice_rolls)
            self.scores.append(score)
        return self.scores
