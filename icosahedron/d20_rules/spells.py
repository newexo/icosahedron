from pydantic import BaseModel
from typing import List


class Spell(BaseModel):
    """
    A class representing a spell in the D20 system.
    """

    name: str
    school: str
    level: int
    casting_time: str
    range: str
    duration: str
    saving_throw: str
    spell_resistance: bool
    components: List[str]
    description: str
