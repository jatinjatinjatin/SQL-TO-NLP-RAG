🧠 NLP → SQL Agent with Schema RAG, Streaming & Evaluation

An end-to-end LLM-powered NLP-to-SQL system that converts natural language questions into executable SQL using schema-aware Retrieval-Augmented Generation (RAG), validates queries through execution, streams responses, and provides automatic evaluation with confidence scoring and dashboards.

✨ Key Features

🔤 Natural Language → SQL using LLMs (Ollama / LLaMA)

🧩 Schema-Aware RAG to ground SQL generation in database structure

⚙️ Automatic SQL Execution & Healing

🔁 Streaming SQL & Results (real-time feedback)

📊 Confidence Score per Answer

🧪 Automated Evaluation Harness with expected SQL

📈 Evaluation Dashboard (accuracy, execution success, latency)

🎨 Animated UI with Streamlit + GSAP + Three.js

🧠 Research-ready architecture (clean, modular, extensible)

🏗️ Architecture Overview

User Question
     ↓
Streamlit UI (GSAP + Three.js)
     ↓
FastAPI Backend
     ↓
Schema RAG (Vector Search over DB schema)
     ↓
LLM (NLP → SQL)
     ↓
SQL Validation & Healing
     ↓
Database Execution (SQLite)
     ↓
Results + Confidence Score
     ↓
Evaluation Dashboard

📁 Project Structure
│
├── backend/
│   ├── app.py                # FastAPI entrypoint
│   ├── sql_engine.py         # SQL generation & execution
│   ├── schema_rag.py         # Schema retrieval (RAG)
│   ├── database.py           # SQLite connection
│   ├── seed.py               # Database seeding
│   ├── evaluation.py         # Test harness & metrics
│   └── models.py             # Confidence scoring logic
│
├── frontend/
│   └── app.py                # Streamlit UI
│
├── data/
│   └── app.db                # SQLite database
│
└── README.md

⚙️ Tech Stack
Layer	    Tools
LLM -->	 Ollama (LLaMA)
Backend -->	 FastAPI
Frontend -->	 Streamlit
RAG	   --> LangChain + Vector Embeddings
Database	 --> SQLite
Animation -->	GSAP, Three.js
Evaluation	--> Python (custom harness)


🚀 Getting Started

1️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Seed the Database
python backend/seed.py

4️⃣ Start Backend (FastAPI)
uvicorn backend.app:app --reload

5️⃣ Start Frontend (Streamlit)
streamlit run frontend/app.py

🧪 Example Queries to Try

Show all customers

Total sales per customer

Which customer has the highest order value?

List orders placed in the last 30 days

Average order value by customer

📊 Automatic Evaluation System

✔ What Gets Evaluated

SQL correctness

Execution success

Schema grounding

Latency

Confidence score alignment

🧪 Test Harness

Each test includes:

{
  "question": "Total sales per customer",
  "expected_sql": "SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id"
}

📈 Metrics Produced

Accuracy (%)

Execution Success Rate

Avg Latency

Confidence Calibration

🧠 Confidence Scoring

Each response includes a confidence score based on:

Schema match quality

SQL execution success

LLM consistency

Result stability

Example:

{
  "sql": "...",
  "result": [...],
  "confidence": 0.87
}

📡 Streaming Support

SQL generation streamed token-by-token

Results streamed row-by-row

Improves transparency and UX

🔬 Research Contributions

Practical schema-grounded NLP-to-SQL

Execution-based validation loop

Confidence-aware LLM outputs

End-to-end evaluation pipeline

UI transparency with streaming

🔮 Future Work

Multi-database support (Postgres, MySQL)

Hallucination detection metrics
