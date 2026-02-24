from fastapi import APIRouter
from backend.database import resumes_collection, jobs_collection
from backend.services.similarity import compute_similarity
from backend.services.ranking import rank_candidates
from backend.config import MODEL_PATH
import joblib
import os

router = APIRouter()

# Safe model loading
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    print("Warning: Model file not found in job_routes. Running without classifier.")
    model = None


@router.post("/submit_job")
async def submit_job(job_description: str):
    jobs_collection.insert_one({"job_description": job_description})

    resumes = list(resumes_collection.find())
    results = []

    for resume in resumes:
        if model:
            sim = compute_similarity(model, resume["resume_text"], job_description)
        else:
            # If model is missing, return similarity as 0
            sim = 0.0

        results.append({
            "resume_text": resume["resume_text"],
            "similarity": sim
        })

    ranked = rank_candidates(results)

    return {
        "ranked_candidates": ranked,
        "note": "Model not loaded" if model is None else "Similarity computed"
    }
