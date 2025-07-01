from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.note import Note
from schemas.note import NoteCreateSchema


class NoteRepository:
    
    async def create_note(self, db: AsyncSession, note: NoteCreateSchema):
        note = Note(
            label=note.label,
            description=note.description
        )
        db.add(note)
        await db.commit()
        await db.refresh(note)
        return note

    async def get_note_by_id(self, db: AsyncSession, note_id: int):
        data = await db.execute(select(Note).where(Note.id==note_id))
        return data.scalars().first()

    async def get_all(self, db: AsyncSession):
        data = await db.execute(select(Note))
        return data.scalars().all()

    async def update(self, db: AsyncSession, note_id: int, note_data: NoteCreateSchema):
        note = await self.get_note_by_id(db=db, note_id=note_id)
        if not note:
            return None
        
        note.label = note_data.label
        note.description = note_data.description
        await db.commit()
        await db.refresh(note)
        return note

    async def delete(self, db: AsyncSession, note_id: int) -> bool:
        note = await self.get_note_by_id(db=db, note_id=note_id)
        if not note:
            return False
        
        await db.delete(note)
        await db.commit()
        return True