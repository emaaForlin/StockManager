from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from internal.types import Item, EditedItem
from internal.admin import *

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World!"}

@router.post("/items/", status_code=201, response_model=Item)
async def add_item(item: Item):
    item = addItem(item)
    if item:
        return item
    else:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content="Cannot create this item") 

@router.get("/items/", status_code=200)
async def get_items():
    itemList = getItems()
    if itemList:
        return itemList
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Zero items found")

@router.get("/items/{param}", status_code=200)
async def get_item(param):
    item = getItem(param)
    if item:
        return item
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="This item not exists")

@router.delete("/items/{id}")
async def delete_item(id):
    res = deleteItem(id)
    if res:
        return JSONResponse(status_code=status.HTTP_200_OK, content="Item deleted successfully")
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="Cannot delete this item, maybe this ID not exists")

@router.patch("/items/{id}")
async def update_item(id, editedItem: EditedItem):
    id = int(id)
    res = updateItem(id, editedItem)
    if res:
        return res
    else:
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content="Cannot edit this item, maybe this ID not exists")