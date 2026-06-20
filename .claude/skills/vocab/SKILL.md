---
name: vocab
description: Run a focused vocabulary session built on the 俞敏洪 15000词 book — teach 8–12 themed words progressively, with spaced review, output practice, and feedback. Use when the user says 背单词, "vocab", "学单词", or asks for a vocabulary session.
---

# /vocab — Vocabulary session

A live, multi-turn vocabulary lesson sourced from the categorized word book at
`materials/vocab-book.pdf` (1,633 pages, 448 themed units). **Progressive by design:** never
load the whole book — pull only one unit's words per session via the extractor script. Default
to English; brief Chinese for meanings/nuance. Target ~15 minutes.

## Stage 0: Prepare (silent — no output to student yet)

1. Read `progress/state.md` (current week + theme), `progress/vocab-progress.md` (words taught,
   last unit, words due for review), and `curriculum/vocab-index.md` (the unit menu).
2. **Pick today's unit** by matching this week's syllabus theme to a chapter (mapping below).
   Skip units already in "Units completed". If the student names a topic, honor it.
3. If `curriculum/vocab-index.md` or `materials/vocab-book.pdf` is missing, tell the student to
   run `python3 scripts/vocab_build_index.py` / restore the PDF, and stop.

**Theme → chapter guidance** (pick a sensible unit; not hardcoded):
W1 自我介绍→Ch2 · W2 过去经历→Ch10/Ch7 · W3 进度汇报→Ch9 · W4 澄清→Ch2(误解/电话) ·
W5 会议→Ch9/Ch15 · W6 委婉反对→Ch9/Ch7 · W7 邮件→Ch2(收发email)/Ch9 · W8 总结→Ch13 ·
W9 演讲→Ch15 · W10 谈判→Ch15 · W11 面试→Ch9(182 漫漫求职路) · W12 辩论→Ch13/Ch19.

## Stage 1: Spaced review (2–3 min)

- If words exist in `progress/vocab-progress.md` with status `learning`/`reviewing`, quiz **3–5
  due words**: give the Chinese (or a gap sentence), student produces the English word.
- Confirm or correct. On a hit, bump `learning`→`reviewing`→`mastered`; on a miss, send it back
  to `learning`. (Skip this stage on the very first session.)

## Stage 2: Teach new words (5–7 min)

1. Run the extractor for the chosen unit:
   ```bash
   python3 scripts/vocab_extract.py --unit <N>
   ```
2. From the output, pick **8–12 high-frequency, transferable words** (skip rare/obscure ones —
   重质不重量). Teach them grouped, each as: **word** + 音标 + 词性 + 中文 + a ◎collocation or a
   one-line example. Cluster related words so they stick.
3. Add a short **发音 note** on 1–2 tricky items (word stress, vowel sounds, silent letters) —
   speaking is the priority skill. Offer a `say -v Samantha "word"` read-aloud if useful.
4. **Reinforce with gap-fill (句子填空)**: right after teaching, give **4–6 fill-in-the-blank
   sentences** (one per key word, context- or Chinese-hint–driven) and have the student supply
   the word. This forces active recall before the freer output task. Confirm/correct each.

## Stage 3: Output (5–7 min) — the core

Force production. Pick ONE task and run it multi-turn (≥3 student turns):
- Student writes sentences using **≥3–4 of the new words**, OR
- A short role-play on the unit's theme where the student must work the words in.

Rules (same as `/lesson`): if a reply is too short, push for more; if they switch to Chinese,
nudge back to English ("rough is fine"); only interrupt for breakdowns — save corrections for
Stage 4.

## Stage 4: Feedback (2–3 min)

- Correct at most **3–4 errors** (frequency × transferability), format:
  ❌ what you said → ✅ natural version → one-line why (Chinese OK).
- Call out 1–2 things done well.
- Log genuine errors to `progress/error-log.md` (exact table format from CLAUDE.md).

## Stage 5: Wrap-up — four items

```
🧠 今日单词总结: the 8–12 words (word — 中文), grouped
✅ Words you produced well: ...
📝 Homework: write 3–4 sentences (or a short paragraph) reusing today's words; ≤10 min
🎯 Next unit: <unit no. + title>
```

## Stage 6: Persist (silent, immediately after wrap-up)

1. `progress/vocab-progress.md`: append today's words to the table (`status = learning`,
   first-taught = today, unit no.); update **Units completed**, **Last unit taught**, **Next
   suggested unit**.
2. `progress/error-log.md`: append/bump any errors from Stage 4.
3. `progress/cheatsheet.md`: append today's 今日单词总结 under a dated heading
   (`## YYYY-MM-DD — Vocab unit <N> <title>`). Create the file with a `# Cheat Sheet` header if
   it doesn't exist.
4. `progress/checkin-log.md`: add `vocab` to today's row (create the row if today isn't logged
   yet), then recompute the summary block per the lenient streak rule in that file.
5. Commit and push:
   ```bash
   git add progress/ curriculum/
   git commit -m "vocab: unit <N> <title> — <count> words (<date>)

   Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
   git push
   ```
   The PDF is git-ignored; only text progress is committed.
