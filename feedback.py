def generate_feedback(skill_gap_result):
    feedback = []
    if skill_gap_result["missing_skills"]:
        feedback.append(
            f"Consider adding experience with: {', '.join(skill_gap_result['missing_skills'])}."
        )
    if skill_gap_result["skill_match_score"] < 0.5:
        feedback.append(
            "Your profile has low alignment with the job role. Consider tailoring your resume."
        )
    if not skill_gap_result["matching_skills"]:
        feedback.append(
            "No strong skill overlap found. Add relevant project experience."
        )
    if not feedback:
        feedback.append("Your resume is well aligned with the job description.")
    return feedback