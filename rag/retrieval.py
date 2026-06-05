# retrieval.py
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import os
from dotenv import load_dotenv



load_dotenv()

# global init — runs once at startup
client = QdrantClient(url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY"))
embedder = SentenceTransformer("BAAI/bge-m3")

# BM25 — scroll all chunks and build index once
all_points = client.scroll(collection_name="jurisai", limit=3000)[0]
texts = [p.payload["page_content"] for p in all_points]
tokenized = [text.split() for text in texts]
bm25 = BM25Okapi(tokenized)

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
    tokens = query.split()
    try:
        scores = bm25.get_scores(tokens)
        top_indices = scores.argsort()[-top_k:][::-1]
        return [
            {
                "text": texts[i],
                "source": all_points[i].payload["source"]
            }
            for i in top_indices
        ]
    except Exception as e:
        raise RuntimeError("Search service unavailable")
# print(f'dense : {dense_search("what is POCSO law?",5)}\n\n\n')
# print(f'bm25 or keyword response {bm25_search("what is POCSO law?",5)}')
