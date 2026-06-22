# LLM Response Quality Evaluator

**Status:** Complete

A pytest-based framework that sends structured test prompts to an OpenAI-compatible LLM API (`qwen3.6-35b-a3b`), scores response quality across three dimensions, and generates a self-contained HTML quality report.

เฟรมเวิร์กที่ใช้ pytest ส่งชุดคำถามทดสอบไปยัง LLM API ที่รองรับ OpenAI (`qwen3.6-35b-a3b`) วัดคุณภาพการตอบสนองใน 3 มิติ และสร้างรายงาน HTML แบบ self-contained

**Stack:** Python · pytest · OpenAI-compatible API · pytest-html · GitHub Actions

---

## Dimensions evaluated / มิติที่ประเมิน

| Evaluator | What it measures / สิ่งที่วัด | Score / คะแนน |
|-----------|-------------------------------|---------------|
| **Latency** | Response time vs. 3s threshold / เวลาตอบสนองเทียบกับ 3 วินาที | 1.0 if ≤3s, degrades linearly / 1.0 ถ้าไม่เกิน 3 วินาที ลดลงเชิงเส้น |
| **Consistency** | Token-overlap similarity across 3 runs / ความคล้ายกันของคำตอบใน 3 รอบ | 0–1 (higher = more consistent / สูง = สม่ำเสมอกว่า) |
| **Hallucination** | Fraction of expected facts present / สัดส่วนข้อเท็จจริงที่ปรากฏในคำตอบ | 0–1 (higher = fewer hallucinations / สูง = หลอนน้อยกว่า) |

---

## Live report / รายงานสด

[View latest quality report / ดูรายงานล่าสุด](https://tonsai987654321.github.io/llm-quality-evaluator/)

---

## Run locally / รันในเครื่อง

```bash
cp .env.example .env
# add your OPENAI_API_KEY (and optionally OPENAI_BASE_URL) to .env
# เพิ่ม OPENAI_API_KEY (และ OPENAI_BASE_URL ถ้าใช้ provider อื่น) ใน .env

pip install -r requirements.txt
pytest tests/
# report generated at reports/index.html
# รายงานจะถูกสร้างที่ reports/index.html
```

## Run unit tests (no API key needed) / รัน unit tests (ไม่ต้องใช้ API key)

```bash
pytest tests/unit/
```

---

> Agent context: see [AGENTS.md](AGENTS.md).
