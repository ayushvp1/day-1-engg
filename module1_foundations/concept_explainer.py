import os
from dotenv import load_dotenv
from litellm import completion
from prompts import SYSTEM_PROMPT, build_prompt

load_dotenv()

def explain(topic, mode):
    user_prompt = build_prompt(topic, mode)

    response = completion(
        model="groq/llama-3.1-8b-instant",  # Change model easily
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    topic = input("Enter topic: ")
    mode = input("Select mode (Shakespeare/Pirate/Bandit): ")

    print("\n--- AI Explanation ---\n")
    print(explain(topic, mode))