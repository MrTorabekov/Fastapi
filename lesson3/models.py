from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None




