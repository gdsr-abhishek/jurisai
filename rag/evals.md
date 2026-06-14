# JurisAI RAG — Eval Baseline

> **Tracking retrieval quality across every improvement. Numbers don't lie.**

| Field | Value |
|---|---|
| Pipeline version | v0.1 — dense + BM25 baseline |
| Chunks in Qdrant | 2082 |
| Embedding model | BGE-M3 (dense vectors) |
| Last updated | 2026-06-02 |

---

## Metrics (target by Artifact 1 — Week 6)

| Metric | Current | Target |
|---|---|---|
| recall@5 | not measured | ≥ 80% |
| Faithfulness | not measured | ≥ 0.8 |
| Citation accuracy | not measured | ≥ 0.8 |

> **Note**
> Formal metrics (recall@5, faithfulness, citation accuracy) require the 50-pair golden eval
> dataset — due Week 4. This file tracks qualitative baselines until then.

---

## Week 2 — Dense vs BM25 baseline

### Method

Three test queries run through both retrieval modes independently.
Top 5 chunks returned by each. Top result noted below.

---

### Query 1 — "what is POCSO law?"

| Mode | Top returned chunk (summary) | Relevant? |
|---|---|---|
| Dense | Labour laws categorization — Central Government enforcement | ❌ Wrong domain |
| BM25 | Evidence Act — definitions of document, offence | ❌ Keyword mismatch |

**Observation:** Dense drifted semantically toward "protection"-related content (labour + domestic violence acts). BM25 matched generic legal keywords ("offence", "law", "person") but missed POCSO entirely. Both fail on abbreviation queries.
---
### Query 2 — "Protection of Children from Sexual Offences"

| Mode | recall@5 | Notes |
|---|---|---|
| Dense | 5/5 ✅ | Perfect — vocabulary matches exactly |
| BM25 | 2/5 ⚠️ | Keyword drift — "offences" matches IT Act, Labour Act |
| Hybrid (RRF k=60) | 4/5 ✅ | One IT Act chunk slipped in at rank 4 |

**Observation:** Dense beats hybrid on this query because vocabulary matches exactly. Hybrid shines on ambiguous or informal queries where dense drifts semantically and BM25 anchors on rare keywords. RRF correctly
---

### Query 3 — "What are the penalties for hacking under the IT Act?"

| Mode | recall@5 | Notes |
|---|---|---|
| Dense | 5/5 ✅ | Semantic understanding of "hacking" — correct IT Act chunks |
| BM25 | 1/5 ❌ | "penalties" matches RTI + CPA — severe keyword drift |
| Hybrid | 4/5 ✅ | Rescued BM25 failure — RRF pushed correct IT Act chunks up |

**Observation:** Hybrid's biggest value is rescuing bad BM25 results. Dense won on both queries tested so far. Hypothesis: hybrid will win over dense on abbreviated or informal queries — test in Week 5 with query expansion.
---

## Failure modes identified — Week 2

| # | Failure mode | Example | Fix | Planned week |
|---|---|---|---|---|
| 1 | Named entity mismatch | "POCSO" (abbreviation) → 0/5, full act name → 5/5 | Query expansion + abbreviation dictionary | Week 5 |
| 2 | Vocabulary mismatch | Informal query words match wrong domain chunks | Hybrid fusion + reranker | Week 2–3 |
| 3 | No source metadata in response | Can't tell which act a chunk came from | Add source + page to payload | This week |
---

## What this tells us

Dense retrieval works well when query vocabulary matches chunk vocabulary.
Both dense and BM25 fail on abbreviations and informal query phrasing.
Hybrid fusion is the next step — combining BM25's rare-keyword anchoring with dense semantic matching should handle both cases better.

---

## Improvement log

| Date | Change | Impact |
|---|---|---|
| 2026-06-02 | Dense search endpoint live (BGE-M3 + Qdrant) | Baseline established |
| 2026-06-02 | BM25 keyword index built from 2082 chunks | Baseline established |
| 2026-06-02 | Vocabulary mismatch failure mode identified | Informs Week 5 query expansion |
| 2026-06-03 | Source metadata added to /search response | Failure mode 3 closed |
| — | Hybrid retrieval (RRF fusion) | Pending Week 2 |
| — | Cross-encoder reranker | Pending Week 3 |
| — | Query expansion for abbreviations | Pending Week 5 |

---

## Golden eval dataset

- [ ] 50 Q&A pairs — due Week 4
- [ ] Verified manually — 10 pairs checked by hand
- [ ] Pushed to `evals/golden_dataset.json`

Format:
```json
{
  "query": "What is the punishment under POCSO for aggravated penetrative sexual assault?",
  "expected_chunk_ids": ["chunk_042", "chunk_043"],
  "expected_answer_contains": ["Section 6", "rigorous imprisonment", "not less than 20 years"]
}
```

---
---
## Baseline eval — Week 3 (2026-06-15)

| Metric | Score | Pass Rate | Threshold |
|---|---|---|---|
| Faithfulness | 0.96 | 93.33% | 0.7 |
| Contextual Recall | 0.84 | 80.00% | 0.7 |
| Overall | — | 76.67% | — |

30 queries. 23 passed. 7 failed. Cost: $1.14 per run.

## Failure modes identified

| ID | Query | Failure | Root cause |
|---|---|---|---|
| 10 | Who can file RTI? | Contextual recall 0.50 | Missing introductory section chunk |
| 12 | RTI appeal procedure | Contextual recall 0.50 | Missing specific sections on filing + 30-day limit |
| 15 | POCSO penetrative assault | Faithfulness 0.50 | LLM overstated natural life definition scope |
| 20 | Consumer rights | Contextual recall 0.14 | Rights enumeration not in retrieved chunks |
| 21 | Consumer complaint procedure | Contextual recall 0.56 | Partial chunk coverage, LLM inferred missing steps |
| 23 | Consumer complaint time limit | Both fail | LLM hallucinated 2-year limit not in corpus |
| 24 | District Commission jurisdiction | Contextual recall 0.33 | Pecuniary limit not in corpus |

## Week 4 fix targets
1. Tighten system prompt — no inference beyond retrieved context
2. Review chunking of introductory/definition sections
3. Mark out-of-corpus queries — exclude from recall metrics
---

> **Rule:** every retrieval change gets a before/after number in this file.
> No change ships without a measured improvement.