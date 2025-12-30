
PRE-COUNCIL NLP → SQL AGENT WITH GSAP + THREE.JS

RUN STEPS:

1) pip install fastapi uvicorn streamlit langchain langchain-community langgraph faiss-cpu ollama

2) ollama serve
   ollama pull llama3

3) python backend/db_setup.py

4) uvicorn backend.app:app --reload

5) streamlit run frontend/app.py

FEATURES:
- Animated GSAP UI
- Three.js Query DAG node
- NLP → SQL with LangGraph
- Self-healing SQL
