from fastapi import APIRouter, Depends, HTTPException
from src.database import AsyncSession, get_async_session
from src.models.user import User
from sqlalchemy import select

router = APIRouter()


async def view_user_profile(username: str, db: AsyncSession = Depends(get_async_session)):
    async with db as session:
        async with session.begin():
            query = select(User).where(User.username == username)
            result = await session.execute(query)
            user = result.scalar()
            if not user:
                raise HTTPException(status_code=404,
                                    detail="Пользователь с таким именем не найден или его уже не существует")

            return user


