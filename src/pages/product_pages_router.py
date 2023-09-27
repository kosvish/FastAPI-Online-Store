from fastapi import APIRouter, Request, Depends
from src.endpoints.product import get_current_product
from src.models.product import Product
from .user_pages_router import templates

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/{product_id}")
def get_product_page(request: Request, product: Product = Depends(get_current_product)):
    return templates.TemplateResponse("product.html", {"request": request, "product": product})

