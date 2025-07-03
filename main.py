from fastapi import FastAPI,Request
from api.routes_root import router as root_router
from api.routes_excuses import router as excuse_router
from fastapi.responses import JSONResponse
from utils.errors import error_handler

app = FastAPI(
    title="Too Lazy as a Service 🦥",
    description="API for procrastination and excuse generation 💤",
    version="0.02"
)

app.add_exception_handler(Exception, error_handler)

app.include_router(root_router)
app.include_router(excuse_router)