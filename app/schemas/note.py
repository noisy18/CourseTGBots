from pydantic import BaseModel
from app.schemas.base import BaseSchema

class NoteCreateSchema(BaseModel):
    label: str
    description: str

class NoteResponseSchema(BaseSchema):
    label: str
    description: str

    class Config:
        from_attributes = True