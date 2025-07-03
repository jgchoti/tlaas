from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.get("/")
async def root():
    now = datetime.now(timezone.utc).isoformat()
    return {
        "message": "Welcome to Too Lazy as a Service! 🦥",
        "time": now,
        "status": "Actively avoiding productivity since ... (too lazy to remember)",
    }
