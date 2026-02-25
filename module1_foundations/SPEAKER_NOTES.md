# 🎤 Speaker Notes — Module 1: Prompt Engineering Foundations

---

## 🟢 Opening (1–2 minutes)

> "In this module, we'll explore the **foundation of every AI application** — Prompt Engineering.
> The goal here is simple: **how you ask determines what you get.**
> We've built a fun, interactive AI Concept Explainer that demonstrates this principle using three creative personas — Shakespeare, a Pirate, and a Wild West Bandit."

**Key point to emphasize:**
- This module has just **2 Python files** and a **prompt template** — that's all you need to build a working AI app.
- The magic isn't in complex code, it's in **how we craft the prompts**.

---

## 📁 File-by-File Walkthrough

---

### 1. `requirements.txt` — Dependencies

```
litellm
python-dotenv
```

**What to say:**
> "We only need two packages:
> - **LiteLLM** — a universal wrapper that lets us call any LLM (OpenAI, Groq, Gemini, etc.) with the same code. If we want to switch models, we just change one string. No code rewrite needed.
> - **python-dotenv** — loads our API key from a `.env` file so we never hardcode secrets."

**Why this matters:**
- LiteLLM abstracts away provider-specific SDKs — you write once, run on any model.
- `.env` files are an industry best practice for secret management.

---

### 2. `.env` — API Key Configuration

**What to say:**
> "This file stores our API key. It's loaded at runtime by `python-dotenv`. We also have a `.gitignore` that excludes this file — so **secrets never go to GitHub**. This is a real-world best practice."

**Do NOT show the actual key on screen.** Just mention the pattern:
```
GROQ_API_KEY=your_key_here
```

---

### 3. `prompts.py` — The Prompt Engineering Layer ⭐

> "This is the **heart of the module**. This file demonstrates that prompt engineering is about giving the AI a **clear role, structured instructions, and a consistent persona**."

#### Part A: `SYSTEM_PROMPT` (Lines 1–6)

```python
SYSTEM_PROMPT = """
You are an expert AI educator.
Adapt explanations based on the target audience.
Ensure clarity and correctness.
Avoid hallucinations.
"""
```

**What to say:**
> "The system prompt sets the AI's **identity and ground rules** — before it even sees the user's question.
> Think of it like a job description:
> - Be an expert educator
> - Adapt to the audience
> - Be clear and correct
> - **Don't hallucinate** — don't make things up
>
> This is sent as the `system` message in the API call. It persists across the conversation and shapes every response."

**Key concept to highlight:**
- **System prompt vs User prompt**: System = who you are. User = what to do right now.
- The system prompt is the **guardrail** — it prevents the AI from going off-script.

---

#### Part B: `build_prompt(topic, mode)` Function (Lines 8–56)

**What to say:**
> "This function is our **prompt template factory**. It takes two inputs — the topic to explain, and the character mode — and assembles a structured prompt."

##### The Three Modes:

**🎭 Shakespeare Mode:**
> "When mode is Shakespeare, we instruct the AI to speak in Early Modern English — thee, thou, doth, forsooth.  
> It must give a dramatic definition, a theatrical metaphor, a poetic soliloquy, and end with a rhyming couplet.  
> The AI doesn't just explain — it **performs**."

**🏴‍☠️ Pirate Mode:**
> "Pirate mode turns the AI into a swashbuckling captain.  
> Everything becomes a sea adventure — buried treasure, Davy Jones' locker.  
> Notice how specific the instructions are — we tell it exactly what slang to use (Arrr, matey, ye).  
> **The more specific your prompt, the more consistent the output.**"

**🤠 Bandit Mode:**
> "The Bandit is a smooth-talking Wild West outlaw around a campfire.  
> Analogies involve train heists and outsmarting the sheriff.  
> It ends with a cowboy motto — fun but educational."

**Error handling:**
> "If someone enters an invalid mode, we raise a `ValueError` with a helpful message. Always validate inputs — even in demos."

##### The Return Statement (Lines 49–56):

```python
return f"""
    Topic: {topic}
    Audience Mode: {mode}
    Instructions:
    {style}
    """
```

**What to say:**
> "Finally, everything is assembled into a structured f-string.  
> The AI sees exactly:
> - **What** topic to explain
> - **Which** mode/persona to use
> - **How** to structure the response
>
> This is a **template pattern** — reusable, modular, and easy to extend. Want a new mode? Just add another `elif` block."

---

### 4. `concept_explainer.py` — The Execution Layer

```python
import os
from dotenv import load_dotenv
from litellm import completion
from prompts import SYSTEM_PROMPT, build_prompt
```

**What to say:**
> "This file is the **executor** — it connects our prompts to the actual AI model."

#### Walk through the flow:

