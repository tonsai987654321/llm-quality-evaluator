import pytest_html
from evaluators import hallucination


def test_hallucination_score(llm_client, factual_prompt_item, extras):
    result = hallucination.evaluate(
        llm_client, factual_prompt_item["prompt"], factual_prompt_item["expected_facts"]
    )
    extras.append(pytest_html.extras.html(
        f"<b>Score:</b> {result['score']:.2f} &nbsp;|&nbsp; "
        f"<b>Expected facts:</b> {', '.join(factual_prompt_item['expected_facts'])}<br>"
        f"<b>Response:</b> {result['response'][:200]}{'…' if len(result['response']) > 200 else ''}"
    ))
    assert result["score"] >= 0.5, (
        f"Hallucination score {result['score']:.2f} too low — "
        f"expected facts {factual_prompt_item['expected_facts']} not found in response"
    )
