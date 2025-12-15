from fastapi import APIRouter, UploadFile, File
import pandas as pd

router = APIRouter()

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df.to_csv("data/lecturers.csv", index=False)
    return {"status": "uploaded"}

