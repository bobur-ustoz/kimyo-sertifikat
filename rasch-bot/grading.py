"""Claude API orqali yozma ish (41, 42, 43-savollar) qo'lyozma yechimlarini baholash.

Talabgorning qo'lyozma yechimi rasm yoki PDF sifatida Claude'ga (vision)
base64 formatida, tegishli rubrika bilan birga yuboriladi. Claude'dan
FAQAT JSON qaytarishi so'raladi: {"ball": int, "izoh": str}.

MUHIM: Bu AI baholash tajribaviy hisoblanadi, natija yakuniy emas —
o'qituvchi tekshiruvi tavsiya etiladi.
"""

from __future__ import annotations

import base64
import json
import logging
import re
from dataclasses import dataclass

from anthropic import Anthropic, APIError

logger = logging.getLogger(__name__)

CLAUDE_MODEL = "claude-sonnet-5"

MAX_BALL = 25
MIN_BALL = 0

# ---------------------------------------------------------------------------
# Rubrikalar (41, 42, 43-topshiriqlar uchun alohida)
# ---------------------------------------------------------------------------

RUBRIKA_41 = """
41-TOPSHIRIQ (Umumiy kimyo) — jami 25 ball.
Baholash ikki qismdan iborat va ular qo'shiladi:
  - M (Metodika/mantiq): ~13-15 ball — yechim yo'li, formulalar tanlovi,
    kimyoviy mantiq to'g'riligi baholanadi.
  - A (Arifmetika): ~10-12 ball — hisob-kitoblar, sonli natijalarning
    to'g'riligi baholanadi.
MUHIM QOIDA: Agar yechim yo'li ko'rsatilmasdan faqat yakuniy javob yozilgan
bo'lsa, YOKI topshiriq to'liq xato yechilgan bo'lsa — 0 ball qo'ying.
"""

RUBRIKA_42 = """
42-TOPSHIRIQ (Organik kimyo) — jami 25 ball.
Faqat M (metodika/mantiq) baholanadi — arifmetika hisobi yo'q yoki alohida
baholanmaydi. Reaksiya tenglamalari, mexanizm, moddalarni aniqlash mantig'i
to'g'riligiga qarab 0 dan 25 gacha ball qo'yiladi.
MUHIM QOIDA: Agar yechim yo'li ko'rsatilmasdan faqat yakuniy javob yozilgan
bo'lsa, YOKI topshiriq to'liq xato yechilgan bo'lsa — 0 ball qo'ying.
"""

RUBRIKA_43 = """
43-TOPSHIRIQ (Anorganik kimyo / Kimyoviy tahlil) — jami 25 ball.
Baholash ikki qismdan iborat va ular qo'shiladi (41-topshiriq kabi):
  - M (Metodika/mantiq): ~13-15 ball
  - A (Arifmetika): ~10-12 ball
MUHIM QOIDA: Agar yechim yo'li ko'rsatilmasdan faqat yakuniy javob yozilgan
bo'lsa, YOKI topshiriq to'liq xato yechilgan bo'lsa — 0 ball qo'ying.
"""

RUBRIKALAR = {
    41: RUBRIKA_41,
    42: RUBRIKA_42,
    43: RUBRIKA_43,
}

_SYSTEM_PROMPT = """Siz kimyo fanidan milliy sertifikat yozma ishlarini baholovchi
ekspert baholovchisiz. Sizga bitta topshiriq uchun rubrika va talabgorning
qo'lyozma yechimi rasm/PDF sifatida beriladi.

Faqat quyidagi formatda, boshqa hech qanday matnsiz, JSON qaytaring:
{"ball": <0 dan 25 gacha butun son>, "izoh": "<qisqa 2-3 gapli tushuntirish, o'zbek tilida>"}
"""


@dataclass
class GradingResult:
    ball: int
    izoh: str
    xato: bool = False


def _extract_json(text: str) -> dict:
    """Claude javobidan JSON obyektni topib, chidamli tarzda parse qiladi."""
    text = text.strip()
    # Ba'zan javob ```json ... ``` bilan o'ralgan bo'lishi mumkin.
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("Javobda JSON topilmadi")
    return json.loads(match.group(0))


def _media_type_for(file_bytes: bytes, filename: str) -> tuple[str, str]:
    """Fayl kengaytmasiga qarab (block_type, media_type) aniqlaydi."""
    lower = filename.lower()
    if lower.endswith(".pdf"):
        return "document", "application/pdf"
    if lower.endswith(".png"):
        return "image", "image/png"
    if lower.endswith(".webp"):
        return "image", "image/webp"
    if lower.endswith(".gif"):
        return "image", "image/gif"
    # Standart: jpeg (Telegram fotolar odatda .jpg bo'lib keladi)
    return "image", "image/jpeg"


def grade_written_answer(
    client: Anthropic,
    savol_raqami: int,
    file_bytes: bytes,
    filename: str,
) -> GradingResult:
    """41/42/43-savol uchun qo'lyozma yechimni Claude vision orqali baholaydi.

    Xatolik yuzaga kelsa (API xatosi, JSON parse xatosi) dastur qulamaydi —
    GradingResult(xato=True) qaytariladi, chaqiruvchi tomon foydalanuvchidan
    qo'lda ball kiritishni so'rashi kerak.
    """
    rubrika = RUBRIKALAR.get(savol_raqami)
    if rubrika is None:
        raise ValueError(f"Noma'lum savol raqami: {savol_raqami}")

    block_type, media_type = _media_type_for(file_bytes, filename)
    b64_data = base64.standard_b64encode(file_bytes).decode("utf-8")

    if block_type == "document":
        content_block = {
            "type": "document",
            "source": {"type": "base64", "media_type": media_type, "data": b64_data},
        }
    else:
        content_block = {
            "type": "image",
            "source": {"type": "base64", "media_type": media_type, "data": b64_data},
        }

    try:
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=1024,
            system=_SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": rubrika},
                        content_block,
                        {
                            "type": "text",
                            "text": "Yuqoridagi rubrika asosida ushbu yechimni baholang. Faqat JSON qaytaring.",
                        },
                    ],
                }
            ],
        )
    except APIError as exc:
        logger.error("Claude API xatosi (savol %s): %s", savol_raqami, exc)
        return GradingResult(ball=0, izoh=f"AI baholashda xatolik yuz berdi: {exc}", xato=True)
    except Exception as exc:  # noqa: BLE001 - kutilmagan xatoliklardan ham chidamli bo'lish uchun
        logger.error("Kutilmagan xatolik (savol %s): %s", savol_raqami, exc)
        return GradingResult(ball=0, izoh=f"Kutilmagan xatolik: {exc}", xato=True)

    try:
        raw_text = "".join(
            block.text for block in response.content if getattr(block, "type", None) == "text"
        )
        data = _extract_json(raw_text)
        ball = int(data["ball"])
        izoh = str(data.get("izoh", "")).strip()
    except Exception as exc:  # noqa: BLE001
        logger.error("JSON parse xatosi (savol %s): %s", savol_raqami, exc)
        return GradingResult(
            ball=0,
            izoh="AI javobini o'qishda xatolik yuz berdi (JSON format buzilgan). Iltimos, ballni qo'lda kiriting.",
            xato=True,
        )

    ball = max(MIN_BALL, min(ball, MAX_BALL))
    if not izoh:
        izoh = "Izoh berilmagan."
    return GradingResult(ball=ball, izoh=izoh, xato=False)
