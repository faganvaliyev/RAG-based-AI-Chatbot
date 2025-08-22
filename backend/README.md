

---


## ⚡ Features


- **RAG Pipeline**: Integrates user queries with a vector-based knowledge base for contextual answers.
- **Streaming Responses**: Supports real-time streaming of LLM outputs to frontend clients.
- **Modular API**: FastAPI backend with versioned endpoints (`/api/v1`) for scalability.
- **Vector Store Integration**: FAISS-based vector store for fast similarity search.
- **Extensible LLM Services**: Easy to add new LLM providers or models.
- **Dockerized**: Ready for containerized deployment.


---


## 🚀 Getting Started


### 1. Clone the repository
   bash
git clone https://github.com/faganvaliyev/RAG-based-AI-Chatbot
cd rag-ai-chatbot/backend

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

### 3. Install dependencies
pip install -r requirements.txt
# or if using poetry/pyproject.toml
poetry install

### 4. Run the backend
uvicorn app.main:app --reload








