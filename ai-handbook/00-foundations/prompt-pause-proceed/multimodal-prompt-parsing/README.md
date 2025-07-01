# ️ Multimodal Prompt Parsing  

*Part of the Prompt Dissection Lab*  
_Design prompts that blend text, image, audio, or more — and understand how AI processes each._

---

##  Table of Contents

- [What This Is](#-what-this-is)
- [Why Multimodal Prompts Matter](#-why-multimodal-prompts-matter)
- [How AI Parses Each Input Type](#-how-ai-parses-each-input-type)
- [Prompt Structure & Tips by Mode](#-prompt-structure--tips-by-mode)
- [Common Multimodal Prompt Failures](#-common-multimodal-prompt-failures)
- [Examples by Modality](#-examples-by-modality)
- [Helpful Diagnostic Prompts](#-helpful-diagnostic-prompts)
- [References & Resources](#-references--resources)

---

##  What This Is


This guide helps you craft **multimodal prompts** — those combining text with images, audio, or other inputs — and explains how AI interprets each mode.

Many users assume AI “sees” images like humans. It doesn’t.  
Multimodal parsing requires intentional, descriptive scaffolding — and awareness of **model capabilities**.

---

##  Why Multimodal Prompts Matter


- You want AI to **analyze an infographic** and write a caption  
- You need help **describing a photo** for accessibility or branding  
- You want AI to **transcribe and summarize audio**  

But:  
AI models trained on text don't “understand” pixels or sound the way we do.  
They **convert them into embeddings** (numeric patterns) and match those with language patterns they've seen.

> _“Garbage in, garbage out” is more literal in multimodal prompts._

---

##  How AI Parses Each Input Type


| Input | What Happens Behind the Scenes | Common Misconception |
|-------|-------------------------------|-----------------------|
| **Text** | Parsed word-by-word as token sequence | AI reads it as naturally as we do |
| **Image** | Transformed into vector data via vision encoder (e.g., ViT) | AI “sees” the image like a human |
| **Audio** | Converted into spectrogram, then embeddings (e.g., via Whisper) | AI listens like a human and understands nuance |
| **Video** | Broken down into frames + audio track → processed separately | AI understands movement and scenes |

🧠 These inputs must be accompanied by **instructions** that tie them together.

---

## ✍️ Prompt Structure & Tips by Mode


### ️ Text + Image


```yaml
You are a [role, e.g., art critic].  
Given this image: [attach image]  
→ Describe what’s happening visually.  
→ What emotion does it evoke?  
→ Give a headline that fits this image for a social media campaign.
```

**Tips:**
- Always include *task* + *tone* + *context*  
- Use “Describe this image as if…” to reframe perspective  
- If asking for analysis, clarify your lens (e.g., marketing, accessibility, emotional tone)

---

###  Text + Audio


```yaml
This is an audio note from a team lead. [attach audio]  
→ Transcribe it accurately.  
→ Then summarize it into a 2-line Slack update.  
→ Assume audience is the project manager.
```

**Tips:**
- Specify transcription **accuracy vs summary**  
- Define the output format (“bullet points,” “Tweet,” etc.)  
- Use follow-up prompts to test AI’s interpretation:  
  “Who do you think this audio was meant for?”

---

###  Text + Video


```yaml
Given this video [attach link if supported], summarize the 3 main actions happening.  
Assume you're reporting for a product demo.  
Then write a one-liner that describes what feature is shown.
```

**Tips:**
- Break down by segment: intro → action → close  
- Use explicit *time markers* (“in the first 5 seconds…”)  
- Not all models process video — check tool compatibility (e.g., Gemini)

---

##  Common Multimodal Prompt Failures


| Mistake | What Happens | Fix |
|--------|---------------|-----|
| ❌ “Look at this” with no direction | AI guesses | Add clear task with context |
| ❌ “Summarize this image” | Too abstract | Use anchor: “summarize from a design perspective” |
| ❌ Uploading multiple inputs with one vague instruction | Conflation or skipped content | Use separate steps: “First, analyze this audio. Then, compare with image.” |
| ❌ Assuming AI knows who/what/why | Misinterpretation | Provide background: “This is an ad for Gen Z.” |

---

##  Examples by Modality


| Modality | Task | Good Prompt |
|----------|------|-------------|
| Image | Caption creation | “Create 3 punchy captions for this protest image aimed at climate-conscious youth.” |
| Audio | Instruction recap | “Transcribe and highlight the 3 action items from this client call.” |
| Image + Text | Contrast prompt | “Compare this ad image with the written tagline. Does the tone match?” |
| Audio + Image | UX insight | “Based on the voice feedback and app screenshot, what pain point is the user expressing?” |

---

##  Helpful Diagnostic Prompts


- “What do you see in this image?”  
- “Describe this audio as if to a blind person.”  
- “How did you connect the image and the caption you generated?”  
- “Which part of the input did you focus on?”  
- “What assumptions did you make about the audience?”

---

##  References & Resources


- [OpenAI GPT-4 with Vision](https://openai.com/index/hello-gpt-4/)  
- [Whisper Speech Recognition](https://github.com/openai/whisper)  
- [Gemini AI Overview](https://blog.google/technology/ai/google-gemini-ai/)  
- [Multimodal Prompting Guide by Anthropic](https://docs.anthropic.com/claude/docs/prompting-best-practices)  
- [HuggingFace: Multimodal Transformers](https://huggingface.co/transformers/model_doc/vit.html)

---

> _“AI doesn’t see, hear, or feel.  
It maps patterns.  
Your job? Provide the landmarks.”_

---

##  Explore More


- [📘 Prompt Dissection Lab Overview](./README.md)  
- [🧭 Clarity & Structure Track](./clarity-structure-track.md)  
- [🧠 Literary & Linguistic Track](./literary-linguistic-track.md)  
- [💥 Prompt Failure Mode Matrix](./failure-mode-matrix.md)
