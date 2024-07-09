from sqlalchemy import Column, Integer, String, Float, Boolean
from ..schemas.itemSchema import ItemSchema

class Item(ItemSchema):
    __tablename__ = "items"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    price: float = Column(Float)
    is_offer: bool = Column(Boolean, default=False)


