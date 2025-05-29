# 🎨 Style Guide for sans-serif-sentiments

**Version 1.0 • 2025-05-19**

_A living framework for calm, clear, human-first documentation._

## 📑 Table of Contents

1. [Purpose of This Guide](#purpose-of-this-guide)  
2. [Tone & Voice](#tone--voice)  
3. [Structure & Hierarchy](#structure--hierarchy)  
4. [Emphasis Rules](#emphasis-rules)  
5. [Language & Word Choice](#language--word-choice)  
6. [Layout Patterns](#layout-patterns)  
7. [Content Philosophy](#content-philosophy)  
8. [Markdown & Commit Style](#markdown--commit-style)  
9. [Accessibility & Inclusivity](#accessibility--inclusivity)  
10. [Localization & Translation](#localization--translation)  
11. [Linking & Cross-Referencing](#linking--cross-referencing)  
12. [Code & Command Snippets](#code--command-snippets)  
13. [Admonitions & Callouts](#admonitions--callouts)  
14. [Asset Management](#asset-management)  
15. [Tables, Lists & Layouts](#tables-lists--layouts)  
16. [Terminology & Glossary](#terminology--glossary)  
17. [Doc Versioning & Changelogs](#doc-versioning--changelogs)  
18. [Review & Feedback Process](#review--feedback-process)  
19. [Automation & Tooling](#automation--tooling)  
20. [SEO & Discoverability](#seo--discoverability)  
21. [Living Documentation](#living-documentation)  
22. [AI-Assisted Writing](#ai-assisted-writing)  
23. [Multi-Format Output](#multi-format-output)  
24. [Evolution Rules](#evolution-rules)

---

---

## 1. Purpose of This Guide

> A style guide is not just about formatting—it's about trust.  
> This document exists to create a **shared voice**, a **clear standard**, and a **reliable starting point** for anyone contributing to sans-serif-sentiments.

You can use this guide when:
- You're writing docs, READMEs, guides, or changelogs
- You're reviewing someone else’s writing
- You’re rewriting dry tech speak into something more human

This isn’t about rules. It’s about rhythm.

---

## 2. Tone & Voice  
_Calm, clear, sincere—never robotic._

Your writing should feel like a conversation with someone who’s:
- Confident but not arrogant
- Knowledgeable but not preachy
- Friendly but not trying too hard

### 🎯 What We Aim For

| Trait     | What It Means                          |
|-----------|-----------------------------------------|
| **Calm**  | No over-explaining. No panic. No exclamation marks unless they earn it. |
| **Clear** | Say what you mean. Cut half your words—if it still works, it’s better. |
| **Sincere** | Be helpful, not hypey. Avoid jargon, sarcasm, or corporate filler. |
| **Minimal** | Don’t write a sentence when a phrase will do. Let whitespace speak. |
| **Human** | We talk like real people. Write like someone who wants to be understood. |

---

### ❌ Cold, Robotic
```markdown
To proceed with installation, users are advised to verify system prerequisites prior to continuing.
```

### ✅ Calm + Human
```markdown
Before you install, check if your system meets the requirements.  
It takes 30 seconds and saves frustration later.
```

---

### ❌ Corporate & Vague
```markdown
Our platform leverages AI capabilities to enhance synergies across verticals.
```

### ✅ Sincere + Clear
```markdown
We use AI to help teams work faster and with fewer manual tasks.
```

---

### ❌ Friendly but Overdone
```markdown
Hey there, champ! 😎 Ready to install some software?! Let’s crush it! 💥
```

### ✅ Friendly and Respectful
```markdown
Let’s get you set up. This guide takes about 3 minutes to follow.
```

---

> Write like you're helping someone intelligent—but tired.  
> That’s the reader who matters most.

---

## 3. Structure & Hierarchy  
_When and how to use headings and whitespace._

Your doc should feel like a conversation with chapters—not a cluttered note.

---

### 📐 Use heading levels to guide the eye:

| Markdown | Purpose |
|----------|---------|
| `#` H1   | Title of the page (only once per doc) |
| `##` H2  | Major sections |
| `###` H3 | Subsections under an H2 |
| `####` H4 | Rarely needed—only for edge-case nesting |

✅ Use **1 blank line** before and after headings.  
✅ Start each section with a quick sentence or blockquote for orientation.

---

### ❌ Cluttered Heading Use
```markdown
# How it Works
## Setup
### Token
#### Details
### Login
### Interface
```

### ✅ Clear Hierarchy
```markdown
# How It Works

## 1. Setup

### Generate a Token  
Explain what it does and why it’s needed.

### Log In  
Describe what users should expect.

## 2. Using the Interface  
Quick intro before listing features.
```

---

### 📌 🔢 Numbering Style Guidelines
- ✅ Use numbers in the TOC for scanning and structure  
- ❌ Do not include numbering in actual document headings (`##`).

> This keeps URLs clean, anchors intuitive, and editing easier.

> **When numbering can help:**  
> - In a tutorial or linear flow where readers need to track “Step 1, Step 2…”  
> - When you’ll reference sections by number in discussion or reviews.  
>  
> **Pros of numbering headings:**  
> - Clarifies sequence and progress  
> - Makes it easy to say “see section 3”  
>  
> **Cons of numbering headings:**  
> - Pollutes anchor links and permalinks  
> - Requires renumbering whenever you insert or reorder sections  
> - Can distract in long or non-linear docs  
>  
> **Hybrid model:**  
> Use numbers in the TOC only for order, but keep your `##` headings unnumbered for clean URLs and easier maintenance.

---

### 📌 📝 Leading Sentences Guidelines
- ✅ Always start a new section or procedural list with a brief intro sentence that explains **why** the reader is here.  
- ❌ Avoid jumping straight into steps without context.

- ### 📌 📝 (More Examples)

| ❌ Don’t Do This                                                                                  | ✅ Do This Instead                                                                                                       |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1. Clone the repo<br>2. Install dependencies<br>3. Start the server                               | Before you start the server, make sure your environment is ready:<br>1. Clone the repo<br>2. Install dependencies<br>3. Start the server |
| 1. Add user to group<br>2. Grant permissions<br>3. Notify user                                    | To onboard a new user, follow these steps:<br>1. Add the user to the group<br>2. Grant permissions<br>3. Notify the user |
| 1. Download the ZIP<br>2. Extract files<br>3. Run installer                                       | Before installing, download and extract the package:<br>1. Download the ZIP<br>2. Extract files<br>3. Run the installer  |
| 1. Write tests<br>2. Execute tests<br>3. Review results                                           | To verify your changes, write and run tests:<br>1. Write tests<br>2. Execute tests<br>3. Review results                   |

> A quick orienting or opening line sets expectations and reduces confusion.

---

### 📌 🔗 Heading Consistency & Parallelism
- ✅ Write related headings in the same grammatical form (e.g., all imperatives: “Install,” “Configure,” “Verify”).  
- ❌ Don’t mix styles like “Installing the Tool” with “Setup Instructions.”  

- ### 📌 🔗 (More Examples)

| ❌ Mixed Styles                                                   | ✅ Parallel Imperatives                             |
|-------------------------------------------------------------------|-----------------------------------------------------|
| ## Installing the Tool<br>## How to Configure Your Account<br>## Verifying Setup | ## Install the Tool<br>## Configure Your Account<br>## Verify the Setup |
| ## Setup Instructions<br>## Troubleshooting Errors<br>## Configuration Options     | ## Set Up the Tool<br>## Troubleshoot Errors<br>## Configure Options     |
| ## Editing Profiles<br>## Profile Settings Overview<br>## How to Save Changes      | ## Edit Your Profile<br>## View Profile Settings<br>## Save Your Changes  |
| ## User Management<br>## Roles and Permissions<br>## Managing Access               | ## Manage Users<br>## Assign Roles & Permissions<br>## Manage Access       |

> Parallel structure helps readers scan and know exactly what to expect.

---

### 🔁 Good vs Bad Examples Summary Table

| ❌ Don’t Do This                                    | ✅ Do This Instead                                                     |
|-----------------------------------------------------|------------------------------------------------------------------------|
| Use numbered section headings like `## 3. Structure` | Use `## Structure` and reserve numbers only for the TOC                |
| Skip a framing sentence before a list of steps      | Add a sentence: “Before you configure, make sure you’ve installed X.” |
| Mix verb forms in headings                          | Keep all headings imperative: “Download,” “Install,” “Verify”         |
| Nest headings deeply without cause                  | Use up to 3 levels unless absolutely required                          |
| Skip spacing between sections                       | Add whitespace before/after headings and between paragraphs            |
| Include all concepts in one bloated section         | Split into logical sub-headings to improve scanning                    |

---

## 📏 Whitespace = Breathing Room

Use whitespace like punctuation. It slows the scroll and helps the eye.

---

### ❌ Wall of Text
```markdown
To install the CLI tool, go to the website and download the installer. After that, run the installer and follow the setup wizard. Finally, verify the installation by typing `tool --version` in the terminal.
```

### ✅ Structured & Skimmable
```markdown
### Install the CLI Tool

1. Go to the [Downloads page](#)
2. Run the installer
3. Follow the setup wizard

✅ To confirm it worked:
```bash
tool --version
```
```

---

> ✅ Structure isn’t just for looks. It tells the reader:  
> “You’re in good hands. Keep going.”

---

### 🧼 Use whitespace like punctuation

- One thought = one paragraph  
- Use bullets or tables instead of dense text  
- Group related content with clear spacing

> If it looks dense, it reads dense.

---

## 4. Emphasis Rules  
_Use emphasis to guide—not distract._

Use `**bold**` and `*italic*` intentionally. Don’t shout. Don’t decorate.

| Use case | Style |
|----------|-------|
| Highlight a key term | `**bold**` |
| Add nuance or light stress | `*italic*` |
| Reference file/code | `` `inline code` `` |
| Technical snippets/output | Triple backticks (```bash) |

---

### ❌ Overdone & Distracting
```markdown
**IMPORTANT**: You MUST click the **FINAL** button at the **END** of the page.
```

### ✅ Balanced and Focused
```markdown
Click the **Final** button at the end of the page.  
This step completes the setup.
```

---

### ❌ Emphasizing full sentences
```markdown
**You should always check the version before upgrading.**
```

### ✅ Use emphasis *within* the sentence
```markdown
You should always check the **version** before upgrading.
```

> ✅ Let emphasis **support meaning**—not add noise.

---

## 5. Language & Word Choice  
_Preferred words, banned jargon._

### ✅ Use simple, common words:
| Bad | Better |
|-----|--------|
| Utilize | Use |
| Leverage (as a verb) | Apply, use |
| Facilitate | Help |
| Navigate to | Go to |
| Interface (as noun) | Screen, page, dashboard |
| In order to | To |

### ❌ Avoid these patterns:
- "It is recommended that…" → say “We recommend…”  
- “At your earliest convenience…” → say “When you’re ready”  
- “Endeavor to…” → just… don’t.

---

### ❌ Vague, bloated
```markdown
Our solution facilitates synergistic workflows across multiple platforms.
```

### ✅ Specific, human
```markdown
Our tool helps teams work together across different apps—without switching tabs.
```
---

### ❌ Legalese-style
```markdown
Users are advised to initiate credential verification upon initial login.
```

### ✅ Human-first
```markdown
When you log in for the first time, we’ll ask you to verify your account.
```

> Write like you're helping a smart friend, not submitting to a legal department.

---

## 6. Layout Patterns  
_Common structures for different doc types._

Use these reusable layouts to speed up writing and bring consistency across docs.

### 📦 Setup Guide

```markdown
## Getting Started

> What this guide helps you do in under 5 minutes.

### Step 1: Install XYZ  
Brief one-line description.

### Step 2: Configure XYZ  
Break it into 2–3 bullets if needed.

### Step 3: Verify  
Show how success looks.
```

---

### 📘 How-To Guide

```markdown
## How to Do One Specific Thing

> What this does and why it’s useful.

1. Step 1  
2. Step 2  
3. Step 3

✅ Result: What the user should see or achieve.
```

---

### 🧠 Concept/Overview Doc

```markdown
## What is [Concept]?

> Short, calm, non-salesy definition

- Why it matters  
- Where it fits in  
- When to use it
```

> ✨ These aren’t strict templates. Think of them as scaffolding—there to support you, not box you in.

---

## 7. Content Philosophy  
_Empathy-led, human-first writing._

We don’t write to look smart.  
We write so the reader doesn’t have to feel stupid.

This guide exists to protect that principle.

---

### 💭 Why This Philosophy Matters

Documentation is the *first real conversation* between your product and your user.  
If that conversation is cold, robotic, or overloaded—they walk away.

---

### 🎯 What We Believe

| Principle | What It Means |
|----------|----------------|
| **Writing is a product** | Docs are part of the experience—not an afterthought |
| **Clarity is kindness** | Confusion costs time. Clarity creates momentum |
| **Brevity isn’t the goal—clarity is** | Sometimes more words are needed to say it simply |
| **Anticipation builds trust** | Predict what might confuse the reader—and address it before they ask |
| **Tone is UX** | A friendly line at the right time does more than a button ever can |

---

### ❌ A Typical, Surface-Level Doc
```markdown
The installation process requires you to download the binary, extract it, and modify your PATH variable accordingly.
```

### ✅ A Human-First Rewrite
```markdown
To install the tool:

1. Download the `.zip` file
2. Extract it to any folder
3. Add that folder to your system PATH (here’s how →)

Not sure what "PATH" means? No worries—[we’ll explain it here](#what-is-path).
```

> 🤝 Help before it’s asked for. Confidence before confusion.

---

### ❌ Corporate Legalese
```markdown
This integration utilizes proprietary methods to ensure optimal connectivity across environments.
```

### ✅ Sans-Serif Sentiments Style
```markdown
We built this integration to be reliable, fast, and easy to connect—no matter your environment.
```

> Say it like you’d say it in real life. Not like you’re talking to a boardroom.

---

## ✅ TL;DR

- People don’t read docs because they *want* to. They read them because they’re stuck.
- We don’t waste their time trying to sound impressive—we respect it by being helpful.
- Empathy isn’t a “nice-to-have”—it’s our UX strategy in writing.

> Clarity is the kindest thing we can offer someone mid-problem.

---

## 8. Markdown & Commit Style  
_The backbone of formatting clarity._

Markdown is the shared language of your documentation.  
Used well, it brings structure and calm. Used carelessly, it creates chaos.

---

### ✅ Markdown Guidelines

| Task | Rule |
|------|------|
| Code blocks | Use triple backticks: \`\`\`bash |
| Inline code | Use backticks: \`filename.txt\` |
| Headings | One `#` per level, no skipping |
| Lists | Use `-` or numbered lists (avoid asterisks) |
| Links | Use `[text](url)` syntax—no raw URLs |

✅ Always use **one blank line** between headings, paragraphs, and list items.  
✅ Use indentation sparingly; avoid nested chaos.

---

### ❗ Common Markdown Mistakes to Avoid

| Mistake | Better Approach |
|--------|-----------------|
| Mixing `*` and `-` in lists | Stick with `-` for all unordered items |
| Raw URLs | ❌ `https://example.com` → ✅ `[Example](https://example.com)` |
| No blank lines around blocks | Markdown breaks—add spacing |
| Code without context | Always add a sentence before code to explain what it does |

---

### 🧠 When to Use Inline vs Block Code

| Use Case | Use This |
|----------|----------|
| Referencing a file, flag, or CLI option | `` `inline code` `` |
| Showing steps, commands, or config | \`\`\`block code\`\`\` with language label |

✅ Be kind to the reader:  
Use inline when referencing, block when teaching.

---

### ✅ Commit Message Style

We use **conventional commit prefixes** for clarity and changelog generation:

```bash
feat: add onboarding checklist template
fix: resolve broken anchor link in API doc
docs: rewrite intro paragraph for tone
refactor: reorganize folder structure
chore: update dependencies
```

✅ Use **present tense** (`add`, not `added`)  
✅ Keep subject lines under 72 characters  
✅ Use lowercase prefixes (no `Feat:` or `Fix:`)

---

### 💬 Why It Matters

Your commit history is not just a log—it’s a **narrative**.  
Clear messages help:
- Auto-generate changelogs
- Scan history during debugging
- Guide code reviewers faster

> A good commit is a small act of documentation.

---

## 9. Accessibility & Inclusivity  
_Alt-text, plain language, and respect for real-world readers._

Accessibility isn't just about screen readers.  
It’s about making your docs usable by people who are tired, rushed, anxious, distracted—or differently abled.

That includes:
- Screen reader users
- Non-native English speakers
- Colorblind users
- Newcomers who don’t know your product (yet)

---

### 🧭 Core Principles

| Principle | What It Means |
|-----------|----------------|
| **Clarity is accessibility** | Dense, jargon-heavy text excludes readers |
| **Alt-text is not optional** | Every image should explain its meaning or context |
| **Structure aids navigation** | Headings, spacing, and order help users skim |
| **Link labels should describe action** | Never say "click here" |
| **Tone should respect all backgrounds** | No idioms, jokes, or references that might alienate |

---

### ❌ Inaccessible Example
```markdown
Hey! Click here to learn more! 🎉

![Graph](graph.png)
```

### ✅ Inclusive Rewrite
```markdown
Want a deeper explanation? [Read the API example guide](../examples/remapped-api.md)

![Line graph showing API response time decreasing after optimization](../assets/images/api-speed.png)
```

✅ The alt text explains what the graph *means*, not just what it *is*.

---

### 🛠 Tools That Help

- [Hemingway Editor](https://hemingwayapp.com/) – Simplify complex sentences
- [WAVE Accessibility Tool](https://wave.webaim.org/) – Audit contrast, alt text, etc.
- [Inclusive Language Checker](https://alexjs.com/) – Detect biased or outdated terms

---

### 📌 TL;DR

- Add alt text that makes sense out of context
- Write like your reader has one eye on the clock and one hand on their toddler
- Don’t assume knowledge—or perfect English
- Never use “click here” as link text
- Keep sentence structure light, clean, and logically ordered

> Accessibility isn’t extra effort. It’s built-in empathy.

---

## 10. Localization & Translation  
_Placeholder syntax, tone shifts, and global awareness._

Good docs speak many languages—even when they’re only written in one.

Localization doesn’t start with translation.  
It starts with writing that’s clear, culture-neutral, and easy to adapt.

---

### 🌍 Key Practices for Localization-Friendly Writing

| Practice | Why It Matters |
|----------|----------------|
| **Keep sentences short** | Easier to translate, less room for misinterpretation |
| **Avoid idioms, slang, or cultural references** | Not all metaphors cross borders |
| **Use consistent terminology** | Reduces translation ambiguity |
| **Don’t hardcode values or labels** | Keep UI strings and placeholders separate |
| **Use neutral date/time formats** | Prefer ISO: `YYYY-MM-DD`, `14:00 UTC` |

---

### ❌ Bad for Translation
```markdown
You’ve nailed it—time to kick things off! 🎉  
Click “Go” and let’s roll!
```

### ✅ Localization-Friendly Version
```markdown
You're ready to begin.  
Click **Go** to start the process.
```

> 🎯 Be specific, not clever. Translators will thank you.

---

### 🧩 Placeholder Format

When writing text that will include dynamic values (e.g., usernames, file paths), use clear and localizable syntax:

✅ Use:
```markdown
Welcome, `{username}`.  
Your report is saved to `{filepath}`.
```

Avoid:
```markdown
Welcome, $username! Your file is in $path
```

---

### 🛠 Helpful Tools

- [Phrase](https://phrase.com) – Translation management platform
- [Crowdin](https://crowdin.com) – Collaborative localization for docs
- [LocalizationLint](https://github.com/DavidAnson/markdownlint) – Lint for localization issues in Markdown

---

### 📌 TL;DR

- Write for translation by writing clearly  
- Avoid wordplay and ambiguity  
- Use placeholders, not hardcoded strings  
- Respect language direction, spacing, and tone

> If your doc can’t travel, it can’t scale.

---

## 11. Linking & Cross-Referencing  
_Teaching users how to navigate like pros._

A good link is like a guidepost. It’s clear, descriptive, and helps the reader move forward confidently—without friction or confusion.

---

### 🔗 Link Types & Formats

| Type | Format | Example |
|------|--------|---------|
| Same page (anchor) | `[text](#section-name)` | `[Go to Setup](#setup-guide)` |
| Another file | `[text](../folder/filename.md)` | `[Style Guide](../STYLE-GUIDE/STYLE-GUIDE.md)` |
| External | `[text](https://url.com)` | `[Visit GitHub](https://github.com)` |

✅ Anchor links are based on the heading text, all lowercase, spaces → `-`, and special characters removed.

---

### ❌ Poor Linking Practices

```markdown
Click [here](https://example.com) to continue.

See [this](../other.md).

Follow this link to [go back](#).
```

### ✅ Clean, Descriptive Links

```markdown
To view our API setup process, [read the Setup Guide](../docs/api-setup.md).

Need the full changelog? [Check the release notes →](../RELEASES.md)

Want to jump ahead? [Skip to Troubleshooting](#troubleshooting)
```

---

### 📌 Internal Anchors: How They Work

GitHub automatically creates an anchor link for every heading.

```markdown
## How to Install → becomes → #how-to-install
## FAQ & Troubleshooting → #faq--troubleshooting
```

Rules:
- Use all lowercase
- Replace spaces with hyphens `-`
- Keep punctuation out unless it’s `&` or `-` (GitHub supports double hyphens for `&`)

✅ Examples:
```markdown
[Jump to Troubleshooting](#faq--troubleshooting)

[See the Doc Types section](#5-doc-types--examples)
```

---

### 🧠 Best Practices

- ✅ Link nouns, not verbs:  
  ❌ `Click here to learn more` → ✅ `Learn more about [markdown formatting]`
- ✅ Test all links in the final rendered view (not just raw Markdown)
- ✅ Keep anchor links updated if headings change

---

> Good links feel invisible. They don’t interrupt.  
> They just move the reader forward at the exact right moment.

---

## 12. Code & Command Snippets  
_Highlight with clarity, not clutter._

Code blocks aren’t just for developers—they’re clarity boosters.  
Done right, they make your docs feel helpful, visual, and skimmable.

---

### 📦 Code Block Guidelines

| Rule | ✅ Do This |
|------|-----------|
| Use triple backticks | \`\`\`bash (or json, html, etc.) |
| Label the language | Enables syntax highlighting |
| No dollar sign in terminal commands | Makes it easy to copy |
| Use inline code for filenames/flags | `` `README.md` ``, `` `--debug` `` |
| Show example output when relevant | Help readers verify results |

---

### ❌ Poorly Formatted Example
```markdown
To install, run the command below:

$ npm install my-package
Then run it.
npm start
```

### ✅ Structured, Clear Version
```markdown
## Install the Package

```bash
npm install my-package
```

## Run the App

```bash
npm start
```
```

> 🧠 Avoid putting `$` before commands—it breaks copy-paste.

---

### ❌ Unlabeled, Unreadable JSON
```markdown
```
{
"success": true,
"msg": "OK"
}
```
```

### ✅ Properly Labeled JSON Block
```json
{
  "success": true,
  "msg": "OK"
}
```

---

### ✅ Inline Code Best Practices

Use inline code (with single backticks) for:
- Filenames: `` `config.yaml` ``
- Flags: `` `--force` ``
- Paths: `` `/usr/local/bin` ``

> Avoid bold or quotes for technical terms. Use `inline code` instead.

---

### 📌 TL;DR

| ❌ Don't | ✅ Do |
|---------|------|
| Mix code and paragraph text | Separate it out visually |
| Skip labeling | Use `bash`, `json`, `sh`, `js`, etc. |
| Use `$` in front of CLI code | Leave it out for easy copying |
| Forget output examples | Help readers verify success |

> If the user has to squint at the code block, you’ve already lost them.

---

## 13. Admonitions & Callouts  
_⚠️ warnings, 💡 tips, ✅ examples._

Documentation isn’t just about **telling**—it’s about **guiding**.  
That means you need more than paragraphs. You need signals.

Admonitions (also called "callouts") help readers:
- Slow down before breaking something
- Pay attention to what’s commonly missed
- Feel reassured when they’re doing it right

---

### 🎯 Types of Admonitions We Use

| Type | Emoji | Use It When… |
|------|-------|--------------|
| **Note** | 📝 or ℹ️ | You’re adding context or useful background |
| **Tip** | 💡 | You want to help users do it faster/smarter |
| **Warning** | ⚠️ | A mistake here could break, delete, or confuse |
| **Example** | ✅ | You’re reinforcing a concept with a use-case |

---

### 💡 How to Format

#### ✅ Basic Markdown
Use blockquotes with emojis + bold labels:

```markdown
> ⚠️ **Warning:** Don’t run this command as root unless you know what you’re doing.
> 💡 **Tip:** Use `--dry-run` to preview the changes before applying them.
> ✅ **Example:** This config disables caching in local dev environments.
```

#### ✅ GitHub-Flavored Markdown (advanced)
If using a static site generator (like Docusaurus or MkDocs), you can use custom containers:

```md
:::tip
You can skip the setup step if you're using version 2.0 or later.
:::

:::warning
Never expose your API key in public repos.
:::
```

---

### ❌ Flat and Forgettable
```markdown
Be careful not to delete your database.
You can use dry-run to test it first.
```

### ✅ Structured & Supportive
```markdown
> ⚠️ **Warning:** Running this will erase all data in the `prod` environment.

> 💡 **Tip:** Add `--dry-run` to preview which records would be deleted before confirming.
```

---

### 🧠 When to Use Them

- ✅ If the reader might mess it up, use a **warning**
- ✅ If there’s a faster path, use a **tip**
- ✅ If it reinforces learning, add an **example**
- ✅ If it’s helpful but non-critical, use a **note**

> Don’t overuse them.  
> A doc full of callouts is just yelling at the user in emoji.

---

### 📌 TL;DR

- Use callouts like a mentor: kind, honest, and clear.
- Don’t write “gotchas” after the fact—guide before the fall.
- Use structure to show empathy: **highlight what matters before it’s too late**.

---

## 14. Asset Management  
_Folder conventions, image specs, and the hidden art of staying organized._

Docs are not just words.  
They’re visuals, downloads, embedded demos, diagrams, and often... a folder full of chaos.

Let’s not do that.

---

### 📁 Folder Structure

All static assets—images, icons, charts, downloadable files—go here:

```
/assets/
   └── images/
   └── diagrams/
   └── downloads/
```

Use lowercase folder and file names, with hyphens instead of spaces:
✅ `api-flowchart.png`  
✅ `user-guide-cover.png`  
❌ `Final Version (3).PNG`

> 📌 Tip: Keep assets **outside** your `/docs/` folder to avoid URL conflicts and clutter.

---

### 🌄 Image Guidelines

| Rule | What To Do |
|------|-------------|
| Format | Use `.png` for diagrams/UI, `.jpg` for photos, `.svg` for icons |
| Alt Text | Every image **must** include meaningful alt text |
| Dimensions | Keep under 1200px wide unless full-screen is needed |
| Compression | Use [TinyPNG](https://tinypng.com) or [Squoosh](https://squoosh.app) to reduce size |
| Naming | Use lowercase, hyphenated, descriptive filenames |

---

### ❌ Bad Practice
```markdown
![img1](../docs/random_assets/finalfinal2.PNG)
```

### ✅ Better
```markdown
![User selecting a date range in the dashboard](../../assets/images/date-filter-ui.png)
```

✅ Alt text describes what’s shown and why it matters.  
✅ Path follows clean folder structure.

---

### 📦 Embeddable Files

If you’re including downloads (PDFs, templates, etc.), place them under `/assets/downloads/`.

Name them clearly:
- `user-onboarding-checklist.pdf`
- `quickstart-template.docx`

Avoid:
- `final-checklist2 (copy).pdf`
- `doc1.docx`

---

### 🧠 Why This Matters

- Images without structure = broken links later  
- Large files = slow docs  
- Confusing names = contributor rage  

> Your readers may never see the asset folder—but your teammates will. Leave a trail of sanity.

---

### 📌 TL;DR

- Use `/assets/` with clear subfolders (`images`, `downloads`, `diagrams`)
- Optimize every image—don’t dump raw screenshots
- Describe visuals with intent—**alt text is content**
- File names should be readable, reusable, and lowercase

---

## 15. Tables, Lists & Layouts  
_When to use which—and why your formatting matters._

Users don’t read docs like a novel.  
They skim, scan, skip, and scroll.  
Your structure should *support that behavior—not fight it*.

---

### 📋 When to Use a List

Use **bulleted lists** when:
- There’s no specific order
- You’re naming tools, options, concepts, requirements

```markdown
- Install Node.js
- Clone the repo
- Open the project in VS Code
```

Use **numbered lists** when:
- Steps must be followed in a specific sequence

```markdown
1. Download the installer  
2. Run the setup wizard  
3. Verify your installation
```

✅ Keep list items short and parallel in tone.  
✅ Add a one-line intro if needed:  
> To install the tool, follow these steps:

---

### ❌ Common Mistakes in Bullet Lists

#### 🚫 Mixed formats
```markdown
- Clone the repo
- Then install dependencies
Run the dev server after that
- Open the browser
```

✅ Fix:
```markdown
- Clone the repo  
- Install dependencies  
- Run the dev server  
- Open the browser
```

---

#### 🚫 Rambly, paragraph-length bullets
```markdown
- First, you’re going to want to make sure your environment is set up correctly, which means checking Node version, Python path, and also ensuring that you have Git installed and configured properly.
```

✅ Fix:
```markdown
- Check your environment:
  - Node.js installed  
  - Python path set  
  - Git configured
```

---

#### 🚫 Inconsistent grammar or tone
```markdown
- Creates the token  
- Deleting the cache  
- Used for session management
```

✅ Fix (same tense):
```markdown
- Create the token  
- Delete the cache  
- Manage session data
```

> 📌 Tip: Read your list out loud.  
> If it sounds like a ramble or grammar rollercoaster, it probably is.

---

### 📐 When to Use a Table

Use a **table** when:
- You’re comparing values side-by-side
- Listing options, flags, configs, or multiple attributes

```markdown
| Flag        | Description                        | Default |
|-------------|------------------------------------|---------|
| `--verbose` | Enables debug output               | `false` |
| `--config`  | Path to custom config file         | `null`  |
| `--watch`   | Rebuild on file change             | `true`  |
```

✅ Keep tables narrow, clean, and skimmable  
✅ Use columns only when each one adds meaning  
❌ Avoid tables just to “make things look neat”

---

### ❌ Overdone Table

```markdown
| Step | Instruction                                                                 |
|------|-----------------------------------------------------------------------------|
| 1    | To begin the setup, go to the website, locate the installer, download it… |
```

✅ Use a list instead:
```markdown
### To set up:

1. Go to the [download page](#)  
2. Download the installer  
3. Run the installer and follow prompts
```

---

### 🧱 Visual Layout Patterns (Micro-Layouts)

Think in **building blocks**:

```markdown
## Heading  
> Intro sentence (optional)  
- List or short paragraph  
- Optional tip or callout  
```

Don’t:
- Nest 3+ levels deep
- Stack multiple tables back-to-back
- Mix long paragraphs into tables

---

### 📌 TL;DR

- Lists are for flow. Tables are for side-by-side comparison.
- Don’t turn your prose into spreadsheets.
- Use consistent tense and style across list items.
- Respect your reader’s eyes—format like it matters.

> If your doc looks like a receipt or a ransom note, reformat it.

---

## 16. Terminology & Glossary  
_Define and link key terms so your readers—and your writers—stay aligned._

Language isn't just what we write—it's the system that supports your product, your UX, and your docs.

This glossary is your **source of truth** for:

- What words mean  
- How they’re spelled and capitalized  
- When (and when not) to use them

---

### 📘 Why It Matters

| Without a glossary | With a glossary |
|--------------------|-----------------|
| “Cache,” “buffer,” and “store” used interchangeably | Writers use the right term, every time |
| Users confused if “project,” “workspace,” and “account” are the same | Terms are defined, linked, and consistent |
| Writers invent new phrases for the same concept | Everyone speaks the same doc language |

---

### 🔤 Example Glossary Table

| Term | Definition | Use it when… | Don’t confuse with |
|------|------------|--------------|--------------------|
| **Token** | A temporary access credential, usually time-limited | Explaining API authentication | Key, credential |
| **Key** | A long-term identifier, typically stored securely | Describing config or setup | Token |
| **Workspace** | A shared environment for users and projects | Referring to org-wide settings | Account, project |
| **Project** | A single unit of work inside a workspace | Naming or scoping builds | Repo, workspace |
| **Slug** | A URL-friendly version of a name (`my-post-title`) | Generating permalinks or doc URLs | ID, alias |

---

### 🧠 Tips for Maintaining the Glossary

- ✅ Add a new term when:
  - You’ve used it 3+ times across docs  
  - You’ve had to explain it in comments or PRs  
  - It could be misinterpreted in another language

- ✅ Link to the glossary:  
  ```markdown
  See our [Glossary →](#16-terminology--glossary) for key definitions.
  ```

- ✅ Define once. Then use consistently.

- 🚫 Don’t:
  - Redefine terms in every doc  
  - Assume technical users already know

---

### 📌 Formatting Rules

| Rule | What to Follow |
|------|----------------|
| Headings | Use `## Glossary` in standalone pages |
| Order | Alphabetical |
| Spelling | Use American English (or define your variant) |
| Capitalization | Only capitalize proper nouns (e.g. GitHub, Node.js) |
| Plurals | Use singular form as the glossary entry (e.g. `token`, not `tokens`) |

---

### 🧨 Common Anti-Patterns

| Problem | Fix |
|--------|-----|
| Multiple terms for the same thing | Choose one canonical term—mark others as synonyms |
| Inconsistent capitalization (`Api` vs `API`) | Define casing rules once, follow everywhere |
| Jargon overload | Add plain English versions or usage examples |

---

### 📌 TL;DR

- Your glossary is a contract between writer and reader
- Define once, use everywhere
- Link generously—don’t force the reader to guess
- Kill synonym drift before it kills your clarity

> Docs don’t get bloated because of too much info.  
> They get bloated because of repeated definitions.

## 17. Doc Versioning & Changelogs  
_Semantic versions, last updated tags, and reader trust._

Your readers won’t always remember what they read last time—but your docs should.

Versioning and changelogs help users know:
- If the doc they’re reading is up to date  
- What’s changed since the last time they followed the steps  
- Whether the current instructions match their software version

---

### 🧮 Versioning Rules (Docs ≠ Product)

Use [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`) for **published docs**, especially when they map to product releases.

| Update Type | Version Bump | Example |
|-------------|--------------|---------|
| Major rewrite or format change | `2.0.0` → `3.0.0` | Switched from Markdown to Docusaurus |
| Added new section or feature doc | `2.0.0` → `2.1.0` | Added OAuth integration docs |
| Typo fix, grammar, formatting | `2.1.0` → `2.1.1` | Minor edits or phrasing updates |

For standalone guides, you can also version **per file** in the frontmatter:

```markdown
_Last updated: May 21, 2025 • Version: 1.2.3_
```

✅ Pro tip: Don’t confuse product version with doc version—track both if needed.

---

### 🗂️ Creating a Great CHANGELOG.md

Keep a root-level changelog that summarizes updates in **plain English** and separates additions, fixes, and changes:

✅ Good changelog format:
```markdown
## [2.1.0] – 2025-05-21
### Added
- Slack bot quickstart template
- Callout formatting section under “Tone & Voice”

### Fixed
- Broken anchor link in API setup
- Grammar issues in intro paragraphs

## [2.0.0] – 2025-04-01
### Changed
- Reorganized entire Style Guide for clarity
- Moved examples into `/examples/` folder
```

---

### ❌ Don’t Do This

#### 1. ❌ Vague Commit Messages
```bash
git commit -m "update docs"
```

✅ Instead:
```bash
git commit -m "docs: clarify setup steps in quickstart guide"
```

---

#### 2. ❌ Messy Changelog
```markdown
- Fixed some stuff  
- Added docs  
- Changed things around
```

✅ Instead:
```markdown
### Fixed
- Removed duplicate command in CLI section

### Added
- New “Writing Principles” subsection with examples
```

---

#### 3. ❌ No “Last Updated” Info
```markdown
## Setup Guide

Step 1: Install the CLI...
```

✅ Instead:
```markdown
## Setup Guide  
_Last updated: May 21, 2025_
```

---

### ✅ Where to Show Versioning

| Place | What to Show |
|-------|---------------|
| Top of a guide | `_Last updated: May 21, 2025_` |
| Footer or sidebar | Doc version (linked to changelog) |
| In repo | `/CHANGELOG.md` + version tags in Git history |

> Don’t just keep docs updated—show that they’re updated.

---

### 📌 TL;DR

- Use semantic versioning when your docs follow product changes  
- Maintain a clean, readable `/CHANGELOG.md`  
- Always show “last updated” info in public-facing docs  
- Track both technical and editorial updates  
- Version commits clearly so humans—not just tools—can follow

> Code tells the computer what changed.  
> Changelogs tell the humans.

## 18. Review & Feedback Process  
_How to propose, review, and merge changes without losing your mind—or your voice._

Great docs don’t just happen.  
They’re reviewed, challenged, edited, and improved—collaboratively.

This section defines how we do that:
- How to submit doc changes
- How we review with care, not ego
- How we merge with clarity and control

---

### ✍️ Submitting a Doc Change (Pull Request Etiquette)

✅ Before opening a pull request:
- Read the [Style Guide](../STYLE-GUIDE/STYLE-GUIDE.md)
- Check for existing terms in the [Glossary](#16-terminology--glossary)
- Use meaningful commit messages
- Add a brief PR description explaining:
  - What changed  
  - Why it changed  
  - If any related sections were affected

#### ❌ Vague PR Description
> “Fixed some typos and stuff.”

#### ✅ Better
> “Clarified token vs. key usage in authentication section. Added alt text to 2 missing diagrams.”

---

### 👀 How We Review

✅ We use this 4-check system:

| Review Check | Ask Yourself… |
|--------------|----------------|
| ✅ Content | Does this doc *work* for the reader? |
| ✅ Clarity | Is it clear, readable, and free of jargon? |
| ✅ Style | Does it match our tone, structure, and voice? |
| ✅ Structure | Are headings, examples, and callouts used properly? |

> Bonus check: Will the *next contributor* understand what’s happening here?

---

### 💬 How to Give Better Feedback

| ❌ Don't Say | ✅ Say Instead |
|-------------|----------------|
| “This makes no sense.” | “Can you clarify what happens after Step 3?” |
| “This isn’t how we usually write it.” | “Let’s align this with the 'Writing Principles' section.” |
| “Why are you even adding this?” | “Is there a specific use case you had in mind for this?” |

> Kindness isn’t optional—it’s part of clarity.

---

### ✅ Merging Guidelines

- Every major update needs 1+ reviewer approval  
- Editorial changes (grammar, spacing, internal links) can be merged solo  
- Contributors **must** tag the latest doc version and update the changelog if the structure changes  
- All merges must follow conventional commit format

---

### 🧠 Pro Tips

- If a change “feels off,” suggest—not block  
- If a section is unclear, ask *what it’s trying to do*, not just how it’s written  
- Don’t just review the code—*review the experience*

---

### 📌 TL;DR

- Reviews are guardrails, not gates  
- Propose clearly, review kindly, and merge consistently  
- Ask: “Will this make someone’s job easier?”—that’s the metric

> Good feedback doesn't just fix the doc. It teaches the writer.

---

## 19. Automation & Tooling  
_Linting, CI checks, and the bots that make us better—not bitter._

Good automation doesn’t just enforce rules—it makes good writing easier.

We use light-touch automation to:
- Keep formatting and structure clean  
- Prevent broken links and missing alt text  
- Avoid noisy or unstructured commits  
- Reduce reviewer burden on repetitive issues

---

### ⚙️ Recommended Tools

| Tool | What It Does | When We Use It |
|------|---------------|----------------|
| `markdownlint` | Checks for heading structure, spacing, and common MD errors | On every commit |
| `prettier` | Formats Markdown and code blocks consistently | Optional but recommended |
| `alex` | Warns about insensitive or biased language | Before publishing |
| `textlint` | Catch long sentences, passive voice, and filler words | During reviews |
| `husky` | Runs checks before commit/push | Used with pre-commit hooks |

---

### 🧠 Example: Pre-Commit Hook with `markdownlint`

`.husky/pre-commit`
```bash
#!/bin/sh
npx markdownlint "**/*.md"
```

✅ This ensures you won’t accidentally commit a doc with broken headings or list formatting.

---

### ✅ GitHub Actions for Docs

You can also add automation to your GitHub repo with minimal overhead.

`.github/workflows/lint-docs.yml`
```yaml
name: Lint Markdown

on: [pull_request]

jobs:
  markdown-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Lint Markdown
        uses: DavidAnson/markdownlint-cli2-action@v13
```

✅ This checks every PR for Markdown issues automatically.

---

### 🤖 Don’t Over-Automate

#### ❌ Anti-patterns
- Blocking PRs because a line is 81 characters  
- Forcing tools that contributors can’t easily install  
- Adding six linters that contradict each other

#### ✅ Better Approach
- Catch *preventable friction* (like broken anchors or missing alt text)  
- Format only what matters (spacing, heading structure)  
- Use automation to assist—not intimidate

---

### 💬 What to Automate vs Review Manually

| Automate | Review Manually |
|----------|------------------|
| Markdown syntax, broken links, alt text | Voice, tone, examples |
| Commit style (`feat:`, `fix:`) | Doc structure and logic |
| Typos, spacing | Is this helpful to the reader? |

---

### 📌 TL;DR

- Use `markdownlint`, `alex`, and pre-commit hooks for clarity and inclusivity  
- Automate the boring stuff so humans can focus on meaning  
- Don’t let bots kill creativity—use them to surface quality

> Automation should clean your docs—not erase their soul.

---

## 20. SEO & Discoverability  
_Slugs, meta-tags, internal linking—and how to be found without selling your soul._

Your documentation is only useful if people can find it.  
Search Engine Optimization (SEO) isn’t about gaming Google—it’s about writing clearly, titling wisely, and linking meaningfully.

> Good SEO = Helping people find the right answer, right when they need it.

---

### 🔍 What Impacts Discoverability in Docs

| Element | Why It Matters |
|--------|-----------------|
| **Headings** | Clear, descriptive H1s and H2s improve skimming and indexing |
| **Slugs (URLs)** | Clean, hyphenated, keyword-rich slugs are easier to remember and share |
| **Meta Descriptions** | Appear in search snippets—summarize the doc’s usefulness in 1–2 lines |
| **Link structure** | Internal links build hierarchy and guide user flow |
| **Anchor names** | Human-readable anchors improve link trust and click-throughs |

---

### ✅ Writing SEO-Friendly Titles

**Bad:**
```markdown
# Features
```

**Better:**
```markdown
# Key Features of the Slack Integration
```

✅ Be specific. Use terms your audience is likely to search for.

---

### 🧭 Writing Meta Descriptions (If Your Platform Supports It)

In frontmatter or metadata blocks:
```yaml
title: "Slack Integration Setup Guide"
description: "Learn how to configure Slack integration with webhooks, auth, and error handling."
```

> ✅ Think like a user: “If I saw this in search, would I click it?”

---

### 📎 Link Placement Best Practices

- Link **related docs inline** where context is relevant  
  ✅ _“To configure the webhook, [see our error-handling guide](./webhook-errors.md).”_

- Avoid generic anchors like `click here`  
  ✅ _“[See OAuth setup instructions →](./oauth-setup.md)”_

- Use **relative paths** for internal links (`./`, not full domain)  

---

### ❌ Common SEO Pitfalls

| Mistake | Better Practice |
|--------|------------------|
| Vague titles (“Getting Started”) | “Getting Started with XYZ CLI (Beginner Guide)” |
| Repeating exact same keywords | Use natural variations (synonyms, question phrasing) |
| Using raw URLs | Use `[descriptive text](url)` instead |
| Keyword stuffing | Prioritize clarity—readers > robots |

---

### 🛠 Tools for Smarter Docs SEO

| Tool | Use Case |
|------|----------|
| [Yoast](https://yoast.com/) | Write SEO-optimized meta descriptions |
| [Google Search Console](https://search.google.com/search-console) | See what queries lead to your docs |
| [Ahrefs Free Tools](https://ahrefs.com/webmaster-tools) | Check backlinks and crawl health |
| [markdown-link-check](https://github.com/tcort/markdown-link-check) | Detect broken links in `.md` files |

---

### 📌 TL;DR

- Title with clarity, not cleverness  
- Write 1–2 sentence summaries (meta descriptions)  
- Use anchor links with purpose—not just out of habit  
- Avoid stuffing keywords; favor discoverability through usefulness  
- Think “search phrases,” not buzzwords

> Search engines don’t rank what’s beautiful.  
> They rank what’s useful—and readable.

---

## 21. Living Documentation  
_Review schedules, ownership, and docs that age gracefully._

Docs are not code—but they *do decay*.

This section helps you keep your documentation relevant, helpful, and trusted—without burning out your team.

A “living” document means:
- It reflects the current state of the product  
- It has an owner, not just a creator  
- It signals when it’s outdated or ready for removal

---

### 🧠 Signs Your Doc Is Dying

| Symptom | What It Means |
|---------|----------------|
| Reader feedback is unclear or contradictory | The doc is outdated or confusing |
| Internal links are broken | Sections have moved or been renamed |
| Screenshots show an old UI | The product evolved but the doc didn’t |
| It only made sense during a sprint | The doc has lost long-term context |

---

### ✅ Review Cadence Suggestions

| Doc Type | Review Every… |
|----------|----------------|
| Core product docs | 3–6 months |
| Integrations / APIs | Quarterly or per release |
| Internal onboarding docs | Twice a year |
| Style Guide | Living edits, with quarterly reviews |

> If it impacts users, review it like a product.

---

### 🧑‍💼 Assigning Ownership

Every major doc should have:
- A **primary maintainer** (can be shared across teams)
- A clear history of contributors (visible via commits or metadata)
- A changelog or “last updated” tag to guide readers and editors

```markdown
_Last reviewed: April 2025 by @devdocqueen_
```

---

### 🪦 How to Retire a Doc (Gracefully)

Don’t just delete it. Deprecate with dignity.

✅ Steps:
1. Add a banner to the top of the doc:
   ```markdown
   > ⚠️ **Deprecated:** This guide is outdated as of April 2024.  
   > For the latest setup, [see the updated OAuth guide](./oauth-v2.md).
   ```

2. Move to `/archive/` or clearly label with `[DEPRECATED]` in the filename  
3. Remove it from nav menus and TOC if it's not actively needed

---

### 🧭 Proactive Doc Maintenance Checklist

| Task | Frequency |
|------|-----------|
| Check for broken links or 404s | Monthly |
| Refresh screenshots and code examples | Quarterly |
| Validate internal links still resolve | Monthly |
| Ask users what’s unclear or missing | Continuously |

---

### ❌ What Not to Do

| Mistake | Better Approach |
|--------|------------------|
| Assume published = finished | Review regularly; treat like product assets |
| Delete docs without redirect | Deprecate visibly or archive with links |
| Ignore reader feedback | Add clarifications or open a PR—even for small notes |

---

### 📌 TL;DR

- Assign doc owners and review cycles—don’t let docs drift  
- Mark outdated guides with version labels or warnings  
- Archive responsibly, and always point readers to what’s next  
- Keep changelogs and last-reviewed metadata visible

> Living docs aren’t constantly changing.  
> They’re just never ignored.

---

## 22. AI-Assisted Writing  
_Guidance on responsible, ethical, and effective use of AI in docs._

AI can draft, polish, rephrase, reformat—and hallucinate.

This section helps you use AI as a writing assistant—not a ghostwriter—and ensures your documentation stays:
- Clear  
- Credible  
- Human-first

---

### 🤖 What AI Can Help With

| Task | AI Is Useful For… |
|------|-------------------|
| Rephrasing text | Making long paragraphs clearer or shorter |
| Formatting Markdown | Cleaning up tables, lists, headings |
| Generating boilerplate | Drafting TOCs, changelogs, or style guide stubs |
| Translating tone | Converting corporate speak to plain English |
| Brainstorming examples | Coming up with analogies, metaphors, or edge cases |

---

### ❌ What AI Should NOT Do

| Task | Why It’s Risky |
|------|----------------|
| Write final technical instructions | May hallucinate commands or concepts |
| Generate real code snippets | Can suggest insecure, untested, or broken code |
| Mimic company voice | Often sounds generic or fake “helpful” |
| Fabricate citations or links | Breaks trust immediately |
| Replace writer ownership | Undermines author intent, empathy, and context

---

### 🧠 Ethical Considerations

| Principle | What It Means |
|----------|----------------|
| **Transparency** | If AI drafted part of a doc, reviewers should know |
| **Human accountability** | Every doc must have a human editor and owner |
| **No silent generation** | Don’t paste AI-generated content without reviewing every word |
| **No plagiarism** | Never lift examples or phrasing from other sources via AI without credit |
| **No fake examples** | Real screenshots, real workflows, or clearly marked demos only |

> ✍️ Writers write.  
> AI assists—but humans are responsible.

---

### ✅ Ethical AI Workflow

1. **Prompt clearly**  
   _“Rewrite this section for a beginner. Avoid jargon, but don’t lose technical meaning.”_

2. **Edit ruthlessly**  
   _If it’s bland, bloated, or incorrect—cut it._

3. **Verify everything**  
   _Check commands, URLs, syntax, formatting, tone._

4. **Mark what’s incomplete**  
   _Add `[INSERT real screenshot of new UI here]` or `[Placeholder: list common error codes]`._

---

### 🔍 Prompt Design: Good vs Bad

Writing for AI is a skill. Here’s how to level up:

#### ❌ Bad Prompt:
> “Write API documentation for my product.”

❌ What you get:
- Hallucinated endpoints  
- Placeholder tokens  
- Random headers and features you don’t support  
- Generic tone with no context

---

#### ✅ Better Prompt:
> “Write a short Getting Started section for a REST API with three endpoints: `/login`, `/logout`, and `/profile`. Focus on tone clarity over cleverness. Audience is mid-level devs familiar with Postman.”

✅ What you get:
- Role-aware, usable draft  
- Structure and examples tailored to real devs  
- Something you can edit, not trash

---

#### ❌ Bad Prompt:
> “Explain JSON to a non-techie.”

❌ What you get:
> “JSON stands for JavaScript Object Notation and is a lightweight data-interchange format. It is easy to read and write…”

✅ Zzzzz...

---

#### ✅ Better Prompt:
> “Explain JSON to a non-technical HR manager who understands spreadsheets. Use a friendly tone. Compare it to a table of columns and rows.”

✅ What you get:
> “Imagine a spreadsheet where each row is an employee, and each column—like name, title, and ID—is a data label. JSON is just that, but for machines to read and pass around.”

Now that’s **readable and reusable**.

---

### ⚠️ Common Pitfalls with AI-Written Docs

| Mistake | Real Impact |
|--------|-------------|
| Copying without editing | Leads to errors, bloated text, robotic tone |
| Using fake file paths | Users get confused or break things |
| Not attributing AI output | Breaks trust and ownership |
| Skipping fact-checking | Introduces silent bugs or false features |

---

### ✅ Good AI Use vs Bad AI Use

#### ✅ Good:
```markdown
> AI-generated: Drafted alt text for all diagrams.  
> Human-edited: Shortened, clarified, and removed 2 inaccurate suggestions.  
> Final: Added context-specific screenshots and corrected link targets.
```

#### ❌ Bad:
```markdown
> AI-generated: Wrote entire user guide.  
> Human: Copied and pasted into main without review.  
> Result: Broken commands, fake endpoints, inconsistent tone.
```

---

### 📌 TL;DR

- Use AI to support—not replace—your writing  
- Disclose, review, and rewrite as needed  
- Write better prompts, and treat AI like an intern—not a savior  
- If it sounds fake, bloated, or risky—it probably is

> AI can accelerate writing.  
> But only humans can write with **intent, empathy, and truth**.

---

## 23. Multi-Format Output  
_PDF, slides, video scripts—and writing that works everywhere._

Your documentation may need to live beyond Markdown.

This section helps you write with adaptability in mind—so your content can move between:
- Slideshows  
- Tutorials or videos  
- Voice-over scripts  
- Interactive tools  
- PDFs or printed booklets

> Great documentation isn’t tied to its format.  
> It’s built on clarity, rhythm, and hierarchy.

---

### 🧭 Format-Agnostic Writing Principles

| Rule | Why It Matters |
|------|----------------|
| Use clear headings | Can be reused as slide titles or section markers |
| Short paragraphs | Easier to voice-over or present visually |
| Avoid inline-only instructions | Screen readers or slides won’t show hover states |
| Separate content from visuals | Easier to reuse content across formats |
| Use consistent callouts and examples | Helps in script narration or alt-text captions |

---

### 🎬 Adapting a Doc to Other Formats

#### ✅ Slide Deck (Presentation)
| Doc Element | Slide Equivalent |
|-------------|------------------|
| `## Heading` | Slide title |
| Bullet list | Slide bullets |
| Code block | Screenshot or side-by-side |
| Callout box | Presenter note or visual emphasis |

#### ✅ Video Tutorial or Script
| Doc Element | Spoken Equivalent |
|-------------|-------------------|
| Step-by-step list | Walkthrough narration |
| Notes or tips | On-screen annotations |
| Visual references | Camera zooms / highlights |
| Examples | Demo clips or animations |

---

### 🧱 Multi-Format Layout Template

```markdown
## Section Title  
_1-sentence intro for context_

### Step-by-step / Concept  
- Step 1: Do the thing  
- Step 2: Verify it worked  
- Step 3: Roll back if needed

> 💡 Tip: Use `--dry-run` before applying live changes.

📎 Related: [Rollback docs →](./rollback.md)

🎙 Voiceover version:  
“Let’s start by cloning the repo and checking if the setup works locally…”
```

---

### ❌ Pitfalls to Avoid

| Problem | Fix |
|--------|-----|
| Long, dense paragraphs | Break into 2–3 line chunks |
| Reliance on layout-specific features | Avoid columns, hover text, or interactive-only notes |
| Visuals with no description | Add alt-text or captions |
| Repetitive formatting across formats | Keep one clean source and generate outputs as needed |

---

### 🛠 Tools to Export From Markdown

| Tool | Output | Notes |
|------|--------|-------|
| [Pandoc](https://pandoc.org) | PDF, DOCX, slides | Great for automation |
| [Marp](https://marp.app) | Slides | Turn Markdown into PowerPoint-like decks |
| [Docsify](https://docsify.js.org/) | Web docs | Live preview-friendly |
| [Lunacy + Figma Plugins](https://www.figma.com/community) | Graphics/slides from doc layouts | For visual-first teams |

---

### 📌 TL;DR

- Write with format flexibility in mind—structure > style  
- Keep language concise and modular for reuse in slides, videos, scripts, and more  
- Separate content from layout, always add alt text  
- Use tools to export—not rewrite

> A well-written doc should be easy to **read**, easy to **present**, and easy to **teach**.

---

## 24. Evolution Rules  
_How and when this guide updates—because writing standards grow, too._

Style guides aren’t holy texts.  
They’re living agreements—meant to evolve with your team, your audience, and your tools.

This section defines how we:
- Propose changes to the guide  
- Decide what gets added, rejected, or rewritten  
- Keep the guide relevant without constant churn

---

### 🧭 When Should the Style Guide Change?

✅ Add or revise a section when:
- There’s **repeated confusion** across docs or contributors  
- A new format or tool (e.g. AI, localization, video) becomes common  
- You’ve spotted **outdated guidance or broken rules**  
- Feedback or onboarding shows friction

✅ Avoid changes just because:
- It’s “how you personally like to write”  
- You want to make a sentence sound cooler  
- You’re trying to match external brands or trends

> This guide evolves for the **collective clarity**—not individual voice.

---

### 🔧 How to Propose a Change

Every style edit—no matter how small—should:
- Be submitted as a Pull Request  
- Include a short rationale in the PR description  
- Reference an example of where the current rule caused confusion or inconsistency

#### ✅ Example PR Description:
```markdown
This PR suggests rewording the “Emphasis Rules” section to better distinguish between emphasis for emotion vs. technical commands. 

We noticed contributors overusing `**bold**` where italics were meant to soften tone.

Issue raised in #42 and #51.
```

---

### 🧠 Who Approves Changes?

| Change Type | Reviewer Required |
|-------------|--------------------|
| Minor copy tweaks or typo fixes | 1 contributor or editor |
| New rule, term, or section | Style guide lead or majority agreement |
| Structural changes to hierarchy or tone | Needs team discussion & review |

✅ Use GitHub Discussions or issues for large proposals before writing a PR.

---

### 🏷️ Versioning the Style Guide

The style guide has its own semantic version.

```markdown
🎨 Style Guide — Version 1.2.0  
_Last updated: May 21, 2025_
```

| Version Type | What Changed |
|--------------|---------------|
| `x.0.0` | Major rewrite or tone change |
| `0.x.0` | Added sections, rules, or glossary terms |
| `0.0.x` | Fixes, rewording, formatting cleanup |

---

### 🔐 What Doesn’t Change Easily

Some sections require higher scrutiny before edits:
- Tone & Voice  
- Glossary Definitions  
- Accessibility Rules  
- Ethical/AI Usage Standards

> These are foundational.  
> Updates should reflect real-world pain—not personal taste.

---

### 📌 TL;DR

- Style guides are agreements, not absolutes  
- Propose changes with examples, not opinions  
- Version the guide, track the changes, and explain the *why*  
- Change what serves the reader—not what flatters the writer

> This guide evolves—but only for the right reasons.

---
