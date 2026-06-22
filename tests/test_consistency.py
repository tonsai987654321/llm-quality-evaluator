from evaluators import consistency


def test_consistency_scores(llm_client, prompt_data):
    for item in prompt_data[:3]:
        result = consistency.evaluate(llm_client, item["prompt"], n=3)
        assert result["score"] >= 0.5, (
            f"Consistency score {result['score']:.2f} too low for prompt: {item['prompt']}"
        )
