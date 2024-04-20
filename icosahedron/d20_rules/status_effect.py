from pydantic import BaseModel


class StatusEffect(BaseModel):
    name: str
    description: str
    duration: str
    saving_throw_check: str
    cure_removal: str
