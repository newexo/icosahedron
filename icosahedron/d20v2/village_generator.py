from .dice_roller import DiceRoller


# Modified VillageGenerator to include DiceRoller
class VillageGenerator:
    def __init__(self, dice_roller: DiceRoller):
        self.dice_roller = dice_roller
        self.tables = {
            "purpose": [
                "Farming Hub",
                "Trade Stop",
                "Fishing Port",
                "Mining Outpost",
                "Artisan’s Retreat",
                "Religious Site",
            ],
            "geographic_location": [
                "Forest Clearing",
                "Riverside",
                "Plains",
                "Hillside",
                "Mountain Foothills",
                "Coastal",
            ],
            "population_size": [
                {
                    "population": 50,
                    "houses": "10-15",
                    "demographics": "Mostly one race, isolated culture.",
                },
                {
                    "population": 100,
                    "houses": "20-30",
                    "demographics": "Mix of races, one predominant culture.",
                },
                {
                    "population": 150,
                    "houses": "30-40",
                    "demographics": "Mixed population, multicultural influences.",
                },
                {
                    "population": 200,
                    "houses": "40-50",
                    "demographics": "Diverse races, strong regional influences.",
                },
                {
                    "population": 250,
                    "houses": "50-60",
                    "demographics": "Multiple races, occasional visitors.",
                },
                {
                    "population": 300,
                    "houses": "60-70",
                    "demographics": "Cosmopolitan for a village, trading hub.",
                },
            ],
            "primary_industry": [
                "Grain Farming",
                "Livestock Rearing",
                "Fishing",
                "Mining",
                "Timber & Lumber",
                "Craftsmanship",
            ],
            "social_structure": [
                "Village Elder",
                "Landowner",
                "Council of Elders",
                "Mayor or Reeve",
                "Religious Leader",
                "Merchant Guild",
            ],
            "village_leaders": [
                {
                    "role": "Elder",
                    "traits": "Wise, stern, and traditional",
                    "motivations": "Protect village customs",
                },
                {
                    "role": "Mill Owner",
                    "traits": "Wealthy, shrewd, and opportunistic",
                    "motivations": "Maintain trade dominance",
                },
                {
                    "role": "Village Priest",
                    "traits": "Pious, compassionate, and devout",
                    "motivations": "Preserve the faith",
                },
                {
                    "role": "Constable",
                    "traits": "Brave, lawful, and gruff",
                    "motivations": "Keep peace and enforce rules",
                },
                {
                    "role": "Merchant",
                    "traits": "Friendly, persuasive, and ambitious",
                    "motivations": "Expand trade opportunities",
                },
                {
                    "role": "Retired Adventurer",
                    "traits": "Mysterious, pragmatic, and resilient",
                    "motivations": "Keep the village safe",
                },
            ],
            "artisans_and_merchants": [
                {
                    "type": "Blacksmith",
                    "traits": "Gruff, hardworking, and loyal",
                    "goods": "Tools, weapons, repairs",
                },
                {
                    "type": "Healer",
                    "traits": "Gentle, quiet, and wise",
                    "goods": "Potions, herbal remedies",
                },
                {
                    "type": "Carpenter",
                    "traits": "Cheerful, chatty, and superstitious",
                    "goods": "Woodworks, repairs",
                },
                {
                    "type": "Innkeeper",
                    "traits": "Welcoming, nosy, and gregarious",
                    "goods": "Rooms, food, information",
                },
                {
                    "type": "Weaver",
                    "traits": "Creative, meticulous, and reclusive",
                    "goods": "Fabrics, clothing",
                },
                {
                    "type": "Baker",
                    "traits": "Kind, motherly, and talkative",
                    "goods": "Bread, pastries, gossip",
                },
            ],
            "infrastructure": [
                "Inn",
                "Tavern",
                "General Store",
                "Blacksmith’s Forge",
                "Temple",
                "Water Mill",
            ],
            "map_layout": [
                "Central Square",
                "Linear Road",
                "Riverside Cluster",
                "Spread Out",
                "Dense Cluster",
                "Circular Pattern",
            ],
            "plot_hooks": [
                "Missing Livestock",
                "Strange Illness",
                "Haunted Ruin",
                "Bandit Threat",
                "Sacred Festival",
                "Lost Child",
            ],
        }

    def generate_village(self):
        # Use dice rolls to select details from each table
        purpose = self._roll_table("purpose", 6)
        location = self._roll_table("geographic_location", 6)
        population_info = self._roll_table("population_size", 6)
        industry = self._roll_table("primary_industry", 6)
        leadership = self._roll_table("social_structure", 6)
        leader = self._roll_table("village_leaders", 6)
        merchant = self._roll_table("artisans_and_merchants", 6)
        infrastructure = self._roll_multiple("infrastructure", 3, 6)
        layout = self._roll_table("map_layout", 6)
        plot_hook = self._roll_table("plot_hooks", 6)

        # Create village description
        village_description = {
            "Purpose": purpose,
            "Geographic Location": location,
            "Population": population_info["population"],
            "Number of Houses": population_info["houses"],
            "Demographics": population_info["demographics"],
            "Primary Industry": industry,
            "Leadership": {
                "Type": leadership,
                "Leader": leader["role"],
                "Traits": leader["traits"],
                "Motivations": leader["motivations"],
            },
            "Notable Artisan or Merchant": {
                "Type": merchant["type"],
                "Traits": merchant["traits"],
                "Goods": merchant["goods"],
            },
            "Infrastructure": infrastructure,
            "Map Layout": layout,
            "Plot Hook": plot_hook,
        }

        return village_description

    def _roll_table(self, table_name, sides):
        roll = self.dice_roller.roll_dice(sides, n=1)[1]
        return self.tables[table_name][roll - 1]

    def _roll_multiple(self, table_name, count, sides):
        rolls = [self.dice_roller.roll_dice(sides, n=1)[1] for _ in range(count)]
        return [self.tables[table_name][roll - 1] for roll in rolls]
