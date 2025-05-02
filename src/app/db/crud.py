from app.db.client import get_database

async def save_chat_message(message_data: dict):
    db = get_database()
    await db["chat_history"].insert_one(message_data)