import requests

API_URL = "http://backend_new:8001/api/v1/chat/stream"

def stream_chat_api(query: str, temperature: float = 0.7, max_tokens: int = 1024):
    """
    Generator to yield streamed tokens from the FastAPI SSE endpoint.
    """
    payload = {
        "query": query,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    with requests.post(API_URL, json=payload, stream=True) as response:
        response.raise_for_status()
        # Use iter_lines for SSE
        for line in response.iter_lines(decode_unicode=True):
            if line:
                # Remove SSE prefix "data: "
                yield line.replace("data: ", "")