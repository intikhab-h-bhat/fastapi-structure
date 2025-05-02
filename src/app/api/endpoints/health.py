from fastapi import APIRouter
from app.models.schemas import HealthCheck

router = APIRouter()

@router.get("/", response_model=HealthCheck)
async def health_check():
    return {"status": "OK"}