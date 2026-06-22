def _normalize(text: str) -> str:
    return text.lower().replace("₀", "0").replace("₁", "1").replace("₂", "2").replace("₃", "3")


def score_hallucination(response: str, expected_facts: list) -> float:
    if not expected_facts:
        return 1.0
    response_norm = _normalize(response)
    found = sum(1 for fact in expected_facts if _normalize(fact) in response_norm)
    return found / len(expected_facts)


def evaluate(client, prompt: str, expected_facts: list) -> dict:
    response = client.chat.completions.create(
        model="qwen3.6-35b-a3b",
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.choices[0].message.content
    return {
        "response": text,
        "score": score_hallucination(text, expected_facts),
    }
