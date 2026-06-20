---
name: review
description: Weekly review — summarize this week's lessons and errors, generate review exercises, update error statuses, write the weekly report. Use when the user says 复习 / "weekly review", or run in headless mode when invoked with the "headless" argument (cron).
---

# /review — Weekly review

Two modes. If the argument contains `headless` (cron-triggered), run **Headless mode**; otherwise **Interactive mode**.

## Shared step 1: Gather

1. Read `progress/state.md` to find the current week number.
2. Read this week's files in `progress/lessons/`, the full `progress/error-log.md`, and `progress/checkin-log.md`.
3. Analyze: which errors recurred this week (count ≥ 2)? Which `active`/`reviewing` items had no recurrence for 2+ weeks? How many days were active this week (from checkin-log)?

## Shared step 2: Update error statuses

In `progress/error-log.md`:
- `active` with no recurrence for 2 weeks → `reviewing`
- `reviewing` with no recurrence for 2 more weeks → `mastered`
- any recurrence → back to `active`, bump count

## Interactive mode

1. Present a short week-in-review (English): lessons done, top recurring errors, wins.
2. Run review exercises live, one at a time, student answers each:
   - 4–5 "fix this sentence" items built from this week's `active` errors (new example sentences)
   - 3 fill-in-the-blank items from `progress/expressions.md` entries learned this week
   - 1 integrative output task: a 4–6 sentence paragraph using ≥3 of this week's expressions, on this week's syllabus theme
3. Give feedback using the same rules as /lesson Stage 4.
4. Write the report (below), tell the student next week's focus.

## Headless mode (no user present — do NOT ask questions or wait)

1. Do shared steps, write the report, and additionally generate a **self-study review sheet** appended to the report: the same exercises as interactive mode but with answers hidden in a `<details>` block.
2. Note in `progress/state.md`: "weekly review YYYY-Wnn generated; start next lesson's warm-up from it".

## Report: `progress/weekly/YYYY-Wnn.md`

```markdown
# Week NN Review (YYYY-MM-DD)
## Summary        — lessons completed, themes covered, milestone met?
## Check-in       — days active this week (X/7), current streak, any rest day used
## Error stats    — by category; recurring offenders; newly mastered
## Wins           — concrete improvements observed
## Review sheet   — (headless mode) exercises + hidden answers
## Next week      — theme from syllabus + 1–2 carry-over weak points
```

If the syllabus pace and actual progress have drifted (e.g., milestone clearly missed), adjust next week's plan in `curriculum/syllabus.md` and note the change in the report.
