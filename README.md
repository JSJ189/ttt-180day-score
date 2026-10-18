# Preoperative 180-day score after first tibial transverse transport

Manuscript under review at *eClinicalMedicine*:

**Preoperative assessment of 180-day outcomes after first tibial transverse transport for severe diabetic foot ulcers**

## Code availability

This repository is a partial release during peer review.

It currently contains only the integer 0–59 point card in Table 2 of the submitted manuscript (`score_card.py`). The card adds published points and assigns the frozen strata (0–23, 24–33, and 34–59). It does not fit models, impute data, or estimate outcome probabilities.

The analysis code used to develop and validate the score will be added to this repository if the manuscript is accepted. Individual participant data are not in this repository and will not be posted.

This code is not a medical device. The submitted manuscript states that severe-outcome probabilities require local recalibration before clinical use.

## Point card

| Predictor | Category | Points |
|---|---|---:|
| Age | <65 years | 0 |
| Age | ≥65 years | 3 |
| Heart failure | Grade 0 (none) | 0 |
| Heart failure | Grade 1 (chronic) | 3 |
| Heart failure | Grade 2 (acute) | 16 |
| Palpated foot temperature | Grade 1 (cold) | 16 |
| Palpated foot temperature | Grade 2 (cool) | 13 |
| Palpated foot temperature | Grade 3 (warm) | 8 |
| Palpated foot temperature | Grade 4 (warmer) | 0 |
| eGFR-based renal function | Grades 1–2 | 0 |
| eGFR-based renal function | Grades 3–4 | 1 |
| eGFR-based renal function | Grade 5 | 8 |
| Wound area | <5 cm² | 0 |
| Wound area | 5–20 cm² | 3 |
| Wound area | >20 to 100 cm² | 9 |
| Wound area | >100 cm² | 10 |
| Infection–inflammation burden grade | Grade 0 | 0 |
| Infection–inflammation burden grade | Grade 1 | 3 |
| Infection–inflammation burden grade | Grades 2–3 | 6 |

Heart-failure, foot-temperature, renal-function, and infection–inflammation grades use the definitions in the manuscript and its supplement. Those definitions are not re-derived here.

## Use

```python
from score_card import score_card

result = score_card(
    age_years=70,
    heart_failure_grade=1,
    foot_temperature_grade=3,
    renal_function_grade=5,
    wound_area_cm2=25,
    ibg_grade=1,
)
print(result.points, result.stratum)
```
