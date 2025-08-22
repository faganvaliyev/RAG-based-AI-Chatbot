import asyncio
import json
import boto3
from botocore.config import Config
from app.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, BEDROCK_REGION


# Initialize Bedrock runtime client
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=BEDROCK_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    config=Config(retries={"max_attempts": 10}),
)


MODEL_ID = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"


# In-memory chat history per session (can later be replaced by per-user storage)
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
        "anthropic_version": "bedrock-2023-05-31",  # Required field
        "system": system_prompt,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }


async def generate_llm_response(query: str, temperature: float = 0.7, max_tokens: int = 1024):
    """
    Async generator that yields assistant tokens for streaming and saves chat context.
    """
    prompt_payload = build_prompt(query, temperature=temperature, max_tokens=max_tokens)


    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(prompt_payload),
        contentType="application/json",
        accept="application/json",
    )


    # Decode the response
    result = response["body"].read().decode("utf-8")
    data = json.loads(result)


    # Extract assistant reply text
    assistant_reply = ""
    for block in data.get("content", []):
        if block.get("type") == "text":
            assistant_reply += block.get("text", "")


    # Save both user query and assistant reply to chat history
    chat_history.append({"role": "user", "content": query})
    chat_history.append({"role": "assistant", "content": assistant_reply})

    chunk_size = 10  
    for i in range(0, len(assistant_reply), chunk_size):
        await asyncio.sleep(0)  
        yield assistant_reply[i:i+chunk_size]
