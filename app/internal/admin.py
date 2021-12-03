from sqlalchemy.sql.elements import Null
from internal.types import Item
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, insert, select, delete

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
        else:
            return True

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
                pass
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
        pass

def getItem(param):
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

    else:
        pass
    
    try:
        res = conn.execute(query)
        return res.fetchall()
    except:
        pass

def deleteItem(idNum: int):
    query = delete(items).where(items.c.id == idNum)
    try:
        res = conn.execute(query)
        return "200 OK"
    except:
        pass