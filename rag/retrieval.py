# retrieval.py
from collections import defaultdict
from typing import List

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import os
from dotenv import load_dotenv

from models import HybridSearchResponse,HybridSearch



load_dotenv()
# global init — runs once at startup
client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))
from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
embedder = SentenceTransformer("BAAI/bge-m3")
def dense_search(query: str, top_k: int = 5):
    try:
        vector = embedder.encode(query).tolist()
    except Exception as e:
        raise RuntimeError("Embedding service unavailable")
    try:
        results = client.query_points(collection_name="jurisai", query=vector, limit=top_k,using='dense')
    except Exception as e:
        raise RuntimeError("Search service unavailable")
    response= [
        {'text':r.payload["page_content"],
         'source':r.payload["source"] 
        }
        for r in results.points]
    return  response


def bm25_search(query: str, top_k: int = 5):
    # BM25 — scroll all chunks and build index once
    all_points = client.scroll(collection_name="jurisai", limit=3000)[0]
    texts = [p.payload["page_content"] for p in all_points]
    sources = [p.payload.get("source", "unknown") for p in all_points]
    tokenized = [text.split() for text in texts]
    bm25 = BM25Okapi(tokenized)
    tokens = query.split()
    try:
        scores = bm25.get_scores(tokens)
        top_indices = scores.argsort()[-top_k:][::-1]
        return [
            {
                "text": texts[i],
                "source": sources[i]
            }
            for i in top_indices
        ]
    except Exception as e:
        raise RuntimeError("Search service unavailable")

def hybrid_search(query,top_k:int = 5) -> HybridSearchResponse:
    dense_result = dense_search(query,top_k)
    bm_25_result = bm25_search(query,top_k)
    scores = defaultdict(float)
    all_sources = defaultdict(str)
    for rank,result in enumerate(dense_result,start=1):
        text = result['text']
        all_sources[text] = result['source']
        scores[text] += 1/(60 + rank)
    for rank,result in enumerate(bm_25_result,start=1):
        text = result['text']
        all_sources[text] = result['source']
        scores[text] +=1/(60+rank)
    ranked = sorted(scores.items(),key=lambda x:x[1],reverse=True)[:top_k]
    result = [ HybridSearch(text=str(i[0]),source=all_sources[i[0]],score=i[1])  for i in ranked]
    return reranker(query,result,top_k//4)
def reranker(query: str, ranked_chunks: List[HybridSearch], top_k: int = 5):
    pairs = [(query, ranked_chunk.text) for ranked_chunk in ranked_chunks]
    scores = reranker_model.predict(pairs)
    
    # normalize to 0-1
    min_score, max_score = scores.min(), scores.max()
    normalized = (scores - min_score) / (max_score - min_score + 1e-8)
    
    ranked = sorted(zip(normalized, ranked_chunks), key=lambda x: x[0], reverse=True)
    return [HybridSearch(text=chunk.text, source=chunk.source, score=round(float(score), 4)) 
            for score, chunk in ranked[:top_k]]
# print(f'dense : {dense_search("what is POCSO law?",5)}\n\n\n')
# print(f'bm25 or keyword response {bm25_search("what is POCSO law?",5)}')
# from sentence_transformers import CrossEncoder
# model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
# score = model.predict([("what is POCSO", "The Protection of Children from Sexual Offences Act")])
# print(score)