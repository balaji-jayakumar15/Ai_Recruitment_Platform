from fastapi import APIRouter, UploadFile, File

from app.services.resume_service import save_resume


router = APIRouter(
    prefix="/upload-resume",
    tags=["Resume"]
)


@router.post("/")
async def upload_resume(file: UploadFile = File(...)):

    file_path = save_resume(file)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "file_path": file_path
    }