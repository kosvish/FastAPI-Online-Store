from src.models.product import Product
from fastapi import APIRouter, Depends
from src.schemas.product import ProductCreate
from src.database import AsyncSession, get_async_session
from src.models.user import User
from src.auth.base_config import current_user
from sqlalchemy import select

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


async def get_all_products(db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        async with session.begin():
            stmt = select(Product)
            result = await session.execute(stmt)
            products = result.scalars().all()
            return products


@router.post("/add_product")
async def add_product(product: ProductCreate, db: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_user)):
    async with db as session:
        db_product = Product(**product.dict(), username=user.username)
        session.add(db_product)
        await db.commit()
        await db.refresh(db_product)
        return db_product
