# LLM Response Quality Evaluator

**Status:** Complete &nbsp;|&nbsp; [ภาษาไทย](README.th.md)

A pytest-based framework that sends structured test prompts to an OpenAI-compatible LLM API (`qwen3.6-35b-a3b`), scores response quality across three dimensions, and generates a self-contained HTML quality report.

**Stack:** Python · pytest · OpenAI-compatible API · pytest-html · GitHub Actions

---

## Dimensions evaluated

| Evaluator | What it measures | Score |
|-----------|-----------------|-------|
| **Latency** | Response time vs. 10s threshold | 1.0 if ≤10s, degrades linearly |
| **Consistency** | Token-overlap similarity across 3 runs | 0–1 (higher = more consistent) |
| **Hallucination** | Fraction of expected facts present in response | 0–1 (higher = fewer hallucinations) |

---

## Live report

[View latest quality report](https://tonsai987654321.github.io/llm-quality-evaluator/)

---

## Run locally

```bash
cp .env.example .env
# add your OPENAI_API_KEY (and optionally OPENAI_BASE_URL) to .env

pip install -r requirements.txt
pytest tests/
# report generated at reports/index.html
```

## Run unit tests (no API key needed)

```bash
pytest tests/unit/
```

---

> Agent context: see [AGENTS.md](AGENTS.md).
