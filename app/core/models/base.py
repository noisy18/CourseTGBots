from sqlalchemy import Boolean, DateTime, func, Column
from app.db.base import Base
from app.settings import get_current_time


class BaseModel(Base):
    __abstract__ = True

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=get_current_time)
    updated_at = Column(DateTime(timezone=True), onupdate=get_current_time)
