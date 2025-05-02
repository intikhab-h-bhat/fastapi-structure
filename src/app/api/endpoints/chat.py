from fastapi import APIRouter, Depends
from app.services.llm_service import process_message
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    return await process_message(request.message)