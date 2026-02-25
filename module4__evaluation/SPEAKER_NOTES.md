# 🎤 Speaker Notes — Module 4: Evaluation & Prompt Comparison

---

## 🟢 Opening (1–2 minutes)

> "We've built AI apps that are creative, structured, and well-architected. But here's the million-dollar question every AI team faces: **how do you know if your prompt is actually good?**
>
> You write Prompt V1. It works. You tweak it into V2. It also works. But which one is **better**?
>
> This module introduces **evaluation** — the process of scoring, measuring, and comparing AI outputs. It's the difference between 'I think this works' and 'I can **prove** this works.'
>
> In the industry, this is called **prompt iteration** or **prompt A/B testing**, and it's how companies decide which prompt version goes to production."

**Key point to emphasize:**
- No AI system ships without evaluation
- This module teaches the **thinking framework**, not just the code
- Evaluation is what separates "I built an AI demo" from "I shipped an AI product"

---

## 📁 File-by-File Walkthrough

---

### 1. `prompt_versions.py` — The Experiment Setup ⭐

#### Part A: `SYSTEM_PROMPT` (Lines 1–6)

```python
SYSTEM_PROMPT = """
You are an academic AI assistant.
Be precise, structured, and factually correct.
If unsure, say you do not know.
Avoid hallucinating facts.
"""
```

**What to say:**
> "Notice the evolution of our system prompts across modules:
>
> | Module | System Prompt Identity | Focus |
> |--------|----------------------|-------|
> | 1 | Expert AI educator | Adaptability |
> | 2 | Precise AI tutor | Structure |
> | 3 | AI Academic Assistant | Conciseness |
> | 4 | Academic AI assistant | **Factual correctness** |
>
> Module 4's prompt adds a critical new instruction: **'If unsure, say you do not know.'** This is an anti-hallucination guardrail. In production, you'd rather have the AI say 'I don't know' than confidently give wrong information."

---

#### Part B: Two Prompt Versions (Lines 8–21)

```python
def prompt_v1(question):
    return f"Explain: {question}"

def prompt_v2(question):
    return f"""
Explain the following clearly and in structured format.

Question: {question}

Provide:
- Explanation
- Example
- Practical Use Case
"""
```

**What to say:**
> "Here's the experiment. We have TWO versions of the same prompt:
>
> **Prompt V1** — The lazy prompt:
> Just 'Explain: {question}'. No structure. No instructions. Let the AI figure it out.
>
> **Prompt V2** — The engineered prompt:
> Structured, with explicit format requirements — explanation, example, use case.
>
> The question we're testing: **Does better prompt engineering actually produce better results?**
>
> Spoiler: yes. But the point of this module is to teach you how to **measure** and **prove** that, not just assume it."

**Key concept — Prompt Versioning:**
> "In production, prompts are versioned just like code. You don't just change a prompt and hope for the best — you test V1 vs V2 on the same input and score them. This is the foundation of **prompt ops** or **LLMOps**."

---

### 2. `model_runner.py` — The Model Layer

```python
MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

def call_model(prompt):
    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=700
    )
    return response["choices"][0]["message"]["content"]
```

**What to say:**
> "This is intentionally identical to Module 3's `llm_layer.py`. Same model, same temperature, same max tokens.
>
> Why? Because in an evaluation experiment, you must **control the variables**. The only thing changing between our two runs is **the prompt**. If we also changed the model or temperature, we wouldn't know what caused the difference in quality.
>
> This is scientific method applied to AI:
> - **Independent variable:** the prompt (V1 vs V2)
> - **Controlled variables:** model, temperature, max_tokens
> - **Dependent variable:** the quality of the output (what we measure)"

---

### 3. `evaluation_metrics.py` — The Scoring Rubric ⭐

```python
def manual_score():
    print("\nRate from 1 to 5")

    relevance = int(input("Relevance: "))
    completeness = int(input("Completeness: "))
    clarity = int(input("Clarity: "))
    consistency = int(input("Consistency: "))
    hallucination = int(input("Hallucination Risk (5 = no hallucination): "))

    final_score = (relevance + completeness + clarity + consistency + hallucination) / 5

    return {
        "Relevance": relevance,
        "Completeness": completeness,
        "Clarity": clarity,
        "Consistency": consistency,
        "Hallucination Safety": hallucination,
        "Final Score": final_score
    }
```

