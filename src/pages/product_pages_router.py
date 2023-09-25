from fastapi import APIRouter, Request, Depends
from src.models.user import User
from src.endpoints.product import get_current_product
from src.models.product import Product
from .user_pages_router import templates, current_user

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.get("/{product_id}")
def get_product_page(request: Request, product: Product = Depends(get_current_product)):
    return templates.TemplateResponse("product.html", {"request": request, "product": product})



