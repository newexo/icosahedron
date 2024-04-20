from pydantic import BaseModel


class StatusEffect(BaseModel):
    """
    Represents a status effect with properties describing its name, description, duration,
    saving throw or check required, and method of cure or removal.

    Attributes:
        name (str): The name of the status effect.
        description (str): A description of the status effect and its effects on characters.
        duration (str): The duration of the status effect, typically specified as a string.
        saving_throw_check (str): The type of saving throw or check required to resist or
            mitigate the effects of the status effect.
        cure_removal (str): The method of cure or removal for the status effect, such as
            spells, abilities, or natural recovery.

    Example:
        # Create a StatusEffect instance
        status_effect = StatusEffect(
            name="Blessed",
            description="Character receives a bonus on attack rolls and saving throws.",
            duration="Variable, typically temporary",
            saving_throw_check="N/A",
            cure_removal="Spells like \"Remove Curse,\" \"Dispel Magic,\" or duration expiration."
        )
    """

    name: str
    description: str
    duration: str
    saving_throw_check: str
    cure_removal: str
