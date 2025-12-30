from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from backend.sql_engine import run_query_stream

app = FastAPI(title="Pre-Council SQL Agent")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/query/stream")
def query_stream(question: str = Query(...)):

    def generator():
        for chunk in run_query_stream(question):
            yield chunk + "\n"

    return StreamingResponse(generator(), media_type="text/plain")
