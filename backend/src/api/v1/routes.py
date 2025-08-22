from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from src.services.llm import generate_llm_response
from src.models.schema import ChatRequest

router = APIRouter(prefix="/api/v1")

@router.post("/chat/stream")
async def chat_stream_endpoint(request: ChatRequest):
    """
    Stream LLM response as Server-Sent Events (SSE).
    """

    async def event_generator():
        async for token in generate_llm_response(
            query=request.query,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        ):
            yield token.encode("utf-8")

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache"}
    )