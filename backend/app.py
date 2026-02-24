from fastapi import FastAPI
from backend.routes import resume_routes, job_routes
app = FastAPI()

app.include_router(resume_routes.router)
app.include_router(job_routes.router)