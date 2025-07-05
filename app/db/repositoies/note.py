from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.note import Note
from app.schemas.note import NoteCreateSchema
from app.db.repositoies.base_repository import BaseRepository


class NoteRepository(BaseRepository[Note]):
    model = Note

    def __init__(self, session: AsyncSession):
        super().init(session)
    
    async def create_note(self, note: NoteCreateSchema) -> Note:
        return await self.create(
            label=note.label,
            description=note.description,
            returning=True
        )
    
    async def get_notes_by_label(self, label: str) -> List[Note]:
        return await self.filter_by(label=label)


    async def get_note_by_id(self, note_id: int, with_related: bool = False) -> Optional[Note]:
        return await self.get_by_id(id_=note_id, with_related=with_related)


    async def get_all(self) -> List[Note]:
        return await super().get_all()

    
    async def update_note(self, note_id: int, note_data: NoteCreateSchema) -> Optional[Note]:
        return await self.update_by_id(
            id_=note_id,
            label=note_data.label,
            description=note_data.description,
            returning=True
        )

    async def delete_note(self, note_id: int) -> bool:
        await self.delete_by_id(id_=note_id)
        return True