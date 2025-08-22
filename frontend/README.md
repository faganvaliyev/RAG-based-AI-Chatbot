# RAG AI Chatbot Frontend

This is the **frontend** for the RAG AI Chatbot, built with **Streamlit**.  
It provides a user interface to chat with the LLM, upload files for RAG context, manage chat history, and stream responses in real-time.

---

## Features

- **Chat UI**: Real-time chat interface with user and assistant messages.
- **Streaming Responses**: Displays LLM output token-by-token.
- **RAG Integration**: Uses uploaded files and backend S3 knowledge base for context.
- **Chat History**: Create, switch, and delete multiple chat sessions.
- **File Uploads**: Supports TXT, PDF, CSV, and DOCX files.

---

## 🏗️ Project Structure

### Application Structure

```
frontend/
├── app.py # Main Streamlit app
├── services/
│ ├── chat_service.py # Chat history, create/delete chats, session management
│ └── api_client.py # API client for streaming chat responses
├── Dockerfile # Docker image for frontend
└── pyproject.toml # Python dependencies

```

### Project Dependencies

Dependencies are managed using **UV** for faster, more reliable installations:

```toml
# pyproject.toml
[project]
dependencies = [
    "pypdf2>=3.0.1",
    "python-docx>=1.2.0",
    "streamlit>=1.48.1",
]
```

## 🚀 Getting Started

### 1. Clone the repository

##### git clone https://github.com/faganvaliyev/RAG-based-AI-Chatbot
##### cd rag-ai-chatbot/frontend

---
### 2. Create virtual environment
##### python -m venv venv
##### source venv/bin/activate       Linux / macOS
##### venv\Scripts\activate          Windows
---
### 3. Install dependencies
---
### 4. Run the frontend
##### uvicorn app.main:app --reload





