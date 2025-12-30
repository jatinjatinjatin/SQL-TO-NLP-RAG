🧠 NLP → SQL Agent with Schema RAG, Streaming & Evaluation

An end-to-end LLM-powered NLP-to-SQL system that converts natural language questions into executable SQL using schema-aware Retrieval-Augmented Generation (RAG), validates queries through execution, streams responses, and provides automatic evaluation with confidence scoring and dashboards.

✨ Key Features
- 🔤 Natural Language → SQL using LLMs (Ollama / LLaMA)
- 🧩 Schema-Aware RAG to ground SQL generation in database structure
- ⚙️ Automatic SQL Execution & Healing (validate, execute, and iterate)
- 🔁 Streaming SQL & Results (real-time feedback)
- 📊 Confidence Score per Answer and evaluation dashboards
- ... (extendable with monitoring, logging, and additional LLM backends)

Getting started
1) Install dependencies:
   pip install fastapi uvicorn streamlit langchain langchain-community langgraph faiss-cpu ollama

2) Run Ollama and pull model (if using Ollama):
   ollama serve
   ollama pull llama3

3) Initialize the database:
   python backend/db_setup.py

4) Start the backend:
   uvicorn backend.app:app --reload

5) Start the frontend:
   streamlit run frontend/app.py

Notes
- Configure your Ollama/LLaMA endpoint and database credentials in the repo config/environment variables before running.
- The system uses schema-aware retrieval to reduce hallucinations and provides automatic evaluation/metrics to track performance.
