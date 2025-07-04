# 04 – Shadow Inference  
_Part of the Deep Structures series in the Prompt Dissection Lab_

> Every prompt carries a shadow.  
> And the AI completes both — the words **and** what hides beneath them.

---

## What Is Shadow Inference?

When you write a prompt, you're not just giving instructions.  
You're also **signaling intent, tone, audience, and context** — even if you don’t say so directly.

These invisible cues form the **shadow** of your prompt.  
AI often completes that shadow as confidently as it completes the visible part.

| Prompt Says              | AI Might Infer                            |
|--------------------------|-------------------------------------------|
| “Give me a summary”      | Formal tone, business setting             |
| “Fix this paragraph”     | You want clarity and correctness          |
| “Make it better”         | Improve for readability or persuasiveness |
| “Add energy to this”     | You want a punchier, possibly informal tone |

---

## Why It Matters

You might say:  
> “But I didn’t mean it _that_ way.”

AI doesn’t know that.  
It doesn’t _understand_ your intention — it completes based on **statistical patterns** and **probable meanings**.

> If your output feels “off,” your shadow may be louder than your words.

Understanding shadow inference helps you:

- Diagnose confusing or misaligned responses  
- Design better roleplay or tone-switching prompts  
- Use silence as a feature — or neutralize unintended vibes  

---

## Types of Shadows to Watch

### 1. **Tone Shadows**  
Unspoken formality or informality.

> “Can you help me write something good for this?”  
→ AI might return a polished, overly corporate tone  
→ Instead: “Make this sound like a confident peer, not a salesperson.”

### 2. **Authority Shadows**  
What power dynamic does the prompt imply?

> “Fix this email.”  
→ AI might assume you're a manager editing a subordinate’s draft  
→ Instead: “Help me adjust this peer-to-peer email for clarity.”

### 3. **Purpose Shadows**  
What outcome does it _feel like_ you're aiming for?

> “Give me pros and cons of remote work.”  
→ AI might infer neutrality — or assume a business decision angle  
→ Add specificity: “Evaluate from the perspective of employee morale.”

### 4. **Cultural/Contextual Shadows**  
Subtle word choices suggest cultural, regional, or ideological positioning.

> “Explain wokeness to a conservative audience without offense.”  
→ Requires navigating inferred identity and bias  
→ Prompting here is _as much psychology as syntax_

---

## How to Surface the Shadow

Use this quick mental check before hitting enter:

```text
Is there a tone I'm implying, but not naming?
↓
Is there a role or audience being assumed?
↓
Is there a goal I'm hinting at, but not stating?
↓
Could this be read multiple ways?
```

If yes — **name the shadow** before AI completes it for you.

---

## Rewrite Exercise: Light vs Shadow

Take the original prompt:

> “Make this paragraph better.”

Unclear. Let’s surface the shadows.

| Rewritten Prompt                                                        | Shadow Revealed               |
|-------------------------------------------------------------------------|-------------------------------|
| “Simplify this paragraph for a grade 6 reader.”                         | Reading level                 |
| “Make this more emotionally persuasive for an NGO donor letter.”       | Audience + tone + outcome     |
| “Edit this for clarity and reduce jargon for a tech blog post.”        | Domain + style expectations   |

---

## Prompt Archetypes with Hidden Shadows

| Prompt Type         | Hidden Shadow                                              |
|---------------------|------------------------------------------------------------|
| “Write something about X” | Assumes you know the purpose, tone, and audience for “something” |
| “Fix this”          | Implies something is wrong — but doesn’t define “better”   |
| “Make it funnier”   | Humor type? Audience? Witty or absurd?                     |
| “Summarize this”    | For whom? For what format? How short is “summary”?         |

Each of these carries invisible baggage. Unpack it.

---

## Closing Thought

> Prompting isn’t just about what you _ask_.  
> It’s also about what you _imply_ — and whether the AI picks up on it, or invents its own.

To prompt better, **learn to see your shadow.**

---

### 📎 Related Files

- [03-deep-mirroring.md](./03-deep-mirroring.md)
- [05-instruction-vs-intention.md](./05-instruction-vs-intention.md)
- [README.md](./README.md)
