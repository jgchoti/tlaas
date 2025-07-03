from fastapi import APIRouter
from datetime import datetime, timezone
from utils.refuse import api_refuse

router = APIRouter()

@router.get("/")
async def root():
    api_refuse()
    now = datetime.now(timezone.utc).isoformat()
    return {
        "message": "Welcome to Too Lazy as a Service! 🦥",
        "time": now,
        "status": "Actively avoiding productivity since ... (too lazy to remember)",
    }
