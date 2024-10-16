from os import path as p
import aiofiles
import json

path = "data.json"
# check the path
def is_path(path:str=path):
    return p.exists(path) and p.isfile(path)
# create and write/overwrite file
async def write_json(data:list=[], path:str=path) -> str:
    async with aiofiles.open(path, 'w') as file:
        await json.dumps(data, file, indent=2)
# read file -> list
def read_json(path:str=path) -> list:
    if(not is_path(path)):
        write_json()
    with open(path) as file:
        data = json.loads(file.read())
    return data