**What to say:**
> "This is where evaluation gets real. We score AI outputs on **5 dimensions**:
>
> | Metric | What it measures | Score Guide |
> |--------|-----------------|-------------|
> | **Relevance** | Did the AI actually answer the question? | 1 = off-topic, 5 = exactly on target |
> | **Completeness** | Did it cover everything needed? | 1 = missing key parts, 5 = comprehensive |
> | **Clarity** | Is the answer easy to understand? | 1 = confusing, 5 = crystal clear |
> | **Consistency** | Does it follow the format and stay coherent? | 1 = chaotic, 5 = well-structured |
> | **Hallucination Safety** | Did it make things up? | 1 = full of fake info, 5 = fully factual |
>
> The final score is the **average of all 5 dimensions**, giving a 1.0–5.0 overall rating.
>
> **Why these specific metrics?** They cover the three pillars of AI quality:
> - **Content quality** (relevance + completeness)
> - **Presentation quality** (clarity + consistency)
> - **Trustworthiness** (hallucination safety)
>
> In the industry, these are similar to the evaluation rubrics used by companies like Anthropic, OpenAI, and Google to benchmark their models."

**Important note on hallucination scoring:**
> "Notice the hallucination metric is **inverted** — 5 means NO hallucination. This is intentional so that a higher score is always better across all dimensions."

---

### 4. `evaluator.py` — The Comparison Engine

```python
def compare_outputs():
    print("\n--- Evaluate Prompt V1 ---")
    score1 = manual_score()

    print("\n--- Evaluate Prompt V2 ---")
    score2 = manual_score()

    print("\n--- Comparison Result ---\n")
    print("Prompt V1 Score:", score1["Final Score"])
    print("Prompt V2 Score:", score2["Final Score"])

    if score1["Final Score"] > score2["Final Score"]:
        print("Prompt V1 performed better.")
    elif score2["Final Score"] > score1["Final Score"]:
        print("Prompt V2 performed better.")
    else:
        print("Both prompts performed equally.")
```

**What to say:**
> "This file runs the evaluation **twice** — once for V1's output, once for V2's output — and then compares.
>
> It's a simple **A/B test**:
> 1. Read V1's output → score it on 5 metrics
> 2. Read V2's output → score it on 5 metrics
> 3. Compare final scores → declare a winner
>
> In production, this would be automated (using LLM-as-a-judge or statistical analysis), but manual evaluation is the foundation. Even OpenAI uses human evaluators alongside automated metrics."

---

### 5. `main.py` — The Full Experiment ⭐

```python
def run_evaluation():
    question = input("Enter question to test: ")

    print("\n--- Generating Output: Prompt V1 ---\n")
    output1 = call_model(prompt_v1(question))
    print(output1)

    print("\n--- Generating Output: Prompt V2 ---\n")
    output2 = call_model(prompt_v2(question))
    print(output2)

    compare_outputs()
```

**What to say:**
> "This is the experiment runner. One question goes through TWO different prompts:
>
> **Step 1:** User enters a question (e.g., 'What is backpropagation?')
> **Step 2:** The SAME question is sent through Prompt V1 (lazy) → AI generates output 1
> **Step 3:** The SAME question is sent through Prompt V2 (engineered) → AI generates output 2
> **Step 4:** You manually score BOTH outputs → the system tells you which prompt won
>
> Watch both outputs carefully during the demo. You'll see that V2 almost always produces a more structured, complete, and clear answer. **That's the measurable impact of prompt engineering.**"

---

## 🔗 Full Evaluation Pipeline

