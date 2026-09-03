from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


class Job(BaseModel):
    title: str
    description: str
    required_skills: List[str]
    experience_required: int


jobs = []


@router.post("/")
def create_job(job: Job):
    job_data = job.model_dump()

    job_data["id"] = len(jobs) + 1

    jobs.append(job_data)

    return {
        "message": "Job created successfully",
        "job": job_data
    }


@router.get("/")
def get_jobs():
    return {
        "count": len(jobs),
        "jobs": jobs
    }