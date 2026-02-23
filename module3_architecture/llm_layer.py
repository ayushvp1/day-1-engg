import os
from dotenv import load_dotenv
from litellm import completion
from prompt_layer import SYSTEM_PROMPT

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

def call_llm(prompt):
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