"""Rasch modeli asosida test natijalarini baholash.

DIQQAT: Ushbu modul ILLYUSTRATIV/taxminiy modeldir. Quyidagi konstantalar
(item qiyinlik parametrlari va skalalash formulasidagi 50/10 sonlari)
Bilim va malakalarni baholash agentligining rasmiy formulasi EMAS — ular
faqat namoyish va sinov maqsadida tanlangan. Kerak bo'lsa, quyidagi
konstantalarni rasmiy qiymatlar bilan almashtiring.
"""

from __future__ import annotations

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# ILLYUSTRATIV KONSTANTALAR — rasmiy qiymatlar bilan almashtirish mumkin
# ---------------------------------------------------------------------------

# Skalalashda ishlatiladigan chiziqli formula: scaled = SCALE_INTERCEPT + SCALE_SLOPE * theta
# Bu qiymatlar (50, 10) shunchaki illyustrativ tanlov — rasmiy agentlik
# formulasi emas.
SCALE_INTERCEPT = 50.0
SCALE_SLOPE = 10.0

# Logit/theta qidiruv oralig'i va bisection iteratsiyalari soni
THETA_MIN = -6.0
THETA_MAX = 6.0
BISECTION_ITERATIONS = 40

# 1-40 savollar (yopiq test): har biri 1 ballik, qiyinlik parametrlari
# -2.0 dan +2.0 gacha tekis taqsimlangan (illyustrativ qiymatlar).
TEST_ITEM_COUNT = 40
TEST_MIN_B = -2.0
TEST_MAX_B = 2.0


def _linspace(start: float, stop: float, count: int) -> list[float]:
    if count == 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + step * i for i in range(count)]


TEST_ITEMS: list[tuple[float, float]] = [
    (b, 1.0) for b in _linspace(TEST_MIN_B, TEST_MAX_B, TEST_ITEM_COUNT)
]
"""TEST_ITEMS: [(qiyinlik b, og'irlik weight), ...] — 40 ta yopiq test itemi."""

# 41, 42, 43-savollar (yozma ish): har biri 25 ballik, qiyinlik
# parametrlari illyustrativ tarzda tanlangan.
YOZMA_ITEMS: list[tuple[float, float]] = [
    (-0.5, 25.0),  # 41-topshiriq
    (0.5, 25.0),  # 42-topshiriq
    (1.6, 25.0),  # 43-topshiriq
]
"""YOZMA_ITEMS: [(qiyinlik b, og'irlik weight), ...] — 3 ta yozma ish itemi."""

TEST_MAX_RAW = sum(weight for _, weight in TEST_ITEMS)  # 40
YOZMA_MAX_RAW = sum(weight for _, weight in YOZMA_ITEMS)  # 75


# ---------------------------------------------------------------------------
# Daraja jadvali
# ---------------------------------------------------------------------------

GRADE_TABLE: list[tuple[float, str]] = [
    (70.0, "A+"),
    (65.0, "A"),
    (60.0, "B+"),
    (55.0, "B"),
    (50.0, "C+"),
    (46.0, "C"),
]
NO_CERTIFICATE = "Sertifikat berilmaydi"


def rasch_probability(theta: float, b: float) -> float:
    """Rasch modeli ehtimollik formulasi: P(theta) = 1 / (1 + e^-(theta-b))."""
    import math

    return 1.0 / (1.0 + math.exp(-(theta - b)))


def _expected_score(theta: float, items: list[tuple[float, float]]) -> float:
    return sum(weight * rasch_probability(theta, b) for b, weight in items)


def raw_score_to_logit(raw_score: float, items: list[tuple[float, float]]) -> float:
    """Xom balldan logit (theta) topish uchun bisection (binary search).

    theta ni THETA_MIN..THETA_MAX oralig'ida taxmin qilib, kutilgan ball
    (barcha itemlar bo'yicha P*weight yig'indisi) haqiqiy xom ballga
    tenglashguncha BISECTION_ITERATIONS marta takrorlanadi.
    """
    max_raw = sum(weight for _, weight in items)
    raw_score = max(0.0, min(raw_score, max_raw))

    lo, hi = THETA_MIN, THETA_MAX
    for _ in range(BISECTION_ITERATIONS):
        mid = (lo + hi) / 2.0
        expected = _expected_score(mid, items)
        if expected < raw_score:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def logit_to_scaled(logit: float) -> float:
    """Logitni skalalangan ballga o'girish: scaled = 50 + 10*logit, 0-100 ga cheklangan."""
    scaled = SCALE_INTERCEPT + SCALE_SLOPE * logit
    return max(0.0, min(scaled, 100.0))


def scaled_to_grade(scaled_umumiy: float) -> str:
    for threshold, grade in GRADE_TABLE:
        if scaled_umumiy >= threshold:
            return grade
    return NO_CERTIFICATE


@dataclass
class PartResult:
    raw: float
    max_raw: float
    logit: float
    scaled: float


@dataclass
class RaschResult:
    test: PartResult
    yozma: PartResult
    umumiy_ball: float
    daraja: str


def calculate_result(test_raw: float, yozma_raw: float) -> RaschResult:
    """Test va yozma ish qismlari uchun ALOHIDA hisob-kitob, so'ng o'rtacha.

    test_raw: 1-40 savollardan to'g'ri javoblar soni (0-40)
    yozma_raw: 41,42,43-savollar uchun jami ball (0-75)
    """
    test_logit = raw_score_to_logit(test_raw, TEST_ITEMS)
    test_scaled = logit_to_scaled(test_logit)

    yozma_logit = raw_score_to_logit(yozma_raw, YOZMA_ITEMS)
    yozma_scaled = logit_to_scaled(yozma_logit)

    umumiy_ball = (test_scaled + yozma_scaled) / 2.0
    daraja = scaled_to_grade(umumiy_ball)

    return RaschResult(
        test=PartResult(raw=test_raw, max_raw=TEST_MAX_RAW, logit=test_logit, scaled=test_scaled),
        yozma=PartResult(raw=yozma_raw, max_raw=YOZMA_MAX_RAW, logit=yozma_logit, scaled=yozma_scaled),
        umumiy_ball=umumiy_ball,
        daraja=daraja,
    )


if __name__ == "__main__":
    # Oddiy qo'lda sinov: python rasch.py
    for test_raw, yozma_raw in [(30, 53), (0, 0), (40, 75), (20, 37)]:
        result = calculate_result(test_raw, yozma_raw)
        print(
            f"test_xom={test_raw} yozma_xom={yozma_raw} -> "
            f"test_logit={result.test.logit:.3f} test_scaled={result.test.scaled:.2f} | "
            f"yozma_logit={result.yozma.logit:.3f} yozma_scaled={result.yozma.scaled:.2f} | "
            f"umumiy_ball={result.umumiy_ball:.2f} daraja={result.daraja}"
        )
