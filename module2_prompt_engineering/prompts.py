SYSTEM_PROMPT = """
You are a precise AI tutor.

Rules:
- Always follow the output format strictly.
- Do not add extra sections.
- Keep explanation clear and structured.
- If question is unclear, ask for clarification.
"""

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