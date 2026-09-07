"""Minimal Telegram Mini App backend — shows a student's results page.

Kept intentionally small: the original webapp's exact design was lost along
with the rest of the source, so this is a plain, functional replacement
that reads the same database the bot writes to.
"""
import os
import sys

from flask import Flask, render_template_string

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db  # noqa: E402

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="uz">
<head>
  <meta charset="utf-8">
  <title>Kimyogar bot — Natijalar</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: system-ui, sans-serif; background:#0f172a; color:#e2e8f0; margin:0; padding:16px; }
    h1 { font-size:18px; }
    .card { background:#1e293b; border-radius:12px; padding:14px 16px; margin-bottom:10px; }
    .score { font-weight:700; color:#4ade80; }
  </style>
</head>
<body>
  <h1>{{ full_name }} — natijalar</h1>
  {% for s in subs %}
    <div class="card">
      <div>{{ s['subject'] }}</div>
      <div class="score">{{ s['final_score'] or '-' }}/100 — {{ s['grade'] or 'kutilmoqda' }}</div>
    </div>
  {% else %}
    <p>Hali natija yo'q.</p>
  {% endfor %}
</body>
</html>
"""


@app.route("/")
def index():
    return "Kimyogar bot webapp ishlayapti."


@app.route("/results/<int:user_id>")
def results(user_id):
    subs = db.list_submissions_for_user(user_id)
    full_name = subs[0]["full_name"] if subs else str(user_id)
    return render_template_string(PAGE, subs=subs, full_name=full_name)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
