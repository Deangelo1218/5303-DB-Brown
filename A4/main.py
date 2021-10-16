# main.py

from typing import Optional
from fastapi import FastAPI
import json 
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float 

@app.post("/items")
async def create_item(item: Item):
    return Item
