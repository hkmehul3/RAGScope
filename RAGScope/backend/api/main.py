
from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="RAGScope")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def root():
    return {"status": "running", "project": "RAGScope"}

@app.post("/query")
async def query_rag(req: QueryRequest):
    start = time.time()

    response = {
        "query": req.query,
        "retrieved_chunks": 4,
        "answer": "Sample generated response from RAG pipeline.",
        "latency_ms": round((time.time() - start) * 1000, 2),
        "tokens_used": 182,
        "cost_per_request": 0.0021
    }

    return response
