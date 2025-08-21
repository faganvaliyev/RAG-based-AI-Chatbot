from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from app.api.v1 import routes

app = FastAPI(title="RAG AI Chatbot Backend (LLM-only)")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your EC2 frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(routes.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "RAG AI Chatbot Backend is running"}

