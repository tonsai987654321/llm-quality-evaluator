# LLM Response Quality Evaluator

**Status:** Complete

A pytest-based framework that sends structured test prompts to the OpenAI API (`gpt-4o-mini`), scores response quality across three dimensions, and generates a self-contained HTML quality report.

**Stack:** Python · pytest · OpenAI · pytest-html · GitHub Actions

## Dimensions evaluated

| Evaluator | What it measures | Score |
|-----------|-----------------|-------|
| **Latency** | Response time vs. 3s threshold | 1.0 if ≤3s, degrades linearly |
| **Consistency** | Token-overlap similarity across 3 runs of the same prompt | 0–1 (higher = more consistent) |
| **Hallucination** | Fraction of expected facts present in the response | 0–1 (higher = fewer hallucinations) |

## Live report

[View latest quality report](https://tonsai987654321.github.io/llm-quality-evaluator/)

## Run locally

```bash
cp .env.example .env
# add your OPENAI_API_KEY to .env

pip install -r requirements.txt
pytest tests/
# report generated at reports/quality_report.html
```

## Run unit tests (no API key needed)

```bash
pytest tests/unit/
```

> Agent context: see [AGENTS.md](AGENTS.md).
