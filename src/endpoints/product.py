from src.models.product import Product
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Request
from src.database import AsyncSession, get_async_session
from src.models.user import User
from src.auth.base_config import current_user
from sqlalchemy import select
from typing import Annotated

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


async def get_current_product(product_id: int, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        async with session.begin():
            stmt = select(Product).where(Product.id == product_id)
            result = await session.execute(stmt)
            product = result.scalar()
            if not product:
                raise HTTPException(status_code=404, detail="Product not found")
            return product


@router.post("/add_product")
async def add_product(
                      name: Annotated[str, Form()],
                      description: Annotated[str, Form()],
                      category: Annotated[str, Form()],
                      price: Annotated[float, Form()],
                      brand: Annotated[str, Form()], file: Annotated[UploadFile, File()] = None,
                      db: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_user),
                      ):

    image_path = file.filename
    with open(f"product_images/{image_path}", "wb") as image_file:
        image_file.write(file.file.read())
    async with db as session:
        db_product = Product(name=name, description=description, category=category, price=price, brand=brand,
                             username=user.username, image_path=image_path)
        session.add(db_product)
        await db.commit()
        await db.refresh(db_product)

    return db_product
