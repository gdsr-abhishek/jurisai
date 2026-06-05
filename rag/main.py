from fastapi import FastAPI, HTTPException
from retrieval import dense_search, bm25_search
from models import SearchRequest , DenseSearchResponse

app = FastAPI()

@app.get('/health')
def get_health():
    return {"status":"ok"}

@app.post("/search")
def search(request: SearchRequest) -> DenseSearchResponse:
    try:
        results =DenseSearchResponse(response=dense_search(request.query))
    except RuntimeError as e:
        raise HTTPException(status_code=503,detail=str(e))

    return results
@app.post("/search/bm25")
def search_bm25(request: SearchRequest) -> DenseSearchResponse:
    try:
        results = DenseSearchResponse(response=bm25_search(request.query))
    except RuntimeError as e:
        raise HTTPException(status_code=503 , detail=str(e))
    return results