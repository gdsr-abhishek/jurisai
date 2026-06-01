from fastapi import FastAPI
from retrieval import dense_search, bm25_search
from models import SearchRequest

app = FastAPI()

@app.get('/health')
def get_health():
    return {"status":"ok"}

@app.post("/search")
def search(request: SearchRequest):
    results = dense_search(request.query)
    return {"results": results}