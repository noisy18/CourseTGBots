from pydantic import BaseModel

class UUIDSchema(BaseModel):
    uuid: str