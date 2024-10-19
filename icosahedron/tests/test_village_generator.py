import pytest

from ..d20v2.village_generator import VillageGenerator, DiceRoller


class TestVillageGenerator:
    @pytest.fixture
    def dice_roller(self):
        # Set up a DiceRoller instance
        return DiceRoller(seed=42)

    @pytest.fixture
    def generator(self, dice_roller):
        # Set up a VillageGenerator instance with a fixed seed
        return VillageGenerator(dice_roller=dice_roller)

    def test_generate_village(self, generator):
        # Generate a village and check that all fields are present
        village = generator.generate_village()

        # Assert that all key components are present
        assert "Purpose" in village
        assert "Geographic Location" in village
        assert "Population" in village
        assert "Number of Houses" in village
        assert "Demographics" in village
        assert "Primary Industry" in village
        assert "Leadership" in village
        assert "Notable Artisan or Merchant" in village
        assert "Infrastructure" in village
        assert "Map Layout" in village
        assert "Plot Hook" in village

    def test_population_values(self, generator):
        # Check if population values are within the expected range
        village = generator.generate_village()

        # Validate the population
        population = village["Population"]
        assert population in [
            50,
            100,
            150,
            200,
            250,
            300,
        ], "Population not within expected range"

    def test_leadership_type(self, generator):
        # Ensure that the leadership type is valid
        village = generator.generate_village()
        leadership_type = village["Leadership"]["Type"]
        expected_types = [
            "Village Elder",
            "Landowner",
            "Council of Elders",
            "Mayor or Reeve",
            "Religious Leader",
            "Merchant Guild",
        ]
        assert (
            leadership_type in expected_types
        ), f"Invalid leadership type: {leadership_type}"

    def test_infrastructure_count(self, generator):
        # Check if exactly 3 infrastructure elements are generated
        village = generator.generate_village()
        infrastructure = village["Infrastructure"]

        # Ensure the length of infrastructure is 3
        assert len(infrastructure) == 3, "Infrastructure count is not equal to 3"

    def test_dice_rolls_in_range(self, generator):
        # Check if dice rolls are within valid ranges during generation
        for _ in range(100):  # Roll 100 times to ensure reliability
            result = generator.dice_roller.d20()
            assert 1 <= result[1] <= 20, "D20 roll is out of range"

    def test_artisan_type(self, generator):
        # Ensure that the artisan/merchant type is valid
        village = generator.generate_village()
        artisan_type = village["Notable Artisan or Merchant"]["Type"]
        expected_types = [
            "Blacksmith",
            "Healer",
            "Carpenter",
            "Innkeeper",
            "Weaver",
            "Baker",
        ]
        assert artisan_type in expected_types, f"Invalid artisan type: {artisan_type}"

    def test_plot_hook(self, generator):
        # Ensure that the plot hook is one of the expected options
        village = generator.generate_village()
        plot_hook = village["Plot Hook"]
        expected_hooks = [
            "Missing Livestock",
            "Strange Illness",
            "Haunted Ruin",
            "Bandit Threat",
            "Sacred Festival",
            "Lost Child",
        ]
        assert plot_hook in expected_hooks, f"Invalid plot hook: {plot_hook}"

    def test_two_examples(self, generator):
        expected = {
            "Purpose": "Mining Outpost",
            "Geographic Location": "Mountain Foothills",
            "Population": 150,
            "Number of Houses": "30-40",
            "Demographics": "Mixed population, multicultural influences.",
            "Primary Industry": "Timber & Lumber",
            "Leadership": {
                "Type": "Religious Leader",
                "Leader": "Mill Owner",
                "Traits": "Wealthy, shrewd, and opportunistic",
                "Motivations": "Maintain trade dominance",
            },
            "Notable Artisan or Merchant": {
                "Type": "Carpenter",
                "Traits": "Cheerful, chatty, and superstitious",
                "Goods": "Woodworks, repairs",
            },
            "Infrastructure": ["General Store", "General Store", "Temple"],
            "Map Layout": "Spread Out",
            "Plot Hook": "Haunted Ruin",
        }

        actual = generator.generate_village()
        assert expected == actual

        expected = {
            "Purpose": "Religious Site",
            "Geographic Location": "Mountain Foothills",
            "Population": 100,
            "Number of Houses": "20-30",
            "Demographics": "Mix of races, one predominant culture.",
            "Primary Industry": "Mining",
            "Leadership": {
                "Type": "Merchant Guild",
                "Leader": "Retired Adventurer",
                "Traits": "Mysterious, pragmatic, and resilient",
                "Motivations": "Keep the village safe",
            },
            "Notable Artisan or Merchant": {
                "Type": "Healer",
                "Traits": "Gentle, quiet, and wise",
                "Goods": "Potions, herbal remedies",
            },
            "Infrastructure": ["Blacksmith’s Forge", "Temple", "Inn"],
            "Map Layout": "Spread Out",
            "Plot Hook": "Strange Illness",
        }
        actual = generator.generate_village()
        assert expected == actual

        expected = {
            "Purpose": "Religious Site",
            "Geographic Location": "Mountain Foothills",
            "Population": 200,
            "Number of Houses": "40-50",
            "Demographics": "Diverse races, strong regional influences.",
            "Primary Industry": "Grain Farming",
            "Leadership": {
                "Type": "Village Elder",
                "Leader": "Village Priest",
                "Traits": "Pious, compassionate, and devout",
                "Motivations": "Preserve the faith",
            },
            "Notable Artisan or Merchant": {
                "Type": "Carpenter",
                "Traits": "Cheerful, chatty, and superstitious",
                "Goods": "Woodworks, repairs",
            },
            "Infrastructure": ["Tavern", "Blacksmith’s Forge", "Blacksmith’s Forge"],
            "Map Layout": "Circular Pattern",
            "Plot Hook": "Lost Child",
        }
        actual = generator.generate_village()
        assert expected == actual
