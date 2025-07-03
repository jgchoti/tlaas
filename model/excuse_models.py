from pydantic import BaseModel
from typing import Optional

class ExcuseResponse(BaseModel):
    excuse: str
    category: str
    api_status: Optional[str] = "too tired to function properly."

class CustomExcuseRequest(BaseModel):
    task: str

class CustomExcuseResponse(BaseModel):
    excuse: str
    topic: str
    believability: str = "Varies by audience"
        