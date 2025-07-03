from fastapi import Request
from fastapi.responses import JSONResponse

async def error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Ugh... something broke, but honestly, who cares?",
            "detail": str(exc),
            "status": "Fix it yourself. I’m too lazy ..."
        }
    )