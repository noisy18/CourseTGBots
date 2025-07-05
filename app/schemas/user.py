from pydantic import EmailStr, BaseModel
from app.schemas.base import BaseSchema

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str

class UserResponseSchema(BaseSchema):
    email: EmailStr

    class Config:
        from_attributes = True
