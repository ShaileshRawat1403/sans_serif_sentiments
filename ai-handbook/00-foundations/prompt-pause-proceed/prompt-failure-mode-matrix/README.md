#  Prompt Failure Mode Matrix  

*A diagnostic guide to identify, understand, and correct common AI prompt issues.*

---

##  Table of Contents


- [What This Is](#-what-this-is)
- [Why Prompts Fail](#-why-prompts-fail)
- [The Failure Mode Matrix](#-the-failure-mode-matrix)
- [Real-World Examples](#-real-world-examples)
- [How to Use This in Practice](#-how-to-use-this-in-practice)
- [Helpful Prompts to Diagnose Output](#-helpful-prompts-to-diagnose-output)
- [References & Resources](#-references--resources)

---

##  What This Is


This guide helps you identify why your AI prompt didn’t deliver what you expected.  
It’s not just about “fixing” bad results — it’s about **understanding where the prompt broke down.**

> _Use this matrix before asking: “Why is ChatGPT so dumb?”_ 😄

---

##  Why Prompts Fail


Even advanced users misjudge prompts because they:

- Overestimate how well AI “understands” intent
- Assume tone, format, or audience will be “inferred”
- Forget AI doesn’t know context unless explicitly told

**AI is not a mind-reader. It’s a pattern completer.**  
This matrix is designed to help you debug that pattern logic.

> _Without clearly defining your end goal, AI has to guess which direction you're heading._

---

##  The Failure Mode Matrix


| Mode | What It Looks Like | Likely Cause | Fix Strategy |
|------|--------------------|--------------|--------------|
| **🟠 Vague Prompt** | Output is generic, off-topic, or unhelpful | No audience, unclear format, broad ask | Add role, tone, format, purpose |
| **🔵 Misaligned Output** | Output “sounds good” but isn’t what you meant | Ambiguous phrasing, no goal | Ask for summary: “What do you understand?” |
| **🟣 Overstuffed Prompt** | AI gets lost or gives wall of text | Too many instructions at once | Break it into sequenced steps |
| **🟤 Under-scoped Prompt** | AI gives 1–2 lines when you expected more | No length or depth guidance | Specify depth, format (e.g. table, story) |
| **⚫ Hallucinated Answer** | Confident but false info | No source constraint, vague context | Add “Cite sources” or use retrieval-based model |
| **⚪ Unexpected Style or Tone** | Sounds robotic or childish when you expected elegant | No tone or audience guidance | Define style and target audience clearly |
| **🟥 Repetition or Loops** | AI repeats ideas unnecessarily | Prompt wording looped or lacked end-goal | Set structure (e.g., “give 3 points, each with 1 sentence”) |
| **🟩 Output is Right, But You Don’t Know Why** | Feels correct but you don’t understand it | Jumped to answer without scaffolding | Ask: “Walk me through your reasoning” |
| **🟧 Assumed Memory** | AI “forgets” previous context or contradicts itself | No memory active or exceeded context window | Rebuild context or chunk prompt history |
| **🟨 Copied Template Gone Wrong** | Output mimics format but not logic | Misused example, misunderstood context | Ask AI to first explain the template's function |

---

##  Real-World Examples


| ❌ Prompt | Result | Failure Mode | ✅ Fix |
|----------|--------|---------------|--------|
| “Help with resume” | Unfocused blob of tips | Vague | “Act as a hiring manager. Review this resume and suggest improvements in bullet points.” |
| “Tell me about climate” | Random fact list | Under-scoped | “Summarize top 3 climate challenges in 2024, with examples and citations.” |
| “Write a witty caption” | Generic jokes | Misaligned Output | “Give 3 witty, clever captions for a marketing post targeting B2B founders.” |
| “Summarize this” | Misses key point | Overstuffed | “Summarize this 300-word email into 2 sentences for a busy executive. Preserve the ask.” |
| “Write a poem” | Drab rhyming output | Under-scoped | “Write a haiku about time, in the tone of Alan Watts.” |
| “Make this clearer” | Dry rewrite, wrong tone | Unexpected Tone | “Rephrase this paragraph in a casual, friendly tone for 20-year-old students.” |
| “Explain taxes” | Technical jargon overload | Misaligned | “Explain what income tax is using a lemonade stand analogy for 10-year-olds.” |

---

## ️ How to Use This in Practice


**1. Diagnose**  
Ask yourself: *Which row of the matrix does my output fall into?*

**2. Reverse-Engineer**  
Ask the AI:  
- “How did you interpret my prompt?”  
- “What assumptions did you make?”  
- “What audience did you write for?”  
- “What part of the prompt seemed most important to you?”

**3. Fix the Prompt**  
Use this format:  
> “You are a [role]. Write a [format] for [audience] about [topic], keeping the tone [X] and length [Y].”

**4. Try Again**  
Only change **one variable** at a time.  
Refinement is a loop — not a reset.

---

##  Optional Visual Decision Tree (Text)


```
[Prompt Failed?]
     ↓
[What's wrong with output?]
     ↓
[Too vague] → Add format + role + tone  
[Too short] → Add depth / scope guidance  
[Wrong tone] → Specify audience + style  
[Hallucinated] → Add source request or switch model  
[Sounds okay, but not what I meant] → Ask AI how it interpreted  
[Lost context] → Rebuild context manually  
     ↓  
Refine + Retry  
```

---

##  Helpful Prompts to Diagnose Output


- “Summarize your interpretation of my prompt in one sentence.”
- “What part of my prompt was unclear?”
- “Who do you think this is for?”
- “On what data or pattern did you base that answer?”
- “Rewrite this response assuming the audience is a 12-year-old.”
- “Can you explain your reasoning like you’re teaching it?”
- “Would you like me to clarify or reframe anything?”

---

##  References & Resources


- [OpenAI Cookbook: Prompt Engineering Best Practices](https://github.com/openai/openai-cookbook/blob/main/articles/how_to_work_with_large_language_models.md)
- [Anthropic Prompting Guide (Claude)](https://docs.anthropic.com/claude/docs/prompting-best-practices)
- [Google Developer Prompt Style Guide](https://developers.google.com/style/prompts)
- [PromptingGuide.ai](https://www.promptingguide.ai)
- [Dan Shipper: Why Your Prompts Don’t Work](https://every.to/chain-of-thought/the-reason-your-prompts-don-t-work)
- [Nielsen Norman Group on UX Writing Clarity](https://www.nngroup.com/articles/ux-writing/)
- [ARC Primer: LLM Evaluation](https://alignment.org/)

---

> _“You don’t need to be a programmer to talk to machines —  
you just need to learn how to **think with precision**.”_

---

##  Next:

- [📘 Prompt Dissection Lab Overview](../README.md)
- [📍 Track 1: Clarity & Structure](./clarity-structure-track.md)
- [📍 Track 2: Literary & Linguistic Guide](./literary-linguistic-track.md)
