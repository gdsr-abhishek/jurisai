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
for item in golden_set:
    response = requests.post(
        "http://localhost:8080/query",
        json={"query": item["query"], "top_k": 5}
    ).json()
    
    test_case = LLMTestCase(
        input=item["query"],
        actual_output=response["answer"],
        expected_output=item["expected_answer"],
        retrieval_context=[c["text"] for c in response["citations"]]
    )
    print(f'test_case : {test_case}')
    test_cases.append(test_case)
print(f"----------------Before eval test_cases: {test_cases}")
# run eval
evaluate(test_cases, [
    FaithfulnessMetric(threshold=0.7),
    ContextualRecallMetric(threshold=0.7)
])