from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str]

class EditedItem(BaseModel):
    name: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    description: Optional[str]