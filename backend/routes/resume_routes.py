from fastapi import APIRouter, UploadFile, File
from backend.database import resumes_collection
from backend.services.preprocessing import preprocess
from backend.services.resume_parser import extract_text
from backend.config import MODEL_PATH
import joblib
import os

router = APIRouter()

# Safe model loading
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    print("Warning: Model file not found. Running without classifier.")
    model = None


@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)

    processed = preprocess(text)

    if model:
        prediction = int(model.predict([processed])[0])
    else:
        prediction = None

    resumes_collection.insert_one({
        "resume_text": processed,
        "predicted_label": prediction
    })

    return {
        "message": "Resume uploaded",
        "prediction": prediction,
        "note": "Model not loaded" if model is None else "Prediction successful"
    }
