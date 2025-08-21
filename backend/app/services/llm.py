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

def build_prompt(prompt: str) -> dict:
    """
    Build the request payload in the format expected by Anthropic Claude on Bedrock.
    """
    system_prompt = "You are a helpful assistant."
    messages = [
        {"role": "user", "content": prompt}
    ]
    return {
        "system": system_prompt,
        "messages": messages,
         "max_tokens": 1024,
         "temperature": 0.7,
    }

async def generate_llm_response(query: str):
    prompt_payload = build_prompt(query)

    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(prompt_payload),
        contentType="application/json",
        accept="application/json",
    )

    # Read and decode the response body
    result = response["body"].read().decode("utf-8")
    data = json.loads(result)

    # Extract assistant reply text
    assistant_reply = data.get("choices", [{}])[0].get("message", {}).get("content", "")

    # Stream response character by character asynchronously
    for char in assistant_reply:
        await asyncio.sleep(0)
        yield char
