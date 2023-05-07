import numpy as np
from abc import ABC, abstractmethod


class BaseAbilityScoreRoller(ABC):
    """
    Abstract base class for rolling ability scores in a d20 game.

    Attributes:
        seed (int): Optional seed for the random number generator.
        rand_state (numpy.random.RandomState): Random number generator instance.

    Methods:
        roll_ability_score(): Abstract method to roll a single ability score.
        roll_ability_scores(): Rolls six ability scores and returns them as a list.
    """

    def __init__(self, seed=None):
        """
        Initializes a new instance of the BaseAbilityScoreRoller class.

        Args:
            seed (int, optional): Seed value for the random number generator.
        """
        self.seed = seed
        self.rand_state = np.random.RandomState(seed=self.seed)

    @abstractmethod
    def roll_ability_score(self):
        """
        Abstract method to roll a single ability score.

        Returns:
            int: The rolled ability score.
        """
        pass

    def roll_ability_scores(self):
        """
        Rolls six ability scores and returns them as a list.

        Returns:
            list: A list of six rolled ability scores.
        """
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
