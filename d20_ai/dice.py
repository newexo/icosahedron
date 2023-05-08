import numpy as np
import json

dice_types = [4, 6, 8, 10, 12, 20]


class D20Roll:
    def __init__(self, dice_type, num_dice=1, modifier=0):
        if dice_type not in dice_types or num_dice < 1:
            raise ValueError("Invalid dice type. Must be one of " + str(dice_types))
        self.dice_type = dice_type
        self.num_dice = num_dice
        self.modifier = modifier

    def to_json(self):
        return json.dumps(
            {
                "dice_type": self.dice_type,
                "num_dice": self.num_dice,
                "modifier": self.modifier,
            }
        )

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data["dice_type"], data.get("num_dice", 1), data.get("modifier", 0))


class D20Roller:
    def __init__(self, random_seed: int = None):
        self.random = np.random.RandomState(random_seed)

    def roll(self, d20roll: D20Roll) -> int:
        results = [
            self.random.randint(1, d20roll.dice_type + 1)
            for _ in range(d20roll.num_dice)
        ]
        return sum(results) + d20roll.modifier
