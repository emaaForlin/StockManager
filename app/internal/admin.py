from internal.types import Item
import sqlalchemy as db
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select


engine = create_engine("sqlite:///stock.db", echo=True)
global conn, items

conn = engine.connect()
meta = MetaData()

items = Table('items', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Integer),
    Column('description', String))
meta.create_all(engine)


def addItem(item: Item):
    query = insert(items).values(name=item.name, price=item.price, description=item.description)
    res = conn.execute(query)
    return item

def getItems():
    query = select(items)
    res = conn.execute(query)
    return res.fetchall()

def getItem(param):
    try:
        param = int(param)
    except:
        pass
    if type(param) == int:
        fields = ['id', 'price']
    elif type(param) == str:
        fields = ['name']
    else:
        print(type(param))
    
    for f in fields:
        query = select(items).where(items.c[f] == param)
        try:
            res = conn.execute(query)
            return res.fetchall()
        except:
            pass
    