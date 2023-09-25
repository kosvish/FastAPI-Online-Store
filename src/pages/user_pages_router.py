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
    tags=["Pages"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

templates = Jinja2Templates(directory="src/templates")

current_user = fastapi_users.current_user()


@router.get('/base')
def get_base_page(request: Request, products: Product = Depends(get_all_products)):
    return templates.TemplateResponse("base.html", {"request": request, "products": products})


@router.get("/user_profile")
def get_user_page(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("user_profile.html", {"request": request, "user": user})


@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("user_login.html", {"request": request})


@router.get("/register")
def get_register_page(request: Request):
    return templates.TemplateResponse("user_register.html", {"request": request})


@router.get("/product/{product_id}")
def get_product_page(request: Request, product: Product = Depends(get_current_product)):
    return templates.TemplateResponse("product.html", {"request": request, "product": product})


@router.get("/product/add_product")
def get_add_product_page(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("add_product_form.html", {"request": request})