import pytest_html
from evaluators import latency


def test_latency_score(llm_client, prompt_item, extras):
    result = latency.evaluate(llm_client, prompt_item["prompt"])
    extras.append(pytest_html.extras.html(
        f"<b>Score:</b> {result['score']:.2f} &nbsp;|&nbsp; "
        f"<b>Elapsed:</b> {result['elapsed_seconds']:.2f}s &nbsp;|&nbsp; "
        f"<b>Threshold:</b> 10s"
    ))
    assert result["score"] >= 0.3, (
        f"Latency score {result['score']:.2f} too low ({result['elapsed_seconds']:.2f}s elapsed)"
    )
