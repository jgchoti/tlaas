from pydantic import BaseModel, Field
from typing import Optional

class ExcuseResponse(BaseModel):
    excuse: str
    category: str
    api_status: Optional[str] = Field(
        default="Successfully served your lazy excuse.",
        description="Status message from the API"
    )
class CustomExcuseRequest(BaseModel):
    task: str

class CustomExcuseResponse(BaseModel):
    excuse: str
    topic: str
    believability: str = Field(
        default="Varies by audience",
        description="How believable the excuse might be"
    )