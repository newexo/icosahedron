from pydantic import BaseModel


class InventoryItem(BaseModel):
    name: str
    weight: float
    description: str = ""
    condition: str = "new"
    value: float = 0.0
