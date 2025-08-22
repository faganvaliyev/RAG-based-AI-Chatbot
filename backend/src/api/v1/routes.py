from fastapi import APIRouter
from src.models.schema import ChatRequest, ChatResponse
from src.services.llm import generate_llm_response

router = APIRouter(prefix="/api/v1")

@router.post("/chat")
def chat_endpoint(request: ChatRequest) -> ChatResponse:
    answer = generate_llm_response(
        query=request.query,
        temperature=request.temperature,
        max_tokens=request.max_tokens
    )
    return ChatResponse(answer=answer)
