---
name: lesson
description: Run today's 20–30 minute English lesson with the five-part flow (warm-up, input, output, feedback, wrap-up). Use when the user says 开始今天课程, "start lesson", or asks for today's lesson.
---

# /lesson — Run today's lesson

A lesson is a live, multi-turn conversation. Never dump the whole lesson in one message — run it stage by stage, waiting for the student's response at every interaction point. Default to English; brief Chinese only for complex grammar or word-nuance explanations.

## Stage 0: Prepare (silent — no output to student yet)

1. Read `progress/state.md`, `progress/error-log.md` (active items), and the most recent file in `progress/lessons/`.
2. Check `homework/` for submissions newer than the last lesson.
3. Check `progress/state.md` for pending imported material in `materials/processed/` — if present, build today's input around it.
4. From `curriculum/syllabus.md`, get this week's theme; combine with active errors to pick **today's single small goal** (e.g., "use past tense consistently when describing problems").
5. If `curriculum/syllabus.md` is missing, stop and run `/setup` instead.

## Stage 1: Warm-up (3–5 min)

- Greet briefly, announce today's single goal in one sentence.
- If homework exists: review it now — praise one thing, correct the 1–2 most transferable errors.
- Quick-fire review: pick 2–3 `active` errors from the error log, present them as "fix this sentence" challenges using NEW example sentences (not the original ones). Student answers; you confirm or correct. Bump `count` in the error log if they get it wrong again.

## Stage 2: Input (5–8 min)

Choose by this week's syllabus skill mix:

**Listening day** — generate an 80–120 word workplace passage or dialogue matching the weekly scenario, then:
```bash
say -v Samantha -r 170 -o "materials/audio/$(date +%F)-1.aiff" "PASSAGE"
afplay "materials/audio/$(date +%F)-1.aiff"
```
Do NOT show the text. Ask 2–3 comprehension questions, or dictation of one key sentence. Offer replays (`-r 150` for slow). Reveal the transcript only after the student's attempt, then highlight 2–3 useful expressions from it.

**Reading day** — show a short passage (or the processed imported material), have the student summarize it in 2 sentences, then unpack 3–4 expressions worth stealing (B2→C1 upgrades: "what you'd say" vs "what a native would say").

## Stage 3: Output (8–12 min) — the core

Design ONE task targeting today's goal. Rotate formats across lessons: role-play (you play the manager/colleague, multiple exchanges), rewrite (upgrade their B1 sentences), opinion prompt, or read-aloud script the student types out first.

Rules:
- Multi-turn: at least 3–4 exchanges where the STUDENT produces language.
- If a reply is one short sentence, push: "Give me two more sentences — add a reason."
- If they switch to Chinese, acknowledge the idea, then: "Now say that in English — rough is fine."
- During the task, only interrupt for breakdowns in communication; save corrections for Stage 4.

## Stage 4: Feedback (3–5 min)

- Correct at most **3–4 errors**, prioritized by: frequency × transferability × workplace relevance. Ignore nitpicks.
- Format each: ❌ what you said → ✅ natural version → one-line why (Chinese OK here).
- Also call out 1–2 things they did WELL (specific, not generic praise).

## Stage 5: Wrap-up — exactly four items

```
📚 Expressions learned today: ...
❗ Key errors: ...
📝 Homework: <one small task, ≤10 min, targeting today's goal; submit as a file in homework/ or paste next lesson>
🎯 Next lesson focus: ...
```

## Stage 6: Persist (silent, immediately after wrap-up)

1. Write `progress/lessons/YYYY-MM-DD.md`: goal, materials used, the four wrap-up items.
2. `progress/error-log.md`: append new errors; bump `count` for repeats (exact table format from CLAUDE.md).
3. `progress/expressions.md`: append today's expressions.
4. `progress/state.md`: advance lesson counter, set next focus, clear consumed material/homework flags.
