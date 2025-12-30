import sqlite3
from backend.database import get_connection
from backend.schema_rag import retrieve_schema
from backend.llm import generate_sql_from_llm

def execute_sql(sql: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    columns = [col[0] for col in cursor.description] if cursor.description else []
    rows = cursor.fetchall()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

def run_query_stream(question: str):
    yield "🧠 Understanding question..."

    schema_context = retrieve_schema(question)
    yield "📚 Retrieved schema context"

    sql = generate_sql_from_llm(question, schema_context)
    yield f"🧾 Generated SQL:\n{sql}"

    try:
        result = execute_sql(sql)
        yield "✅ SQL executed successfully"
        yield f"📊 Result:\n{result}"
    except Exception as e:
        yield f"❌ SQL execution failed: {e}"
