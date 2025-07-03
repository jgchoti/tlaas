from fastapi import FastAPI
from api.routes_root import router as root_router
from api.routes_excuses import router as excuse_router

app = FastAPI(
    title="Too Lazy as a Service",
    description="The ultimate API for procrastination and excuse generation",
    version="0.02"
)

app.include_router(root_router)
app.include_router(excuse_router)