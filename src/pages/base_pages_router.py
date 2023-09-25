from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi_users import FastAPIUsers
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.models.user import User
from src.endpoints.product import get_all_products, get_current_product
from src.models.product import Product

router = APIRouter(
    prefix="/pages",
    tags=["Base_pages"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

templates = Jinja2Templates(directory="src/templates")

current_user = fastapi_users.current_user()


@router.get('/main')
def get_base_page(request: Request, products: Product = Depends(get_all_products)):
    return templates.TemplateResponse("base.html", {"request": request, "products": products})


@router.get("/add_product")
def get_add_product_page(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("add_product_form.html", {"request": request})
