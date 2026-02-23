def manual_score():
    print("\nRate from 1 to 5")

    relevance = int(input("Relevance: "))
    completeness = int(input("Completeness: "))
    clarity = int(input("Clarity: "))
    consistency = int(input("Consistency: "))
    hallucination = int(input("Hallucination Risk (5 = no hallucination): "))

    final_score = (relevance + completeness + clarity + consistency + hallucination) / 5

    return {
        "Relevance": relevance,
        "Completeness": completeness,
        "Clarity": clarity,
        "Consistency": consistency,
        "Hallucination Safety": hallucination,
        "Final Score": final_score
    }