import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.file_service import process_file

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    result = process_file(file_path)

    return {
        "filename": file.filename,
        "characters": result["characters"],
        "chunks": result["chunks"],
        "embedding_dimension": result["embedding_dimension"],
        "preview": result["preview"]
    }