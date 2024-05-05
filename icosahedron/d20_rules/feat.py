from pydantic import BaseModel
from typing import Optional


class Feat(BaseModel):
    """
    Class representing a feat in a role-playing game.
    """

    name: str
    prerequisites: str
    benefit: str
    description: str
    usage: str
    normal_use: Optional[str] = None
