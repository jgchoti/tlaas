from pydantic import BaseModel

class ExcuseResponse(BaseModel):
    excuse: str
    category: str

class CustomExcuseRequest(BaseModel):
    task: str

class CustomExcuseResponse(BaseModel):
    excuses: str
    topic: str
    believability: str = "Varies by audience"
        
        