from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreateSchema

class UserRepository:
    async def get_user_by_id(self, db: AsyncSession, user_id: int):
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    async def get_user_by_email(self, db: AsyncSession, email: str):
        result = await db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create_user(self, db: AsyncSession, user: UserCreateSchema):
        user = User(
            email=user.email,
            password=user.password
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user