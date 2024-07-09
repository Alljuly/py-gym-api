from pydantic import BaseModel
from typing import Union

class ItemSchema(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None]= None