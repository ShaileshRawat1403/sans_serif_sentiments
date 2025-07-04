# 05 – Instruction vs Intention  
_Part of the Deep Structures series in the Prompt Dissection Lab_

> A prompt is not just a command.  
> It's a negotiation between what you said and what you meant.

---

## Why This Distinction Matters

Many AI prompt failures happen not because the instruction was missing —  
but because the **intention** behind it wasn’t clear or aligned.

| Prompt          | AI Action                         | But You Meant…                             |
|-----------------|-----------------------------------|--------------------------------------------|
| “Shorten this”  | Trims words mechanically          | Keep the _tone_, lose _fluff_              |
| “Rewrite this”  | Overhauls structure + language     | Just fix one awkward sentence              |
| “Make it better”| Improves grammar and flow         | Inject more _emotion_ or _punch_           |

You got the **literal output** — not the **intended one**.

---

## The Misalignment Gap

We often assume AI will “know what we meant.”  
It won’t. It completes patterns.

If your **intention** is emotional, strategic, or stylistic —  
you must signal it **explicitly**, or the AI will guess.

> Good prompting is just **clarifying the subtext.**

---

## Common Intention Conflicts

| Instruction               | Likely AI Behavior                    | Hidden Intention That Fails                 |
|---------------------------|----------------------------------------|---------------------------------------------|
| “Summarize this”          | Generic summary                        | Make it _engaging_ for presentation         |
| “Improve this paragraph”  | Fix grammar                           | Add persuasive force for marketing          |
| “Simplify this section”   | Shortens sentences                    | Reframe for _clarity_, not just brevity     |
| “Write a caption”         | Neutral tone                          | You wanted _humor_ or _urgency_             |

---

## Prompting for Intention

When giving a prompt, ask yourself:

```text
What do I want this to _feel_ like?
↓
Who am I speaking to, really?
↓
What outcome am I aiming for?
↓
What trade-off matters more: tone, speed, accuracy, style?
```

Then reframe the instruction to reflect that.

---

## Sample Rewrite Patterns

> Original: “Fix this paragraph.”

| Rewrite Intent       | Prompt Example                                                         |
|----------------------|-------------------------------------------------------------------------|
| Emotional Alignment  | “Make this more hopeful, but still grounded in realism.”                |
| Format Shift         | “Turn this into a concise list for a busy executive.”                   |
| Persuasion           | “Adjust this to feel more convincing, as if pitching to a skeptic.”     |
| Cultural Awareness   | “Rewrite this to be more neutral and respectful for a global audience.” |

---

## Prompt Layering Tip

When unsure, **layer** your intention:

```text
Step 1: Give the main instruction.
Step 2: Add role or audience.
Step 3: Add desired impact or feel.
Step 4: Add example or comparison.
```

🪜 Example:

> “Rewrite this as a LinkedIn post → for mid-level professionals → make it sound casually confident, not too formal → Think tone like Adam Grant, but shorter.”

---

## Closing Reflection

> Clarity is just one layer.  
> **Intention** is the soul of the prompt.

To collaborate well with AI, you must learn to make the invisible **visible**.

---

### 📎 Related Files

- [04-shadow-inference.md](./04-shadow-inference.md)
- [06-deep-context-framing.md](./06-deep-context-framing.md)
- [README.md](./README.md)
