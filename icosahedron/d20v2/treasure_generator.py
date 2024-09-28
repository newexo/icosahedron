from abc import ABC, abstractmethod
from .dice_roller import DiceRoller

class BaseTreasureGenerator(ABC):
    """
    Abstract base class for generating treasure in a d20 game based on CR and other factors.

    Attributes:
        dice_roller (DiceRoller): An instance of the DiceRoller for generating random results.
    """

    def __init__(self, dice_roller: DiceRoller):
        """
        Initializes the treasure generator.

        Args:
            dice_roller (DiceRoller): An existing instance of the DiceRoller.
        """
        self.dice_roller = dice_roller

    @abstractmethod
    def generate_treasure(self, cr: int, use_average: bool = False) -> dict:
        """
        Abstract method to generate treasure based on the Challenge Rating (CR).

        Args:
            cr (int): The challenge rating of the encounter or dungeon.
            use_average (bool): Whether to use average rolls for treasure generation.

        Returns:
            dict: The generated treasure including coins, gems, and magic items.
        """
        pass


class DungeonTreasureGenerator(BaseTreasureGenerator):
    """
    Class for generating treasure in a dungeon based on Challenge Rating (CR).
    Includes coins, gems, and magic items.
    """

    def generate_treasure(self, cr: int, use_average: bool = False) -> dict:
        """
        Generates treasure based on CR. Determines coins, gems, and magic items.

        Args:
            cr (int): The challenge rating of the dungeon.
            use_average (bool): If True, uses average values instead of rolling.

        Returns:
            dict: The generated treasure with keys 'coins', 'gems', and 'magic_items'.
        """
        treasure = {
            "coins": self.generate_coins(cr, use_average),
            "gems": self.generate_gems(cr, use_average),
            "magic_items": self.generate_magic_items(cr, use_average),
        }
        return treasure

    def generate_coins(self, cr: int, use_average: bool = False) -> dict:
        """
        Generate coins based on the CR of the encounter or dungeon.

        Args:
            cr (int): The challenge rating of the dungeon.
            use_average (bool): If True, use average values instead of rolling.

        Returns:
            dict: A dictionary of coin types and their amounts.
        """
        coins = {}

        if cr <= 4:
            # CR 0-4: Small amounts of copper, silver, and a little gold
            copper = 1 * (100 if use_average else self.dice_roller.d6()[0][0])
            silver = 10 if use_average else self.dice_roller.d6()[0][0]
            gold = 1 if use_average else self.dice_roller.d6()[0][0]
            coins = {"cp": copper, "sp": silver, "gp": gold}

        elif cr <= 10:
            # CR 5-10: Larger amounts of gold, silver, and some platinum
            gold = 100 if use_average else 10 * self.dice_roller.d6()[0][0]
            platinum = 10 if use_average else self.dice_roller.d6()[0][0]
            coins = {"gp": gold, "pp": platinum}

        elif cr <= 16:
            # CR 11-16: Higher amounts of gold and platinum
            gold = 500 if use_average else 100 * self.dice_roller.d6()[0][0]
            platinum = 20 if use_average else 2 * self.dice_roller.d6()[0][0]
            coins = {"gp": gold, "pp": platinum}

        else:
            # CR 17+: Vast amounts of platinum and gold
            gold = 1000 if use_average else 500 * self.dice_roller.d6()[0][0]
            platinum = 50 if use_average else 5 * self.dice_roller.d6()[0][0]
            coins = {"gp": gold, "pp": platinum}

        return coins

    def generate_gems(self, cr: int, use_average: bool = False) -> list:
        """
        Generate gems based on CR.

        Args:
            cr (int): The challenge rating of the dungeon.
            use_average (bool): If True, use average values instead of rolling.

        Returns:
            list: A list of gems, where each gem is represented by its value in gold.
        """
        gems = []
        if cr <= 4:
            # CR 0-4: 1d6 gems worth 10gp each
            num_gems = 1 if use_average else self.dice_roller.d6()[0][0]
            gems = [10] * num_gems

        elif cr <= 10:
            # CR 5-10: 1d6 gems worth 50gp each
            num_gems = 3 if use_average else self.dice_roller.d6()[0][0]
            gems = [50] * num_gems

        elif cr <= 16:
            # CR 11-16: 1d6 gems worth 100gp each
            num_gems = 5 if use_average else self.dice_roller.d6()[0][0]
            gems = [100] * num_gems

        else:
            # CR 17+: 1d6 gems worth 500gp each
            num_gems = 6 if use_average else self.dice_roller.d6()[0][0]
            gems = [500] * num_gems

        return gems

    def generate_magic_items(self, cr: int, use_average: bool = False) -> list:
        """
        Generate magic items based on CR.

        Args:
            cr (int): The challenge rating of the dungeon.
            use_average (bool): If True, use average values instead of rolling.

        Returns:
            list: A list of magic items.
        """
        magic_items = []

        # Example logic for magic items, could be expanded with real item generation
        if cr <= 4:
            # CR 0-4: Common magic items like potions
            magic_items = ["Potion of Healing"] if not use_average else ["Potion of Healing", "Scroll of Light"]

        elif cr <= 10:
            # CR 5-10: Uncommon magic items
            magic_items = ["+1 Weapon"] if not use_average else ["+1 Weapon", "Bag of Holding"]

        elif cr <= 16:
            # CR 11-16: Rare magic items
            magic_items = ["+2 Weapon"] if not use_average else ["+2 Weapon", "Cloak of Protection"]

        else:
            # CR 17+: Very rare or legendary magic items
            magic_items = ["+3 Weapon"] if not use_average else ["+3 Weapon", "Staff of Power"]

        return magic_items
