import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

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

    return{
        "filename": file.filename,
        "message" : "upload file successfull"
    }
