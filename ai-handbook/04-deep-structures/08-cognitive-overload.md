# 08 – Cognitive Overload  
_Part of the Deep Structures series in the Prompt Dissection Lab_

---

## What It Means

Cognitive overload happens when a prompt contains too many ideas, layers, instructions, or unclear sequencing — causing AI to deliver either a jumbled response or default to generic output.

This isn’t just a language problem. It’s a **thinking structure problem**.

---

## Signs You’ve Overloaded the Prompt

| Symptom                      | Description                                                              |
|------------------------------|--------------------------------------------------------------------------|
| 🧠 Generic Answers           | AI skips nuance and gives boilerplate responses.                        |
| 🔄 Mixed Objectives          | Output shifts mid-way due to conflicting goals.                         |
| ⛔ Incomplete Execution       | AI stops early or misses parts of your instruction.                     |
| 🪞 False Confidence           | Output _sounds_ right but lacks alignment with your actual need.        |

---

## Why It Happens

- Asking for **too many actions** in one prompt
- Combining **instruction + opinion + metaphor + style + emotion** with no hierarchy
- Failing to clarify the **primary task vs nice-to-have**
- Layering **nested logic** without breaks

---

## Visual: What Overload Looks Like

```text
Do all of this →
→ Summarize + critique + rewrite + empathize
→ Be formal, but poetic, and inspiring, but neutral
→ Use a metaphor, include 3 examples, keep it short
→ Target execs, but also beginners
→ Use my writing tone, but not too obvious
```

Result: 💥 Confused completion

---

## Fix It With This Filter

Before sending your prompt, run it through this test:

### ✅ The Prompt Focus Filter

Ask:

- What’s the **primary action** I want from this?
- Is there more than one goal? Can I split it?
- Have I asked for **style, structure, content, emotion** all at once?
- Can I group or sequence instructions instead?

---

## Clarity Moves That Help

| Move                | Fix                                                                 |
|---------------------|----------------------------------------------------------------------|
| **Split prompts**    | Use 2–3 smaller prompts instead of one massive one.                 |
| **Sequence actions** | Tell AI the order: “First summarize, then reflect.”                |
| **Use bullet goals** | e.g., “Make it: 1. Clear, 2. Relatable, 3. Poetic”                  |
| **Explicit limits**  | “Keep to under 150 words” or “Focus only on tone, not content”     |

---

## Rewrites in Action

> ❌ Overloaded:  
“Help me rewrite this to sound inspiring, but also formal, like Steve Jobs but for HR leaders, and use a metaphor that involves light, but don’t make it cheesy. Also summarize the main points.”

> ✅ Refined:  
“Summarize this for HR leaders in 3 bullet points. Then, rewrite the first line to sound inspiring using a light-based metaphor (avoid clichés). Use a professional tone.”

---

## Closing Insight

> The more you stuff into your prompt, the less you control what comes out.

Keep your thinking clean — and your prompt even cleaner.
