
from pydantic import BaseModel


class Product(BaseModel):
    brand: str
    name: str 
    price: float
    description: str 
    parameters: dict 

