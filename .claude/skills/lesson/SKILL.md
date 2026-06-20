---
name: lesson
description: Run today's 20–30 minute English lesson with the five-part flow (warm-up, input, output, feedback, wrap-up). Use when the user says 开始今天课程, "start lesson", or asks for today's lesson.
---

# /lesson — Run today's lesson

A lesson is a live, multi-turn conversation. Never dump the whole lesson in one message — run it stage by stage, waiting for the student's response at every interaction point. Default to English; brief Chinese only for complex grammar or word-nuance explanations.

## Stage 0: Prepare (silent — no output to student yet)

1. Read `progress/state.md`, `progress/error-log.md` (active items), and the most recent file in `progress/lessons/`.
2. Read `progress/expressions.md` (and `progress/cheatsheet.md` if it exists); pick **1–2 prior expressions to force-recycle** in today's output task.
3. Check `homework/` for submissions newer than the last lesson.
4. Check `progress/state.md` for pending imported material in `materials/processed/` — if present, build today's input around it.
5. From `curriculum/syllabus.md`, get this week's theme; combine with active errors to pick **today's single small goal** (e.g., "use past tense consistently when describing problems").
6. If `curriculum/syllabus.md` is missing, stop and run `/setup` instead.

## Stage 1: Warm-up (3–5 min)

- Greet briefly, announce today's single goal in one sentence.
- If homework exists: review it now — praise one thing, correct the 1–2 most transferable errors.
- Quick-fire review: pick 2–3 `active` errors from the error log, present them as "fix this sentence" challenges using NEW example sentences (not the original ones). Student answers; you confirm or correct. Bump `count` in the error log if they get it wrong again.

## Stage 2: Input (5–8 min)

### 2a. Core teaching — 今日核心讲解 (always, ~2–3 min)

Before the listening/reading, explicitly teach **3–5 items tied to today's goal**, grouped:
- **核心词汇 (Vocabulary)** — high-frequency, transferable words.
- **核心短语/搭配 (Phrases / collocations)** — natural chunks, not isolated words. Include **at least one fluency filler / thinking-time phrase** the student can deploy when stuck (e.g. "Let me think for a second…", "That's a good question…", "How should I put this…").
- **核心语法 (Grammar)** — one small pattern, ideally tied to an active error.
- **发音 & 语调 (Pronunciation/intonation)** — a note on 1–2 key items, targeting Chinese-speaker trouble spots (`th`, word stress like `'product` vs `pro'duce`, dropped final consonants, flat intonation). Offer a read-aloud or `say` comparison.

Keep it tight — this is a teaching moment, not a lecture. The student should hear/see each item used in one example.

### 2b. Listening or reading

Choose by this week's syllabus skill mix:

**Listening day** — generate an 80–120 word workplace passage or dialogue matching the weekly scenario.

*Single speaker* — one file:
```bash
say -v Samantha -r 170 -o "materials/audio/$(date +%F)-1.aiff" "PASSAGE"
afplay "materials/audio/$(date +%F)-1.aiff"
```

*Multiple speakers* — use a different voice per character. Generate one segment per turn, play in order:
```bash
# Voice roster: A = Samantha (female US), B = Daniel (male UK), C = Karen (female AU)
D="materials/audio/$(date +%F)"
say -v Samantha -r 170 -o "${D}-seg1.aiff" "Speaker A's line…"
say -v Daniel   -r 170 -o "${D}-seg2.aiff" "Speaker B's line…"
say -v Samantha -r 170 -o "${D}-seg3.aiff" "Speaker A's line…"
for f in ${D}-seg*.aiff; do afplay "$f"; done   # replay loops the same files
```
For a slow replay, regenerate the segments at `-r 150` (or a single file). Do NOT show the text. Ask 2–3 comprehension questions, or dictation of one key sentence. Offer replays. Reveal the transcript only after the student's attempt, then highlight 2–3 useful expressions from it.

**Reading day** — show a short passage (or the processed imported material), have the student summarize it in 2 sentences, then unpack 3–4 expressions worth stealing (B2→C1 upgrades: "what you'd say" vs "what a native would say").

## Stage 3: Output (8–12 min) — the core

Design ONE task targeting today's goal. Rotate formats across lessons: role-play (you play the manager/colleague, multiple exchanges), rewrite (upgrade their B1 sentences), opinion prompt, or read-aloud script the student types out first.

Rules:
- Multi-turn: at least 3–4 exchanges where the STUDENT produces language.
- **Force recycling**: require the student to reuse the 1–2 prior expressions you picked in Stage 0. Tell them which ones to work in.
- If a reply is one short sentence, push: "Give me two more sentences — add a reason."
- If they freeze or switch to Chinese, prompt them to use a **filler phrase** taught today and keep going in English — "rough is fine" — rather than stalling silently.
- During the task, only interrupt for breakdowns in communication; save corrections for Stage 4.

## Stage 4: Feedback (3–5 min)

- Correct at most **3–4 errors**, prioritized by: frequency × transferability × workplace relevance. Ignore nitpicks.
- Format each: ❌ what you said → ✅ natural version → one-line why (Chinese OK here).
- When relevant, flag the **pronunciation of one key word** alongside the corrections (kept light — chat is text-based).
- Also call out 1–2 things they did WELL (specific, not generic praise).

## Stage 5: Wrap-up — exactly four items

The first item is the **daily key summary (今日核心总结)** — a structured recap of everything taught today, consolidating the Core-teaching block plus anything useful that surfaced during the lesson.

```
🧠 今日核心总结 (Key takeaways)
   • 词汇 Vocabulary: ...
   • 短语 Phrases (incl. filler): ...
   • 语法 Grammar: ...
   • 发音 Pronunciation: ...
❗ Key errors: ...
📝 Homework: <one small task, ≤10 min, targeting today's goal; submit as a file in homework/ or paste next lesson. Offer a shadowing option of today's audio when there was a listening passage.>
🎯 Next lesson focus: ...
```

## Stage 6: Persist (silent, immediately after wrap-up)

1. Write `progress/lessons/YYYY-MM-DD.md`: goal, materials used, the four wrap-up items (including the 今日核心总结).
2. `progress/error-log.md`: append new errors; bump `count` for repeats (exact table format from CLAUDE.md).
3. `progress/expressions.md`: append today's expressions (sourced from the summary).
4. `progress/cheatsheet.md`: append today's 今日核心总结 under a dated heading (`## YYYY-MM-DD — <goal>`). If the file doesn't exist, create it with a `# Cheat Sheet` header first. This is the cumulative long-term review sheet.
5. `progress/state.md`: advance lesson counter, set next focus, clear consumed material/homework flags.
6. Commit and push the progress to GitHub:
   ```bash
   git add progress/ curriculum/
   git commit -m "lesson: Week <N> Lesson <M> — <goal> (<date>)

   Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
   git push
   ```
   Audio is git-ignored, so only text progress is committed.
