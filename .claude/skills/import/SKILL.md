---
name: import
description: Turn user-provided material (articles, resumes, emails, meeting notes, video subtitles) into lesson-ready course material. Use when the user pastes content, drops a file into materials/inbox/, or asks to import material.
---

# /import — Turn my material into course material

Input: a file in `materials/inbox/` (ask which one if several are new) or content pasted directly into chat. If pasted, first save the raw content to `materials/inbox/YYYY-MM-DD-<slug>.md`.

## Processing

Read the material and produce `materials/processed/YYYY-MM-DD-<slug>.md`:

```markdown
# <Title>  (source: <inbox file>, type: article|resume|email|meeting-notes|subtitles)

## Key expressions (5–8)
| expression | meaning | why it's useful for me |
- Pick high-frequency, transferable, workplace-relevant phrases — same priority rule as corrections.

## Upgrade pairs (3–5)
| how I'd probably say it (B1/B2) | how the material says it (C1/native) |

## Comprehension & discussion (3–5 questions)
- Mix factual and opinion questions usable in a lesson's Input stage.

## Output task (exactly 1)
- One task grounded in THIS material (e.g., reply to the email, summarize the meeting, retell the subtitle scene).

## Audio
- listening-suitable: yes/no — yes if it's dialogue-like or narrative, ≤150 words excerptable.
- If yes: include an 80–120 word excerpt (cleaned for TTS) ready for `say`.
```

Special handling by type:
- **Resume**: focus on self-presentation language; output task = mock interview answer using upgraded phrasing.
- **Email/meeting notes**: focus on tone (directness vs politeness); output task = write the reply / the follow-up summary.
- **Subtitles**: clean timestamps/tags first; treat as listening material (audio: yes).

## After processing

1. Update `progress/state.md`: add "pending material: materials/processed/<file> — use in next lesson's Input stage".
2. Tell the student (briefly, English): what was extracted, and that the next lesson will be built on it. Do NOT start teaching it now unless asked.
