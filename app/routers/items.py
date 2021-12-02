from fastapi import APIRouter
from internal.types import Item
from internal.admin import *

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World!"}

@router.post("/items/", response_model=Item)
async def add_item(item: Item):
    addItem(item)
    return item

@router.get("/items/")
async def get_items():
    itemList = getItems()
    return itemList

@router.get("/items/{param}")
async def get_item(param):
    item = getItem(param)
    return item