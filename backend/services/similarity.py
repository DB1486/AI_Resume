from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(tfidf_model, resume_text, job_text):
    resume_vec = tfidf_model.named_steps["tfidf"].transform([resume_text])
    job_vec = tfidf_model.named_steps["tfidf"].transform([job_text])

    score = cosine_similarity(resume_vec, job_vec)[0][0]
    return float(round(score, 4))