# Backend - Plant Health Recognition API

This folder contains the **Python backend** for the project. It provides a simple API that receives a leaf image, runs the plant-health analysis pipeline, and returns a **severity score** together with a **severity category**.

The backend is designed to be used by the AR front end, but it can also be tested independently with local images or API tools such as Postman.

---

## Overview

The backend has two main responsibilities:

1. **Expose an HTTP API** for image-based prediction.
2. **Run the leaf analysis pipeline** that estimates disease severity from the uploaded image.

The current API includes one main endpoint:

- `POST /predict` — accepts an image file and returns the prediction result.

---

## How the Backend Works

When an image is uploaded to the server, the backend performs the following steps:

1. Reads the uploaded image.
2. Converts it into an OpenCV-compatible format.
3. Preprocesses the leaf image to isolate the leaf region.
4. Segments possible lesion or infected areas.
5. Extracts handcrafted image features.
6. Loads the trained regression model.
7. Predicts a numerical severity score.
8. Converts that score into a severity label.
9. Returns the result as JSON.

The severity categories are:

- **Normal**: score < 25
- **Minor**: 25 <= score < 50
- **Medium**: 50 <= score < 75
- **Serious**: score >= 75

---

## Main Files

### `server.py`
Defines the FastAPI server and the `/predict` endpoint.

### `pipeline.py`
Connects preprocessing, segmentation, feature extraction, and model inference into one reusable prediction function.

### `main.py`
Runs the prediction pipeline locally on a test image without starting the API server.

### `models/leaf_severity_model.pkl`
Saved trained regression model used by the backend during inference.

### `preprocessing/`
Contains leaf preprocessing logic.

### `segmentation/`
Contains lesion segmentation logic.

### `features/`
Contains handcrafted feature extraction functions.

---

## Project Structure

```text
backend/
├── server.py
├── pipeline.py
├── main.py
├── requirements.txt
├── models/
│   └── leaf_severity_model.pkl
├── preprocessing/
├── segmentation/
├── features/
├── prediction/
├── build_dataset.py
├── train_model.py
└── simulate_infection_spread.py
```

---

## Installation

Create and activate a Python virtual environment, then install the dependencies.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Additional API dependencies

The current `requirements.txt` covers the image-processing and machine-learning pipeline, but the API server also needs these packages:

```bash
pip install fastapi uvicorn python-multipart pillow
```

This is necessary because `server.py` imports FastAPI and Pillow, and file uploads in FastAPI require `python-multipart`.

---

## Running the Backend Server

Start the FastAPI server with:

```bash
uvicorn server:app --reload
```

By default, the server runs at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### `POST /predict`

Uploads a leaf image and returns the predicted severity.

#### Request

- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Field name:** `file`

#### Response

Example successful response:

```json
{
  "found": true,
  "severity_score": 42.73,
  "category": "Minor"
}
```

Example error response:

```json
{
  "found": false,
  "error": "...error message..."
}
```

---

## Example Test with cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@prediction/input/unseen_leaf3.jpg"
```

## Notes for Integration with AR Front End

- CORS is enabled in `server.py`, so the front end can call the backend directly.
- The API accepts image uploads and returns lightweight JSON, which makes it suitable for AR or mobile-connected workflows.
- The backend does not currently handle authentication, database storage, or request history.

---

## Important Notes

- The trained model file must exist at `models/leaf_severity_model.pkl`.
- The prediction result depends on the quality of the uploaded image and whether the leaf is clearly visible.
- The backend currently returns a prediction result or an error message, but it does not yet return intermediate masks or visual debugging outputs through the API.

---


## Summary

This backend acts as the bridge between the AR client and the plant-disease analysis pipeline. It receives an image, runs the trained plant-health recognition workflow, and returns a severity prediction in a simple API format that can be integrated into the larger project.
