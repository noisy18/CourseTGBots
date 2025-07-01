from sqlalchemy import Column, Integer, String
from core.models.base import BaseModel
from core.models.uuid import UUIDModel

class Note(BaseModel, UUIDModel):
    __tablename__ = "Notes"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, nullable=False)
    description = Column(String, nullable=False)