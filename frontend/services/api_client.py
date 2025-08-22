import requests


API_URL = "http://backend:8000/api/v1/chat/stream"


def stream_chat_api(query: str, temperature: float = 0.7, max_tokens: int = 1024):
    """
    Generator that yields tokens from the streaming FastAPI endpoint.
    Accepts query, temperature, and max_tokens.
    """
    payload = {
        "query": query,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


    with requests.post(API_URL, json=payload, stream=True) as response:
        response.raise_for_status()  # Ensure errors are caught
        for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
            if chunk:
                yield chunk