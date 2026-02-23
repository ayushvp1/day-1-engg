from evaluation_metrics import manual_score

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