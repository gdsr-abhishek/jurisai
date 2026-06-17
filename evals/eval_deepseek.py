from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric, ContextualRecallMetric
from deepeval.test_case import LLMTestCase
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# load golden set
with open("./golden_dataset.json") as f:
    golden_set = json.load(f)

# run each query through pipeline
test_cases = []
skipped = []

for item in golden_set:
    query_id = item.get("id", "?")
    try:
        resp = requests.post(
            "http://localhost:8080/query",
            json={"query": item["query"], "top_k": 5},
            timeout=30
        )
        resp.raise_for_status()
        response = resp.json()

    except requests.exceptions.HTTPError:
        print(f"[SKIP] {query_id} — HTTP {resp.status_code}: {resp.text[:200]}")
        skipped.append(query_id)
        continue
    except requests.exceptions.JSONDecodeError:
        print(f"[SKIP] {query_id} — empty or invalid response body")
        skipped.append(query_id)
        continue
    except requests.exceptions.Timeout:
        print(f"[SKIP] {query_id} — request timed out")
        skipped.append(query_id)
        continue
    except requests.exceptions.RequestException as e:
        print(f"[SKIP] {query_id} — request failed: {e}")
        skipped.append(query_id)
        continue

    # guard against missing keys in response
    if "answer" not in response or "citations" not in response:
        print(f"[SKIP] {query_id} — unexpected response shape: {str(response)[:200]}")
        skipped.append(query_id)
        continue

    test_case = LLMTestCase(
        input=item["query"],
        actual_output=response["answer"],
        expected_output=item["expected_answer"],
        retrieval_context=[c["text"] for c in response["citations"]]
    )
    print(f"[OK] {query_id}")
    test_cases.append(test_case)

print(f"\n--- Summary ---")
print(f"Loaded:  {len(golden_set)}")
print(f"Ready:   {len(test_cases)}")
print(f"Skipped: {len(skipped)} — {skipped}")
print(f"---------------\n")

if not test_cases:
    print("No test cases to evaluate — check your API is running on localhost:8080")
else:
    evaluate(test_cases, [
        FaithfulnessMetric(threshold=0.7),
        ContextualRecallMetric(threshold=0.7)
    ])