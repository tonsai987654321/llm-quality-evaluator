# LLM Response Quality Evaluator

**สถานะ:** เสร็จสมบูรณ์ &nbsp;|&nbsp; [English](README.md)

เฟรมเวิร์กสำหรับทดสอบคุณภาพการตอบสนองของ LLM ผ่าน API ที่รองรับ OpenAI โดยใช้ pytest เป็นแกนหลัก ระบบส่งชุดคำถามทดสอบไปยังโมเดล `qwen3.6-35b-a3b` วัดผลใน 3 มิติ และสร้างรายงาน HTML แบบ self-contained

**เทคโนโลยีที่ใช้:** Python · pytest · OpenAI-compatible API · pytest-html · GitHub Actions

---

## มิติที่ประเมิน

| ตัวประเมิน | สิ่งที่วัด | คะแนน |
|-----------|-----------|-------|
| **Latency** | เวลาตอบสนองเทียบกับเกณฑ์ 10 วินาที | 1.0 ถ้าไม่เกิน 10 วินาที ลดลงเชิงเส้นหลังจากนั้น |
| **Consistency** | ความคล้ายกันของคำตอบ (token-overlap) ใน 3 รอบ | 0–1 ยิ่งสูงยิ่งสม่ำเสมอ |
| **Hallucination** | สัดส่วนข้อเท็จจริงที่ปรากฏในคำตอบ | 0–1 ยิ่งสูงยิ่งแม่นยำ |

---

## รายงานสด

[ดูรายงานล่าสุด](https://tonsai987654321.github.io/llm-quality-evaluator/)

---

## รันในเครื่อง

```bash
cp .env.example .env
# เพิ่ม OPENAI_API_KEY และ OPENAI_BASE_URL (ถ้าใช้ provider อื่น) ใน .env

pip install -r requirements.txt
pytest tests/
# รายงานจะถูกสร้างที่ reports/index.html
```

## รัน unit tests (ไม่ต้องใช้ API key)

```bash
pytest tests/unit/
```

---

## โครงสร้างโปรเจกต์

```
evaluators/        ตัวประเมินแต่ละมิติ (latency, consistency, hallucination)
tests/             test cases หลักและ unit tests
prompts/           ชุดคำถาม JSON พร้อม expected facts
assets/            dark theme CSS สำหรับรายงาน
reports/           ผลรายงาน HTML (สร้างหลัง pytest รัน)
.github/workflows/ CI pipeline และ deploy ไป GitHub Pages
```

---

> บริบทสำหรับ Agent: ดู [AGENTS.md](AGENTS.md)
