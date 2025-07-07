from fastapi import FastAPI,Request
from api.routes_root import router as root_router
from api.routes_excuses import router as excuse_router
from fastapi.responses import JSONResponse
from utils.errors import error_handler
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Too Lazy as a Service 🦥",
    description="API for procrastination and excuse generation 💤",
    version="0.02"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(Exception, error_handler)

app.include_router(root_router)
app.include_router(excuse_router)




