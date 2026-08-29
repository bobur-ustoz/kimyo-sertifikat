# -*- coding: utf-8 -*-
"""book_raw.pdf -> sahifa raqamlari va kolontitul bilan yakuniy PDF."""
import io, sys
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SRC, DST = sys.argv[1], sys.argv[2]
pdfmetrics.registerFont(TTFont("DVS", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
ACCENT = (0.776, 0.157, 0.157)

reader = PdfReader(SRC)
n = len(reader.pages)
buf = io.BytesIO()
c = canvas.Canvas(buf, pagesize=A4)
W, Hh = A4
for i in range(n):
    if i >= 1:  # sahifa raqami: muqovadan boshqa hammasida
        c.setFont("DVS", 8.2)
        c.setFillColorRGB(*ACCENT)
        c.drawCentredString(W / 2, 22, f"— {i + 1} —")
    if i >= 2:  # kolontitul: muqova va tituldan keyin
        c.setFillColorRGB(0.55, 0.55, 0.55)
        c.setFont("DVS", 6.6)
        c.drawCentredString(W / 2, 812, "KIMYO · MILLIY SERTIFIKAT · ORGANIK KIMYO · 2-BOB — ALKENLAR, ALKADIYENLAR, ALKINLAR")
        c.setStrokeColorRGB(0.75, 0.8, 0.85)
        c.setLineWidth(0.5)
        c.line(60, 808, W - 60, 808)
    c.showPage()
c.save()
buf.seek(0)
stamps = PdfReader(buf)
w = PdfWriter()
for i, page in enumerate(reader.pages):
    page.merge_page(stamps.pages[i])
    w.add_page(page)
with open(DST, "wb") as f:
    w.write(f)
print(f"{DST}: {n} sahifa raqamlandi")
