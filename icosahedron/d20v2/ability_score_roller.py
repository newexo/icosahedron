from abc import ABC, abstractmethod
from .dice_roller import DiceRoller  # Assuming DiceRoller is imported


class BaseAbilityScoreRoller(ABC):
    """
    Abstract base class for rolling ability scores in a d20 game.

    Attributes:
        dice_roller (DiceRoller): Dice roller instance for rolling dice.
    """

    def __init__(self, dice_roller: DiceRoller):
        """
        Initializes a new instance of the BaseAbilityScoreRoller class.

        Args:
            dice_roller (DiceRoller): An existing DiceRoller instance.
        """
        self.dice_roller = dice_roller

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
        dice_rolls, _ = self.dice_roller.d6(n=4)  # Roll 4d6
        dropped_die = min(dice_rolls)
        return sum(dice_rolls) - dropped_die


class ClassicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_score(self):
        dice_rolls, _ = self.dice_roller.d6(n=3)  # Roll 3d6
        return sum(dice_rolls)


class HeroicAbilityScoreRoller(BaseAbilityScoreRoller):
    def roll_ability_score(self):
        # Roll 3d6, then ensure each die is at least 4 by using max(roll, 4)
        dice_rolls, _ = self.dice_roller.d6(n=3)
        adjusted_rolls = [
            max(roll, 4) for roll in dice_rolls
        ]  # Ensure each roll is at least 4
        return sum(adjusted_rolls)
