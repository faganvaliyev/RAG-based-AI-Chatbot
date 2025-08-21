from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.llm import generate_llm_response
from app.models.schema import ChatRequest

router = APIRouter(prefix="/api/v1")

@router.post("/chat/stream")
async def chat_stream_endpoint(request: ChatRequest):
    """
    Stream LLM response character-by-character.
    """

    async def event_generator():
        # No need to await, because generate_llm_response is now an async generator
        async for token in generate_llm_response(request.query):
            yield token.encode("utf-8")

    return StreamingResponse(event_generator(), media_type="text/plain")
