
from pydantic import BaseModel


class StatusEffect(BaseModel):
    name: str
    description: str
    duration: str
    saving_throw_check: str
    cure_removal: str


# Example instantiation
status_effect = StatusEffect(
    name="Blessed",
    description="Character receives a bonus on attack rolls and saving throws.",
    duration="Variable, typically temporary",
    saving_throw_check="N/A",
    cure_removal="Spells like \"Remove Curse,\" \"Dispel Magic,\" or duration expiration."
)

print(status_effect)