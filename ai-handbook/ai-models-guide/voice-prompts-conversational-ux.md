# Voice Prompts and Conversational UX

_Designing Natural Interactions for Humans — Not Just Commands for AI_

***

## 📁 Table of Contents

* [What Is Conversational UX (And Why It Matters)](voice-prompts-conversational-ux.md#what-is-conversational-ux-and-why-it-matters)
* [How Voice Prompts Differ from Text Prompts](voice-prompts-conversational-ux.md#how-voice-prompts-differ-from-text-prompts)
* [Designing for Natural Conversations](voice-prompts-conversational-ux.md#designing-for-natural-conversations)
* [Common Pitfalls in Voice-Driven AI UX](voice-prompts-conversational-ux.md#common-pitfalls-in-voice-driven-ai-ux)
* [Prompt Structures for Better Voice Inputs](voice-prompts-conversational-ux.md#prompt-structures-for-better-voice-inputs)
* [Examples: Good vs Bad Voice Prompts](voice-prompts-conversational-ux.md#examples-good-vs-bad-voice-prompts)
* [Testing and Calibrating Voice UX](voice-prompts-conversational-ux.md#testing-and-calibrating-voice-ux)
* [Reflection Activity: Voice Audit Sprint](voice-prompts-conversational-ux.md#reflection-activity-voice-audit-sprint)
* [Resources and Toolkits](voice-prompts-conversational-ux.md#resources-and-toolkits)

***

## 🧠 What Is Conversational UX (And Why It Matters)

Conversational UX is about designing interactions that feel **human**, **fluid**, and **intent-driven** — not robotic, repetitive, or overly scripted.

Voice is:

* Personal and ambient
* Context-dependent
* A trust signal (in tone, pacing, and hesitation)

> 🗣️ A good voice experience feels like help — not a quiz.

***

## 🔄 How Voice Prompts Differ from Text Prompts

| Feature           | Text Prompts                  | Voice Prompts                        |
| ----------------- | ----------------------------- | ------------------------------------ |
| Input Method      | Typed                         | Spoken                               |
| Clarity Need      | High (reader controls pacing) | Higher (listener has no scrollback)  |
| Structure         | Flexible                      | Needs stronger guidance, intent cues |
| Context Retention | Persistent in chat            | Requires memory or re-prompts        |
| Interruptions     | Rare                          | Frequent, natural in conversation    |

Voice requires:

* Simpler phrasing
* Repeatable formats
* Anticipation of misunderstanding

***

## 🎨 Designing for Natural Conversations

To make AI feel conversational:

* **Start with a warm opener** → "Hey there, what are you working on today?"
* **Use follow-ups instead of long forms** → Break into back-and-forth prompts
* **Acknowledge previous input** → "You mentioned needing a draft — should I use the same tone as last time?"
* **Repeat or rephrase if unsure** → "Just to confirm — do you want a summary or an outline?"

> 🤖 Good AI doesn’t just generate — it converses, confirms, and clarifies.

***

## ⚠️ Common Pitfalls in Voice-Driven AI UX

* ❌ **Info dumping** — Too much at once; causes overwhelm
* ❌ **No interrupt handling** — User interjections break the flow
* ❌ **Ambiguous confirmations** — "Got it" when it’s not clear what was got
* ❌ **Flat tone or pacing** — No vocal variety = user drop-off
* ❌ **Context forgetfulness** — Not referencing earlier points

Fix by:

* Building turn-based logic
* Using natural filler phrases
* Implementing soft failbacks

***

## 🏗️ Prompt Structures for Better Voice Inputs

### 🧱 Modular Prompt Format

> "Let’s start with the basics: What’s your goal today?"

Then:

* Clarify intent
* Offer categories or choices
* Confirm and summarize

### 🎯 Voice Prompt Template

> "I can help you with \[task type], \[task type], or \[task type]. What would you like to do?"

→ Follow-up:

> "Got it — for that task, do you want something \[tone 1] or \[tone 2]?"

→ Confirm again before output:

> "So you’d like a \[type] in a \[tone] voice — shall I begin?"

***

## 🧪 Examples: Good vs Bad Voice Prompts (Flavor + Function)

### 🎙️ Use Case: Writing a Quick Summary

**❌ Bad Prompt:**

> "Welcome to the system. Please state the purpose of your inquiry in 25 words or less."

**✅ Flavor + Function Prompt:**

> "Alright, what are we summarizing today — a meeting, a doc, or a wall of chaos?"

***

### 🔍 Use Case: Getting Customer Feedback

**❌ Bad Prompt:**

> "Please leave your comments regarding the service in the following recording window."

**✅ Flavor + Function Prompt:**

> "Mind sharing how that went? The good, the bad, or the glitchy — we want it all."

***

### ✍️ Use Case: Preparing a Daily Brief

**❌ Bad Prompt:**

> "State your morning priorities for task sorting and workflow optimization."

**✅ Flavor + Function Prompt:**

> "What’s on your plate today? Think: Must-do, could-wait, and might-explode."

***

### 💬 Use Case: Clarifying Input Tone

**❌ Bad Prompt:**

> "Select communication format and emotional register."

**✅ Flavor + Function Prompt:**

> "How should this sound — polite and polished, or plain and punchy?"

> 🧠 Great voice prompts respect confusion. They anticipate real human moods — not perfect behavior.

***

## 🧪 Testing and Calibrating Voice UX

Checklist:

* [ ] Are voice prompts **short, warm, and clear**?
* [ ] Can the user **interrupt** and be understood?
* [ ] Does the AI handle **repetition or confusion** gracefully?
* [ ] Is tone varied (not robotic or overly formal)?
* [ ] Do transitions between steps feel **natural**?
* [ ] Can it remember **user preferences**?

Tools:

* Voiceflow, Alan AI, Speechly
* Whisper (OpenAI), Mozilla DeepSpeech
* User testing with playback reviews

***

## 🔍 Reflection Activity: Voice Audit Sprint

Run a 30-minute audit of your product’s voice UX:

1. Pick 3 common user journeys.
2. Simulate them by voice.
3. Record how often you felt:
   * Confused
   * Interrupted
   * Surprised (good or bad)
4. List where clarification or warmth was missing.
5. Rewrite 3 key voice prompts with:
   * Human opener
   * Confirmation step
   * Personalized close

***

## 📚 Resources and Toolkits

* [Voiceflow Design Guides](https://www.voiceflow.com/)
* [Google Conversational Design](https://designguidelines.withgoogle.com/conversation-design)
* [Speechly](https://www.speechly.com/blog)
* [Whisper by OpenAI](https://openai.com/research/whisper)
* [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech)
* [BBC Voice + Tone Guidelines](https://bbc.github.io/gel/guidelines/voice-and-tone/)

***

📘 Next in Series: [Risks, Red Flags, and Responsible Use](ai-risks-responsibility.md)
