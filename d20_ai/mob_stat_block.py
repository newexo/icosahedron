import json


class NPC:
    def __init__(
        self,
        name,
        hit_points,
        armor_class,
        attack_bonus,
        damage,
        speed,
        abilities,
        skills,
        special_abilities,
        equipment,
        alignment,
        description,
    ):
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attack_bonus = attack_bonus
        self.damage = damage
        self.speed = speed
        self.abilities = abilities
        self.skills = skills
        self.special_abilities = special_abilities
        self.equipment = equipment
        self.alignment = alignment
        self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)


# Example usage:

# Create an instance of the NPC class for Iggy
iggy = NPC(
    name="Iggy",
    hit_points=12,
    armor_class=14,
    attack_bonus=4,
    damage="1d6+2",
    speed=30,
    abilities={"str": 12, "dex": 16, "con": 10, "int": 8, "wis": 8, "cha": 6},
    skills={"stealth": 6},
    special_abilities={"nimbleEscape": True},
    equipment=["Shortsword", "Shortbow", "Leather Armor"],
    alignment="Chaotic Evil",
    description="Iggy is a small, wiry goblin with beady eyes and a wicked grin. He wears a ragged leather tunic and carries a shortsword and shortbow. He is always looking for an opportunity to cause chaos and sow discord.",
)

# Convert the Iggy object to a JSON string
iggy_json = iggy.to_json()
print(iggy_json)

# Recreate the Iggy object from the JSON string
iggy_from_json = NPC.from_json(iggy_json)
print(iggy_from_json.name)  # prints "Iggy"


# Create an instance of the NPC class for Bob the Evil Wizard
# bob = NPC(
#     name="Bob the Evil Wizard",
#     hit_points=40,
#     armor_class=15,
#     attack_bonus=7,
#     damage="2d6+4",
#     speed=30,
#     abilities={
#         "str": 10,
#         "dex": 14,
#         "con": 12,
#         "int": 18,
#         "wis": 16,
#         "cha": 8
#     },
#     skills={
#         "arcana": 8,
