import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3"


def generate_sql_from_llm(question: str, schema_context: str) -> str:
    """
    Uses Ollama (llama3) to generate SQL using schema-aware prompting
    """

    prompt = f"""
You are a senior data engineer.

ONLY output valid SQLite SQL.
DO NOT explain anything.
DO NOT use markdown.

Database schema:
{schema_context}

Question:
{question}

SQL:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    raw = response.json()["response"]

    # 🧹 Cleanup (very important)
    sql = raw.strip().strip("```").replace("sql", "").strip()

    return sql
