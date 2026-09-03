from pathlib import Path

from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/analyze-resume",
    tags=["Resume Analysis"]
)


@router.post("/")
async def analyze_resume(filename: str):

    file_path = Path("uploads") / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Resume file not found"
        )

    return {
        "message": "Resume received for analysis",
        "filename": filename,
        "status": "ready for analysis"
    }