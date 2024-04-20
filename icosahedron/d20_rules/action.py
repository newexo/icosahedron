
from pydantic import BaseModel

class Action(BaseModel):
    name: str
    action_type: str
    aoo: str
    description: str

    class Config:
        allow_mutation = False