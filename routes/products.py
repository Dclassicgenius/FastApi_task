
from typing import List, Optional
from fastapi import APIRouter,Body
from fastapi.param_functions import Query
from models import models
from repositories import products
from schemas import schemas

router = APIRouter(
    prefix="/products",
    tags=['Products']
)

@router.post('/', response_description="Add new product", response_model=models.ProductModel)
def create(product: models.ProductModel = Body(...)):
    return products.create(product)

@router.get(
    "/", response_description="List all products", response_model=List[models.ProductModel])
def list_products(brand: Optional[str]=Query(None), name: Optional[str]= Query(None)):
    return products.list_products(brand, name)
    

@router.get(
    "/{id}", response_description="Get a single product", response_model=schemas.Product)
def show_product(id: str):
    return products.show_product(id)

@router.put("/{id}", response_description="Update a product", response_model=models.ProductModel)
def update_product(id: str, product: models.UpdateProductModel = Body(...)):
    return products.update_product(id, product)

@router.delete("/{id}", response_description="Delete a Product")
def delete_product(id: str):
    return products.delete_product(id)