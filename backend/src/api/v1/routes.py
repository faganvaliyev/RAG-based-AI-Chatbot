from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.models.schema import ChatRequest, ChatResponse
from src.services.llm import generate_llm_response

router = APIRouter(prefix="/api/v1")

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        answer = generate_llm_response(
            query=request.query,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        return ChatResponse(answer=answer)
    except Exception as e:
        # Log the error
        print("Backend error:", e)
        return JSONResponse(status_code=500, content={"error": str(e)})