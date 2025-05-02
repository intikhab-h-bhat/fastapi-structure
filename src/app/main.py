from fastapi import FastAPI
from app.api.endpoints import health, chat
from app.core.config import settings

app = FastAPI(title="LLM App")

# Include routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(chat.router, prefix="/api/endpoints", tags=["chat"])