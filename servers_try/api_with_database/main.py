from fastapi import FastAPI as api, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel as Model
from typing import Optional
import psycopg as psy
from psycopg.rows import dict_row

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
    # set up retrieved data as dict
    cur = conn.cursor(row_factory=dict_row)
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
        

@app.get('/', status_code=status.HTTP_200_OK)
def index():
    return {"message": "WELCOME"}

@app.post('/items', status_code=status.HTTP_201_CREATED)
async def items_post(new_item: Item):
    cur.execute("""INSERT INTO items (price, on_sell, name, description)
                VALUES(%s, %s, %s, %s)""", 
                (new_item.price, new_item.on_sell, new_item.name, new_item.description))
    conn.commit()
    return {'data': new_item}

@app.get('/items', status_code=status.HTTP_200_OK)
def items_get():
    cur.execute("""select * from items""")
    items = cur.fetchall()
    return {"items": items}

@app.get('/items/{id}')
def item_get(id:int):
    cur.execute("""SELECT * FROM items where id=%s""", [id])
    item = cur.fetchone()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'{id} was not found')
    return {"item": item}

@app.put('/items/{id}', status_code=status.HTTP_200_OK)
def item_update(id:int, new_item: Item):
    cur.execute("""UPDATE items SET price=%s, on_sell=%s, name=%s, description=%s WHERE id=%s""", 
                (new_item.price, new_item.on_sell, new_item.name, new_item.description, f'{id}'))
    conn.commit()
    return {"item": new_item}

@app.delete('/items/{id}', status_code=status.HTTP_200_OK)
def item_delete(id:int):
    cur.execute("""DELETE FROM items WHERE id=%s""", [id])
    conn.commit()
    return {"message": "Remove"}
