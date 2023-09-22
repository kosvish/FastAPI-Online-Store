from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    category: str
    price: float
    brand: str
