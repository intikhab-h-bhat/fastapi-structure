from app.db.crud import save_chat_message
from app.models.schemas import ChatResponse
import uuid

async def process_message(message: str) -> ChatResponse:
    # Mock LLM call (replace with actual API call)
    llm_response = f"Processed: {message}"
    
    # Save to DB
    message_id = str(uuid.uuid4())
    await save_chat_message({
        "message_id": message_id,
        "input": message,
        "output": llm_response
    })
    
    return ChatResponse(response=llm_response, message_id=message_id)