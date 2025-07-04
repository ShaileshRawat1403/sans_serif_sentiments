# 06 – Deep Context Framing  
_Part of the Deep Structures series in the Prompt Dissection Lab_

> “Context is not extra.  
> It's the architecture of meaning.”

---

## Why Deep Context Beats Shallow Prompts

AI doesn’t just complete tasks — it completes **frames**.

If you give it a shallow frame (“write this”), you’ll get shallow output.

But if you embed **contextual cues** — audience, purpose, constraints, examples —  
you build a frame that **guides**, **informs**, and **prevents hallucinations**.

---

## The Two Levels of Context

| Level          | What It Includes                                                  | Why It Matters                             |
|----------------|-------------------------------------------------------------------|---------------------------------------------|
| **Surface**    | Topic, format, role, tone                                         | Helps AI simulate correct _structure_       |
| **Deep**       | Audience psychology, cultural nuance, purpose, emotional stakes   | Helps AI simulate correct _meaning_         |

> Most prompts only give surface context.  
> **System thinkers design both.**

---

## Prompt Anatomy: Framed vs Unframed

### ❌ Unframed Prompt:
> “Write a conclusion for this article.”

- No hint about audience, purpose, or impact.
- AI will default to generic, passive closing lines.

---

### ✅ Deep-Framed Prompt:
> “You’re writing for startup founders who skim. End with a short, high-impact line that makes them want to share this article.”

- Audience + Format + Impact = framed meaning

---

## Components of a Deep Frame

| Component        | How to Add It                                                   |
|------------------|------------------------------------------------------------------|
| 🎯 **Audience**       | “For first-time users in developing markets...”                  |
| 🎭 **Emotion**        | “Keep the tone warm but not overly sentimental.”                 |
| 🧭 **Purpose**        | “The goal is to reassure — not just inform.”                     |
| 🧩 **Constraints**    | “Use simple vocabulary. Avoid technical jargon.”                 |
| 💬 **Voice/Role**     | “Speak like a community leader, not a product marketer.”         |

These shape how the AI decides **what not to say**, which is just as crucial.

---

## Mental Model: Frame First, Then Flow

Here’s a usable model for building deep context:

```text
[WHO is this for?]
↓
[WHY does it matter to them?]
↓
[WHAT outcome do I want?]
↓
[HOW should it feel or be delivered?]
↓
[WHERE will it live? (email, UI, speech, etc.)]
```

Treat this like scaffolding for your prompt.

---

## Real Prompt Rewrite Example

> 🧱 Starting Point:
> “Write a welcome message.”

> 🧠 With Deep Context:
> “You’re a UX writer for a climate app. Write a short welcome message for first-time users who are skeptical about data privacy. Tone should be calm and transparent, no hype.”

See the difference?

---

## Common Pitfalls Without Framing

| Mistake                      | Result                                          |
|-----------------------------|--------------------------------------------------|
| No audience specified        | Output sounds generic or too broad              |
| No purpose stated            | Output lacks focus or CTA                       |
| No tone mentioned            | Wrong emotional register                        |
| No context of platform       | Output doesn’t match channel expectations       |
| No constraints               | Too verbose or overly technical                 |

---

## Final Tip: Prompt as a Brief

The best prompts are not questions.  
They’re **mini briefs** with structure, intent, and empathy baked in.

> “Think of prompting like building scaffolding —  
> not just shouting instructions.”

---

### 🧠 Related Concepts

- [Instruction vs Intention](./05-instruction-vs-intention.md)
- [Structural Dissonance](./02-structural-dissonance.md)
- [Literary Framing Models](../literary-techniques/03-rhetorical-moves.md)

---

### ✅ Try This Template

> “Act as [role] writing for [audience] to [purpose or goal].  
> Use [tone or emotion].  
> Output should be [format or style].  
> Avoid [specific things to exclude].”

📍 Example:

> “Act as a mentor writing for junior designers to help them avoid burnout. Use a reflective but encouraging tone. Output should be 5 key lessons, in list format. Avoid technical jargon and overused advice.”

---


