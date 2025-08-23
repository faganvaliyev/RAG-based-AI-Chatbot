# RAG AI Chatbot

This is a **Retrieval-Augmented Generation (RAG) AI Chatbot** that combines **large language models (LLMs)**
It allows users to chat in real-time, upload files for context.

---
## 💬  Demo 🎥

https://github.com/user-attachments/assets/e0be246c-3467-4616-b279-c4bb21d76988

---
## ⚡ Features

- **RAG Pipeline**: Combines user queries with vector-based knowledge for contextual answers.  
- **Streaming Responses**: LLM output is streamed token-by-token.  
- **Chat History**: Users can create, switch, and delete chat sessions.  
- **File Uploads**: Supports TXT, PDF, CSV, and DOCX files to augment context.  
- **Vector Store Integration**: FAISS-based vector store for fast similarity search.  
- **Dockerized**: Both frontend and backend can run in containers.  

---


## 🏗️ Project Structure

```
├── backend/
│ ├── src/ 
│ │ ├── api/v1/routes.py # API routes
│ │ ├── services/
│ │ │ ├── llm.py # LLM wrappers & streaming
│ │ │ └── retrieval.py # Knowledge retrieval logic
│ │ ├── models/schema.py # Request/response validation
│ │ ├── db/vector_store.py # Vector store (FAISS) management
│ │ └── config.py # API keys, model options, etc.
│ ├── app.py # FastAPI entrypoint
│ ├── Dockerfile
│ └── pyproject.toml
└── frontend/
├── app.py # Streamlit main app
├── services/
│ ├── chat_service.py # Chat session management
│ └── api_client.py # Backend API client
├── Dockerfile
└── pyproject.toml
