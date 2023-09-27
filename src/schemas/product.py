from pydantic import BaseModel
from typing import Optional, Annotated
from fastapi import UploadFile, File, Form


class ProductCreate(BaseModel):
    name: Annotated[str, Form()]
    description: Annotated[str, Form()]
    category: Annotated[str, Form()]
    price: Annotated[float, Form()]
    brand: Annotated[str, Form()]