**Step 1 — Environment Setup (Lines 1–6):**
> "We import our tools: `os` for environment access, `dotenv` to load the API key, `litellm` for the API call, and our own `prompts.py` for the system prompt and prompt builder. Then `load_dotenv()` reads the `.env` file."

**Step 2 — The `explain()` function (Lines 8–21):**

```python
def explain(topic, mode):
    user_prompt = build_prompt(topic, mode)    # ← Build the prompt

    response = completion(
        model="groq/llama-3.1-8b-instant",     # ← Model selection
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},  # ← System prompt
            {"role": "user", "content": user_prompt}       # ← User prompt
        ],
        temperature=0.7,                        # ← Creativity level
        max_tokens=500                          # ← Response length cap
    )

    return response["choices"][0]["message"]["content"]  # ← Extract text
```

**What to say:**
> "Here's where messages to the API are structured:
> 1. `build_prompt()` creates the user message with topic + mode instructions
> 2. `completion()` sends it to the model — we're using **Groq's Llama 3.1 8B** (fast and free)
> 3. The messages array has exactly **2 messages**: system (persona) and user (task)
>
> **Key parameters:**
> - `temperature=0.7` — Controls randomness. 0 = robotic/deterministic, 1 = very creative. 0.7 is a sweet spot for creative yet coherent responses.
> - `max_tokens=500` — Caps the response length so we don't get a 10-page essay.
>
> The beauty of LiteLLM: to switch to GPT-4, just change the model string to `openai/gpt-4`. **One line change, completely different brain.**"

**Step 3 — The `__main__` block (Lines 24–29):**
> "This is the user-facing entry point. It asks for a topic and a mode, then prints the AI's response. Simple, clean, interactive."

---

## 🔗 Architecture Summary (Draw on whiteboard or slide)

```
User Input
   │
   ├── topic: "Neural Networks"
   └── mode: "Pirate"
         │
         ▼
   ┌─────────────┐
   │  prompts.py  │  ← Prompt Template Factory
   │              │
   │ SYSTEM_PROMPT│  → "You are an expert AI educator..."
   │ build_prompt │  → "Arrr! Topic: Neural Networks..."
   └──────┬───────┘
          │
          ▼
   ┌──────────────────────┐
   │ concept_explainer.py  │  ← Execution Layer
   │                       │
   │  litellm.completion() │  → Sends to Groq/Llama 3.1
   └──────┬────────────────┘
          │
          ▼
   🏴‍☠️ AI Response in Pirate Voice!
```

---

## 💡 Key Takeaways to Emphasize

1. **Prompt Engineering = Controlling AI behavior through text instructions**
   - System prompt = identity & rules
   - User prompt = task & style

2. **Separation of Concerns**
   - `prompts.py` handles **what to say** (prompt construction)
   - `concept_explainer.py` handles **how to send it** (API call)
   - This makes the code modular and easy to extend

3. **Temperature & Max Tokens**
   - These are the two most important API parameters
   - Temperature controls creativity; max_tokens controls length

4. **LiteLLM Abstraction**
   - Write once, switch models with a string change
   - No vendor lock-in

5. **Security Best Practices**
   - API keys in `.env`, excluded via `.gitignore`
   - Never hardcode secrets

---

## 🎯 Live Demo Script

1. Run the script:
   ```
   python concept_explainer.py
   ```
2. Enter topic: `"Hallucination in AI"`
3. First demo with **Shakespeare** mode → Show the dramatic response
4. Run again with **Pirate** mode → Contrast the style difference
5. Run again with **Bandit** mode → Show the third persona

> **Point to make:** "Same topic, same model, same code — **only the prompt changed**. That's the power of prompt engineering."

---

## ❓ Anticipated Questions & Answers

**Q: Why not use OpenAI directly?**
> "LiteLLM gives us model flexibility. We can switch to GPT-4, Claude, or Gemini with one line. No vendor lock-in."

**Q: What is temperature exactly?**
> "It controls the randomness of token selection. At 0, the model always picks the most probable next word. At 1, it samples more freely. 0.7 gives us creative but coherent output."

**Q: Can we add more modes?**
> "Absolutely! Just add another `elif` block in `prompts.py`. The architecture is designed to be extensible — that's the point of separating prompts from execution."

**Q: What is a hallucination?**
> "When the AI generates information that sounds confident but is factually wrong or completely made up. Our system prompt explicitly tells it to avoid this."

**Q: Why Groq/Llama instead of GPT-4?**
> "Groq offers fast inference on open-source models for free. Great for demos and learning. In production, you'd benchmark different models for your use case."

---

## 🔄 Transition to Module 2

> "Now that we understand how to **control AI behavior through prompts**, the next question is: what if the AI needs **external knowledge** it wasn't trained on? That's where **Module 2: Retrieval-Augmented Generation (RAG)** comes in. Instead of relying only on the model's training data, we'll teach it to **look things up** before answering."
