from fastapi import FastAPI
from typing import Union
from src.models.itemModel import Item

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id" : item_id, "q" : q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"Item_name" : item.name, "item_id": item_id}
        