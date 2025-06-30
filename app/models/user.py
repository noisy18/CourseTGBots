from sqlalchemy import Column, Integer, String, Boolean
from core.models.base import BaseModel
from core.models.uuid import UUIDModel

class User(BaseModel, UUIDModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
