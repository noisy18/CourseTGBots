from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class BaseSchema(BaseModel):
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True