def skill_gap_analysis(resume_text, jd_text, extractor):
    resume_skills = set(extractor(resume_text))
    jd_skills = set(extractor(jd_text))
    missing_skills = jd_skills - resume_skills
    matching_skills = jd_skills.intersection(resume_skills)
    if len(jd_skills) == 0:
        match_score = 0
    else:
        match_score = len(matching_skills) / len(jd_skills)
    return {
        "resume_skills": list(resume_skills),
        "jd_skills": list(jd_skills),
        "missing_skills": list(missing_skills),
        "matching_skills": list(matching_skills),
        "skill_match_score": round(match_score, 3)
    }