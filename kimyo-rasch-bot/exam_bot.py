"""Kimyogar bot (@Kimyo_Rasch_bot) — rebuilt from the recovered database
schema after the original source was lost. Core flows: exam key entry with
photo-based grading, homework, lessons, streaks, AI Q&A and a small admin
panel for teachers.
"""
import json
import logging
import os
from datetime import datetime

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

import db
import grading

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("exam_bot")

BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_IDS = {int(x) for x in os.environ.get("ADMIN_IDS", "").replace(" ", "").split(",") if x}
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "")

# ---- menu ----
BTN_NEW_EXAM = "📝 Yangi imtihon"
BTN_ENTER_KEY = "🔑 Kalit kiritish"
BTN_UPLOAD_LESSON = "🎥 Dars yuklash"
BTN_HOMEWORK = "📋 Uy vazifasi"
BTN_QUESTIONS = "📝 Savol matnlari"
BTN_STATUS = "📊 Holat"
BTN_PDF = "📄 PDF Natijalar"
BTN_ACTIVITY = "📈 Faollik"
BTN_STUDENTS = "👥 Imtihonchilar"

STUDENT_MENU = [
    [BTN_ENTER_KEY, BTN_HOMEWORK],
    [BTN_QUESTIONS],
    [BTN_STATUS, BTN_PDF],
    [BTN_ACTIVITY],
]
ADMIN_MENU = [
    [BTN_NEW_EXAM, BTN_ENTER_KEY],
    [BTN_UPLOAD_LESSON, BTN_HOMEWORK],
    [BTN_QUESTIONS],
    [BTN_STATUS, BTN_PDF],
    [BTN_ACTIVITY, BTN_STUDENTS],
]

# ---- conversation states ----
(
    KEY_WAIT_CODE,
    KEY_WAIT_PHOTO_41,
    KEY_WAIT_PHOTO_42,
    KEY_WAIT_PHOTO_43,
) = range(4)

(
    NEWEXAM_SUBJECT,
    NEWEXAM_CODE,
    NEWEXAM_ANSWERS,
    NEWEXAM_DEADLINE,
    NEWEXAM_MINSCORE,
) = range(10, 15)

(LESSON_TOPIC, LESSON_VIDEO) = range(20, 22)

(HW_ANSWERING,) = range(30, 31)

(QUESTION_WAIT,) = range(40, 41)


def main_menu(user_id):
    rows = ADMIN_MENU if user_id in ADMIN_IDS else STUDENT_MENU
    return ReplyKeyboardMarkup(rows, resize_keyboard=True)


def is_admin(user_id):
    return user_id in ADMIN_IDS


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bekor qilindi.", reply_markup=main_menu(update.effective_user.id))
    context.user_data.clear()
    return ConversationHandler.END


# ---------------------------------------------------------------- /start ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    db.upsert_user(u.id, u.username, u.full_name)
    await update.message.reply_text(
        f"Assalomu alaykum, {u.first_name}! 👋\n\n"
        "Kimyogar botga xush kelibsiz. Quyidagi menyudan foydalaning.",
        reply_markup=main_menu(u.id),
    )


# ---------------------------------------------------------- Kalit kiritish ---

async def enter_key_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Imtihon kalitini (4 xonali kod) kiriting:")
    return KEY_WAIT_CODE


async def enter_key_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()
    exam = db.get_exam_by_code(code)
    if not exam:
        await update.message.reply_text("Bunday kalit topilmadi yoki imtihon faol emas. Qaytadan kiriting yoki /cancel.")
        return KEY_WAIT_CODE

    u = update.effective_user
    existing = db.get_submission(u.id, exam["id"])
    if existing and existing["is_complete"]:
        await update.message.reply_text(
            f"Siz bu imtihonni ({exam['subject']}) allaqachon topshirgansiz. "
            f"Natija: {existing['final_score']}",
            reply_markup=main_menu(u.id),
        )
        return ConversationHandler.END

    db.start_submission(u.id, exam["id"], u.full_name)
    context.user_data["exam"] = dict(exam)
    await update.message.reply_text(
        f"✅ Kalit qabul qilindi: {exam['subject']}\n\n"
        "Endi javoblaringiz yozilgan 1-varaqning (41-bet) rasmini yuboring."
    )
    return KEY_WAIT_PHOTO_41


async def _handle_answer_photo(update: Update, context: ContextTypes.DEFAULT_TYPE, page: str, next_state, next_prompt):
    exam = context.user_data.get("exam")
    if not exam:
        await update.message.reply_text("Avval /start orqali kalit kiriting.")
        return ConversationHandler.END

    photo = update.message.photo[-1]
    file = await photo.get_file()
    photo_bytes = await file.download_as_bytearray()
    answer_key = json.loads(exam["answer_key"] or "{}")

    await update.message.reply_text("Rasm tekshirilmoqda, biroz kuting...")
    score, feedback = grading.grade_answer_photo(bytes(photo_bytes), "image/jpeg", answer_key, page)
    db.save_submission_photo(update.effective_user.id, exam["id"], page.split("_")[-1], photo.file_id, score)

    await update.message.reply_text(f"Ball: {score:.0f}/100\n{feedback}")

    if next_state is None:
        subs = db.get_submission(update.effective_user.id, exam["id"])
        scores = [s for s in (subs["score_41"], subs["score_42"], subs["score_43"]) if s is not None]
        final = sum(scores) / len(scores) if scores else 0
        grade = "O'tdi ✅" if final >= exam["min_score"] else "O'tmadi ❌"
        db.finish_submission(update.effective_user.id, exam["id"], final, grade, len(scores))
        db.bump_streak(update.effective_user.id)
        await update.message.reply_text(
            f"🏁 Imtihon yakunlandi!\n\nYakuniy ball: {final:.0f}/100\nNatija: {grade}",
            reply_markup=main_menu(update.effective_user.id),
        )
        context.user_data.pop("exam", None)
        return ConversationHandler.END

    await update.message.reply_text(next_prompt)
    return next_state


async def enter_key_photo_41(update, context):
    return await _handle_answer_photo(update, context, "photo_41", KEY_WAIT_PHOTO_42, "Endi 2-varaqning (42-bet) rasmini yuboring.")


async def enter_key_photo_42(update, context):
    return await _handle_answer_photo(update, context, "photo_42", KEY_WAIT_PHOTO_43, "Endi 3-varaqning (43-bet) rasmini yuboring.")


async def enter_key_photo_43(update, context):
    return await _handle_answer_photo(update, context, "photo_43", None, "")


# -------------------------------------------------------------- Yangi imtihon (admin) ---

async def new_exam_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Bu funksiya faqat adminlar uchun.")
        return ConversationHandler.END
    await update.message.reply_text("Yangi imtihon mavzusini kiriting (masalan: 'Murakkab efirlar'):")
    return NEWEXAM_SUBJECT


async def new_exam_subject(update, context):
    context.user_data["new_exam"] = {"subject": update.message.text.strip()}
    await update.message.reply_text(
        "Kalit kodini kiriting (4 xonali raqam), yoki 'auto' deb yozing avtomatik yaratish uchun:"
    )
    return NEWEXAM_CODE


async def new_exam_code(update, context):
    import random

    code = update.message.text.strip()
    if code.lower() == "auto":
        code = str(random.randint(1000, 9999))
    context.user_data["new_exam"]["code"] = code
    await update.message.reply_text(
        "Javoblar kalitini JSON ko'rinishida kiriting.\n"
        'Masalan: {"1": "A", "2": "C", "3": "B"}'
    )
    return NEWEXAM_ANSWERS


async def new_exam_answers(update, context):
    try:
        answer_key = json.loads(update.message.text.strip())
    except json.JSONDecodeError:
        await update.message.reply_text("JSON formatida xato bor, qaytadan urinib ko'ring.")
        return NEWEXAM_ANSWERS
    context.user_data["new_exam"]["answer_key"] = answer_key
    await update.message.reply_text("Muddatini kiriting (YYYY-MM-DD HH:MM), yoki 'yoq' deb yozing:")
    return NEWEXAM_DEADLINE


async def new_exam_deadline(update, context):
    text = update.message.text.strip()
    context.user_data["new_exam"]["deadline"] = None if text.lower() == "yoq" else text
    await update.message.reply_text("O'tish balli neча foiz bo'lsin? (masalan: 60)")
    return NEWEXAM_MINSCORE


async def new_exam_minscore(update, context):
    try:
        min_score = int(update.message.text.strip())
    except ValueError:
        await update.message.reply_text("Raqam kiriting, masalan: 60")
        return NEWEXAM_MINSCORE

    data = context.user_data.pop("new_exam")
    db.create_exam(data["subject"], data["code"], data["answer_key"], data["deadline"], min_score)
    await update.message.reply_text(
        f"✅ Imtihon yaratildi!\n\nMavzu: {data['subject']}\nKalit: `{data['code']}`",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=main_menu(update.effective_user.id),
    )
    return ConversationHandler.END


# -------------------------------------------------------------- Dars yuklash (admin) ---

async def lesson_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Bu funksiya faqat adminlar uchun.")
        return ConversationHandler.END
    await update.message.reply_text("Dars mavzusini kiriting:")
    return LESSON_TOPIC


async def lesson_topic(update, context):
    context.user_data["lesson_topic"] = update.message.text.strip()
    await update.message.reply_text("Endi video darsni yuboring:")
    return LESSON_VIDEO


async def lesson_video(update, context):
    video = update.message.video or update.message.document
    if not video:
        await update.message.reply_text("Iltimos, video fayl yuboring.")
        return LESSON_VIDEO
    topic = context.user_data.pop("lesson_topic")
    db.add_lesson(topic, video.file_id)
    await update.message.reply_text(
        f"✅ '{topic}' darsi yuklandi.", reply_markup=main_menu(update.effective_user.id)
    )
    return ConversationHandler.END


# ------------------------------------------------------------------ Uy vazifasi ---

async def homework_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sets = db.list_homework_sets()
    if not sets:
        await update.message.reply_text("Hozircha uy vazifalari mavjud emas.")
        return
    buttons = [
        [InlineKeyboardButton(f"{s['topic']} ({s['n']} savol)", callback_data=f"hw:{s['hw_code']}")]
        for s in sets
    ]
    await update.message.reply_text("Uy vazifasini tanlang:", reply_markup=InlineKeyboardMarkup(buttons))


async def homework_pick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    hw_code = query.data.split(":", 1)[1]
    items = db.get_homework_set(hw_code)
    if not items:
        await query.edit_message_text("Bu vazifa topilmadi.")
        return
    context.user_data["hw_code"] = hw_code
    context.user_data["hw_items"] = [dict(i) for i in items]
    context.user_data["hw_index"] = 0
    await query.edit_message_text(f"'{items[0]['topic']}' vazifasi boshlandi ({len(items)} savol).")
    await _send_next_homework_question(update.effective_chat.id, context)


