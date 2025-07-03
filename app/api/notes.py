from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict

from app.db.dependencies import get_db
from app.utils.docs.tags import NOTES
from app.schemas.note import NoteCreateSchema, NoteResponseSchema
from app.db.repositoies.note import NoteRepository

router = APIRouter(
    prefix="/notes",
    tags=[NOTES]
)

repo = NoteRepository()

@router.post("", summary="Create new note", response_model=NoteResponseSchema)
async def post(data: NoteCreateSchema, db: AsyncSession = Depends(get_db)):
    try:
        note = await repo.create_note(db=db, note=data)
        return note
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("", summary="Get all notes", response_model=List[NoteResponseSchema])
async def get_all(db: AsyncSession = Depends(get_db)):
    return await repo.get_all(db=db)

@router.get("/{note_id}", summary="Get note by ID", response_model=NoteResponseSchema)
async def get_by_id(note_id: int, db: AsyncSession = Depends(get_db)):
    note = await repo.get_note_by_id(db=db, note_id=note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.put("/{note_id}", summary="Update note")
async def put(note_id: int, data: NoteCreateSchema, db: AsyncSession = Depends(get_db)):
    note = await repo.update(db=db, note_id=note_id, note_data=data)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.delete("/{note_id}", summary="Delete note")
async def delete(note_id: int, db: AsyncSession = Depends(get_db)):
    note = await repo.delete(db=db, note_id=note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")