# English Level-Up Coach 🎯

A 12-week, AI-coached English course that runs entirely inside [Claude Code](https://claude.com/claude-code).
Every conversation in this directory is a **coaching session** — Claude reads the course's memory
files, runs the lesson, and saves your progress back to git.

Built for a Chinese-native learner around **B1–B2**, prioritizing **speaking > listening >
workplace English**.

## How it works

The course "remembers" everything through markdown files in `progress/` and `curriculum/`.
Claude reads them before each session and updates them after, then auto-commits to GitHub — so
the course memory is always backed up and portable.

Just open this folder in Claude Code and type one of the commands below.

## Commands

| 你说 / You say | 触发 | What it does |
|---|---|---|
| `开始今天课程` / "start lesson" | `/lesson` | A 20–30 min lesson: warm-up → core teaching → input → output → feedback → wrap-up |
| `背单词` / "vocab" | `/vocab` | Themed 8–12-word session from the 俞敏洪 15000词 book, with spaced review |
| `复习` / "weekly review" | `/review` | Weekly review: recap, exercises, error-status updates, weekly report |
| `进度` / "how am I doing" | `/progress` | Read-only dashboard: week, streak, errors, pace |
| (paste an article / email / subtitles) | `/import` | Turns your material into lesson-ready content |
| (first time) | `/setup` | Level check + generates the 12-week syllabus |

Finishing a `/lesson` or `/vocab` **auto-checks-in** today's activity and updates your 🔥 streak.

## Project structure

```
CLAUDE.md                  # Coach instructions (the rules every session follows)
curriculum/
  syllabus.md              # 12-week outline: themes, skill mix, milestones
  daily-routine.md         # 30–60 min/day study rhythm
  vocab-index.md           # Menu of all 448 vocab-book units
progress/                  # The course's long-term memory
  state.md                 # Pointer: current week/lesson, next focus
  error-log.md             # Running error log (the core asset)
  expressions.md           # Expressions learned
  cheatsheet.md            # Cumulative key-takeaways for review
  vocab-progress.md        # Vocabulary tracker (status per word)
  checkin-log.md           # Daily check-in & streak
  lessons/                 # Per-lesson records
  weekly/                  # Weekly review reports
scripts/                   # vocab_build_index.py · vocab_extract.py
materials/                 # Audio (TTS) + the vocab-book PDF (both git-ignored)
homework/                  # Your homework submissions
```

## Requirements

- **Claude Code**
- **macOS** for listening audio — uses the built-in `say` TTS (multi-voice dialogues) and `afplay`
- **Python 3 + `pypdf`** for vocabulary extraction (`pip install pypdf`)
- The vocab source `materials/vocab-book.pdf` (《超实用15000词分类速记》俞敏洪) is git-ignored;
  re-copy the book there if missing, then run `python3 scripts/vocab_build_index.py`.

## Daily rhythm

See `curriculum/daily-routine.md`. In short: **show up every day, and always speak out loud.**
The streak rule is lenient — one rest day per week won't break it.
