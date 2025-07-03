from pydantic import EmailStr, BaseModel
from app.core.schemas.base import BaseSchema
from app.core.schemas.uuid import UUIDSchema

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str

class UserResponseSchema(BaseSchema, UUIDSchema):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
