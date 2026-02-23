# 🏗 Module 3 — LLM Application Architecture

This module focuses on designing a modular LLM application pipeline using clean software engineering principles.

Instead of writing everything in one file, we separate responsibilities into layers — similar to real-world AI systems.

---

## 🎯 Objective

Build a structured LLM pipeline:

User Input → Prompt Layer → LLM Layer → Post-Processing → Output

---

## 🧠 Concepts Covered

- Modular AI system design
- Separation of concerns
- Prompt abstraction layer
- Model invocation layer
- Post-processing layer
- Production-style architecture

---

## 📂 Project Structure

module3_architecture/

- input_layer.py
- prompt_layer.py
- llm_layer.py
- post_processing.py
- pipeline.py
- requirements.txt
- .env.example

---

## 🏗 Architecture Overview

1️⃣ Input Layer  
Handles user interaction.

2️⃣ Prompt Layer  
Builds structured prompts.

3️⃣ LLM Layer  
Sends request to Groq via LiteLLM.

4️⃣ Post Processing  
Cleans and formats output.

5️⃣ Pipeline  
Orchestrates the entire workflow.

---

## ⚙ Installation

### 1. Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate
---

### 2. Install Dependencies


pip install -r requirements.txt


---

### 3. Add Environment Variables

Create a `.env` file:


GROQ_API_KEY=your_key_here
MODEL_NAME=groq/llama-3.1-8b-instant


Do NOT upload `.env` to GitHub.

---

## ▶ Run the Project


python pipeline.py


---

## 🎓 Learning Outcome

After completing this module, students will:

- Understand AI workflow design
- Build modular LLM systems
- Separate prompt logic from model logic
- Design scalable GenAI applications

---

## 🚀 Why This Matters

Real-world AI systems are NOT single scripts.

They are modular pipelines with:
- Input validation
- Prompt engineering
- Model abstraction
- Output processing

This module builds that engineering mindset.