from fastapi import FastAPI, HTTPException
from retrieval import dense_search, bm25_search,hybrid_search
from models import HybridSearchResponse, SearchRequest , DenseSearchResponse , LegalResponse,Citation
import instructor
from litellm import acompletion
import litellm
from dotenv import load_dotenv
from langfuse.decorators import observe
litellm._turn_on_debug()
load_dotenv()

app = FastAPI()
@app.get('/health')
async def get_health():
    return {"status":"ok"}

@app.post("/search")
async def search(request: SearchRequest) -> DenseSearchResponse:
    try:
        results =DenseSearchResponse(response=dense_search(request.query))
    except RuntimeError as e:
        raise HTTPException(status_code=503,detail=str(e))

    return results
@app.post("/search/bm25")
async def search_bm25(request: SearchRequest) -> DenseSearchResponse:
    try:
        results = DenseSearchResponse(response=bm25_search(request.query))
    except RuntimeError as e:
        raise HTTPException(status_code=503 , detail=str(e))
    return results
@app.post("/search/hybrid")
async def search_hybrid(request: SearchRequest) -> HybridSearchResponse:
    try:
        results = HybridSearchResponse(response=hybrid_search(query=request.query,top_k=request.top_k *4))
    except RuntimeError as e:
        raise HTTPException(status_code=503 , detail=str(e))
    return results

client = instructor.from_litellm(completion=acompletion)
@app.post("/query")
@observe(name='jurisai-legal-query')
async def query_rag_system(request: SearchRequest) -> LegalResponse:
    try:
        reranked = hybrid_search(query=request.query, top_k=request.top_k * 4)
        
        context = "\n\n".join([
            f"[{i+1}][{chunk.source}]: {chunk.text}"
            for i, chunk in enumerate(reranked)
        ])
        
        response = await acompletion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a legal assistant for Indian citizens. Answer based strictly on the numbered context below. Be plain and clear."},
                {"role": "user", "content": f"Question: {request.query}\n\nContext:\n{context}"}
            ]
        )

        answer = response.choices[0].message.content

        legal_response = LegalResponse(
            answer=answer,
            citations=[Citation(text=c.text, source=c.source, score=c.score) for c in reranked],
            confidence=float(reranked[0].score),
            abstain=float(reranked[0].score) < 0.6,
            abstain_reason="Low retrieval confidence" if float(reranked[0].score) < 0.6 else None
        )

    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    
    return legal_response