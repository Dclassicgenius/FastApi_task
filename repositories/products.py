
from fastapi import Body, HTTPException, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from models import models
from config import database


def create(product: models.ProductModel= Body(...)):
    product = jsonable_encoder(product)
    new_product =  database.db["products"].insert_one(product)
    created_product= database.db["products"].find_one({"_id": new_product.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_product)

def list_products(brand: Optional[str]= Query(None), name: Optional[str]=Query(None)):
    
    if brand:
        return list(database.db["products"].find({"brand": brand}))
    if name:
        return list(database.db["products"].find({"name": name}))
    if name and brand:
        return list(database.db["products"].find({"brand": brand, "name": name}))
    else:
        items = list(database.db["products"].find({}))
    return items


def show_product(id: str):
    if (product := database.db["products"].find_one({"_id": id})) is not None:
        return product

    raise HTTPException(status_code=404, detail=f"Product {id} not found")


def update_product(id: str, product: models.UpdateProductModel = Body(...)):
    product = {i: j for i, j in product.dict().items() if j is not None}

    if len(product) >= 1:
        update_result = database.db["products"].update_one({"_id": id}, {"$set": product})

        if update_result.modified_count == 1:
            if (
                updated_product := database.db["products"].find_one({"_id": id})
            ) is not None:
                return updated_product

    if (existing_product := database.db["products"].find_one({"_id": id})) is not None:
        return existing_product

    raise HTTPException(status_code=404, detail=f"Product {id} not found")


def delete_product(id: str):
    delete_result = database.db["products"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return "done"
        
    raise HTTPException(status_code=404, detail=f"Product {id} not found")