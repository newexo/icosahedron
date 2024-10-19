class Character:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.xp = 0  # Total experience points earned

    def add_xp(self, xp: int):
        self.xp += xp

    def __repr__(self):
        return f"{self.name} (Level {self.level}) - XP: {self.xp}"


class Monster:
    XP_TABLE = {
        (1 / 4): {3: 75},  # CR 1/4 monsters provide 75 XP to a 3rd level party
        (1 / 2): {3: 150},  # CR 1/2 monsters provide 150 XP to a 3rd level party
        1: {3: 300},  # CR 1 monsters provide 300 XP to a 3rd level party
        5: {3: 1800},  # CR 5 monsters provide 1800 XP to a 3rd level party
    }

    def __init__(self, name: str, cr: float):
        self.name = name
        self.cr = cr

    def get_xp_value(self, party_level: int) -> int:
        return self.XP_TABLE.get(self.cr, {}).get(party_level, 0)

    def __repr__(self):
        return f"{self.name} (CR {self.cr})"


class Encounter:
    def __init__(self, monsters: list, participants: list):
        self.monsters = monsters
        self.participants = (
            participants  # List of Characters who contributed to the encounter
        )

    def calculate_total_xp(self, party_level: int):
        total_xp = sum(monster.get_xp_value(party_level) for monster in self.monsters)
        return total_xp

    def distribute_xp(self, party_level: int):
        total_xp = self.calculate_total_xp(party_level)
        if len(self.participants) == 0:
            return
        xp_per_character = total_xp // len(self.participants)

        # Distribute XP to each participating character
        for character in self.participants:
            character.add_xp(xp_per_character)


class Party:
    def __init__(self, characters: list):
        self.characters = characters  # List of Character objects

    def get_average_level(self):
        total_levels = sum(char.level for char in self.characters)
        return total_levels // len(self.characters)

    def __repr__(self):
        return f"Party: {[str(char) for char in self.characters]}"
