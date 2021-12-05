from fastapi import APIRouter
from internal.types import Item, EditedItem
from internal.admin import *

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World!"}

@router.post("/items/", status_code=201, response_model=Item)
async def add_item(item: Item):
    addItem(item)
    return item

@router.get("/items/", status_code=200)
async def get_items():
    itemList = getItems()
    return itemList

@router.get("/items/{param}", status_code=200)
async def get_item(param):
    item = getItem(param)
    return item

@router.delete("/items/{id}")
async def delete_item(id):
    res = deleteItem(id)
    return res

@router.patch("/items/{id}")
async def update_item(id, editedItem: EditedItem):
    id = int(id)
    res = updateItem(id, editedItem)
    return res