from pydantic import BaseModel, Field
from typing import List, Dict


class CharacterSheet(BaseModel):
    name: str
    race: str
    char_class: str
    level: int
    alignment: str
    ability_scores: Dict[str, int]
    skills: Dict[str, int]
    feats: List[Dict[str, str]]
    equipment: List[str]
    spells_known: Dict[str, List[str]]
    background: str
