def generate_feedback(result):
    feedback = []

    if result["gap_severity"] == "High Skill Gap":
        feedback.append("Significant skill mismatch with job requirements.")
    elif result["gap_severity"] == "Medium Skill Gap":
        feedback.append("Partial skill alignment detected. Improvement recommended.")
    else:
        feedback.append("Strong alignment with required skills.")

    if result["experience_bonus"] == 0:
        feedback.append("Consider clearly mentioning years of experience.")

    for category, score in result["category_scores"].items():
        if score < 0.5:
            feedback.append(f"Improve skills in {category} domain.")

    return feedback