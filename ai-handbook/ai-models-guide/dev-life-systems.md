---
icon: dev
---

# dev-life-systems


##  Dev Life Systems


> _“You’re not just coding a product. You’re coding your perception of time, sanity, and scale.”_

A modular, markdown-first system to help developers:

* Think before they code 🧠
* Communicate better than they explain 💬
* Grow without burning out 🪴

This isn't a dev bootcamp.\
It's a **thinking and clarity system** to help you ship better code, cleaner messages, and a more sustainable developer life.

***

###  Table of Contents


* [📦 What Is This, Really?](dev-life-systems.md#what-is-this-really)
* [🌱 Why This Exists](dev-life-systems.md#why-this-exists)
* [🧩 How to Use This](dev-life-systems.md#how-to-use-this)
* [📘 Repo Overview: Full Section Map](dev-life-systems.md#repo-overview-full-section-map)
* [🔗 Related Systems](dev-life-systems.md#related-systems)
* [🚀 Let’s Begin](dev-life-systems.md#lets-begin)

***

###  What Is This, Really?


This is a **modular, markdown-first guide** to:

| Layer                           | Description                                                     |
| ------------------------------- | --------------------------------------------------------------- |
| `Thinking Before Code`          | Problem framing, architecture tradeoffs, AI as thinking partner |
| `Doing During Code`             | Function design, debugging, Git clarity, Copilot prompts        |
| `Communicating Beyond Code`     | Dev writing, async updates, decision docs                       |
| `Existing Outside the Terminal` | Burnout, mental models, growth compass                          |
| `Starter Kits`                  | Templates, reflection journals, dev README                      |

Each module is standalone. Use what resonates. Remix the rest.

***

###  Why This Exists


Because most developer resources teach you how to _write code._\
Few teach you how to **survive the ecosystem** around it:

* The meetings, merges, migraines
* The PR reviews and Slack messages
* The weekend rebuilds

We want to offer a **system** that scales with your brain, not just your repo.

A system rooted in:

* 🧠 Reflection over reaction
* ✍️ Communication over explanation
* 🧭 Thinking over tooling

***

###  How to Use This


#### Start Here:


* Calibrate your mindset with [Thinking Before Code](dev-life-systems.md#thinking-before-code)
* Choose a module that reflects where you’re stuck (thinking, doing, communicating, or living)

#### Then:


* Use the prompts, templates, and mental models in your own workflow
* Pair them with AI tools, journaling, or even team retros
* Revisit this doc as your career — and cognition — evolves

***

###  Repo Overview: Full Section Map


```
dev-life-systems.md
│
├── 0-start-here
│   ├── dev-life-intro (Why this exists)
│   └── how-to-use-this (Daily/Weekly application)
│
├── 1-thinking-before-code
│   ├── friction-first (Problem framing)
│   ├── ladders-vs-loops (Architecture thinking model)
│   ├── ai-as-thought-partner (Prompting + scaffolds)
│   └── cognitive-design-laws (Recursion, echo, etc.)
│
├── 2-doing-during-code
│   ├── code-by-contract (Function clarity)
│   ├── debug-like-a-theorist (Root cause analysis)
│   ├── commit-with-clarity (Git messages, PRs)
│   └── ai-copilot-templates (Scoped prompting)
│
├── 3-communicating-beyond-code
│   ├── fnf-for-dev-writing (Docs, async updates)
│   ├── technical-decision-making (Explaining trade-offs)
│   ├── handoff-systems (Code transfer clarity)
│   └── writing-for-non-devs (Translation layer)
│
├── 4-existing-outside-terminal
│   ├── burnout-checklist (Wellbeing)
│   ├── weekly-dev-reflection (Mini-journaling)
│   ├── dev-growth-compass (Career roadmap)
│   └── developer-routines (Schedule sanity)
│
└── 5-starter-kits
    ├── dev-readme-template (Personal intros)
    ├── ai-copilot-primer (AI scaffolding)
    ├── pair-dev-guide (Pair programming)
    └── clarity-checklist (Before release)
```

***

###  Related Systems


➡️ [_Flavor & Function – Writing as a system_](../../fnf/flavor-and-function.md)\
➡️ [_Prompted But Not Prepared – The AI Gap Handbook_](../prompted-but-not-prepared/)\
➡️ [_This Might Change Everything – Change Comms Toolkit_](../../change-communications/this-might-change-everything/)

***

###  Lets Begin


We start, not with code—but with friction.\
👉 [Go to: Thinking Before Code →](dev-life-systems.md#thinking-before-code)

{% hint style="info" %}
Or reflect before you write:\
👉 [Jump to: Weekly Dev Journal →](dev-life-systems.md#weekly-dev-reflection) (**WIP**)
{% endhint %}

**This isn’t a sprint. It’s a system.**

***

##  Thinking Before Code


> _“Good code solves problems. Great code questions them first.”_

***

###  Friction First: Why We Dont Start with Code


> _“Clarity isn’t found in velocity. It’s found in friction.”_

Before you optimize your function, optimize your framing.\
This section introduces a simple but overlooked truth:\
**rushing into code often solves the wrong problem well.**

***

####  What Is Friction First?


Friction First is a thinking habit:

* Pause before typing
* Frame before building
* Question before solving

It’s not procrastination — it’s **problem definition in disguise.**\
You’re not avoiding momentum. You’re avoiding misdirection.

***

####  Why It Matters


Bad code isn’t just buggy — it’s often irrelevant.\
We don’t just waste time building the wrong feature.\
We waste **trust, team hours, and brain energy.**

When friction is ignored:

* Requirements mutate mid-sprint
* PRs get rewritten by people not in the room
* Documentation lags because no one knew what was being solved

***

#### ️ How to Apply It


Use these before you open your editor:

```markdown
🧠 Friction Prompts

- What is the actual problem — not the visible symptom?
- Who else interprets this problem differently?
- What has already been tried or ruled out?
- What does “good enough” look like for this?
- If we didn't solve this — what would happen?
```

You can also use AI to reflect before coding:

```markdown
🤖 Example Prompt (to use with ChatGPT or Copilot)

“I’m about to build [feature X].  
Here’s what I understand so far:  
- [Known context]  
- [User pain point]  
- [Team assumption]

Can you help me reframe this as a real-world problem worth solving?”
```

***

#### ⏳ When to Use It


* Before estimating a ticket
* When handed a vague spec
* While stuck mid-sprint
* Before merging something that feels “off”

Friction isn’t a blocker.\
It’s a beacon.

***

###  Ladders vs Loops: Thinking in Systems, Not Steps


> _“Most code moves in steps. Most problems move in circles.”_

This section reframes how developers think about architecture, logic, and decision-making.\
Because not all progress is linear — especially in systems with recursion, feedback loops, and team dependencies.

***

####  What Are Ladders and Loops?


* **Ladders** are linear.\
  They assume steps A → B → C will get you to D.\
  Great for tutorials, onboarding, and well-bounded functions.
* **Loops** are systemic.\
  They revisit past states.\
  Ideal for feedback systems, real-time apps, learning algorithms.

Both are valid.\
The danger is applying ladder thinking to a looped reality.

***

####  Why It Matters


We often build with ladder assumptions:

* “Once I fix this bug, it’s solved.”
* “If we refactor now, it’ll stay clean.”
* “This decision won’t come back next sprint.”

Reality is looped:

* New bugs appear from old fixes
* Clean code decays with features
* Technical decisions echo across domains

Knowing the **loop** helps you design for it.

***

#### ️ How to Apply It


Before building:

* Ask: Is this system **stateful or stateless**?
* Check: Will users revisit this? Will the output become future input?
* Map: What happens if this process runs more than once?

Loop Awareness Prompts:

```markdown
- What’s the most likely recursive failure in this system?
- How does this process reset, recover, or re-trigger?
- Are we treating a loop like a ladder just to feel done?
```

***

####  Loop vs Ladder → A Mental Shortcut


| Pattern        | Ladder Thinking          | Loop Thinking                          |
| -------------- | ------------------------ | -------------------------------------- |
| User Flows     | Finish registration once | Return to profile, settings, re-engage |
| Team Habits    | One-off PR review        | Ongoing review patterns                |
| Technical Debt | Clean once and forget    | Accept rot and schedule rework cycles  |

***

####  Bonus: AI Copilot Prompt


```markdown
Prompt:
“I’m designing a [feature/process] that feels linear, but might behave cyclically.

Here’s how I see the flow:
- [Steps]

Can you help explore possible loop states, failure recursions, or revisit paths?
```

***

###  AI as Thought Partner: Dont Just Prompt - Reflect


> _“A good developer doesn’t just use AI. They train it to think with them.”_

Most people treat AI like a code vending machine.\
But its real strength isn’t in writing code — it’s in **questioning assumptions, generating perspectives, and co-framing problems.**

This section helps you move from **commanding AI** to **collaborating with it.**

***

####  What Does “AI as Thought Partner” Mean?


It means using AI to:

* **Co-frame** the problem, not just solve it
* **Reflect** on blind spots
* **Simulate** counterpoints
* **Document** understanding

Think of it as rubber duck debugging,\
if the duck had access to the internet, StackOverflow, and your team’s Slack threads.

***

####  Why It Matters


Most errors come from misframed problems, not mistyped code.

Using AI as a collaborator helps:

* Reduce tunnel vision
* Generate architectural tradeoffs
* Translate complexity into clarity
* Explore “what if” scenarios faster than whiteboards

AI isn't here to replace your thinking.\
It’s here to extend it — when prompted right.

***

#### ️ How to Apply It


**🧩 Thought Partner Prompt Template**

```markdown
“I’m working on [feature/module/system].

Here’s what I understand:
- Context: [short summary]
- Constraint: [edge case or limitation]
- Question: [what I want to explore]

Can you simulate:
- Tradeoffs?
- Counter-approaches?
- Known failure patterns?

Act like a teammate who asks ‘have you considered…?’”
```

***

**💡 More Prompts to Try**

```markdown
🧠 “What might I be assuming that isn’t true?”
💬 “How would a new engineer misunderstand this?”
🔍 “What would break if this runs 10x more often?”
📚 “What’s a metaphor or analogy for this system?”
```

***

####  Bonus Tip: Run the Reversal


Ask AI:

```markdown
“Pretend I’m doing the opposite of what’s ideal here.  
What flaws or missed opportunities would show up?”  
```

***

###  Cognitive Design Laws: How Minds Actually Use Systems


> _“You’re not just designing code. You’re designing cognition.”_

Most dev systems fail not because they’re broken —\
but because they’re **mentally expensive.**

This section outlines four foundational **cognitive design laws** to help you build systems that align with how humans think, remember, and decide.

***

####  What Are Cognitive Design Laws?


These are mental heuristics based on human psychology —\
adapted for system thinkers and developers:

1. **Friction Law** – The harder something feels, the faster people bail.
2. **Echo Law** – People only remember what you repeat.
3. **Assembly Law** – If something must be pieced together, make the pieces obvious.
4. **Recursion Law** – People don’t retain info in steps. They loop until it clicks.

***

####  Why It Matters


Most software guides, dev onboarding flows, and even team rituals:

* Demand too much cognitive load
* Hide dependencies in linear documents
* Confuse clarity with completeness

By applying these laws, you build systems that **work with the brain**, not against it.

***

####  How to Apply It


**Friction Law**

**Make the first action obvious and low effort.**

```markdown
✅ Start with one-click dev setup  
✅ Show sample output before config  
❌ Long README before first line of code  
```

**Echo Law**

**Repeat the right idea in multiple ways.**

```markdown
✅ Restate goals at top + inline + in commits  
✅ Align variable names with problem language  
❌ Only explain once in a kickoff call  
```

**Assembly Law**

**Expose the pieces needed for synthesis.**

```markdown
✅ Use visual TOC or callouts for modules  
✅ Create “If you’re here, you need…” sections  
❌ Assume readers will mentally map your file tree  
```

**Recursion Law**

**Design for re-entry, not perfect flow.**

```markdown
✅ Let users jump in at any section  
✅ Add TL;DRs + re-frames per module  
❌ Force completion of steps to understand next  
```

***

####  When to Use These Laws


* Writing documentation or internal tools
* Creating onboarding flows
* Designing modular systems or helper functions
* Reviewing someone else’s architecture

***

##  Doing During Code


> _“Your function isn’t just outputting logic. It’s declaring intent.”_

The moment you start coding, you’ve started communicating — with your future self, your teammates, and sometimes the product itself.

This section covers how to **code with clarity, context, and cognitive reduction** in mind.

***

###  Code by Contract: The Function is a Promise


> _“A good function does something. A great function means something.”_

Most devs are taught to “make it work.”\
But professional-grade devs code like they’re making a **contract.**

***

####  What Is Code by Contract?


Every function or module is a **promise**:

* If called with X, it will return Y
* It won’t throw unless Z happens
* It has boundaries you can count on

The function is a small system.\
And every system needs **intent, guarantees, and conditions.**

***

####  Why It Matters


When functions don’t declare contracts:

* Tests break on side effects
* Other devs misuse them
* Bugs hide in ambiguity

Code by contract prevents **cognitive outsourcing** — where others have to guess what you meant.

***

#### ️ How to Apply It


**Step 1. Start With Intent**

```markdown
// Good
function getUserProfile(userId) {
  // returns profile with metadata for a given user
}

// Better
/**
 * Fetches complete profile metadata.
 * Throws error if user not found.
 */
function getUserProfile(userId) {
  ...
}
```

**Step 2. Declare Assumptions and Failures**

```markdown
/**
 * Assumes valid userId string.
 * Rejects with 404 if user not found.
 * Cached for 1hr.
 */
```

**Step 3. Write Self-Documenting Logic**

```js
// ❌ Obscure
if (user && user.active && !user.banned) { ... }

// ✅ Clear
const isEligible = user?.active && !user?.banned;
if (isEligible) { ... }
```

***

####  Prompt to Use With AI


```markdown
“I’m writing a utility function called [X].

Help me define:
- What it guarantees (contract)
- Its expected edge cases
- How to communicate assumptions via comments or naming”
```

***

Next: [Debug Like a Theorist →](dev-life-systems.md#debug-like-a-theorist)

***

###  Debug Like a Theorist: Root Cause, Not Quick Fix


> _“Fixing the bug isn’t the same as understanding it.”_

Most developers debug to remove the error.\
But great developers debug to **map the cause.**

This section is about treating bugs like **symptoms**, not interruptions.

***

####  What Does “Debug Like a Theorist” Mean?


* Think like a systems analyst, not a patcher
* Seek the pattern, not just the line
* Document what broke _and_ why it broke that way

It’s not about solving faster.\
It’s about preventing repetition.

***

####  Why It Matters


Fixes without theory:

* Get reversed next sprint
* Miss deeper systemic flaws
* Lead to false confidence

True debugging helps uncover:

* Unexpected side effects
* Architectural mismatches
* Forgotten assumptions

***

#### ️ How to Apply It


**Step 1. Trace Back, Not Down**

```markdown
❌ “Where is this breaking?”
✅ “What chain of logic led here — and why was it trusted?”
```

**Step 2. Document The Bug, Not Just the Fix**

```markdown
// BAD: “Fixed null error”
commit: fix(user): added null check

// GOOD:
commit: fix(user): handle deleted users gracefully
context: some profiles were still referenced after deletion
```

**Step 3. Use the 3 Why Ladder**

```markdown
- Why did this error happen?
- Why was that allowed in this system?
- Why was it unnoticed until now?
```

***

####  Bonus Tool: Failure Friction Map


Create a quick sketch or note:

```markdown
[ Symptom ]
↓
[ Entry Point ]
↓
[ Misassumption ]
↓
[ Systemic Cause ]
```

This becomes valuable for:

* Future contributors
* Documentation retros
* AI-based co-debugging

***

####  Prompt to Use With AI


```markdown
“I encountered this error: [paste message]

Here’s the flow it happened in:
- [Step 1]
- [Step 2]
- [Trigger]

Can you simulate:
- Possible chain of logic behind it
- Assumptions that were likely false
- Ways to frame this for teammates?”
```

***

###  Commit With Clarity: Messaging as Engineering


> _“Every commit is a design decision — say it like you mean it.”_

We think of Git as a log.\
But it’s a **shared brain** — how teams trace decisions, roll back errors, and onboard new devs.

This section helps you **write commits like cognitive breadcrumbs** — readable, reliable, and reusable.

***

####  What It Means to “Commit With Clarity”


* Your future self will read this
* Your team might debug this
* Your code might outlive your job

Clear commits aren’t for vanity.\
They’re for **sustainable development.**

***

####  Why It Matters


Poor commits lead to:

* Useless version histories
* Confusion during code reviews
* Extra time reversing or explaining changes

Clear commits:

* Save time
* Speed up onboarding
* Strengthen team trust

***

#### ️ How to Apply It


**Step 1. Use Conventional Commits (as a baseline)**

```markdown
feat(module): add payment retry logic  
fix(api): handle missing auth token  
chore(docs): update README with new config  
```

**Step 2. Add Context When It Matters**

```markdown
✅ fix(auth): add null check to avoid crash
context: crash occurred when user’s profile was not initialized

✅ feat(ui): support dark mode toggle
includes theme context + localStorage persist
```

**Step 3. Write Like a Change, Not a Reflection**

```markdown
❌ “Tried fixing crash”  
✅ “Fix: handle null profile on auth startup”
```

***

####  Bonus: PR Template Checklist


```markdown
##  What Changed

- Added X
- Removed Y
- Modified Z

##  Why It Matters

- Solves A
- Avoids B

##  Test Instructions

1. Go to…
2. Trigger…
3. Observe…

##  Additional Context

- Related to bug #ID
- Inspired by [link]
```

***

####  Prompt to Use With AI


```markdown
“I’m committing this change: [describe]

Can you help:
- Frame it in conventional commit format
- Summarize the context clearly
- Make it future-searchable?”
```

***

###  AI Copilot Templates: Smart Prompts for Scoped Output


> _“The better the framing, the better the function.”_

Most developers ask AI to code.\
Great developers ask AI to think — _within boundaries._

This section gives you **copilot-ready prompt templates** that reduce rework, hallucinations, and bloat.

***

####  Whats the Goal Here?


Write better prompts for:

* Utility functions
* API integrations
* Unit tests
* Explaining design patterns
* Translating logic across languages

AI should **snap to your scaffolding** — not create from chaos.

***

####  Why It Matters


Vague prompts lead to:

* Bloated code
* Wrong assumptions
* Misaligned patterns

Scoped prompts give you:

* Cleaner output
* Easier debugging
* Safer integrations

***

#### ️ How to Apply It


**Step 1. Scaffolded Function Template**

```markdown
I need a function for:
- [Goal]: What should it do
- [Input]: What format/data is expected
- [Output]: Format and handling
- [Constraints]: Any edge cases, limits
- [Language/Framework]: If applicable

Return:
- Function only
- With inline comments
- No execution unless stated
```

***

**Step 2. Test Generator Template**

```markdown
I have a function called [function name].

Generate:
- 3 passing tests
- 2 edge cases
- 1 intentionally failing test

Use [testing framework]. Keep assertions clean.
```

***

**Step 3. Refactor With Reason**

```markdown
Here’s a block of code:
[paste]

Can you:
- Refactor for readability
- Reduce nesting
- Add brief comment above each logical block
```

***

**Step 4. Design Patterns Aid**

```markdown
I’m solving [problem].

What pattern (from [language/framework]) best fits this?

Explain why briefly. Optional: sample implementation.
```

***

**Step 5. Translate Logic**

```markdown
I have code in [language] that does [function].

Can you convert it to [target language], 
keeping logic intact and idiomatic?

Explain any differences.
```

***

####  Copilot Philosophy


AI is here to speed up structure, not skip understanding.\
Always:

* Prompt with clarity
* Edit with skepticism
* Learn from the output

***

## ️ Communicating Beyond Code


> _“If your code needs explanation — explain it well.”_

Being a great developer isn’t just about logic.\
It’s about **communication clarity** — across docs, comments, PRs, emails, and decisions.

This section shares developer-specific writing strategies using the **Flavor & Function (FnF)** framework.

***

###  FnF for Dev Writing: Writing That Does More Than Inform


> _“Writing is not a handoff. It’s part of the build.”_

Most developers write as an afterthought.\
But written clarity is an act of engineering —\
especially when you're handing over decisions, not just code.

This section shows how to apply **FnF writing** to your:

* README files
* PR descriptions
* Architecture docs
* Async updates
* Dev blogs

***

####  Whats Flavor & Function (FnF)?


It’s a writing model for **clarity and usability**:

* **Flavor** = Human tone, rhythm, reader empathy
* **Function** = Structure, scannability, clarity of action

Great dev writing **guides attention**, not just dumps info.

***

####  Why It Matters


Bad writing isn’t just boring — it’s expensive:

* Slower handoffs
* Confused readers
* Redundant explanations

FnF helps:

* Make async updates actionable
* Reduce misinterpretation
* Strengthen team trust

***

#### ️ How to Apply It


**For README Sections**

```markdown
❌ “This repo handles the payment system”
✅ “This repo powers secure payment workflows — from checkout to webhook receipt”

❌ “Usage”
✅ “Getting Started: 2-min local run”
```

**For PRs**

```markdown
## What Changed

Refactored cart logic to support multi-currency display

## Why It Matters

Old logic failed on currency-switching. This aligns with global rollout goals.
```

**For Dev Blogs or Docs**

```markdown
Start with friction:
> “Our auth system was failing silently. Here’s how we rebuilt trust.”

Use a story + structure combo:
- Problem  
- Attempt  
- Insight  
- Rebuild  
```

***

####  Optional: FnF Checklist for Devs


```markdown
- Is it skimmable?
- Does it answer “why now?”
- Is the title/action label meaningful?
- Will a non-author understand the context?
```

***

####  Prompt to Use With AI


```markdown
“I’m writing a [README, doc, PR, blog] for [topic].

Help me:
- Make it more scannable
- Add a useful intro line
- Reframe the title/action into a reader-friendly label”
```

***

###  Technical Decision-Making: Explain It Like a System


> _“It’s not just what you chose — it’s what you ruled out.”_

Every technical choice implies **trade-offs**, even if you don’t state them.\
Good engineers choose.\
Great engineers explain.

This section helps you **frame and communicate your decisions** — so your reasoning scales.

***

####  What It Means


Technical communication isn’t about dumbing down.\
It’s about **structuring clarity** for:

* Other engineers
* Stakeholders
* Future you

The goal?\
Make decisions transparent, not just traceable.

***

####  Why It Matters


Poorly communicated decisions lead to:

* Redundant debates
* Architecture erosion
* Loss of trust in tech judgment

But clear decision writing helps:

* Align teams faster
* Avoid repeating mistakes
* Build design maturity

***

#### ️ How to Apply It


**Step 1. Use a Decision Memo Format (Lightweight)**

```markdown
###  Decision

Use [X library] for image optimization

###  Context

We had latency issues on mobile for large media loads.

###  Options Considered

- Option A: Client-side compression → good DX, inconsistent results
- Option B: CDN rewrite rules → complex config, limited control
- ✅ Option C: [Chosen solution] → stable, configurable, lower runtime cost

###  Trade-Offs

- Adds a 30kb lib
- May require server cache tuning

### ✅ Reason

Balance of speed + simplicity for our near-term roadmap
```

***

**Step 2. Create a “Why This Exists” Header in Code Files**

```js
// Why this file:
// Handles webhook auth edge case for vendor XYZ
// Exists because their payload schema is non-standard
```

***

**Step 3. Avoid Passive “We Decided” Phrasing**

```markdown
❌ “We decided to go with X.”

✅ “Given [goal] and [constraint], we chose X because [reason].”
```

***

####  Prompt to Use With AI


```markdown
“I made a technical decision to [do X] because of [Y].

Can you help me:
- Write it out using context/options/trade-offs/reason
- Keep it skimmable and reusable in docs or PRs”
```

***

###  Handoff Systems: Dont Just Push Code, Pass Context


> _“A clean commit is not a clean handoff.”_

Shipping code isn’t the finish line — **shared understanding is**.\
Great teams treat handoffs as **system checkpoints**, not personal sign-offs.

This section helps you make your handoffs:

* Thoughtful
* Trackable
* Teachable

***

####  What Makes a Great Handoff?


It’s not about dumping everything.\
It’s about making sure the **next person doesn’t guess.**

A good handoff answers:

* What was built?
* Why was it built this way?
* What are the open threads?

***

####  Why It Matters


Bad handoffs cause:

* Delayed QA/testing
* Bugs during deploy
* Endless Slack clarifications

Strong handoffs enable:

* Async velocity
* Smarter code reviews
* Developer trust

***

#### ️ How to Apply It


**Step 1. Add a “Handoff Context” Section in PRs**

```markdown
##  Handoff Context

- This PR completes X feature but requires Y integration
- Edge case Z is partially handled, needs UX validation
- Watch for bug #1425 regression

Ask: "If I leave tomorrow, will this note help someone pick up?”
```

***

**Step 2. Code Comments for Handoff Hooks**

```js
// This temp override is for hotfix #92
// Revert by 2025-07-01 after refactor PR #212
```

***

**Step 3. Include a “Next Steps” Footer**

```markdown
##  Next Steps

- Merge this after config branch is updated
- Run [script] for final check
- Notify [QA/contact] post-merge
```

***

**4. Use Async Handoff Templates for Remote Teams**

```markdown
###  Summary

[X module] updated to support [feature].

###  Design Rationale

Chosen approach minimizes impact on legacy systems.

### ⚠️ Edge Cases to Note

- Breaks if config.json is missing
- May lag in Safari < 14

###  Ask

Please test with legacy data format.
```

***

####  Prompt to Use With AI


```markdown
“I’m handing off this PR/task.

Help me write:
- A concise handoff summary
- Highlight trade-offs and next steps
- Mention who should be notified or involved”
```

***

###  Writing for Non-Devs: Translate Without Losing Truth


> _“Explaining technical choices isn’t dumbing down. It’s leveling up.”_

You’re not just writing for developers.\
You’re writing for:

* Product managers
* Designers
* Clients
* Future you (with half the context)

This section teaches how to **translate technical concepts** without oversimplifying.

***

####  What It Means


Non-devs don’t want the full stack.\
They want:

* What changed
* Why it matters
* What to expect

And they want it in their **language of goals and outcomes**.

***

####  Why It Matters


Most cross-functional confusion stems from:

* Tech jargon
* Assumed context
* Poor framing

Clear writing prevents:

* Wrong decisions
* Missed dependencies
* Tech-debt misunderstandings

***

#### ️ How to Apply It


**Step 1. Rewrite Commit/PR Titles for Broader Clarity**

```markdown
❌ “Refactor auth controller”

✅ “Streamlined login logic to reduce user login errors”
```

**Step 2. Use Outcomes as the Opening Line**

```markdown
✅ “This update reduces failed payments during checkout by retrying token fetch.”

Not:
❌ “Updated StripeConfigManager and added retry logic.”
```

**Step 3. Map Tech to Biz Impact**

```markdown
Change: Switched image loader from X to Y  
Reason: Improved load time by ~25%  
Impact: Faster onboarding for mobile-first users
```

**Step 4. Use “Explain Like I Own the Feature”**

```markdown
Imagine the person reading funds your feature.

Explain:
- What changed  
- Why they should care  
- What it enables next
```

***

####  Prompt to Use With AI


```markdown
“I’m trying to explain this dev update to a non-dev stakeholder.

Help me:
- Reframe it in outcome language
- Remove jargon
- Highlight impact in 1–2 lines”
```

***

##  Existing Outside the Terminal


> _“You are not just a developer. You are a system running on borrowed energy.”_

***

####  What This Section Is


This is a survival protocol for those who code at cognitive cliffs.\
It’s not about self-care hashtags.\
It’s about **operating system hygiene** —\
because when your inner stack crashes, no deploy will fix it.

You don’t need another Notion tracker.\
You need a feedback loop with yourself.

***

####  Why This Matters


Code doesn’t burn out. Coders do.

But burnout isn’t loud — it’s sneaky:

* You finish tickets, but feel nothing.
* You reread the same function 7 times.
* You ghost team calls because you're “catching up.”
* You scroll in bed knowing the fix… but dreading it.

This isn't weakness. It's system overload.\
And like any system, it can be rebalanced — with friction, not force.

***

#### ️ How to Apply It


**✅ Dev Hygiene Checkpoints (Weekly)**

These are system alerts.\
Run them every Friday, quietly.

```markdown
- [ ] Did I finish something I’m proud of — not just done with?
- [ ] Did I teach, mentor, or explain something to someone else?
- [ ] Did I ship without dread?
- [ ] Did I reclaim 1 hour from meetings or distractions?
- [ ] Did I say “no” at least once this week?
```

> Less than 3: Pause. Less than 2: Reset.

***

**⏳ 5-Minute Reflection: Your Dev Build Log**

Your Git log tells others what you did.\
Your **inner log** tells you what it meant.

```markdown
🧠 This Week Drained Me When...  
⚙️ This Week Clicked When...  
💬 A Conversation That Shifted Something Was...  
🎯 One Win I’ll Actually Remember:
```

This isn't for public retros.\
This is for personal signal tuning.

***

####  When to Use This


* Friday 5 PM → Close the loop
* Sunday 9 PM → Reboot your week
* Anytime you think, “Am I the only one feeling this way?”

***

####  Prompt to Use With AI


```markdown
“Help me reflect on this week as a developer.

Ask me:
- Where did I feel friction?
- What did I ship that gave me peace?
- What’s one human moment I appreciated this week?”
```

***

###  Dev Growth Compass: Navigating Beyond “Senior”


> _“Your career is not a ladder. It’s a recursive function.”_

***

####  What This Is


This isn’t about leveling up to Staff or Principal.\
It’s about building a **growth map that honors clarity, not just complexity.**

Too often, “growth” gets misdiagnosed as:

* Learning a new framework
* Joining a bigger company
* Managing people who write code you used to love

But real growth is:

* Knowing when not to optimize
* Teaching without being asked
* Writing code that ages well, not just ships fast

This section helps you design your compass, not just chase someone else's map.

***

####  Why It Matters


Developers often mistake velocity for direction.

Without a compass:

* Burnout becomes the cost of “impact”
* Prestige feels hollow
* You forget why you started

With a compass:

* You choose projects that stretch, not stress
* You advocate without ego
* You grow from coherence, not just complexity

***

#### ️ How to Apply It


**Step 1. Define Your “Compasses” – Not Goals**

```markdown
🧠 Thinking:  
Am I being challenged to think differently?

🛠️ Building:  
Am I solving meaningful problems with elegance?

💬 Sharing:  
Am I helping others think, write, or build better?

📚 Expanding:  
Am I learning anything beyond frameworks and syntax?
```

> Growth isn’t about saying yes to more.\
> It’s about saying no with better reasoning.

***

**Step 2. Audit Your Past Year with This Prompt**

```markdown
"What did I grow into this year — that no title change captured?"
```

You might find:

* A better communicator
* A more patient reviewer
* A builder of tools that made others faster

These are your **career force multipliers**.

***

**Step 3. Create a “Dev North Star” Card**

```markdown
🧭 What do I want to be known for as a developer?  
🧪 What am I experimenting with right now?  
🕸️ Where do I need more context or mentorship?
```

Put it in your notes, your README, or your mirror.

***

####  Prompt to Use With AI


```markdown
“Help me map my developer growth.

Ask me:
- What am I proud of building this year?
- What am I struggling to explain clearly?
- What kind of dev do I want to become — regardless of title?”
```

***

### ️ Developer Routines: Coding Rhythm, Not Rigid Habits


> _“You don’t need motivation. You need motion.”_

***

####  What This Is


This isn’t a morning routine post.\
This is about creating **repeatable rhythms** that:

* Protect your focus
* Reduce task thrashing
* Help you **recover** your attention when it breaks

You don’t need to wake up at 5 AM.\
But you do need a **default operating rhythm**\
— so context-switching doesn’t eat your day.

***

####  Why It Matters


Dev work is long-tail thinking with short-term interruptions.

Without a routine:

* Every Slack ping feels urgent
* You forget what “deep work” felt like
* The terminal becomes the only window you stare into

But with the right rhythm:

* Flow becomes predictable
* Meetings stop fragmenting your zone
* You preserve your best hours for your real work

***

#### ️ How to Apply It


**🍱 Try the “3-Modes” Workday**

Break your day into **mental energy zones**:

```markdown
💡 Mode 1: Deep Focus (2-3 hrs)  
Hard problems. No meetings.  
Use blockers. Build momentum.

📤 Mode 2: Output + Sync (1-2 hrs)  
PRs, team updates, check-ins.  
Batch communication here.

🔁 Mode 3: Cleanup + Drift (1 hr)  
Bug fixes, notes, small wins.  
Let your brain cool down.
```

The goal isn’t strict hours — it’s **bounded cognitive space.**

***

**🔄 Add Rituals, Not Just Tasks**

```markdown
🧼 Before work:  
- Tab group reset  
- Sticky note of 1 friction area from yesterday  

🚪 After work:  
- Write 1-line “what I built today” log  
- 30-sec “PR summary” voice note to future you
```

***

####  When to Reset Your Rhythm


* After sprint burnout
* After a long vacation
* After a chaotic release

Routines aren’t constraints. They’re cushions.

***

####  Prompt to Use With AI


````markdown
“My schedule keeps breaking my focus.

Can you:
- Suggest a 3-mode dev work routine
- Add rituals to open and close my day

---

#  5. Starter Kits: Build Smarter, Not Just Sooner  

> _“Your first draft isn’t throwaway. It’s a template in disguise.”_

---

###  What This Is


Starter Kits are **plug-and-think resources** for developers.  
Not generic templates — but **mental scaffolds** to build the right habits from day one.

If the earlier sections were systems,  
this is where the **gear lives.**

Every resource is minimal, editable, and philosophically sharp.

---

##  dev-readme-template.md  

> _“If you don’t write your story, others will make assumptions.”_

Your personal README isn’t branding fluff.  
It’s a **working contract** — with your teammates and your future self.

It shows:

- What kind of developer you are  
- What to expect from you  
- What values you code with

---

### ️ Starter Fields to Include


```markdown
#  About Me  

I’m a [role] who values [clarity, feedback loops, etc.].  
I write code that [describe philosophy briefly].

#  How I Work  

- I prefer async for decisions, sync for alignment  
- I ask questions early — clarity beats assumptions  
- I review PRs for thought process, not just diffs  

# ️ Tooling I Use  

- Editor: VS Code / Neovim / etc.  
- Terminal: Warp / iTerm2  
- Shell: ZSH / Fish  
- Theme: Minimal dark (yes, I’m that dev)  

#  Reach Me  

Slack: [handle]  
Email: [email]  
Time Zone: [XX]

#  What Im Learning Right Now  

- [Framework, practice, or pattern]  
- [Philosophy or concept]
````

***

####  Prompt to Use With AI


```markdown
“Help me write a personal developer README.

Include:
- My working style
- My preferred tools
- How I collaborate
- What I’m learning”
```

***

Next: [AI Copilot Primer →](dev-life-systems.md#ai-copilot-primer)

***

###  AI Copilot Primer


> _“You’re not outsourcing thinking. You’re externalizing it.”_

***

####  What This Is


This is not a prompt list.\
This is a **thinking primer** for developers who want to use AI as a **thought partner**, not a shortcut engine.

It’s designed to:

* Speed up clarity, not just tasks
* Sharpen your architecture, not just autocomplete
* Respect your judgment, not replace it

If you're using ChatGPT, GitHub Copilot, or any LLM —\
this is how to stay **in the driver’s seat.**

***

####  Why It Matters


Most AI interactions look like:

```plaintext
“Write me a Python function for X.”
```

But that misses the point.

The best devs use AI to:

* Stress test ideas
* Frame trade-offs
* Uncover edge cases
* Document better, explain deeper

This primer helps you **shift from command → collaboration**.

***

#### ️ How to Apply It


**🔄 The 3 Modes of Prompting**

```markdown
🧱 Scaffold
“Help me plan this feature with edge cases and structure.”

🔍 Critique
“Here’s what I wrote — what’s unclear, brittle, or over-abstracted?”

🧠 Refactor + Explain
“Refactor this and explain the design decision trade-offs.”
```

***

**💬 Ask AI to Ask You First**

```markdown
“Before giving me the code, ask me:
- What context do you need?
- What assumptions should we check?
- What input/output constraints matter here?”
```

This flips AI into **diagnostic mode**, not dictation mode.

***

####  Copilot Prompt Starters (Examples)


```markdown
“I’m working on a CLI tool. Suggest input validation patterns I should follow.”  
“What should I unit test in this recursive function?”  
“Convert this logic into a state machine — show me the transition diagram too.”  
“Help me write a docstring that explains this for junior devs.”  
“Explain this regex like I’m 12 but curious.”
```

***

####  Bonus: AI Doesnt Have Intuition. You Do.


Use AI to fill in possibilities — not make decisions for you.

***

###  Pair Dev Guide


> _“Pair programming isn’t about two keyboards. It’s about two perspectives.”_

***

####  What This Is


A short, repeatable guide for **pair programming** —\
so it doesn’t turn into one person typing while the other silently nods.

Great pairing is:

* Mentally tiring
* Emotionally vulnerable
* Incredibly productive

But only when both developers feel **safe, seen, and structurally engaged**.

***

####  Why It Matters


Without structure:

* One dev takes over
* The other zones out
* Tension builds in silence

With this guide:

* Roles are clear
* Time is respected
* Ideas flow without ego

***

#### ️ How to Apply It


**🤝 Role Clarity: Driver & Navigator**

```markdown
🚗 Driver:  
- Types, implements, builds the actual logic  
- Thinks tactically

🧭 Navigator:  
- Guides logic, watches for bugs or edge cases  
- Thinks strategically, suggests alternatives
```

🌀 Switch roles every 15–30 minutes (or after solving a function).\
Use a timer if needed — it **resets focus**.

***

**📣 The “PAIR” Protocol for Communication**

```markdown
P – Pause before offering suggestions  
A – Ask clarifying questions (“What’s our goal here?”)  
I – Invite alternatives, don’t impose them  
R – Reflect on what’s working after each session  
```

> Good pairing feels like a **brain merge**, not a code battle.

***

####  Prompt to Use With AI (While Pairing)


```markdown
“We’re pair programming a refactor.

Can you:
- Help us identify assumptions in our code?
- Suggest test cases we might miss?
- Offer a diagram of this logic?”
```

***

###  Clarity Checklist


> _“Before you merge, make sure you’ve translated.”_

***

####  What This Is


A last-mile checklist before you:

* Merge a PR
* Release a feature
* Leave for vacation
* Hand off to another dev

It’s not a QA checklist. It’s a **comprehension audit** — for clarity, not just correctness.

***

####  Why It Matters


Your code might run.\
But does the next developer understand:

* Why it’s written this way?
* What _not_ to touch?
* What edge cases you accounted for?

If not, you haven’t shipped clarity — you’ve shipped **technical debt with a time bomb**.

***

#### ✅ The Clarity Checklist


```markdown
- [ ] Can a junior dev explain what this code does — and why?
- [ ] Have I named things with intent, not just function?
- [ ] Did I leave any TODOs without a timeframe or note?
- [ ] Is there a 2-liner summary at the top of the file or PR?
- [ ] Did I write down the trade-offs I considered (even if I rejected them)?
- [ ] Can this be debugged without me in the room?
```

If you say “it’s obvious” — it’s not.

***

####  Add This to Your PR Template


```markdown
###  Why I Built It This Way  

[Explain trade-offs or reasoning]

###  What Could Be Improved  

[List known issues, possible future refactors]

###  How To Extend or Use  

[Usage notes, assumptions, or mental models]
```

***

####  Prompt to Use With AI


```markdown
“I’m about to ship this PR.

Can you:
- Review for clarity and naming?
- Point out any hidden assumptions?
- Suggest a 2-line summary I can include at the top?”
```

***

### ✅ Youre Ready to Ship Systems, Not Just Code


***

##  LICENSE & CONTRIBUTING.md


> _“Good systems grow when others can build on them.”_

***

###  License


This content is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to:

* ✅ Share — copy and redistribute the material in any medium or format
* ✅ Adapt — remix, transform, and build upon the material for any purpose, even commercially

Just give appropriate credit — link back to the original project and note if changes were made.

Full license text: [https://creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0)

***

###  Contributing


This is a living system.\
If you have:

* 💡 Smarter frameworks
* 📎 Better examples
* 🧠 Sharper mental models
* 🙌 Dev tools or prompts that helped you

Feel free to fork, suggest edits, or open a pull request.

But before you do, ask yourself:

> _“Is this addition helping a developer think clearer, not just move faster?”_

If yes — we’d love to build it with you.

***

### ✨ Acknowledgement Culture


We value:

* Thoughtful contributions
* Shared systems thinking
* Empathy for the next dev who reads this

You don’t need to be loud. You just need to be clear.

***

Next: [Return to README →](dev-life-systems.md#dev-life-systems)
