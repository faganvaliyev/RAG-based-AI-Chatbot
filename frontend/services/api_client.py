import requests

API_URL = "http://localhost:8001/api/v1/chat"

def chat_api(query: str, temperature: float = 0.7, max_tokens: int = 1024) -> str:
    payload = {
        "query": query,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()["answer"]
