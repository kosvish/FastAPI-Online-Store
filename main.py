from fastapi import FastAPI
from src.auth.base_config import auth_backend, fastapi_users
from src.schemas.user import UserRead, UserCreate
from src.pages.router import router as pages_router
from src.endpoints.auth_status import router as auth_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Online Store"
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(fastapi_users.get_auth_router(auth_backend),
                   prefix="/auth",
                   tags=["Auth"]
                   )

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(pages_router)
