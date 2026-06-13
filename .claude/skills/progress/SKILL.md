---
name: progress
description: Read-only progress dashboard — current week, lessons completed, error statistics, mastered items, pace vs syllabus. Use when the user asks 进度 / "how am I doing" / "show progress".
---

# /progress — Progress dashboard

Read-only: read `progress/state.md`, `progress/error-log.md`, `progress/expressions.md`, `curriculum/syllabus.md`, and count files in `progress/lessons/`. Do NOT modify anything.

Present a compact dashboard (English, with the student's numbers — never invent data):

```
📍 Week N of 12 — <theme> | Lessons completed: X
🎯 Current focus: <from state.md>

❗ Errors: A active / B reviewing / C mastered
   By category: grammar X · word-choice X · collocation X · pragmatics X
   Top recurring (count ≥ 2): <up to 5, with counts>

📚 Expressions learned: N (most recent 3 as a sample)

⏱ Pace check: lessons done vs ~3/week expected → on track / behind / ahead
   <If behind: one-sentence suggestion, e.g., shorter catch-up lessons. If a
   milestone was missed in the last weekly report, mention it.>
```

End with one encouraging, specific observation drawn from the data (e.g., "your pragmatics errors dropped from 4 active to 1 — your meeting language is getting noticeably more natural").
