from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.models.user import User
from fastapi import Depends

router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

current_user = fastapi_users.current_user()


@router.get("/status")
def protected_route(user: User = Depends(current_user)):
    return f'Hello, {user.username}'
