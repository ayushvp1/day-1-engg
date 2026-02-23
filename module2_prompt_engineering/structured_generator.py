import os
from dotenv import load_dotenv
from litellm import completion
from prompts import SYSTEM_PROMPT, build_prompt

load_dotenv()

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


if __name__ == "__main__":
    question = input("Enter question: ")

    print("\n--- Structured Answer ---\n")
    print(generate_answer(question))