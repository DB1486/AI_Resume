def generate_skill_heatmap(resume_skills, jd_skills):
    resume_set = set(skill.lower().strip() for skill in resume_skills)
    jd_set = set(skill.lower().strip() for skill in jd_skills)

    matched = list(resume_set & jd_set)
    missing = list(jd_set - resume_set)
    extra = list(resume_set - jd_set)

    match_percentage = round((len(matched) / len(jd_set)) * 100, 2) if jd_set else 0.0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
        "match_percentage": match_percentage
    }
