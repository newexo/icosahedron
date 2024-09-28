from abc import ABC, abstractmethod
from .dice_roller import DiceRoller


class BaseHitPointCalculator(ABC):
    """
    Abstract base class for calculating hit points in a d20 game.

    Attributes:
        dice_roller (DiceRoller): An existing dice roller instance.
        constitution_modifier (int): The character's Constitution modifier.
        level (int): The current level of the character.
    """

    def __init__(self, dice_roller: DiceRoller, constitution_modifier: int):
        """
        Initializes the hit point calculator.

        Args:
            dice_roller (DiceRoller): An instance of the DiceRoller.
            constitution_modifier (int): The character's Constitution modifier.
        """
        self.dice_roller = dice_roller
        self.constitution_modifier = constitution_modifier

    @abstractmethod
    def calculate_hit_points(self, level: int, use_average: bool = False) -> int:
        """
        Abstract method to calculate total hit points for a character up to the specified level.

        Args:
            level (int): The character's level.
            use_average (bool): Whether to use average rolls for hit dice.

        Returns:
            int: The total hit points.
        """
        pass


class FighterHitPointCalculator(BaseHitPointCalculator):
    def calculate_hit_points(self, level: int, use_average: bool = False) -> int:
        """
        Calculates the total hit points for a Fighter character.

        Args:
            level (int): The current level of the character.
            use_average (bool): If True, use average hit points instead of rolling.

        Returns:
            int: The total hit points for the fighter.
        """
        total_hp = 10 + self.constitution_modifier  # Max hit die at 1st level for Fighter (d10)

        for lvl in range(2, level + 1):
            if use_average:
                # Average roll for d10 is 5.5, rounding up to 6
                total_hp += 6 + self.constitution_modifier
            else:
                # Roll the d10 for each level and add Constitution modifier
                roll, _ = self.dice_roller.d10()
                total_hp += roll[0] + self.constitution_modifier

            # Ensure the HP gained per level is at least 1 (minimum 1 HP rule)
            if total_hp < 1:
                total_hp = 1

        return total_hp


class WizardHitPointCalculator(BaseHitPointCalculator):
    def calculate_hit_points(self, level: int, use_average: bool = False) -> int:
        """
        Calculates the total hit points for a Wizard character.

        Args:
            level (int): The current level of the character.
            use_average (bool): If True, use average hit points instead of rolling.

        Returns:
            int: The total hit points for the wizard.
        """
        total_hp = 6 + self.constitution_modifier  # Max hit die at 1st level for Wizard (d6)

        for lvl in range(2, level + 1):
            if use_average:
                # Average roll for d6 is 3.5, rounding up to 4
                total_hp += 4 + self.constitution_modifier
            else:
                # Roll the d6 for each level and add Constitution modifier
                roll, _ = self.dice_roller.d6()
                total_hp += roll[0] + self.constitution_modifier

            # Ensure the HP gained per level is at least 1 (minimum 1 HP rule)
            if total_hp < 1:
                total_hp = 1

        return total_hp
