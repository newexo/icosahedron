import numpy as np

from pydantic import BaseModel

dice_types = [4, 6, 8, 10, 12, 20, 100]


class DiceRoll(BaseModel):
    """
    Represents a D20 roll with a given dice type, number of dice, and modifier.
    """

    dice_type: int
    num_dice: int = 1
    modifier: int = 0

    def __init__(self, dice_type: int, num_dice: int = 1, modifier: int = 0):
        """
        Initializes a D20Roll instance with the specified parameters.

        Args:
            dice_type (int): The type of dice to roll, such as 4, 6, 8, 10, 12, or 20.
            num_dice (int, optional): The number of dice to roll. Defaults to 1.
            modifier (int, optional): The modifier to add to the roll result. Defaults to 0.

        Raises:
            ValueError: If the specified dice type is not one of the valid types.
            ValueError: If the number of dice is less than 1.
        """
        if dice_type not in dice_types:
            raise ValueError("Invalid dice type. Must be one of {}.".format(dice_types))
        if num_dice < 1:
            raise ValueError("Number of dice must be greater than or equal to 1.")
        super().__init__(dice_type=dice_type, num_dice=num_dice, modifier=modifier)


class DiceRoller:
    """A class that simulates rolling a D20 dice.

    This class uses a numpy RandomState object to generate random numbers
    for the dice rolls.

    Attributes:
        random (numpy.random.RandomState): The random number generator.

    Args:
        random_seed (int): An optional seed value to initialize the random
            number generator. If None, the generator is initialized using the
            system time.

    """

    def __init__(self, random_seed: int = None):
        """Initializes a new D20Roller object with the given random seed.

        Args:
            random_seed (int): An optional seed value to initialize the random
                number generator. If None, the generator is initialized using the
                system time.

        """
        self.random = np.random.RandomState(random_seed)

    def roll(self, d20roll: DiceRoll) -> int:
        """Simulates rolling the given D20Roll object.

        Args:
            d20roll (DiceRoll): The D20Roll object to simulate.

        Returns:
            int: The result of the dice roll.

        """
        results = [
            self.random.randint(1, d20roll.dice_type + 1)
            for _ in range(d20roll.num_dice)
        ]
        return sum(results) + d20roll.modifier
