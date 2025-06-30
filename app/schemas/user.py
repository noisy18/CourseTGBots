from pydantic import EmailStr, BaseModel
from core.schemas.base import BaseSchema
from core.schemas.uuid import UUIDSchema

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str

class UserResponseSchema(BaseSchema, UUIDSchema):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
