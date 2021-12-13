from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse
from internal.types import Item, EditedItem
from internal.admin import *
from datetime import datetime
import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
router = APIRouter()

@router.get("/")
async def root(background_task: BackgroundTasks):
    background_task.add_task(logging.info, "App working")
    return {"message": "Hello World!"}

@router.post("/items/", status_code=201, response_model=Item)
async def add_item(item: Item, background_task: BackgroundTasks):
    item = addItem(item)
    if item:
        background_task.add_task(logging.info, "Item successfully added")
        return item
    else:
        background_task.add_task(logging.warning, "Item cannot be created")
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content="Item cannot be created") 

@router.get("/items/", status_code=200)
async def get_items(background_task: BackgroundTasks):
    itemList = getItems()
    if itemList:
        background_task.add_task(logging.info, "Show items requested")
        return itemList
    else:
        background_task.add_task(logging.warning, "Something was wrong getting the items")
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Zero items found")

@router.get("/items/{param}", status_code=200)
async def get_item(param, background_task: BackgroundTasks):
    item = getItem(param)
    if item:
        background_task.add_task(logging.info, "Show an item requested")
        return item
    else:
        background_task.add_task(logging.warning, "This item not exists")
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="This item not exists")

@router.delete("/items/{id}")
async def delete_item(id, background_task: BackgroundTasks):
    res = deleteItem(id)
    if res:
        background_task.add_task(logging.info, "Item deleted successfully")
        return JSONResponse(status_code=status.HTTP_200_OK, content="Item deleted successfully")
    else:
        background_task.add_task(logging.warning, "Cannot delete this item, maybe this ID not exists")
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Cannot delete this item, maybe this ID not exists")

@router.patch("/items/{id}")
async def update_item(id, editedItem: EditedItem, background_task: BackgroundTasks):
    id = int(id)
    res = updateItem(id, editedItem)
    if res:
        background_task.add_task(logging.info, res)
        return res
    else:
        background_task.add_task(logging.warning, "Cannot edit this item, maybe this ID not exists")
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content="Cannot edit this item, maybe this ID not exists")