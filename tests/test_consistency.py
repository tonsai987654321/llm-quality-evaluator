import pytest_html
from evaluators import consistency


def test_consistency_score(llm_client, open_ended_prompt_item, extras):
    result = consistency.evaluate(llm_client, open_ended_prompt_item["prompt"], n=3)
    extras.append(pytest_html.extras.html(
        f"<b>Score:</b> {result['score']:.2f} &nbsp;|&nbsp; <b>Runs:</b> 3<br>"
        + "<br>".join(
            f"<b>Run {i+1}:</b> {r[:120]}{'…' if len(r) > 120 else ''}"
            for i, r in enumerate(result["responses"])
        )
    ))
    assert result["score"] >= 0.4, (
        f"Consistency score {result['score']:.2f} too low"
    )
