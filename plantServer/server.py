import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import cv2
import io
from PIL import Image

from pipeline import predict_from_bgr

app = FastAPI()

# Allow frontend (AR app) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        print("[/predict] received:", file.filename, file.content_type)

        contents = await file.read()
        print("[/predict] bytes:", len(contents))

        image = Image.open(io.BytesIO(contents)).convert("RGB")
        print("[/predict] PIL size:", image.size)

        image_np = np.array(image)
        print("[/predict] np shape:", image_np.shape, "dtype:", image_np.dtype)

        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        score, category = predict_from_bgr(image_bgr)
        print("[/predict] OK score:", score, "category:", category)

        return {"found": True, "severity_score": float(score), "category": category}

    except Exception as e:
        print("[/predict] ERROR:", repr(e))
        return {"found": False, "error": str(e)}
