SYSTEM_PROMPT = """
You are an expert AI educator.
Adapt explanations based on the target audience.
Ensure clarity and correctness.
Avoid hallucinations.
"""

def build_prompt(topic, mode):

    if mode == "technical":
        style = """
        Provide:
        - Precise definition
        - Core working principle
        - Mathematical or architectural insight
        - Real-world application
        """

    elif mode == "beginner":
        style = """
        Provide:
        - Simple explanation
        - Easy example
        - Why it matters
        """

    elif mode == "kid":
        style = """
        Explain using:
        - Very simple words
        - Fun analogy
        - Short sentences
        """

    else:
        raise ValueError("Invalid mode selected.")

    return f"""
    Topic: {topic}

    Audience Mode: {mode}

    Instructions:
    {style}
    """