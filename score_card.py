"""Integer point card from the submitted manuscript, Table 2.

This module adds the published points. It does not estimate probabilities.
"""

from __future__ import annotations

from dataclasses import dataclass


HEART_FAILURE_POINTS = {0: 0, 1: 3, 2: 16}
FOOT_TEMPERATURE_POINTS = {1: 16, 2: 13, 3: 8, 4: 0}
RENAL_FUNCTION_POINTS = {1: 0, 2: 0, 3: 1, 4: 1, 5: 8}
IBG_POINTS = {0: 0, 1: 3, 2: 6, 3: 6}

LOW_MAX = 23
INTERMEDIATE_MAX = 33
POINT_MAX = 59


@dataclass(frozen=True)
class ScoreResult:
    points: int
    stratum: str


def age_points(age_years: float) -> int:
    if age_years < 0:
        raise ValueError("age_years must be >= 0")
    return 0 if age_years < 65 else 3


def wound_area_points(wound_area_cm2: float) -> int:
    if wound_area_cm2 < 0:
        raise ValueError("wound_area_cm2 must be >= 0")
    if wound_area_cm2 < 5:
        return 0
    if wound_area_cm2 <= 20:
        return 3
    if wound_area_cm2 <= 100:
        return 9
    return 10


def _lookup(name: str, value: int, table: dict[int, int]) -> int:
    if value not in table:
        allowed = ", ".join(str(k) for k in sorted(table))
        raise ValueError(f"{name} must be one of: {allowed}")
    return table[value]


def stratum_for(points: int) -> str:
    if points < 0 or points > POINT_MAX:
        raise ValueError(f"points must be between 0 and {POINT_MAX}")
    if points <= LOW_MAX:
        return "low"
    if points <= INTERMEDIATE_MAX:
        return "intermediate"
    return "high"


def score_card(
    age_years: float,
    heart_failure_grade: int,
    foot_temperature_grade: int,
    renal_function_grade: int,
    wound_area_cm2: float,
    ibg_grade: int,
) -> ScoreResult:
    """Return the Table 2 total and the frozen 24/34 stratum."""
    points = (
        age_points(age_years)
        + _lookup("heart_failure_grade", heart_failure_grade, HEART_FAILURE_POINTS)
        + _lookup("foot_temperature_grade", foot_temperature_grade, FOOT_TEMPERATURE_POINTS)
        + _lookup("renal_function_grade", renal_function_grade, RENAL_FUNCTION_POINTS)
        + wound_area_points(wound_area_cm2)
        + _lookup("ibg_grade", ibg_grade, IBG_POINTS)
    )
    return ScoreResult(points=points, stratum=stratum_for(points))
