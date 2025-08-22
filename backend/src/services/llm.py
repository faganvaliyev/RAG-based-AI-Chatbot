import asyncio
import json
import functools
import boto3
from botocore.config import Config
from src.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, BEDROCK_REGION

# Initialize Bedrock runtime client
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=BEDROCK_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    config=Config(retries={"max_attempts": 10}),
)

MODEL_ID = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"

# In-memory chat history per session
chat_history = []

def build_prompt(prompt: str, temperature: float = 0.7, max_tokens: int = 1024) -> dict:
    """
    Build the request payload including previous chat messages.
    """
    system_prompt = "You are a helpful assistant."

    # Include previous messages
    messages = chat_history.copy()
    messages.append({"role": "user", "content": prompt})

    return {
        "anthropic_version": "bedrock-2023-05-31",
        "system": system_prompt,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

async def generate_llm_response(query: str, temperature: float = 0.7, max_tokens: int = 1024):
    """
    Async generator that yields assistant tokens as SSE (Server-Sent Events) and saves chat context.
    """
    yield "data: \n\n"
    prompt_payload = build_prompt(query, temperature=temperature, max_tokens=max_tokens)

    # Async-friendly Bedrock API call
    response = await asyncio.to_thread(
        functools.partial(
            bedrock_runtime.invoke_model,
            modelId=MODEL_ID,
            body=json.dumps(prompt_payload),
            contentType="application/json",
            accept="application/json",
        )
    )

    # Decode the response
    result = response["body"].read().decode("utf-8")
    data = json.loads(result)

    # Extract assistant reply
    assistant_reply = ""
    for block in data.get("content", []):
        if block.get("type") == "text":
            assistant_reply += block.get("text", "")

    # Save chat history
    chat_history.append({"role": "user", "content": query})
    chat_history.append({"role": "assistant", "content": assistant_reply})

    # Stream in chunks for SSE
    chunk_size = 256
    for i in range(0, len(assistant_reply), chunk_size):
        await asyncio.sleep(0)
        # SSE format: "data: <chunk>\n\n"
        yield f"data: {assistant_reply[i:i+chunk_size]}\n\n"



