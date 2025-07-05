from functools import cached_property
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositoies.note import NoteRepository
from app.db.repositoies.user import UserRepository

class DB:
    def __init__(self, session: AsyncSession):
        self.session = session

    @cached_property
    def notes(self) -> NoteRepository:
        return NoteRepository(self.session)
    
    @cached_property
    def users(self) -> UserRepository:
        return UserRepository(self.session)