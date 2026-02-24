from fastapi import APIRouter
from backend.database import resumes_collection, jobs_collection
from backend.services.similarity import compute_similarity
from backend.services.ranking import rank_candidates
from backend.config import MODEL_PATH
import joblib

router = APIRouter()

model = joblib.load(MODEL_PATH)

@router.post("/submit_job")
async def submit_job(job_description: str):
    jobs_collection.insert_one({"job_description": job_description})

    resumes = list(resumes_collection.find())

    results = []

    for resume in resumes:
        sim = compute_similarity(model, resume["resume_text"], job_description)
        results.append({
            "resume_text": resume["resume_text"],
            "similarity": sim
        })

    ranked = rank_candidates(results)

    return {"ranked_candidates": ranked}