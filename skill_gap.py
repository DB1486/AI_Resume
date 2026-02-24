import re
from skill_config import SKILL_WEIGHTS, SKILL_CATEGORIES, EXPERIENCE_KEYWORDS


def detect_experience_bonus(resume_text):
    bonus = 0
    for phrase in EXPERIENCE_KEYWORDS:
        if phrase in resume_text.lower():
            bonus += 0.05
    return min(bonus, 0.2)  # cap bonus


def categorize_skills(skills):
    category_scores = {}
    for category, skill_list in SKILL_CATEGORIES.items():
        matched = set(skills).intersection(skill_list)
        category_scores[category] = len(matched) / len(skill_list)
    return category_scores


def weighted_skill_score(resume_skills, jd_skills):
    total_weight = 0
    matched_weight = 0

    for skill in jd_skills:
        weight = SKILL_WEIGHTS.get(skill, 1)
        total_weight += weight
        if skill in resume_skills:
            matched_weight += weight

    if total_weight == 0:
        return 0

    return matched_weight / total_weight


def classify_gap(score):
    if score >= 0.75:
        return "Low Skill Gap"
    elif score >= 0.5:
        return "Medium Skill Gap"
    else:
        return "High Skill Gap"


def skill_gap_analysis(resume_text, job_description, extract_skills_func):
    resume_skills = extract_skills_func(resume_text)
    jd_skills = extract_skills_func(job_description)

    weighted_score = weighted_skill_score(resume_skills, jd_skills)
    experience_bonus = detect_experience_bonus(resume_text)

    final_skill_score = min(weighted_score + experience_bonus, 1.0)

    category_scores = categorize_skills(resume_skills)

    severity = classify_gap(final_skill_score)

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "weighted_skill_score": round(weighted_score, 3),
        "experience_bonus": round(experience_bonus, 3),
        "final_skill_score": round(final_skill_score, 3),
        "category_scores": category_scores,
        "gap_severity": severity
    }