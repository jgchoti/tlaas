from fastapi import FastAPI,Request
from api.routes_root import router as root_router
from api.routes_excuses import router as excuse_router
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Too Lazy as a Service",
    description="The ultimate API for procrastination and excuse generation",
    version="0.02"
)


@app.exception_handler(Exception)
async def error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Ugh... something broke, but honestly, who cares?",
            "detail": str(exc),
            "status": "Fix it yourself. I’m too lazy ..."
        }
    )
    
app.include_router(root_router)
app.include_router(excuse_router)