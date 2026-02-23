from prompt_versions import prompt_v1, prompt_v2
from model_runner import call_model
from evaluator import compare_outputs

def run_evaluation():

    question = input("Enter question to test: ")

    print("\n--- Generating Output: Prompt V1 ---\n")
    output1 = call_model(prompt_v1(question))
    print(output1)

    print("\n--- Generating Output: Prompt V2 ---\n")
    output2 = call_model(prompt_v2(question))
    print(output2)

    compare_outputs()


if __name__ == "__main__":
    run_evaluation()