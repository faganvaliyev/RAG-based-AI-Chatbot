

---


## ⚡ Features


- **RAG Pipeline**: Integrates user queries with a vector-based knowledge base for contextual answers.
- **Streaming Responses**: Supports real-time streaming of LLM outputs to frontend clients.
- **Modular API**: FastAPI backend with versioned endpoints (`/api/v1`) for scalability.
- **Vector Store Integration**: FAISS-based vector store for fast similarity search.
- **Extensible LLM Services**: Easy to add new LLM providers or models.
- **Dockerized**: Ready for containerized deployment.


---
## 🏗️ Project Structure

### Application Structure

```
backend/
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── api/v1/routes.py # API routes for chat
│ ├── services/
│ │ ├── llm.py # LLM wrappers & streaming
│ │ └── retrieval.py # Knowledge retrieval logic
│ ├── models/schema.py # Pydantic request/response models
│ ├── db/vector_store.py # Vector store (FAISS) management
│ └── config.py # API keys, model options, etc.
├── Dockerfile # Docker image
└── pyproject.toml # Python dependencies

```

### Project Dependencies

Dependencies are managed using **UV** for faster, more reliable installations:

```toml
# pyproject.toml
[project]
dependencies = [
    "boto3>=1.40.13",
    "dotenv>=0.9.9",
    "fastapi>=0.116.1",
    "python-dotenv>=1.1.1",
    "requests>=2.32.5",
    "uvicorn>=0.35.0",
]

```

## 🚀 Getting Started


### 1. Clone the repository
   
##### git clone https://github.com/faganvaliyev/RAG-based-AI-Chatbot
##### cd rag-ai-chatbot/backend
---
### 2. Create virtual environment
##### python -m venv venv
##### source venv/bin/activate       Linux / macOS
##### venv\Scripts\activate          Windows
---
### 3. Install dependencies
##### pip install -r requirements.txt
##### or if using poetry/pyproject.toml
##### poetry install
---
### 4. Run the backend
##### uvicorn app.main:app --reload








