from ..d20v2.xp_compute import Character, Monster, Encounter, Party


def test_character_initialization():
    # Test character initialization
    fighter = Character("Fighter", 3)
    assert fighter.name == "Fighter"
    assert fighter.level == 3
    assert fighter.xp == 0


def test_monster_initialization():
    # Test monster initialization and XP value lookup
    zombie = Monster("Zombie", 1 / 2)
    assert zombie.name == "Zombie"
    assert zombie.cr == 1 / 2
    assert (
        zombie.get_xp_value(3) == 150
    )  # Zombie CR 1/2 should give 150 XP for a 3rd level party

    wraith = Monster("Wraith", 5)
    assert (
        wraith.get_xp_value(3) == 1800
    )  # Wraith CR 5 should give 1800 XP for a 3rd level party


def test_party_initialization():
    # Test party initialization and average level calculation
    fighter = Character("Fighter", 3)
    cleric = Character("Cleric", 3)
    party = Party([fighter, cleric])

    assert party.get_average_level() == 3
    assert len(party.characters) == 2


def test_encounter_xp_distribution_single_encounter():
    # Test a simple encounter where two characters fight two zombies
    fighter = Character("Fighter", 3)
    cleric = Character("Cleric", 3)

    zombie1 = Monster("Zombie", 1 / 2)
    zombie2 = Monster("Zombie", 1 / 2)

    # Create an encounter and distribute XP
    encounter = Encounter([zombie1, zombie2], [fighter, cleric])
    encounter.distribute_xp(3)

    # Both characters should receive 150 XP each (300 total split between 2)
    assert fighter.xp == 150
    assert cleric.xp == 150


def test_encounter_xp_distribution_unequal_participation():
    # Test an encounter with different participants
    fighter = Character("Fighter", 3)
    cleric = Character("Cleric", 3)
    rogue = Character("Rogue", 3)

    ghoul1 = Monster("Ghoul", 1)
    ghoul2 = Monster("Ghoul", 1)

    # Fighter and Cleric participate in killing the ghouls, but the Rogue is paralyzed and doesn't participate
    encounter = Encounter([ghoul1, ghoul2], [fighter, cleric])
    encounter.distribute_xp(3)

    # Total XP for two ghouls is 600, and it should be split between the fighter and cleric
    assert fighter.xp == 300
    assert cleric.xp == 300
    assert rogue.xp == 0  # Rogue didn't participate, so XP should remain 0


def test_wraith_escape_no_xp_awarded():
    # Test an encounter where the wraith escapes and no XP is awarded for it
    fighter = Character("Fighter", 3)
    cleric = Character("Cleric", 3)
    wizard = Character("Wizard", 3)

    wraith = Monster("Wraith", 5)

    # Assume the wraith escapes, so we don't add it to the encounter
    encounter = Encounter([], [fighter, cleric, wizard])
    encounter.distribute_xp(3)

    # No monsters in the encounter, so no XP should be awarded
    assert fighter.xp == 0
    assert cleric.xp == 0
    assert wizard.xp == 0


def test_mixed_monsters_encounter():
    # Test a complex encounter with multiple monster types and different participants
    fighter = Character("Fighter", 3)
    cleric = Character("Cleric", 3)
    wizard = Character("Wizard", 3)
    rogue = Character("Rogue", 3)

    zombie1 = Monster("Zombie", 1 / 2)
    zombie2 = Monster("Zombie", 1 / 2)
    ghoul1 = Monster("Ghoul", 1)
    ghoul2 = Monster("Ghoul", 1)

    # Scenario: Fighter and Cleric kill the zombies, while Fighter, Cleric, and Wizard fight the ghouls
    # Rogue is paralyzed, and doesn't participate in the ghouls' fight

    # First encounter: Zombies (Fighter and Cleric only)
    encounter1 = Encounter([zombie1, zombie2], [fighter, cleric])
    encounter1.distribute_xp(3)

    # Second encounter: Ghouls (Fighter, Cleric, Wizard)
    encounter2 = Encounter([ghoul1, ghoul2], [fighter, cleric, wizard])
    encounter2.distribute_xp(3)

    # XP Breakdown:
    # - Zombie encounter (300 XP split between Fighter and Cleric): 150 XP each
    # - Ghoul encounter (600 XP split between Fighter, Cleric, Wizard): 200 XP each

    # Final XP values
    assert fighter.xp == 150 + 200  # 350 XP total
    assert cleric.xp == 150 + 200  # 350 XP total
    assert wizard.xp == 200  # 200 XP total
    assert rogue.xp == 0  # Rogue didn't participate, so XP should remain 0
