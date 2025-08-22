from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import routes

app = FastAPI(title="RAG AI Chatbot Backend (LLM-only)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.get("/")
async def root():
    return {"message": "RAG AI Chatbot Backend is running"}

