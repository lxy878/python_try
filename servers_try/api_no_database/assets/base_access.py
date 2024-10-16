from os import path as p
import os
import json

path = "data.json"
# check the path
def is_path(path:str=path):
    return p.exists(path) and p.isfile(path)
# create and write/overwrite file
def write_json(data:list=[], path:str=path) -> str:
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)
    print("file write done")
# read file -> list
def read_json(path:str=path) -> list:
    if(not is_path(path)):
        write_json()
    with open(path) as file:
        data = json.loads(file.read())
    return data