from pydantic import BaseModel, field_serializer
from uuid import UUID

class UUIDSchema(BaseModel):
    uuid: UUID

    @field_serializer('uuid')
    def serialize_uuid(self, uuid: UUID, _info):
        """Конвертируем UUID в строку при сериализации"""
        return str(uuid)