import json
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

chat_history = []

def build_prompt(prompt: str, temperature: float = 0.7, max_tokens: int = 1024) -> dict:
    system_prompt = "You are a helpful assistant."
    messages = chat_history.copy()
    messages.append({"role": "user", "content": prompt})
    return {
        "anthropic_version": "bedrock-2023-05-31",
        "system": system_prompt,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

def generate_llm_response(query: str, temperature: float = 0.7, max_tokens: int = 1024) -> str:
    """
    Synchronous LLM call. Returns full assistant response in one go.
    """
    prompt_payload = build_prompt(query, temperature=temperature, max_tokens=max_tokens)

    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(prompt_payload),
        contentType="application/json",
        accept="application/json",
    )

    result = response["body"].read().decode("utf-8")
    data = json.loads(result)

    assistant_reply = "".join(
        block.get("text", "") for block in data.get("content", []) if block.get("type") == "text"
    )

    chat_history.append({"role": "user", "content": query})
    chat_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply