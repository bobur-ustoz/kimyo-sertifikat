"""SQLite access layer for the Kimyogar exam bot.

Schema matches the recovered production database exactly (see
exam_bot_RECOVERED.db) so the bot keeps working with existing users,
exams, submissions and homework without any migration.
"""
import os
import sqlite3
import json
from contextlib import contextmanager
from datetime import datetime

DB_PATH = os.environ.get("DB_PATH", "/data/exam_bot.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    user_id    INTEGER PRIMARY KEY,
    username   TEXT    DEFAULT '',
    full_name  TEXT    DEFAULT '',
    created_at TEXT    DEFAULT (datetime('now','localtime')),
    grade TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS exams (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    subject    TEXT    NOT NULL,
    code       TEXT    UNIQUE,
    answer_key TEXT    NOT NULL DEFAULT '{}',
    deadline   TEXT,
    min_score  INTEGER DEFAULT 60,
    is_active  INTEGER DEFAULT 1,
    created_at TEXT    DEFAULT (datetime('now','localtime')),
    exam_type TEXT
);
CREATE TABLE IF NOT EXISTS submissions (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      INTEGER NOT NULL,
    exam_id      INTEGER NOT NULL,
    full_name    TEXT    DEFAULT '',
    answers      TEXT    DEFAULT '{}',
    photo_41     TEXT,
    photo_42     TEXT,
    photo_43     TEXT,
    score        REAL    DEFAULT 0,
    total        INTEGER DEFAULT 0,
    score_41     REAL    DEFAULT NULL,
    score_42     REAL    DEFAULT NULL,
    score_43     REAL    DEFAULT NULL,
    final_score  REAL    DEFAULT NULL,
    grade        TEXT    DEFAULT NULL,
    is_complete  INTEGER DEFAULT 0,
    submitted_at TEXT    DEFAULT (datetime('now','localtime')),
    UNIQUE(user_id, exam_id)
);
CREATE TABLE IF NOT EXISTS lessons (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    topic      TEXT NOT NULL,
    file_id    TEXT NOT NULL,
    transcript TEXT DEFAULT '',
    created_at TEXT DEFAULT (datetime('now','localtime'))
);
CREATE TABLE IF NOT EXISTS lesson_views (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL,
    lesson_id  INTEGER NOT NULL,
    viewed_at  TEXT DEFAULT (datetime('now','localtime'))
);
CREATE TABLE IF NOT EXISTS homework (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    topic       TEXT DEFAULT '',
    number      INTEGER,
    question    TEXT DEFAULT '',
    answer      TEXT NOT NULL,
    answer_type TEXT DEFAULT 'abcd',
    created_at  TEXT DEFAULT (datetime('now','localtime')),
    total INTEGER DEFAULT 0, hw_set_id INTEGER DEFAULT 1, hw_code TEXT DEFAULT '', hw_group_id INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS homework_results (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL,
    homework_id INTEGER NOT NULL,
    is_correct  INTEGER DEFAULT 0,
    submitted_at TEXT DEFAULT (datetime('now','localtime')),
    photo_file_id TEXT, student_answers TEXT, checked INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS questions_log (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL,
    question   TEXT NOT NULL,
    answer     TEXT,
    asked_at   TEXT DEFAULT (datetime('now','localtime'))
);
CREATE TABLE IF NOT EXISTS ai_limit (
    user_id      INTEGER PRIMARY KEY,
    day_count    INTEGER DEFAULT 0,
    day_date     TEXT DEFAULT '',
    last_asked   TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS streak (
    user_id     INTEGER PRIMARY KEY,
    count       INTEGER DEFAULT 0,
    last_date   TEXT DEFAULT '',
    max_streak  INTEGER DEFAULT 0,
    notified    INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS tahlil (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_code  TEXT NOT NULL,
    number     INTEGER NOT NULL,
    text       TEXT DEFAULT '',
    voice_id   TEXT DEFAULT '',
    created_at TEXT DEFAULT (datetime('now','localtime')),
    UNIQUE(exam_code, number)
);
CREATE TABLE IF NOT EXISTS solved_examples (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    mavzu               TEXT NOT NULL,
    qiyinlik            INTEGER DEFAULT 1,
    masala_matni        TEXT NOT NULL,
    yechim_bosqichlari  TEXT DEFAULT '[]',
    yakuniy_javob       TEXT NOT NULL,
    embedding           TEXT DEFAULT '[]',
    ishlatilgan_marta   INTEGER DEFAULT 0,
    created_at          TEXT DEFAULT (datetime('now','localtime'))
);
"""


def init_db():
    with get_conn() as con:
        con.executescript(SCHEMA)


@contextmanager
def get_conn():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def today():
    return datetime.now().strftime("%Y-%m-%d")


# ---- users ----

def upsert_user(user_id, username, full_name):
    with get_conn() as con:
        con.execute(
            "INSERT INTO users (user_id, username, full_name) VALUES (?, ?, ?) "
            "ON CONFLICT(user_id) DO UPDATE SET username=excluded.username, full_name=excluded.full_name",
            (user_id, username or "", full_name or ""),
        )


def is_admin(user_id, admin_ids):
    return user_id in admin_ids


def count_users():
    with get_conn() as con:
        return con.execute("SELECT COUNT(*) c FROM users").fetchone()["c"]


def list_users(limit=50):
    with get_conn() as con:
        return con.execute(
            "SELECT * FROM users ORDER BY created_at DESC LIMIT ?", (limit,)
        ).fetchall()


# ---- exams ----

def create_exam(subject, code, answer_key, deadline, min_score, exam_type=None):
    with get_conn() as con:
        con.execute(
            "INSERT INTO exams (subject, code, answer_key, deadline, min_score, exam_type) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (subject, code, json.dumps(answer_key, ensure_ascii=False), deadline, min_score, exam_type),
        )


def get_exam_by_code(code):
    with get_conn() as con:
        return con.execute(
            "SELECT * FROM exams WHERE code = ? AND is_active = 1", (code,)
        ).fetchone()


def list_exams(active_only=False):
    with get_conn() as con:
        q = "SELECT * FROM exams"
        if active_only:
            q += " WHERE is_active = 1"
        q += " ORDER BY created_at DESC"
        return con.execute(q).fetchall()


def deactivate_exam(exam_id):
    with get_conn() as con:
        con.execute("UPDATE exams SET is_active = 0 WHERE id = ?", (exam_id,))


# ---- submissions ----

def get_submission(user_id, exam_id):
    with get_conn() as con:
        return con.execute(
            "SELECT * FROM submissions WHERE user_id = ? AND exam_id = ?",
            (user_id, exam_id),
        ).fetchone()


def start_submission(user_id, exam_id, full_name):
    with get_conn() as con:
        con.execute(
            "INSERT INTO submissions (user_id, exam_id, full_name) VALUES (?, ?, ?) "
            "ON CONFLICT(user_id, exam_id) DO UPDATE SET full_name=excluded.full_name",
            (user_id, exam_id, full_name),
        )


def save_submission_photo(user_id, exam_id, page, file_id, score):
    col_photo = f"photo_{page}"
    col_score = f"score_{page}"
    with get_conn() as con:
        con.execute(
            f"UPDATE submissions SET {col_photo} = ?, {col_score} = ? "
            "WHERE user_id = ? AND exam_id = ?",
            (file_id, score, user_id, exam_id),
        )


def finish_submission(user_id, exam_id, final_score, grade, total):
    with get_conn() as con:
        con.execute(
            "UPDATE submissions SET final_score = ?, grade = ?, total = ?, "
            "is_complete = 1, submitted_at = ? WHERE user_id = ? AND exam_id = ?",
            (final_score, grade, total, now(), user_id, exam_id),
        )


def list_submissions_for_exam(exam_id):
    with get_conn() as con:
        return con.execute(
            "SELECT * FROM submissions WHERE exam_id = ? ORDER BY final_score DESC",
            (exam_id,),
        ).fetchall()


def list_submissions_for_user(user_id):
    with get_conn() as con:
        return con.execute(
            "SELECT s.*, e.subject FROM submissions s JOIN exams e ON e.id = s.exam_id "
            "WHERE s.user_id = ? ORDER BY s.submitted_at DESC",
            (user_id,),
        ).fetchall()


# ---- lessons ----

def add_lesson(topic, file_id, transcript=""):
    with get_conn() as con:
        con.execute(
            "INSERT INTO lessons (topic, file_id, transcript) VALUES (?, ?, ?)",
            (topic, file_id, transcript),
        )


def list_lessons():
    with get_conn() as con:
        return con.execute("SELECT * FROM lessons ORDER BY created_at DESC").fetchall()


def log_lesson_view(user_id, lesson_id):
    with get_conn() as con:
        con.execute(
            "INSERT INTO lesson_views (user_id, lesson_id) VALUES (?, ?)",
            (user_id, lesson_id),
        )


# ---- homework ----

def add_homework(topic, number, question, answer, answer_type, total, hw_set_id, hw_code, hw_group_id=0):
    with get_conn() as con:
        con.execute(
            "INSERT INTO homework (topic, number, question, answer, answer_type, total, hw_set_id, hw_code, hw_group_id) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (topic, number, question, answer, answer_type, total, hw_set_id, hw_code, hw_group_id),
        )


def get_homework_set(hw_code):
    with get_conn() as con:
        return con.execute(
            "SELECT * FROM homework WHERE hw_code = ? ORDER BY number", (hw_code,)
        ).fetchall()


def list_homework_sets():
    with get_conn() as con:
        return con.execute(
            "SELECT hw_code, topic, COUNT(*) n FROM homework WHERE hw_code != '' "
            "GROUP BY hw_code ORDER BY MAX(created_at) DESC"
        ).fetchall()


def save_homework_result(user_id, homework_id, is_correct, student_answers=None, photo_file_id=None):
    with get_conn() as con:
        con.execute(
            "INSERT INTO homework_results (user_id, homework_id, is_correct, student_answers, photo_file_id) "
            "VALUES (?, ?, ?, ?, ?)",
            (user_id, homework_id, int(is_correct), student_answers, photo_file_id),
        )


def homework_progress(user_id, hw_code):
    with get_conn() as con:
        return con.execute(
            "SELECT hr.* FROM homework_results hr JOIN homework h ON h.id = hr.homework_id "
            "WHERE hr.user_id = ? AND h.hw_code = ?",
            (user_id, hw_code),
        ).fetchall()


# ---- AI question log & daily limit ----

def log_question(user_id, question, answer):
    with get_conn() as con:
        con.execute(
            "INSERT INTO questions_log (user_id, question, answer) VALUES (?, ?, ?)",
            (user_id, question, answer),
        )


def check_and_bump_ai_limit(user_id, daily_limit=10):
    with get_conn() as con:
        row = con.execute("SELECT * FROM ai_limit WHERE user_id = ?", (user_id,)).fetchone()
        today_str = today()
        if row is None:
            con.execute(
                "INSERT INTO ai_limit (user_id, day_count, day_date, last_asked) VALUES (?, 1, ?, ?)",
                (user_id, today_str, now()),
            )
            return True, 1, daily_limit
        if row["day_date"] != today_str:
            con.execute(
                "UPDATE ai_limit SET day_count = 1, day_date = ?, last_asked = ? WHERE user_id = ?",
                (today_str, now(), user_id),
            )
            return True, 1, daily_limit
        if row["day_count"] >= daily_limit:
            return False, row["day_count"], daily_limit
        new_count = row["day_count"] + 1
        con.execute(
            "UPDATE ai_limit SET day_count = ?, last_asked = ? WHERE user_id = ?",
            (new_count, now(), user_id),
        )
        return True, new_count, daily_limit


# ---- streak ----

def bump_streak(user_id):
    """Call once per day a user does something. Returns (count, max_streak, is_new_day)."""
    with get_conn() as con:
        row = con.execute("SELECT * FROM streak WHERE user_id = ?", (user_id,)).fetchone()
        today_str = today()
        if row is None:
            con.execute(
                "INSERT INTO streak (user_id, count, last_date, max_streak) VALUES (?, 1, ?, 1)",
                (user_id, today_str),
            )
            return 1, 1, True
        if row["last_date"] == today_str:
            return row["count"], row["max_streak"], False
        from datetime import date, timedelta
        yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        new_count = row["count"] + 1 if row["last_date"] == yesterday else 1
        new_max = max(new_count, row["max_streak"])
        con.execute(
            "UPDATE streak SET count = ?, last_date = ?, max_streak = ? WHERE user_id = ?",
            (new_count, today_str, new_max, user_id),
        )
        return new_count, new_max, True


def get_streak(user_id):
    with get_conn() as con:
        row = con.execute("SELECT * FROM streak WHERE user_id = ?", (user_id,)).fetchone()
        return row


# ---- tahlil (per-question explanation) ----

def get_tahlil(exam_code, number):
    with get_conn() as con:
        return con.execute(
            "SELECT * FROM tahlil WHERE exam_code = ? AND number = ?",
            (exam_code, number),
        ).fetchone()


def set_tahlil(exam_code, number, text="", voice_id=""):
    with get_conn() as con:
        con.execute(
            "INSERT INTO tahlil (exam_code, number, text, voice_id) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(exam_code, number) DO UPDATE SET text=excluded.text, voice_id=excluded.voice_id",
            (exam_code, number, text, voice_id),
        )
