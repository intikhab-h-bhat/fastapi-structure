# app/services/database_service.py
from typing import Optional, List
from app.models.database_models import ChatMessage, PyObjectId
from app.db.crud import get_database
from datetime import datetime

class DatabaseService:
    def __init__(self):
        self.db = get_database()
        self.chat_collection = self.db["chat_history"]

    async def save_message(self, message: ChatMessage) -> ChatMessage:
        """Save chat message to database"""
        message_dict = message.dict(by_alias=True, exclude_none=True)
        result = await self.chat_collection.insert_one(message_dict)
        return await self.get_message(result.inserted_id)

    async def get_message(self, message_id: PyObjectId) -> Optional[ChatMessage]:
        """Retrieve single message by ID"""
        if (doc := await self.chat_collection.find_one({"_id": message_id})) is not None:
            return ChatMessage(**doc)
        return None

    async def get_user_messages(
        self, 
        user_id: str, 
        limit: int = 100,
        start_date: Optional[datetime] = None
    ) -> List[ChatMessage]:
        """Get all messages for a user with optional filters"""
        query = {"user_id": user_id}
        if start_date:
            query["created_at"] = {"$gte": start_date}
        
        cursor = self.chat_collection.find(query).sort("created_at", -1).limit(limit)
        return [ChatMessage(**doc) async for doc in cursor]

    async def delete_user_messages(self, user_id: str) -> int:
        """Delete all messages for a user"""
        result = await self.chat_collection.delete_many({"user_id": user_id})
        return result.deleted_count