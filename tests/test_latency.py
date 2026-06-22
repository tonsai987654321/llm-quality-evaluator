import pytest
from evaluators import latency


def test_latency_scores(llm_client, prompt_data):
    for item in prompt_data[:3]:
        result = latency.evaluate(llm_client, item["prompt"])
        assert result["score"] >= 0.5, (
            f"Latency score {result['score']:.2f} too low for prompt: {item['prompt']} "
            f"({result['elapsed_seconds']:.2f}s)"
        )