```
       ┌──────────────────────────────┐
       │         main.py              │
       │     (Experiment Runner)      │
       └──────────────┬───────────────┘
                      │
            Enter question: "What is X?"
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
   ┌───────────┐            ┌───────────┐
   │ prompt_v1 │            │ prompt_v2 │
   │ "Explain: │            │ Structured│
   │  What is  │            │  template │
   │    X?"    │            │  + format │
   └─────┬─────┘            └─────┬─────┘
         │                        │
         ▼                        ▼
   ┌───────────┐            ┌───────────┐
   │model_runner│           │model_runner│
   │ (same AI)  │           │ (same AI)  │
   └─────┬─────┘            └─────┬─────┘
         │                        │
         ▼                        ▼
    Output V1                Output V2
         │                        │
         └────────────┬───────────┘
                      ▼
              ┌──────────────┐
              │  evaluator   │
              │  .py         │
              │              │
              │ Score both   │
              │ Compare      │
              │ Declare      │
              │ winner       │
              └──────────────┘
```

---

## 💡 Key Takeaways to Emphasize

1. **Prompt Engineering is Testable**
   - Don't guess which prompt is better — measure it
   - V1 vs V2 with controlled variables = scientific approach

2. **The 5 Evaluation Dimensions**
   - Relevance, Completeness, Clarity, Consistency, Hallucination Safety
   - These map to content quality, presentation quality, and trustworthiness

3. **Manual Evaluation is the Foundation**
   - Even Google and OpenAI use human evaluators
   - Automated evaluation (LLM-as-judge) is built ON TOP of manual baselines

4. **Prompt Versioning = Code Versioning**
   - Treat prompts like code: version them, test them, measure them
   - Never change a production prompt without A/B testing

5. **The Full Day 1 Journey**
   - Module 1: How to make AI **creative** (personas)
   - Module 2: How to make AI **structured** (templates)
   - Module 3: How to **architect** AI systems (pipeline)
   - Module 4: How to **prove** AI quality (evaluation)

---

## 🎯 Live Demo Script

1. Run the experiment:
   ```
   python main.py
   ```
2. Enter question: `"What is gradient descent?"`
3. **Wait for both outputs to appear** — show them side by side
4. Point out the differences:
   > "V1 might give a decent answer, but look at V2 — it has clear sections, examples, and use cases. Structure matters."
5. Score V1 first (be honest — probably 2–3 on structure, maybe 4 on relevance)
6. Score V2 next (probably 4–5 across the board)
7. Show the comparison result

> **Point to make:** "We just **proved** with data that a well-engineered prompt outperforms a lazy one. This is how AI teams make decisions — not by gut feeling, but by measured evaluation."

---

## ❓ Anticipated Questions & Answers

**Q: Can the AI evaluate itself instead of manual scoring?**
> "Yes! That's called 'LLM-as-a-judge.' You send the output to another LLM and ask it to score based on a rubric. But manual evaluation is your ground truth — you need it to validate that the auto-evaluator is accurate."

**Q: Isn't manual scoring subjective?**
> "It is, which is why real evaluation uses multiple evaluators and statistical measures like inter-rater agreement (Cohen's Kappa). For our purposes, consistent self-evaluation still reveals clear winners."

**Q: What if V1 scores higher sometimes?**
> "That can happen! Evaluation should be done on MULTIPLE questions, not just one. You'd run 20–50 questions through both prompts and compare aggregate scores. One question is a spot check, not a benchmark."

**Q: How do companies like OpenAI evaluate their models?**
> "They use a combination of: automated benchmarks (MMLU, HumanEval), human evaluation (like what we're doing), adversarial testing (trying to break the model), and real-world A/B tests with users."

---

## 🔄 Day 1 Wrap-Up

> "Let's zoom out and see the journey we've taken today:
>
> | Module | Question Answered | Key Skill |
> |--------|------------------|-----------|
> | 1 | How do I make AI respond in different styles? | Persona-based prompting |
> | 2 | How do I make AI follow a strict format? | Structured/template prompting |
> | 3 | How do I build AI apps like an engineer? | Pipeline architecture |
> | 4 | How do I know if my AI is good? | Evaluation & comparison |
>
> Together, these four modules give you the **complete foundation** for building production AI systems. You can prompt, structure, architect, and evaluate — the four pillars of applied AI engineering."
