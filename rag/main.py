from fastapi import FastAPI
from retrieval import dense_search, bm25_search
from models import SearchRequest , DenseSearchResponse

app = FastAPI()

@app.get('/health')
def get_health():
    return {"status":"ok"}

@app.post("/search")
def search(request: SearchRequest) -> DenseSearchResponse:
    results =DenseSearchResponse(response=dense_search(request.query))
    return results
@app.post("/search/bm25")
def search_bm25(request: SearchRequest) -> DenseSearchResponse:
    results = DenseSearchResponse(response=bm25_search(request.query))
    return results