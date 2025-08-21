import requests

API_URL = "http://localhost:8000/api/v1/chat/stream"

def stream_chat_api(query: str):
    """
    Generator that yields tokens from the streaming FastAPI endpoint
    """
    with requests.post(API_URL, json={"query": query}, stream=True) as response:
        for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
            if chunk:
                yield chunk


    





