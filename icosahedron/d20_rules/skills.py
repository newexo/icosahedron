from pydantic import BaseModel
from typing import List, Dict, Union


class Skill(BaseModel):
    """
    Represents a skill object with various attributes.
    """

    name: str
    description: str
    ability_score: str
    class_skill: bool
    synergy: List[Dict[str, Union[str, int]]]
    retry: bool
    special: List[str]
