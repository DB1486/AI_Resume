from backend.explainability.skill_heatmap import generate_skill_heatmap
from backend.analytics.model_metrics import get_model_metrics
from fastapi import FastAPI
from backend.routes import resume_routes, job_routes
app = FastAPI()

app.include_router(resume_routes.router)
app.include_router(job_routes.router)

@app.post("/skill-heatmap")
def skill_heatmap(data: dict):
    return generate_skill_heatmap(
        data.get("resume_skills", []),
        data.get("jd_skills", [])
    )

@app.get("/model-performance")
def model_performance():
    return get_model_metrics()