async def _send_next_homework_question(chat_id, context: ContextTypes.DEFAULT_TYPE):
    items = context.user_data.get("hw_items", [])
    idx = context.user_data.get("hw_index", 0)
    if idx >= len(items):
        await context.bot.send_message(
            chat_id, "🎉 Uy vazifasi tugadi! Yaxshi ishladingiz.",
        )
        context.user_data.pop("hw_items", None)
        context.user_data.pop("hw_index", None)
        return
    item = items[idx]
    text = f"{item['number']}. {item['question']}"
    if item["answer_type"] == "abcd":
        buttons = [
            [InlineKeyboardButton(letter, callback_data=f"hwans:{item['id']}:{letter}") for letter in "ABCD"]
        ]
        await context.bot.send_message(chat_id, text, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await context.bot.send_message(chat_id, text + "\n\n(Javobingizni matn sifatida yozing)")


async def homework_answer_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    _, hw_id, letter = query.data.split(":")
    items = context.user_data.get("hw_items", [])
    idx = context.user_data.get("hw_index", 0)
    item = items[idx] if idx < len(items) else None
    if item is None or str(item["id"]) != hw_id:
        return
    is_correct = letter.strip().upper() == item["answer"].strip().upper()
    db.save_homework_result(update.effective_user.id, item["id"], is_correct, student_answers=letter)
    result_label = "✅ To'g'ri" if is_correct else "❌ Xato"
    await query.edit_message_text(
        query.message.text + f"\n\nJavobingiz: {letter} — {result_label}"
    )
    context.user_data["hw_index"] = idx + 1
    db.bump_streak(update.effective_user.id)
    await _send_next_homework_question(update.effective_chat.id, context)


async def homework_answer_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = context.user_data.get("hw_items")
    if not items:
        return False
    idx = context.user_data.get("hw_index", 0)
    if idx >= len(items):
        return False
    item = items[idx]
    student_answer = update.message.text.strip()
    is_correct = student_answer.lower() == item["answer"].strip().lower()
    db.save_homework_result(update.effective_user.id, item["id"], is_correct, student_answers=student_answer)
    await update.message.reply_text("✅ To'g'ri!" if is_correct else f"❌ Xato. To'g'ri javob: {item['answer']}")
    context.user_data["hw_index"] = idx + 1
    db.bump_streak(update.effective_user.id)
    await _send_next_homework_question(update.effective_chat.id, context)
    return True


# ------------------------------------------------------------------- Savol matnlari (AI) ---

async def question_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kimyo bo'yicha savolingizni yozing:")
    return QUESTION_WAIT


async def question_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    ok, count, limit = db.check_and_bump_ai_limit(u.id)
    if not ok:
        await update.message.reply_text(
            f"Kunlik AI savollar limiti ({limit} ta) tugadi. Ertaga qayta urining.",
            reply_markup=main_menu(u.id),
        )
        return ConversationHandler.END

    await update.message.reply_text("Javob tayyorlanmoqda...")
    answer = grading.ask_chemistry_question(update.message.text.strip())
    db.log_question(u.id, update.message.text.strip(), answer)
    await update.message.reply_text(
        f"{answer}\n\n({count}/{limit} kunlik savol ishlatildi)",
        reply_markup=main_menu(u.id),
    )
    return ConversationHandler.END


# ------------------------------------------------------------------------------- Holat ---

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    subs = db.list_submissions_for_user(u.id)
    streak = db.get_streak(u.id)
    lines = [f"📊 <b>{u.full_name}</b> uchun holat:\n"]
    if subs:
        lines.append("<b>Imtihonlar:</b>")
        for s in subs:
            status_icon = "✅" if s["is_complete"] else "⏳"
            score = f"{s['final_score']:.0f}" if s["final_score"] is not None else "—"
            lines.append(f"{status_icon} {s['subject']}: {score}")
    else:
        lines.append("Hali imtihon topshirmagansiz.")
    if streak:
        lines.append(f"\n🔥 Faollik: {streak['count']} kun (rekord: {streak['max_streak']})")
    await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.HTML)


# --------------------------------------------------------------------------- PDF Natijalar ---

async def pdf_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from fpdf import FPDF

    u = update.effective_user
    subs = db.list_submissions_for_user(u.id)
    if not subs:
        await update.message.reply_text("Hali natijangiz yo'q.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=14)
    pdf.cell(0, 10, "Kimyogar bot - Natijalar", ln=True)
    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 8, f"O'quvchi: {u.full_name}", ln=True)
    pdf.ln(4)
    for s in subs:
        score = f"{s['final_score']:.0f}" if s["final_score"] is not None else "-"
        pdf.cell(0, 8, f"- {s['subject']}: {score}/100 ({s['grade'] or ''})", ln=True)

    out_path = f"/tmp/natija_{u.id}.pdf"
    pdf.output(out_path)
    await update.message.reply_document(document=open(out_path, "rb"), filename="natijalar.pdf")
    os.remove(out_path)


