from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi_users import FastAPIUsers
from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.models.user import User
from src.endpoints.product import get_all_products, get_current_product
from src.models.product import Product
from src.endpoints.user import view_user_profile
from src.endpoints.product import get_user_product
router = APIRouter(
    prefix="/user",
    tags=["User_pages"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

templates = Jinja2Templates(directory="src/templates")

current_user = fastapi_users.current_user()



@router.get("/profile")
def get_user_page(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("user_profile.html", {"request": request, "user": user})


@router.get("/login")
def get_login_page(request: Request):
    return templates.TemplateResponse("user_login.html", {"request": request})


@router.get("/register")
def get_register_page(request: Request):
    return templates.TemplateResponse("user_register.html", {"request": request})


@router.get("/{username}")
def get_users_profile(request: Request, user: User = Depends(view_user_profile),
                      product: Product = Depends(get_user_product)):
    return templates.TemplateResponse("strange_user_profile.html", {"request": request, "user": user,
                                                                    "user_products": product})
