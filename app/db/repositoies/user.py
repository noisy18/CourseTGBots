from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreateSchema
from app.db.repositoies.base_repository import BaseRepository

class UserRepository(BaseRepository[User]):
    model = User

    def __init__(self, session: AsyncSession):
        super().init(session)

    async def create_user(self, user: UserCreateSchema) -> User:
        return await self.create(
            email=user.email,
            password=user.password,
            returning=True
        )
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        users = await self.filter_by(email=email)
        return users[0] if users else None

    async def get_user_by_id(self, user_id: int, with_related: bool = False) -> Optional[User]:
        return await self.get_by_id(id_=user_id, with_related=with_related)