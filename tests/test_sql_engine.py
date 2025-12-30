from backend.sql_engine import run_query_stream


def test_sql_engine_runs():
    question = "Show all customers"

    result = run_query_stream(question)

    assert result is not None
