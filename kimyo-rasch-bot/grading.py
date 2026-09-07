"""Photo-based answer grading and free-text Q&A, backed by Claude vision."""
import base64
import json
import os

from anthropic import Anthropic

CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "")
_client = Anthropic(api_key=CLAUDE_API_KEY) if CLAUDE_API_KEY else None

MODEL = "claude-sonnet-4-5"


def grade_answer_photo(image_bytes: bytes, media_type: str, answer_key: dict, page_label: str) -> tuple[float, str]:
    """Compare a photographed answer sheet against the exam's answer key.

    Returns (score_0_to_100, short_feedback_in_uzbek).
    """
    if _client is None:
        return 0.0, "AI baholash sozlanmagan (CLAUDE_API_KEY yo'q)."

    prompt = (
        "Siz kimyo fanidan imtihon javoblarini tekshiruvchi yordamchisiz. "
        f"Quyidagi rasm o'quvchining '{page_label}' varag'idagi javoblari. "
        "To'g'ri javoblar kaliti (savol raqami -> to'g'ri javob) JSON ko'rinishida:\n"
        f"{json.dumps(answer_key, ensure_ascii=False)}\n\n"
        "Rasmdagi qo'lyozma javoblarni o'qing, ularni kalit bilan solishtiring va "
        "FAQAT quyidagi JSON formatida javob bering, boshqa hech narsa yozmang:\n"
        '{"score": <0-100 oralig\'ida son>, "feedback": "<qisqa, o\'zbek tilida izoh>"}'
    )

    resp = _client.messages.create(
        model=MODEL,
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": base64.b64encode(image_bytes).decode("ascii"),
                        },
                    },
                ],
            }
        ],
    )
    text = resp.content[0].text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    try:
        data = json.loads(text)
        return float(data.get("score", 0)), str(data.get("feedback", ""))
    except (json.JSONDecodeError, ValueError):
        return 0.0, "Baholashda xatolik yuz berdi, admin bilan bog'laning."


def ask_chemistry_question(question: str) -> str:
    if _client is None:
        return "AI yordamchi hozircha sozlanmagan."
    resp = _client.messages.create(
        model=MODEL,
        max_tokens=1000,
        system=(
            "Siz kimyo fanidan o'zbek tilida javob beruvchi o'qituvchi yordamchisiz. "
            "Qisqa, aniq va tushunarli javob bering, formulalarni to'g'ri yozing."
        ),
        messages=[{"role": "user", "content": question}],
    )
    return resp.content[0].text.strip()
