import random


class D20Roller:
    def __init__(self):
        self.dice_types = [4, 6, 8, 10, 12, 20]

    def roll(self, dice_type, num_dice=1, modifier=0):
        if dice_type not in self.dice_types:
            raise ValueError("Invalid dice type. Must be one of " + str(self.dice_types))

        result = modifier
        for i in range(num_dice):
            roll = random.randint(1, dice_type)
            result += roll
        return result


import json


def roll_dice(json_obj):
    # Load the JSON object and extract the values for the roll
    data = json.loads(json_obj)
    dice_type = data['dice_type']
    num_dice = data.get('num_dice', 1)
    modifier = data.get('modifier', 0)

    # Create a D20Roller object and roll the dice
    roller = D20Roller()
    result = roller.roll(dice_type, num_dice=num_dice, modifier=modifier)

    # Return the result as a JSON object
    return json.dumps({'result': result})


import json


class D20Roll:
    def __init__(self, dice_type, num_dice=1, modifier=0):
        self.dice_type = dice_type
        self.num_dice = num_dice
        self.modifier = modifier

    def to_json(self):
        return json.dumps({
            'dice_type': self.dice_type,
            'num_dice': self.num_dice,
            'modifier': self.modifier
        })

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['dice_type'], data.get('num_dice', 1), data.get('modifier', 0))

