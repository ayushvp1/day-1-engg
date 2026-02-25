# 🎤 Speaker Notes — Module 2: Prompt Engineering (Structured Output)

---

## 🟢 Opening (1–2 minutes)

> "In Module 1, we saw how changing the **persona** changes the AI's style. But in real-world applications, style isn't enough — you need the AI to follow a **strict output format**.
>
> Imagine building a chatbot for a company — the CEO doesn't want creative poetry, they want answers in a **Definition → Example → Use Case** structure, every single time.
>
> This module teaches you how to **force the AI into a specific output structure** using prompt engineering — no extra library, just better instructions."

**Key point to emphasize:**
- Module 1 = controlling **style/tone** (fun personas)
- Module 2 = controlling **structure/format** (strict output templates)
- This is the difference between a toy demo and a production-ready AI system.

---

## 📁 File-by-File Walkthrough

---

### 1. `requirements.txt` — Dependencies

```
litellm
python-dotenv
```

**What to say:**
> "Same two packages as Module 1. This is intentional — it shows that you don't need new tools to get structured output. The improvement comes entirely from **better prompt engineering**."

---

### 2. `prompts.py` — The Structured Prompt Template ⭐

#### Part A: `SYSTEM_PROMPT` (Lines 1–9)

```python
SYSTEM_PROMPT = """
You are a precise AI tutor.

Rules:
- Always follow the output format strictly.
- Do not add extra sections.
- Keep explanation clear and structured.
- If question is unclear, ask for clarification.
"""
```

**What to say:**
> "Notice how different this system prompt is from Module 1:
>
> - Module 1 said 'You are an expert AI educator' — broad and flexible
> - Module 2 says 'You are a **precise** AI tutor' with explicit **rules**
>
> The word 'precise' matters. We're also adding **negative instructions**: 'Do not add extra sections.' This is a key technique — telling the AI what **NOT** to do is often more effective than telling it what to do.
>
> The last rule — 'If question is unclear, ask for clarification' — prevents hallucination. Instead of guessing, the AI should ask."

**Key concepts to highlight:**
- **Positive vs Negative instructions**: "Do X" and "Don't do Y" work together
- **Specificity ladder**: Module 1 was loose → Module 2 is tight → Production is even tighter
- The system prompt now acts as a **contract** — rules the AI must follow

---

#### Part B: `build_prompt(question)` Function (Lines 11–26)

```python
def build_prompt(question):
    return f"""
Answer the following question in this exact structure:

Definition:
<clear and concise definition>

Example:
<simple understandable example>

Real Use Case:
<practical real-world use case>

Question:
{question}
"""
```

**What to say:**
> "This is the core evolution from Module 1. Instead of saying 'explain this in pirate voice,' we're giving the AI a **fill-in-the-blank template**.
>
> Notice the structure:
> - **Definition:** → forces a clear definition first
> - **Example:** → forces a practical example
> - **Real Use Case:** → forces real-world relevance
>
> The angle brackets `<clear and concise definition>` act as **placeholder hints** — they tell the AI not just WHERE to put the answer, but HOW to answer (clear, concise, simple, practical).
>
> This is called **structured prompting** or **template prompting**. It's the #1 technique used in production AI systems."

**Key design decisions to explain:**
- The template is in the **user prompt**, not the system prompt — because the format may change per request
- Putting `Question:` at the **end** (after the template) ensures the AI reads the format rules before seeing the question
- This pattern is directly used in ChatGPT plugins, API integrations, and enterprise AI tools

---

### 3. `structured_generator.py` — The Execution Layer

```python
MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

def generate_answer(question):
    prompt = build_prompt(question)
    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=600
    )
    return response["choices"][0]["message"]["content"]
```

**What to say:**
> "Two important differences from Module 1's `concept_explainer.py`:
>
> **1. `MODEL_NAME` is now configurable via environment variable (Line 8):**
> Instead of hardcoding the model, we read it from `.env`. This means you can switch models **without touching the code** — just change the env var. This is a production best practice.
>
> **2. `temperature=0.3` instead of 0.7:**
> This is the key difference. Lower temperature = more **deterministic** output. When you want the AI to follow a strict format every time, you don't want randomness. Think of it this way:
> - Temperature 0.7 (Module 1) = 'Be creative, have fun'
> - Temperature 0.3 (Module 2) = 'Follow the rules, be consistent'
> - Temperature 0.0 = 'Give the exact same answer every time'
>
> **3. `max_tokens=600` instead of 500:**
> Slightly more room because the structured format (Definition + Example + Use Case) needs more space than a single-style explanation."

---

## 🔗 Architecture Comparison — Module 1 vs Module 2

```
MODULE 1 (Creative)               MODULE 2 (Structured)
──────────────────                 ──────────────────────
Persona-based prompts              Template-based prompts
temperature = 0.7 (creative)       temperature = 0.3 (deterministic)
Flexible output format             Strict Definition/Example/Use Case
Model hardcoded                    Model from environment variable
Fun & engaging                     Precise & production-ready
```

**What to say:**
> "Both modules use the exact same tech stack — LiteLLM, Groq, dotenv. The only difference is **how we write the prompts and configure the parameters**. That's the entire lesson."

---

## 💡 Key Takeaways to Emphasize

1. **Structured Prompting = Giving the AI a template to fill**
   - Use labeled sections (Definition:, Example:, etc.)
   - Use placeholder hints in angle brackets

2. **Temperature controls format adherence**
   - Lower temperature → more consistent structure
   - Higher temperature → more creative but less predictable

3. **Negative instructions are powerful**
   - "Do not add extra sections" prevents the AI from going off-script
   - "If unsure, ask for clarification" prevents hallucination

4. **Environment-based configuration**
   - Model name in `.env` = zero-code model switching
   - This is how production systems manage AI configurations

5. **Evolution from Module 1**
   - Module 1: "How do I make AI fun?" → Personas
   - Module 2: "How do I make AI reliable?" → Structured templates

---

## 🎯 Live Demo Script

1. Run the script:
   ```
   python structured_generator.py
   ```
2. Enter question: `"What is a Neural Network?"`
3. Show the structured output (Definition → Example → Use Case)
4. Run again with: `"What is overfitting?"`
5. Compare the two outputs — **same structure, different content**

> **Point to make:** "The AI follows the same format every time. That's the power of structured prompting. In production, this means your frontend can **parse** the AI's output reliably."

---

## ❓ Anticipated Questions & Answers

**Q: Why not just use JSON output?**
> "JSON output is the next level of structured prompting. Some models support `response_format={'type': 'json_object'}`. But understanding text-based templates first is essential — it works on ALL models."

**Q: What if the AI breaks the format?**
> "Lower the temperature further, add stronger instructions like 'You MUST follow this exact format,' or use post-processing to validate structure. Module 3 introduces post-processing for this."

**Q: Why is the question at the end of the prompt?**
> "The AI reads the prompt sequentially. Putting format instructions BEFORE the question ensures it 'reads the rules' before 'seeing the task.' This improves format compliance."

---

## 🔄 Transition to Module 3

> "Now we know how to control AI **style** (Module 1) and **structure** (Module 2). But we've been writing everything in 2 files. Real AI systems have multiple layers — input handling, prompt building, model calling, output cleaning. Module 3 teaches us how to build a **proper modular pipeline architecture** — the engineering side of AI."
