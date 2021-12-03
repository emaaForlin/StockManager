from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str] = None