from internal.types import Item, EditedItem

from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, insert, select, delete, update

engine = create_engine("sqlite:///stock.db", echo=True)
global conn, items

conn = engine.connect()
meta = MetaData()

items = Table('items', meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String, nullable=False),
    Column('price', Float, nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('description', String))
meta.create_all(engine)


class db:
    def checkId(idNum: int):
        query = select(items).where(items.c.id == idNum)
        res = conn.execute(query)
        if len(res.fetchall()) == 0:
          return False

    def getMaxId() -> int:
        query = select(items)
        res = conn.execute(query)
        return len(res.fetchall()) + 1


def addItem(item: Item):
    for i in range(1, db.getMaxId()):
        if db.checkId(i) == False:
            query = insert(items).values(id=i, name=item.name, price=item.price, quantity=item.quantity, description=item.description)
            try:
                res = conn.execute(query)
                return (item, "200 OK")
            except:
                return
        else:
            pass
    query = insert(items).values(name=item.name, price=item.price, quantity=item.quantity, description=item.description)
    try:
        res = conn.execute(query)
        return (item, "200 OK")
    except:
        return 

def getItems():
    query = select(items)
    try:
        res = conn.execute(query)
        return res.fetchall()
    except:
        return

def getItem(param) -> Item: 
    try:
        param = int(param)
    except:
        pass

    if type(param) == int:
        field = 'id'
        query = select(items).where(items.c[field] == param)
    elif type(param) == str:
        field = 'name'
        query = select(items).where(items.c[field] == param or items.c[field] == param.upper() or items.c[field] == param.lower() or items.c[field] == param.capitalize())
    
    try:
        raw = conn.execute(query)
        raw = raw.fetchall()
    
        res = Item(id = raw[0][0], name = raw[0][1], price = raw[0][2], quantity = raw[0][3], description = raw[0][4])
        
        return res
    except:
        return "Error getting this item"

def deleteItem(idNum: int):
    query = delete(items).where(items.c.id == idNum)
    try:
        res = conn.execute(query)
        return "200 OK"
    except:
        return

def updateItem(idNum: int, newItem: EditedItem):
    oldItem = getItem(idNum)

    if newItem.name in ("", None):
        newItem.name = oldItem.name
    if not newItem.price:
        newItem.price = oldItem.price
    if not newItem.quantity:
        newItem.quantity = oldItem.quantity
    if newItem.description in ("", None):
        newItem.description = oldItem.description

    
    
    query = update(items).where(items.c.id == idNum).values(id=idNum, name = newItem.name, price = newItem.price, quantity = newItem.quantity, description = newItem.description)
    res = conn.execute(query)
    
    return "200 OK"