# Module 2 - Structured Answer Generator

This project builds a structured response generator using:

- LiteLLM
- Groq API
- Prompt Engineering

## Features
- Controlled output format
- Deterministic prompting
- Production-style prompt separation

## Setup

1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt

3. Add .env file:
   GROQ_API_KEY=your_key_here
   MODEL_NAME=groq/llama-3.1-8b-instant

4. Run:
   python structured_generator.py