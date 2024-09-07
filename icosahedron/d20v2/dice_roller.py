import numpy as np


class Context(object):
    def __init__(self, seed=1):
        self.__seed = seed
        self.__random_state = np.random.RandomState(seed)

    @property
    def r(self):
        return self.__random_state

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, seed):
        self.__seed = seed
        self.reset()

    @property
    def random_state(self):
        return self.__random_state

    @random_state.setter
    def random_state(self, random_state):
        self.__random_state = random_state
        self.__seed = random_state.get_state()[1][0]

    def reset(self):
        self.__random_state.seed(self.__seed)


class DiceRoller(Context):
    def __init__(self, seed=1):
        super().__init__(seed)

    def roll_dice(self, sides: int, n: int = 1, modifier: int = 0):
        """
        Rolls an n-sided dice 'n' times with an optional modifier.

        :param sides: Number of sides on the dice (e.g., 4 for d4, 6 for d6).
        :param n: Number of dice to roll.
        :param modifier: Modifier to add to the total result.
        :return: List of individual rolls and the total with modifier.
        """
        rolls = self.r.randint(1, sides + 1, size=n)  # Roll 'n' dice
        total = sum(rolls) + modifier
        return rolls.tolist(), total

    def d4(self, n: int = 1, modifier: int = 0):
        return self.roll_dice(4, n, modifier)

    def d6(self, n: int = 1, modifier: int = 0):
        return self.roll_dice(6, n, modifier)

    def d8(self, n: int = 1, modifier: int = 0):
        return self.roll_dice(8, n, modifier)

    def d10(self, n: int = 1, modifier: int = 0):
        return self.roll_dice(10, n, modifier)

    def d12(self, n: int = 1, modifier: int = 0):
        return self.roll_dice(12, n, modifier)

    def d20(self, n: int = 1, modifier: int = 0):
        return self.roll_dice(20, n, modifier)

    def d00(self, n: int = 1, modifier: int = 0):
        """
        Rolls percentile dice (d00), which simulates rolling two ten-sided dice:
        one for the tens digit and one for the ones digit.

        :param n: Number of percentile dice to roll.
        :param modifier: Modifier to add to the total result.
        :return: List of individual rolls and the total with modifier.
        """
        rolls = self.r.randint(0, 100, size=n)  # Roll 'n' d00
        total = sum(rolls) + modifier
        return rolls.tolist(), total
