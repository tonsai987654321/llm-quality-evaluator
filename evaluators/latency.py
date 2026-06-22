import time


def score_latency(elapsed_seconds: float, threshold: float = 10.0) -> float:
    if elapsed_seconds <= threshold:
        return 1.0
    return max(0.0, 1.0 - (elapsed_seconds - threshold) / threshold)


def evaluate(client, prompt: str) -> dict:
    start = time.time()
    response = client.chat.completions.create(
        model="qwen3.6-35b-a3b",
        messages=[{"role": "user", "content": prompt}],
    )
    elapsed = time.time() - start
    return {
        "response": response.choices[0].message.content,
        "elapsed_seconds": elapsed,
        "score": score_latency(elapsed),
    }
