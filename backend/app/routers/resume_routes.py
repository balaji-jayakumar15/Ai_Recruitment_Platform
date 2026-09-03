from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.resume_service import save_resume


router = APIRouter(
    prefix="/upload-resume",
    tags=["Resume"]
)


ALLOWED_EXTENSIONS = {".pdf", ".doc", ".docx"}


@router.post("/")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOC, and DOCX files are allowed"
        )

    file_path = save_resume(file)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "file_path": file_path
    }