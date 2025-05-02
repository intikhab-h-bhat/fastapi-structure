from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    message_id: str