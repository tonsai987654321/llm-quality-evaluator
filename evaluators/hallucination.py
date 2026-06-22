import re


def _normalize(text: str) -> str:
    text = re.sub(r'\*+', '', text)        # markdown bold/italic
    text = re.sub(r'\$', '', text)         # LaTeX math delimiters
    text = re.sub(r'_(\d)', r'\1', text)   # LaTeX subscripts: H_2O → H2O
    for sub, digit in zip('₀₁₂₃₄₅₆₇₈₉', '0123456789'):
        text = text.replace(sub, digit)
    return text.lower()


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
