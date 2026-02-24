import pandas as pd
from bias_reduction import remove_bias
from skill_extraction import extract_skills
from skill_gap import skill_gap_analysis
from semantic_matching import semantic_similarity
from feedback import generate_feedback
from model_comparison import compare_models

resumes = pd.read_csv("data/resumes.csv")
jobs = pd.read_csv("data/jobs.csv")

job_description = jobs.iloc[0]["text"]

for index, row in resumes.iterrows():

    print("\n==============================")
    print("Resume ID:", row["resume_id"])

    cleaned_resume = remove_bias(row["text"])

    gap_result = skill_gap_analysis(
        cleaned_resume,
        job_description,
        extract_skills
    )

    print("\n--- Skill Gap Analysis ---")
    print("Resume Skills:", gap_result["resume_skills"])
    print("JD Skills:", gap_result["jd_skills"])
    print("Weighted Skill Score:", gap_result["weighted_skill_score"])
    print("Experience Bonus:", gap_result["experience_bonus"])
    print("Final Skill Score:", gap_result["final_skill_score"])
    print("Category Scores:", gap_result["category_scores"])
    print("Gap Severity:", gap_result["gap_severity"])

    sim_score = semantic_similarity(cleaned_resume, job_description)
    print("\nSemantic Similarity Score:", round(sim_score, 4))

    final_composite_score = (
        0.5 * gap_result["final_skill_score"] +
        0.5 * sim_score
    )

    print("Final Composite Score:", round(final_composite_score, 4))

    feedback_result = generate_feedback(gap_result)
    print("\n--- Feedback ---")
    for item in feedback_result:
        print("-", item)

print("\n==============================")
print("MODEL COMPARISON")

X = resumes["text"]
y = resumes["label"]

results = compare_models(X, y)

print("\nModel Performance:")
for model_name, metrics in results.items():
    print(f"\n{model_name}")
    print("Accuracy:", metrics["accuracy"])
    print("Precision (Class 1):", metrics["1"]["precision"])
    print("Recall (Class 1):", metrics["1"]["recall"])
    print("F1 Score (Class 1):", metrics["1"]["f1-score"])