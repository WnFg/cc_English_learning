---
name: setup
description: First-time course initialization — quick level assessment, then generate the 12-week syllabus and progress files. Use when curriculum/syllabus.md does not exist or the user asks to restart the course.
---

# /setup — Initialize the 12-week course

If `curriculum/syllabus.md` already exists, confirm with the user before overwriting (restarting wipes the syllabus but MUST keep `progress/error-log.md` and `progress/expressions.md`).

## Step 1: Quick assessment (10–15 min, in English)

Run a short placement conversation. One thing at a time:

1. Ask for a free-writing sample (5–8 sentences): "Describe a recent challenge at work and how you handled it."
2. Then 3–4 interactive questions, escalating in difficulty: daily routine → opinion ("Do you prefer remote or office work? Why?") → hypothetical ("If your manager rejected your proposal, what would you say?") → workplace role-play (one exchange).
3. Silently note: grammar control, vocabulary range, collocation naturalness, pragmatic appropriateness. Do NOT correct during assessment — just observe.

## Step 2: Diagnose

Summarize in English (with brief Chinese for nuance): estimated sub-level per skill (e.g., writing B2, speaking B1+), top 3 strengths, top 3 gaps. Seed `progress/error-log.md` with the 3–5 clearest high-frequency errors from the assessment.

## Step 3: Generate `curriculum/syllabus.md`

12 weeks, biased toward the student's priorities (speaking, listening, workplace English). Structure:

```markdown
# 12-Week Syllabus  (started: YYYY-MM-DD)

## Phase 1 (Weeks 1–4): Foundations & ear training
## Phase 2 (Weeks 5–8): Workplace scenarios
## Phase 3 (Weeks 9–12): Fluency & real-world performance

### Week N: <theme>
- Focus skill mix: listening X% / speaking X% / reading X% / writing X%
- Scenario: <workplace scenario, e.g., status updates, disagreeing in meetings>
- Milestone: <one observable ability, e.g., "can summarize a 1-min audio clip in 3 sentences">
```

Themes must cover (adjust order to assessment results): self-introduction & small talk, status updates, asking for clarification, disagreeing politely, meetings, email writing, negotiation, presentations, interviews, storytelling, summarizing, debate.

## Step 4: Initialize progress files

- `progress/state.md` — set Week 1, Lesson 0 (next = Lesson 1), next focus from syllabus
- `progress/error-log.md` — table header + assessment errors (use the exact format in CLAUDE.md)
- `progress/expressions.md` — table header

## Step 5: Hand off

Tell the student the course is ready, show the Week 1 plan, and say: next time just say **"开始今天课程"**.
