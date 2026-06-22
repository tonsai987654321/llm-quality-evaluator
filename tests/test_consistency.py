from evaluators import consistency


def test_consistency_scores(llm_client, prompt_data):
    # Use open-ended prompts — short factual questions produce format-varied responses
    # (LaTeX vs plain) that give misleadingly low token-overlap scores.
    open_ended = [item for item in prompt_data if not item.get("expected_facts")]
    assert open_ended, "Need at least one open-ended prompt in prompts.json"
    for item in open_ended:
        result = consistency.evaluate(llm_client, item["prompt"], n=3)
        assert result["score"] >= 0.4, (
            f"Consistency score {result['score']:.2f} too low for prompt: {item['prompt']}"
        )
