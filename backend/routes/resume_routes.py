from fastapi import APIRouter, UploadFile, File
from backend.database import resumes_collection
from backend.services.preprocessing import preprocess
from backend.services.resume_parser import extract_text
from backend.config import MODEL_PATH
import joblib

router = APIRouter()

model = joblib.load(MODEL_PATH)

@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)

    processed = preprocess(text)
    prediction = int(model.predict([processed])[0])

    resumes_collection.insert_one({
        "resume_text": processed,
        "predicted_label": prediction
    })

    return {"message": "Resume uploaded", "prediction": prediction}