
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ProductModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    brand: str = Field(...)
    name: str = Field(...)
    price: float = Field(...)
    description: str = Field(...)
    parameters: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "brand": "Apple",
                "name": "phone",
                "price": 35000,
                "description": "Great phone",
                "parameters":{"memory":'256Gb', "RAM":'8GB' }

            }
        }


class UpdateProductModel(BaseModel):
    brand: Optional[str]
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
    parameters: Optional[dict]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "brand": "Apple",
                "name": "iphone x",
                "price": 35000,
                "description": "Great phone",
                "parameters":{"memory":'256Gb', "RAM":'8GB' }
            }
        }