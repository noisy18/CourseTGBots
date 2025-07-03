from pydantic import BaseModel
from app.core.schemas.base import BaseSchema
from app.core.schemas.uuid import UUIDSchema

class NoteCreateSchema(BaseModel):
    label: str
    description: str

class NoteResponseSchema(BaseSchema, UUIDSchema):
    id: int
    label: str
    description: str

    class Config:
        from_attributes = True