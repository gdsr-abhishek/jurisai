#!/usr/bin/env python3
"""
Grounding audit for the JurisAI golden eval set.

Purpose
-------
DeepEval's Contextual Recall penalizes you when the EXPECTED answer contains
claims that the retrieval context does not support. That is not always a model
bug — often it means the golden answer was written from outside knowledge that
your corpus cannot surface.

This script does NOT fix anything automatically. It lays each golden query's
expected answer next to the chunks your retriever actually returns, so you can
eyeball, sentence by sentence, whether the expected answer is grounded.

Then YOU rewrite each expected answer to contain only what the chunks support
(or mark it as a retrieval gap / abstention case). Ground truth = your source
PDFs, never a model's memory.

Usage
-----
    export JURISAI_URL="http://localhost:8000"     # or your Railway URL
    python grounding_audit.py golden_dataset.json

    # options
    python grounding_audit.py golden_dataset.json --top-k 5 --only-ids 005,013,021
    python grounding_audit.py golden_dataset.json --out audit_report.md

Output
------
A Markdown report (default: grounding_audit_report.md) with, per query:
  - the query and current expected answer
  - the retrieved chunks (source + score + text)
  - a checklist scaffold for you to mark each expected sentence supported/not
"""

import argparse
import json
import os
import sys
import textwrap
import urllib.request
import urllib.error


def call_hybrid(base_url: str, query: str, top_k: int, timeout: int = 30):
    """Hit POST /search/hybrid and return the list of retrieved chunks.

    Adjust the response parsing if your HybridSearchResponse shape differs.
    This expects something like: {"response": [{"text": ..., "source": ..., "score": ...}, ...]}
    """
    url = base_url.rstrip("/") + "/search/hybrid"
    payload = json.dumps({"query": query, "top_k": top_k}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}"
    except urllib.error.URLError as e:
        return None, f"URL error: {e.reason}"
    except Exception as e:  # noqa: BLE001
        return None, f"Unexpected error: {e}"

    # Be liberal about the response shape — pull the list of chunks wherever it is.
    chunks = data.get("response", data) if isinstance(data, dict) else data
    if not isinstance(chunks, list):
        return None, f"Could not find a chunk list in response: {str(data)[:300]}"
    return chunks, None


def split_sentences(text: str):
    """Crude sentence split — good enough for a manual checklist scaffold."""
    out = []
    for para in text.split("\n"):
        para = para.strip()
        if not para:
            continue
        # split on '. ' but keep it simple; the human is reading anyway
        parts = [p.strip() for p in para.replace("? ", "?. ").split(". ") if p.strip()]
        out.extend(parts)
    return out


def fmt_chunk(i, chunk):
    if isinstance(chunk, dict):
        source = chunk.get("source", "?")
        score = chunk.get("score", "?")
        text = chunk.get("text", "")
    else:  # pydantic object or similar
        source = getattr(chunk, "source", "?")
        score = getattr(chunk, "score", "?")
        text = getattr(chunk, "text", "")
    score_str = f"{score:.4f}" if isinstance(score, (int, float)) else str(score)
    wrapped = textwrap.fill(str(text), width=100, subsequent_indent="    ")
    return f"  [{i+1}] source={source}  score={score_str}\n    {wrapped}"


def main():
    ap = argparse.ArgumentParser(description="Grounding audit for JurisAI golden set")
    ap.add_argument("dataset", help="Path to golden_dataset.json")
    ap.add_argument("--url", default=os.environ.get("JURISAI_URL", "http://localhost:8080"),
                    help="Base URL of the JurisAI API (env JURISAI_URL)")
    ap.add_argument("--top-k", type=int, default=5,
                    help="top_k sent to /search/hybrid (note: your endpoint multiplies by 4 internally)")
    ap.add_argument("--only-ids", default="",
                    help="Comma-separated golden ids to audit, e.g. 005,013,021")
    ap.add_argument("--out", default="grounding_audit_report.md", help="Output markdown path")
    args = ap.parse_args()

    with open(args.dataset, "r", encoding="utf-8") as f:
        golden = json.load(f)

    only = {x.strip() for x in args.only_ids.split(",") if x.strip()}
    if only:
        golden = [g for g in golden if g.get("id") in only]

    lines = []
    lines.append(f"# Grounding Audit Report\n")
    lines.append(f"- API: `{args.url}`")
    lines.append(f"- top_k: {args.top_k}")
    lines.append(f"- queries audited: {len(golden)}\n")
    lines.append("For each query: read the retrieved chunks, then mark every sentence "
                 "of the expected answer as **[S]upported** or **[U]nsupported**. "
                 "If most sentences are U, the expected answer — not the model — is the bug. "
                 "Verify any factual disagreement against the source PDF, not from memory.\n")
    lines.append("---\n")

    errors = 0
    for g in golden:
        gid = g.get("id", "?")
        query = g.get("query", "")
        expected = g.get("expected_answer", "")
        exp_source = g.get("expected_source", "?")
        domain = g.get("domain", "?")

        lines.append(f"## [{gid}] {query}")
        lines.append(f"*domain:* `{domain}`  ·  *expected_source:* `{exp_source}`\n")

        chunks, err = call_hybrid(args.url, query, args.top_k)
        if err:
            errors += 1
            lines.append(f"> ⚠️ retrieval failed: {err}\n")
            lines.append("---\n")
            print(f"[{gid}] FAILED: {err}", file=sys.stderr)
            continue

        # Retrieval gap signal: does any retrieved chunk even come from the expected source?
        retrieved_sources = []
        for c in chunks:
            s = c.get("source") if isinstance(c, dict) else getattr(c, "source", None)
            if s is not None:
                retrieved_sources.append(s)
        source_hit = any(exp_source.lower() in str(s).lower() or str(s).lower() in exp_source.lower()
                         for s in retrieved_sources)
        flag = "✅ expected source present in retrieval" if source_hit \
            else "🚩 expected source NOT in retrieved chunks — likely a RETRIEVAL gap"
        lines.append(f"**{flag}**\n")

        lines.append("### Retrieved chunks")
        if not chunks:
            lines.append("  (none — model should abstain; expected answer must be an abstention)\n")
        else:
            for i, c in enumerate(chunks):
                lines.append(fmt_chunk(i, c))
            lines.append("")

        lines.append("### Expected answer — sentence grounding checklist")
        for sent in split_sentences(expected):
            lines.append(f"- [ ] S / U — {sent}")
        lines.append("")
        lines.append("### Verdict (fill in)")
        lines.append("- [ ] Expected answer is fully grounded — keep as is")
        lines.append("- [ ] Rewrite expected answer to only what chunks support")
        lines.append("- [ ] Retrieval gap — fix chunking/indexing, not the answer")
        lines.append("- [ ] Abstention case — expected answer should say 'not in context'")
        lines.append("- [ ] Factual conflict with PDF — verify against source, correct ground truth")
        lines.append("\n---\n")

        print(f"[{gid}] audited — {len(chunks)} chunks, source_hit={source_hit}", file=sys.stderr)

    report = "\n".join(lines)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nWrote {args.out}", file=sys.stderr)
    if errors:
        print(f"{errors} queries failed retrieval — check API URL / endpoint shape", file=sys.stderr)


if __name__ == "__main__":
    main()