# -------------------------------------------------------------------------------- Faollik ---

async def activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    count, max_streak, is_new = db.bump_streak(u.id)
    msg = f"🔥 Joriy faollik: {count} kun ketma-ket\n🏆 Rekord: {max_streak} kun"
    if is_new and count > 1:
        msg = "Ajoyib, davom eting! 👏\n\n" + msg
    await update.message.reply_text(msg)


# -------------------------------------------------------------------------- Imtihonchilar (admin) ---

async def students(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("Bu funksiya faqat adminlar uchun.")
        return
    total = db.count_users()
    rows = db.list_users(limit=30)
    lines = [f"👥 Jami o'quvchilar: {total}\n"]
    for r in rows:
        uname = f"@{r['username']}" if r["username"] else "—"
        lines.append(f"{r['user_id']} — {r['full_name']} ({uname})")
    text = "\n".join(lines)
    for chunk_start in range(0, len(text), 3500):
        await update.message.reply_text(text[chunk_start:chunk_start + 3500])


# ------------------------------------------------------------------------------------ misc ---

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await homework_answer_text(update, context):
        return
    await update.message.reply_text(
        "Menyudan birini tanlang.", reply_markup=main_menu(update.effective_user.id)
    )


def build_app():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(filters.Regex(f"^{BTN_ENTER_KEY}$"), enter_key_start)],
            states={
                KEY_WAIT_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_key_code)],
                KEY_WAIT_PHOTO_41: [MessageHandler(filters.PHOTO, enter_key_photo_41)],
                KEY_WAIT_PHOTO_42: [MessageHandler(filters.PHOTO, enter_key_photo_42)],
                KEY_WAIT_PHOTO_43: [MessageHandler(filters.PHOTO, enter_key_photo_43)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )
    )

    app.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(filters.Regex(f"^{BTN_NEW_EXAM}$"), new_exam_start)],
            states={
                NEWEXAM_SUBJECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, new_exam_subject)],
                NEWEXAM_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, new_exam_code)],
                NEWEXAM_ANSWERS: [MessageHandler(filters.TEXT & ~filters.COMMAND, new_exam_answers)],
                NEWEXAM_DEADLINE: [MessageHandler(filters.TEXT & ~filters.COMMAND, new_exam_deadline)],
                NEWEXAM_MINSCORE: [MessageHandler(filters.TEXT & ~filters.COMMAND, new_exam_minscore)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )
    )

    app.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(filters.Regex(f"^{BTN_UPLOAD_LESSON}$"), lesson_start)],
            states={
                LESSON_TOPIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, lesson_topic)],
                LESSON_VIDEO: [MessageHandler(filters.VIDEO | filters.Document.VIDEO, lesson_video)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )
    )

    app.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(filters.Regex(f"^{BTN_QUESTIONS}$"), question_start)],
            states={
                QUESTION_WAIT: [MessageHandler(filters.TEXT & ~filters.COMMAND, question_answer)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )
    )

    app.add_handler(MessageHandler(filters.Regex(f"^{BTN_HOMEWORK}$"), homework_menu))
    app.add_handler(CallbackQueryHandler(homework_pick, pattern=r"^hw:"))
    app.add_handler(CallbackQueryHandler(homework_answer_callback, pattern=r"^hwans:"))

    app.add_handler(MessageHandler(filters.Regex(f"^{BTN_STATUS}$"), status))
    app.add_handler(MessageHandler(filters.Regex(f"^{BTN_PDF}$"), pdf_results))
    app.add_handler(MessageHandler(filters.Regex(f"^{BTN_ACTIVITY}$"), activity))
    app.add_handler(MessageHandler(filters.Regex(f"^{BTN_STUDENTS}$"), students))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))

    return app


def main():
    db.init_db()
    app = build_app()
    log.info("Kimyogar bot ishga tushdi (polling).")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
