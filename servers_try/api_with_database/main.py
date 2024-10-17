from fastapi import FastAPI as api
from fastapi.params import Body
from pydantic import BaseModel as Model
from typing import Optional
import psycopg as psy

# <NAME_OF_API>
app = api()
# inherit BaseModel
class Item(Model):
    name: str
    price: float
    # Set as default
    on_sell: bool = False
    # Set attributes as Optional whether string or none
    description: Optional[str] = None

try:
    conn = psy.connect(conninfo='host=localhost password=open87855522  dbname=fastapi_python user=postgres port=5432')
    cur = conn.cursor()
    # cur.execute("""CREATE TABLE items(
    #     id serial,
    #     price numeric NOT NULL,
    #     on_sell boolean DEFAULT False,
    #     name character varying NOT NULL,
    #     description character varying NOT NULL,
    #     create_at time with time zone NOT NULL DEFAULT now(),
    #     PRIMARY KEY (id)
    #     )""")
    # conn.commit()
    # print("database: ", "table created")
    
except Exception as error:
    print('Error: ',error)
        

@app.get('/')
def index():
    return {"message": "WELCOME"}

@app.post('/create')
def post(payload: dict = Body()):
    # cur.execute("""INSERT INTO items(
	# id, price, on_sell, name, description, create_at)
	# VALUES (?, ?, ?, ?, ?, ?)""", ())
    return {"message": payload}

@app.post('/items')
async def items_post(new_item: Item):
    # data.append(new_item)
    # await ba.write_json(data)
    return {'data': new_item}

@app.get('/items')
def items_get():
    cur.execute("""select * from items""")
    items = cur.fetchall()
    print(type(items))
    return {"items": items}


