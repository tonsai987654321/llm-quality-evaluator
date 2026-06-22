import pytest
from evaluators import hallucination


def test_hallucination_scores(llm_client, prompt_data):
    factual = [item for item in prompt_data if item.get("expected_facts")]
    assert len(factual) >= 3, "Need at least 3 prompts with expected_facts"
    for item in factual:
        result = hallucination.evaluate(llm_client, item["prompt"], item["expected_facts"])
        assert result["score"] >= 0.5, (
            f"Hallucination score {result['score']:.2f} too low for prompt: {item['prompt']}\n"
            f"Expected facts: {item['expected_facts']}\n"
            f"Response: {result['response']}"
        )
