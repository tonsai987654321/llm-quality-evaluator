# llm-quality-evaluator — Agent Context

## Purpose
A pytest-based framework that sends structured test prompts to an LLM API, scores response
quality (consistency, hallucination rate, latency), and generates an HTML quality report.
Extension of existing chatbot automation work.

## Status
In Progress.

## Tech Stack
Python · pytest · LLM testing · AI quality assurance · HTML reporting.

## Architecture Intent
pytest drives structured prompts against an LLM API. Scoring logic lives in dedicated
evaluator modules (consistency, hallucination rate, latency). Results aggregate into an
HTML quality report.

## Planned Layout (not yet created)
- `prompts/` — structured test prompts / datasets
- `tests/` — pytest test modules
- `evaluators/` — scoring logic (consistency, hallucination, latency)
- `reports/` — generated HTML reports
- `requirements.txt` — deps (pytest, anthropic or relevant LLM SDK, pytest-html)
- `.env` — API keys (gitignored)

## Conventions
- Relative paths only — repo is portable.
- API keys via `.env`, never committed.
