# JurisAI

> **AI-powered legal rights assistant for Indian citizens. Plain language. Cited. Honest about limits.**

[![Railway](https://img.shields.io/badge/deployed-railway-blueviolet)](https://jurisai-production-8ee2.up.railway.app)
[![Status](https://img.shields.io/badge/status-active-green)]()

---

## What is JurisAI?

JurisAI helps Indian citizens understand their legal rights in plain language. Ask a question about an Indian law — get back cited chunks from the actual legislation.

No hallucination. No legal advice. Just the law, cited.

---

## Live Demo

**Base URL:** `https://jurisai-production-8ee2.up.railway.app`

```bash
# Health check
curl https://jurisai-production-8ee2.up.railway.app/health

# Search
curl -X POST https://jurisai-production-8ee2.up.railway.app/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Protection of Children from Sexual Offences"}'
```

---

## Architecture

```
User query
    ↓
FastAPI (Railway)
    ↓
BGE-M3 — embed query into dense vector
    ↓
Qdrant Cloud — find top-5 similar chunks
    ↓
Response with text + source citation
```

**Parallel retrieval:**
```
Query → Dense search (BGE-M3 + Qdrant) → ranked by semantic similarity
Query → BM25 search (keyword index)    → ranked by keyword frequency
```

---

## Tech Stack

| Layer | Tool | Why |
|---|---|---|
| Backend | FastAPI | Async-first, Pydantic-native |
| Vector DB | Qdrant Cloud | Native hybrid search, best free tier |
| Embeddings | BGE-M3 | Multilingual, 8192 token context, dense + sparse in one pass |
| Keyword search | rank-bm25 | BM25Okapi index over 2082 chunks |
| Deployment | Railway + Docker | Container-based, auto-deploy from GitHub |

---

## Endpoints

### `GET /health`
```json
{"status": "ok"}
```

### `POST /search`
Dense semantic search over Indian legal acts.

**Request:**
```json
{
  "query": "Protection of Children from Sexual Offences",
  "top_k": 5
}
```

**Response:**
```json
{
  "response": [
    {
      "text": "THE PROTECTION OF CHILDREN FROM SEXUAL OFFENCES ACT, 2012...",
      "source": "POCSO-2012-32"
    }
  ]
}
```

### `POST /search/bm25`
Keyword-based search using BM25 index.

Same request/response format as `/search`.

---

## Data

| Source | Chunks | Acts |
|---|---|---|
| Indian bare acts (PDF) | 2082 | 10 |

**Acts ingested:**
- POCSO Act 2012
- IT Act 2000
- Bharatiya Nyaya Sanhita
- Labour Act
- Consumer Protection Act
- + 5 more

---

## Eval Baseline

See `EVALS.md` for full details.

| Query | Dense recall@5 | BM25 recall@5 |
|---|---|---|
| "POCSO law" (abbreviation) | 0/5 | 0/5 |
| "Protection of Children from Sexual Offences" | 5/5 | 2/5 |

**Failure modes identified:**
1. Named entity mismatch — abbreviation vs full name
2. Vocabulary mismatch — informal query vs formal legal language
3. Source metadata missing — fixed Week 2

---

## Roadmap

| Week | Deliverable |
|---|---|
| Week 3 | Cross-encoder reranker + Langfuse tracing |
| Week 4 | 50-pair golden eval dataset + recall@5 baseline |
| Week 5 | Query classifier + abbreviation expansion |
| Week 6 | CI badge + WHY.md + Artifact 1 complete |
| Week 7–10 | LangGraph agentic workflow |
| Week 9–10 | Next.js frontend |

---

## Local Development

```bash
# Clone
git clone https://github.com/abhishek/jurisai
cd jurisai/rag

# Environment
cp .env.example .env
# Add QDRANT_URL and QDRANT_API_KEY

# Run with Docker
docker compose up --build

# Or directly
pip install -r requirements.txt
fastapi run main.py
```

---

## Project Structure

```
jurisai/
├── rag/
│   ├── main.py          # FastAPI app
│   ├── retrieval.py     # Dense + BM25 search
│   ├── models.py        # Pydantic schemas
│   ├── scripts/
│   │   └── ingest.py    # PDF extraction + embedding pipeline
│   ├── EVALS.md         # Retrieval quality tracking
│   ├── Dockerfile
│   └── docker-compose.yml
├── agents/              # Week 7+
├── finetune/            # Week 11+
├── frontend/            # Week 9+
└── evals/               # Week 4+
```

---

*Built as part of a 26-week Applied AI Engineer portfolio. JurisAI — Week 1–6 of 26.*