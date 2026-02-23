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
    gap_result = skill_gap_analysis(cleaned_resume, job_description, extract_skills)
    print("Skill Gap Result:", gap_result)
    sim_score = semantic_similarity(cleaned_resume, job_description)
    print("Semantic Similarity Score:", sim_score)
    feedback_result = generate_feedback(gap_result)
    print("Feedback:", feedback_result)
X = resumes["text"]
y = resumes["label"]
results = compare_models(X, y)
print("\nModel Performance:")
print(results)