# 10 – Prompt Entropy  
_Part of the Deep Structures series in the Prompt Dissection Lab_

---

## What It Means

Prompt entropy refers to **how much uncertainty, ambiguity, or contradiction** exists within a single prompt.

High-entropy prompts often:

- Mix too many goals or tones
- Contradict themselves
- Create unclear hierarchies of importance
- Confuse both the AI — and the user reading the result

> Entropy isn’t just randomness — it’s disorder in meaning.

---

## Why It Matters

| Problem                  | Impact                                                           |
|--------------------------|------------------------------------------------------------------|
| 🎯 Conflicting Intent     | AI tries to satisfy too many objectives at once                 |
| 🌀 Output Drift           | The completion wanders, loops, or contradicts itself            |
| ❓ Ambiguous Expectations | You don’t know how to measure if the answer is “right”          |
| 🧱 Cognitive Fatigue      | Repeated revisions without knowing what’s actually broken        |

---

## Real Example

> ❌ High-Entropy Prompt:  
“Write a funny but serious blog post about AI’s impact on humanity, in the tone of both George Carlin and Sam Altman, with a call to action for corporate leaders and Gen Z students.”

- Who is the audience?
- What’s the dominant tone?
- What’s the purpose: inspire, warn, joke, or sell?

Even a human would struggle.

---

## Diagnosing Prompt Entropy

Ask:

- Does my prompt contain more than one **role**?
- Did I layer **tone + task + format + metaphor + constraint** without priority?
- Is there **any contradiction** in goals or framing?
- Would I know if the result “worked”?

---

## Ways to Reduce Prompt Entropy

| Fix Technique        | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🧹 Strip the Layers   | Temporarily remove metaphor, tone, or format to test core logic             |
| 🧩 Sequence Goals     | Break into multiple prompts — each with one clear outcome                  |
| 🪞 Re-echo the Task    | Ask AI to restate your goal in its own words before generating             |
| 🧪 A/B the Outcome     | Test two simpler prompts vs one complex hybrid                             |

---

## Low vs High Entropy: Example

> ✅ Low Entropy Prompt:  
“Explain the risks of AI bias in 5 bullet points for policymakers.”

> ❌ High Entropy Prompt:  
“Tell a story about AI bias using sarcasm and statistics, with policy suggestions embedded like Easter eggs.”

---

## The Design Principle

Entropy is not always bad — **but unintentional entropy is**.

Use entropy deliberately when crafting:

- Satirical or surreal writing
- Juxtaposition or layered metaphors
- Experimental formats

Otherwise, aim for **ordered clarity** — even when complexity is involved.

---

## Prompt Fix Activity

Start with your current prompt. Ask:

1. How many outcomes does this prompt expect?
2. Is there conflicting tone or purpose?
3. Could I break this into 2–3 simpler prompts?
4. Am I expecting one result or many?

Now revise.

---

## Final Insight

> “Entropy makes systems collapse — or evolve.”

Your prompt is a system.  
Minimize chaos _unless_ your goal is creative risk.

Write with intention.  
Let entropy serve the story — not sabotage it.
