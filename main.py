from fastapi import FastAPI
from src.auth.base_config import auth_backend, fastapi_users
from src.schemas.user import UserRead, UserCreate
from src.pages.user_pages_router import router as pages_router
from src.endpoints.auth_status import router as auth_router
from fastapi.staticfiles import StaticFiles
from src.endpoints.product import router as product_router
from src.pages.product_pages_router import router as pages_product_router
from src.pages.base_pages_router import router as pages_base_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Online Store"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.mount("/product_images", StaticFiles(directory="product_images"), name="product_images")

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

app.include_router(product_router)
app.include_router(pages_router)
app.include_router(pages_product_router)
app.include_router(pages_base_router)
