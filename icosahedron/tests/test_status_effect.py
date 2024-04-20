from ..d20_rules.status_effect import StatusEffect


def test_status_effect_initialization():
    status_effect = StatusEffect(
        name="Blessed",
        description="Character receives a bonus on attack rolls and saving throws.",
        duration="Variable, typically temporary",
        saving_throw_check="N/A",
        cure_removal='Spells like "Remove Curse," "Dispel Magic," or duration expiration.',
    )
    assert status_effect.name == "Blessed"
    assert (
        status_effect.description
        == "Character receives a bonus on attack rolls and saving throws."
    )
    assert status_effect.duration == "Variable, typically temporary"
    assert status_effect.saving_throw_check == "N/A"
    assert (
        status_effect.cure_removal
        == 'Spells like "Remove Curse," "Dispel Magic," or duration expiration.'
    )


def test_status_effect_loading_from_dict():
    status_effect_data = {
        "name": "Blessed",
        "description": "Character receives a bonus on attack rolls and saving throws.",
        "duration": "Variable, typically temporary",
        "saving_throw_check": "N/A",
        "cure_removal": 'Spells like "Remove Curse," "Dispel Magic," or duration expiration.',
    }
    status_effect = StatusEffect(**status_effect_data)
    assert status_effect.dict() == status_effect_data


def test_status_effect_saving_to_dict():
    status_effect = StatusEffect(
        name="Blessed",
        description="Character receives a bonus on attack rolls and saving throws.",
        duration="Variable, typically temporary",
        saving_throw_check="N/A",
        cure_removal='Spells like "Remove Curse," "Dispel Magic," or duration expiration.',
    )
    status_effect_data = {
        "name": "Blessed",
        "description": "Character receives a bonus on attack rolls and saving throws.",
        "duration": "Variable, typically temporary",
        "saving_throw_check": "N/A",
        "cure_removal": 'Spells like "Remove Curse," "Dispel Magic," or duration expiration.',
    }
    assert status_effect.dict() == status_effect_data
