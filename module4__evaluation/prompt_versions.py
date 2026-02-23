SYSTEM_PROMPT = """
You are an academic AI assistant.
Be precise, structured, and factually correct.
If unsure, say you do not know.
Avoid hallucinating facts.
"""

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