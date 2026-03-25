import cv2
import joblib
import pandas as pd

from preprocessing.preprocess_leaf import preprocess_leaf
from segmentation.auto_threshold import auto_segment_lesions
from features.extract_features import extract_features

MODEL_PATH = "models/leaf_severity_model.pkl"
_model = None

def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def severity_category(score: float) -> str:
    if score < 25:
        return "Normal"
    elif score < 50:
        return "Minor"
    elif score < 75:
        return "Medium"
    else:
        return "Serious"

def predict_from_bgr(image_bgr):
    # Step 1
    gray_filtered, leaf_mask = preprocess_leaf(image_bgr, debug=False)

    # Step 2
    lesion_mask, _ = auto_segment_lesions(gray_filtered, leaf_mask, image_bgr=image_bgr)

    # Step 3
    features = extract_features(image_bgr, gray_filtered, lesion_mask, leaf_mask)
    input_df = pd.DataFrame([features])

    # Step 4-5
    model = get_model()
    score = float(model.predict(input_df)[0])

    return score, severity_category(score)
