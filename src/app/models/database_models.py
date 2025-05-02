# app/models/database_models.py
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return str(v)

class ChatMessage(BaseModel):
    """
    MongoDB Document Model for Chat Messages
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: str
    message: str
    llm_response: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: dict = Field(default_factory=dict)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            PyObjectId: str
        }
        arbitrary_types_allowed = True