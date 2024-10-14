from fastapi import FastAPI as api
from fastapi.params import Body
from pydantic import BaseModel as Model
from typing import Optional

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

@app.get('/')
def index():
    return {"message": "WELCOME"}

@app.post('/create')
def post(payload: dict = Body()):
    return {"message": payload}

@app.post('/items')
def items_post(new_item: Item):
    return {'data': new_item}

@app.get('/items/{id}')
def item_get(id:int):
    print(id)
    return {'id': None}