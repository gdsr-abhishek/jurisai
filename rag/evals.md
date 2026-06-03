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

| Mode | Top returned chunk (summary) | Relevant? |
|---|---|---|
| Dense | POCSO Act preamble — offences of sexual assault, harassment, pornography | ✅ Correct |
| Dense | POCSO arrangement of sections — Chapter I to IX | ✅ Correct |
| Dense | POCSO definitions — child means any person below 18 years | ✅ Correct |
| Dense | POCSO miscellaneous — Section 39 to 46 | ✅ Correct |
| Dense | POCSO preamble repeat — sexual exploitation heinous crimes | ✅ Correct |
| BM25 | POCSO — sexual exploitation enacted by Parliament | ✅ Correct |
| BM25 | IT Act 2000 — Chapter XII intermediaries | ❌ Wrong act |
| BM25 | POCSO — alternate punishment Section 42 | ✅ Correct |
| BM25 | Labour Act — Factories Act 1948 | ❌ Wrong act |
| BM25 | Bharatiya Nyaya Sanhita — property offences | ❌ Wrong act |

**Dense recall@5: 5/5 = 1.0** — perfect retrieval when full act name is used.
**BM25 recall@5: 2/5 = 0.4** — keyword "offences" and "protection" appear across many acts causing drift.

**Observation:** Dense wins on semantic coherence. BM25 gets confused by common legal keywords appearing across multiple acts. Hybrid fusion should combine dense precision with BM25 keyword anchoring.
---

### Query 3 — (add next test query here)

| Mode | Top returned chunk (summary) | Relevant? |
|---|---|---|
| Dense | | |
| BM25 | | |

**Observation:**

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

> **Rule:** every retrieval change gets a before/after number in this file.
> No change ships without a measured improvement.