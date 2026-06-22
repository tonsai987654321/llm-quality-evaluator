def score_hallucination(response: str, expected_facts: list) -> float:
    if not expected_facts:
        return 1.0
    response_lower = response.lower()
    found = sum(1 for fact in expected_facts if fact.lower() in response_lower)
    return found / len(expected_facts)


def evaluate(client, prompt: str, expected_facts: list) -> dict:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.choices[0].message.content
    return {
        "response": text,
        "score": score_hallucination(text, expected_facts),
    }
