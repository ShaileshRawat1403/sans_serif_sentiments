---
title: Visual Troubleshooting Map
description: A quick-reference map to diagnose common prompt failures
---

# Visual Troubleshooting Map

A simple flow-based guide to help you **figure out why your prompt didn’t work** — and where to improve.

> _Don’t delete your prompt. Diagnose it._

---

## 🧭 Start Here

```text
Does the output match your expectation?
       ↓
     No? 
       ↓
Did you clearly define what success looks like?
       ↓
     No? → Add success criteria (length, format, tone, audience)
       ↓
     Yes
       ↓
Was the instruction vague or overly broad?
       ↓
     Yes → Add constraints (length, goal, style, limit scope)
       ↓
     No
       ↓
Did you include the right context (audience, format, use case)?
       ↓
     No? → Add real-world framing or role
       ↓
     Yes
       ↓
Did you assign a clear role or tone?
       ↓
     No? → Use “Act like...” or set voice/tone preferences
       ↓
     Yes
       ↓
Did the AI hallucinate or go off-topic?
       ↓
     Yes → Add anchor phrases or content boundaries
       ↓
     No → Try “What did you understand from my prompt?”
```

---

## 📌 Common Diagnoses

| Symptom                            | Likely Cause                                 | Quick Fix                                                  |
| ---------------------------------- | --------------------------------------------- | ---------------------------------------------------------- |
| Output too generic                 | No constraints or target audience             | Add specifics, format, and use case                        |
| Tone is robotic or stiff           | No tone or role set                           | Use “Act like…” or define emotional tone                   |
| Output is long and meandering      | No length guidance or structure               | Add “In under 200 words” or “Give 5 bullet points”         |
| Missed the real point              | Prompt buried key question or lacked focus    | Start prompt with the core instruction or intention        |
| Answer sounds obvious or surface   | Lacks context depth or background             | Add input text or describe what depth you expect           |
| AI is refusing or hesitating       | Ambiguous goal, conflicting task instructions | Refine prompt to be one clear action or task               |
| Wrong audience or reading level    | No clarity on who it’s for                    | Add “for a beginner” or “for 12-year-olds” etc.            |

---

## 🔍 Bonus Tip: Reflect With the AI

If you're still stuck:

> **Prompt:**  
> _“How did you interpret my instruction? What were the main cues you picked up?”_

This often reveals what the model assumed — and where your wording misfired.

---

## 📘 Pair With

- [`why-your-prompt-didnt-work.md`](./why-your-prompt-didnt-work.md)
- [`mini-diagnostic-audit.md`](./mini-diagnostic-audit.md)
- [`team-retrospective-prompts.md`](./team-retrospective-prompts.md)

---

> _“AI doesn’t ignore your instruction. It misinterprets your language.”_
