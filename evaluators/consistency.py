def _token_overlap(a: str, b: str) -> float:
    tokens_a = set(a.lower().split())
    tokens_b = set(b.lower().split())
    if not tokens_a and not tokens_b:
        return 1.0
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def score_consistency(responses: list) -> float:
    if len(responses) < 2:
        return 1.0
    pairs = [
        (responses[i], responses[j])
        for i in range(len(responses))
        for j in range(i + 1, len(responses))
    ]
    return sum(_token_overlap(a, b) for a, b in pairs) / len(pairs)


def evaluate(client, prompt: str, n: int = 3) -> dict:
    responses = [
        client.chat.completions.create(
            model="qwen3.6-35b-a3b",
            messages=[{"role": "user", "content": prompt}],
        ).choices[0].message.content
        for _ in range(n)
    ]
    return {
        "responses": responses,
        "score": score_consistency(responses),
    }
