from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    query: str
    temperature: Optional[float] = 0.7  
    max_tokens: Optional[int] = 1024     


class ChatResponse(BaseModel):
    answer: str