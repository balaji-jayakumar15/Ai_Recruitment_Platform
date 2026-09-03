from fastapi import FastAPI

from app.routers.job_routes import router as job_router
from app.routers.resume_routes import router as resume_router


app = FastAPI(
    title="AI Recruitment Platform API",
    description="AI-powered recruitment platform",
    version="1.0.0"
)


app.include_router(job_router)
app.include_router(resume_router)


@app.get("/")
def root():
    return {
        "message": "AI Recruitment Platform API is running"
    }