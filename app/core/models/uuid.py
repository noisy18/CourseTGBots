import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from db.base import Base


class UUIDModel(Base):
    __abstract__ = True

    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, index=True, nullable=False)