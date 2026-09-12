"""Kimyo fanidan milliy sertifikat uslubidagi test natijalarini Rasch modeli
asosida baholovchi Telegram bot.

Oqim:
1. /start - talabgor ismini so'raydi
2. 1-40 savollardan nechtasi to'g'ri ekanini so'raydi (0-40)
3. 41, 42, 43-savollar uchun navbat bilan rasm/PDF so'raydi va Claude
   vision orqali baholaydi (grading.py)
4. Yakuniy Rasch hisob-kitobini (rasch.py) chiqaradi va data/students.json
   ga saqlaydi
5. /royxat - saqlangan talabgorlar jadvali
6. /bekor - joriy suhbatni bekor qilish
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from anthropic import Anthropic

import grading
import rasch

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_FILE = DATA_DIR / "students.json"

WRITTEN_SAVOLLAR = [41, 42, 43]

# ConversationHandler holatlari
NAME, TEST_SCORE, WRITTEN_FILE, MANUAL_BALL = range(4)

DISCLAIMER = "\n\n⚠️ AI bahosi tajribaviy, o'qituvchi tekshirishi tavsiya etiladi."

_anthropic_client: Anthropic | None = None


def get_anthropic_client() -> Anthropic:
    global _anthropic_client
    if _anthropic_client is None:
        _anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)
    return _anthropic_client


# ---------------------------------------------------------------------------
# Ma'lumotlarni saqlash
# ---------------------------------------------------------------------------


def load_students() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        logger.error("students.json o'qishda xatolik: %s", exc)
        return []


def save_student(record: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    students = load_students()
    students.append(record)
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
    except OSError as exc:
        logger.error("students.json yozishda xatolik: %s", exc)


# ---------------------------------------------------------------------------
# Yordamchi funksiyalar
# ---------------------------------------------------------------------------


def _current_savol(context: ContextTypes.DEFAULT_TYPE) -> int:
    idx = context.user_data.get("written_index", 0)
    return WRITTEN_SAVOLLAR[idx]


async def _ask_for_written(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    savol = _current_savol(context)
    await update.message.reply_text(
        f"{savol}-savol uchun qo'lyozma yechimingizni rasm yoki PDF sifatida yuboring."
    )
    return WRITTEN_FILE


async def _record_ball_and_advance(
    update: Update, context: ContextTypes.DEFAULT_TYPE, ball: int, izoh: str
) -> int:
    savol = _current_savol(context)
    context.user_data.setdefault("yozma_natijalar", {})[savol] = {"ball": ball, "izoh": izoh}

    idx = context.user_data.get("written_index", 0) + 1
    context.user_data["written_index"] = idx

    if idx < len(WRITTEN_SAVOLLAR):
        return await _ask_for_written(update, context)

    return await _finalize(update, context)


async def _finalize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ism = context.user_data["ism"]
    test_raw = context.user_data["test_raw"]
    yozma_natijalar: dict[int, dict] = context.user_data.get("yozma_natijalar", {})
    yozma_raw = sum(item["ball"] for item in yozma_natijalar.values())

    natija = rasch.calculate_result(test_raw, yozma_raw)

    izohlar_matni = "\n".join(
        f"  {savol}-savol: {yozma_natijalar[savol]['ball']} ball — {yozma_natijalar[savol]['izoh']}"
        for savol in WRITTEN_SAVOLLAR
        if savol in yozma_natijalar
    )

    xabar = (
        f"📊 {ism} uchun yakuniy natija\n\n"
        f"— Test qismi (1-40) —\n"
        f"Xom ball: {natija.test.raw:.0f} / {natija.test.max_raw:.0f}\n"
        f"Logit: {natija.test.logit:.3f}\n"
        f"Skalalangan ball: {natija.test.scaled:.2f}\n\n"
        f"— Yozma ish qismi (41-43) —\n"
        f"Xom ball: {natija.yozma.raw:.0f} / {natija.yozma.max_raw:.0f}\n"
        f"Logit: {natija.yozma.logit:.3f}\n"
        f"Skalalangan ball: {natija.yozma.scaled:.2f}\n\n"
        f"{izohlar_matni}\n\n"
        f"🏆 Umumiy ball: {natija.umumiy_ball:.2f}\n"
        f"🎓 Daraja: {natija.daraja}"
        f"{DISCLAIMER}"
    )
    await update.message.reply_text(xabar, reply_markup=ReplyKeyboardRemove())

    record = {
        "ism": ism,
        "sana": datetime.now().isoformat(timespec="seconds"),
        "test_xom": test_raw,
        "yozma_xom": yozma_raw,
        "yozma_natijalar": yozma_natijalar,
        "test_scaled": round(natija.test.scaled, 2),
        "yozma_scaled": round(natija.yozma.scaled, 2),
        "umumiy_ball": round(natija.umumiy_ball, 2),
        "daraja": natija.daraja,
    }
    save_student(record)

    context.user_data.clear()
    return ConversationHandler.END


async def _download_telegram_file(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> tuple[bytes, str] | None:
    message = update.message
    if message.photo:
        tg_file = await context.bot.get_file(message.photo[-1].file_id)
        filename = "photo.jpg"
    elif message.document:
        tg_file = await context.bot.get_file(message.document.file_id)
        filename = message.document.file_name or "document"
    else:
        return None

    file_bytes = bytes(await tg_file.download_as_bytearray())
    return file_bytes, filename


# ---------------------------------------------------------------------------
# Handler funksiyalari
# ---------------------------------------------------------------------------


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    await update.message.reply_text(
        "Assalomu alaykum! Kimyo fanidan milliy sertifikat natijalarini "
        "Rasch modeli asosida baholovchi botga xush kelibsiz.\n\n"
        "Iltimos, ism-familiyangizni kiriting:"
    )
    return NAME


async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ism = (update.message.text or "").strip()
    if not ism:
        await update.message.reply_text("Ism bo'sh bo'lishi mumkin emas. Qaytadan kiriting:")
        return NAME

    context.user_data["ism"] = ism
    await update.message.reply_text(
        "1-40 savollardan nechtasiga to'g'ri javob berdingiz? (0 dan 40 gacha butun son kiriting)"
    )
    return TEST_SCORE


async def receive_test_score(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    matn = (update.message.text or "").strip()
    try:
        ball = int(matn)
    except ValueError:
        await update.message.reply_text(
            "Iltimos, 0 dan 40 gacha butun son kiriting (masalan: 32)."
        )
        return TEST_SCORE

    if not (0 <= ball <= 40):
        await update.message.reply_text("Ball 0 dan 40 gacha bo'lishi kerak. Qaytadan kiriting:")
        return TEST_SCORE

    context.user_data["test_raw"] = ball
    context.user_data["written_index"] = 0
    context.user_data["yozma_natijalar"] = {}

    await update.message.reply_text(
        f"Qabul qilindi: {ball}/40.\n\nEndi 41, 42, 43-savollar uchun qo'lyozma "
        "yechimlaringizni navbat bilan yuborasiz."
    )
    return await _ask_for_written(update, context)


async def receive_written_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    savol = _current_savol(context)

    downloaded = await _download_telegram_file(update, context)
    if downloaded is None:
        await update.message.reply_text(
            f"Iltimos, {savol}-savol uchun rasm yoki PDF fayl yuboring (matn emas)."
        )
        return WRITTEN_FILE

    file_bytes, filename = downloaded
    await update.message.reply_text("🤖 AI orqali baholanmoqda...")

    try:
        client = get_anthropic_client()
        natija = await asyncio.to_thread(
            grading.grade_written_answer, client, savol, file_bytes, filename
        )
    except Exception as exc:  # noqa: BLE001
        logger.error("Baholashda kutilmagan xatolik (savol %s): %s", savol, exc)
        context.user_data["awaiting_manual_for"] = savol
        await update.message.reply_text(
            "AI baholashda xatolik yuz berdi. Iltimos, ushbu savol uchun ballni "
            "qo'lda kiriting (0-25):"
        )
        return MANUAL_BALL

    if natija.xato:
        context.user_data["awaiting_manual_for"] = savol
        await update.message.reply_text(
            f"⚠️ {natija.izoh}\n\nIltimos, {savol}-savol uchun ballni qo'lda kiriting (0-25):"
        )
        return MANUAL_BALL

    await update.message.reply_text(
        f"✅ {savol}-savol baholandi: {natija.ball}/25 ball\nIzoh: {natija.izoh}"
    )
    return await _record_ball_and_advance(update, context, natija.ball, natija.izoh)


async def receive_written_wrong_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    savol = _current_savol(context)
    await update.message.reply_text(f"Iltimos, {savol}-savol uchun rasm yoki PDF yuboring.")
    return WRITTEN_FILE


async def receive_manual_ball(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    matn = (update.message.text or "").strip()
    try:
        ball = int(matn)
    except ValueError:
        await update.message.reply_text("Iltimos, 0 dan 25 gacha butun son kiriting.")
        return MANUAL_BALL

    if not (0 <= ball <= 25):
        await update.message.reply_text("Ball 0 dan 25 gacha bo'lishi kerak. Qaytadan kiriting:")
        return MANUAL_BALL

    context.user_data.pop("awaiting_manual_for", None)
    return await _record_ball_and_advance(update, context, ball, "Qo'lda kiritilgan ball")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    await update.message.reply_text(
        "Suhbat bekor qilindi. Qaytadan boshlash uchun /start buyrug'ini yuboring.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


async def royxat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    students = load_students()
    if not students:
        await update.message.reply_text("Hozircha saqlangan natijalar yo'q.")
        return

    qatorlar = ["Ism | Umumiy ball | Daraja", "-" * 30]
    for s in students:
        qatorlar.append(f"{s.get('ism', '-')} | {s.get('umumiy_ball', '-')} | {s.get('daraja', '-')}")

    await update.message.reply_text("📋 Saqlangan talabgorlar:\n\n" + "\n".join(qatorlar))


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Xatolik yuz berdi: %s", context.error, exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "Kutilmagan xatolik yuz berdi. Iltimos, /bekor buyrug'i bilan qaytadan boshlang."
            )
        except Exception:  # noqa: BLE001
            pass


def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN topilmadi. .env fayliga TELEGRAM_BOT_TOKEN qiymatini kiriting."
        )
    if not ANTHROPIC_API_KEY:
        raise RuntimeError(
            "ANTHROPIC_API_KEY topilmadi. .env fayliga ANTHROPIC_API_KEY qiymatini kiriting."
        )

    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)],
            TEST_SCORE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_test_score)],
            WRITTEN_FILE: [
                MessageHandler(filters.PHOTO | filters.Document.ALL, receive_written_file),
                MessageHandler(filters.TEXT & ~filters.COMMAND, receive_written_wrong_type),
            ],
            MANUAL_BALL: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_manual_ball)],
        },
        fallbacks=[CommandHandler("bekor", cancel)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("royxat", royxat))
    application.add_error_handler(error_handler)

    logger.info("Bot ishga tushdi...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
