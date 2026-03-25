# Plant Health Recognition with AR (AR.js & MindAR)

## Project Overview
This project was developed for a AFC course and combines Augmented Reality (AR) with a plant health recognition model.

The system allows a user to scan a plant leaf using a mobile device camera through a web-based AR interface. The system captures a region of the leaf, sends the image to a backend server, and returns the plant health prediction, which is then displayed in the AR interface.

Since we didn't use a real leaf we also put the sample.jpg to test the project.

The project consists of three main parts:
1. Backend server (plant health prediction model)
2. MindAR frontend
3. AR.js frontend

---

## Project Structure
project
├── plantServer
│   ├── server.py
│   ├── predict.py
│   ├── requirements.txt
│   └── README.md
│
├── MindAR
│   ├── main.html
│   ├── targets.mind
│   └── README.md
│
├── ARjs
│   ├── index.html
│   └── README.md
│
└── README.md

---

## System Workflow
The overall system pipeline works as follows:

1. The user opens the AR webpage on a phone or computer.
2. The camera opens and detects the target image / marker.
3. The user selects or scans a leaf region.
4. The frontend captures the Region of Interest (ROI).
5. The captured image is sent to the backend server.
6. The backend runs the plant health recognition model.
7. The backend returns the prediction result.
8. The result is displayed in the AR interface.

Pipeline summary:
Camera → AR (MindAR / AR.js) → ROI Capture → Backend Server → Prediction → Result Display

---

## Running the Whole Project
We developed seperate ReadMe files for each folder to explain how to set them up and how they work.
---

## Technologies Used
- Computer Vision
- FastAPI (Backend)
- Machine Learning Model
- MindAR (Web Augmented Reality)
- AR.js (Web Augmented Reality)
- JavaScript / HTML
- Python
- OpenCV / NumPy / ML libraries

---

## Notes
- The backend server must be running before starting the AR frontend.
- HTTPS is required for camera access on smartphones.
- Replace [your_ip] with your computer's local IP address.
- MindAR and AR.js provide two different AR implementations for the same backend system.

---

## Project Purpose
The goal of this project was to combine Computer Vision, Machine Learning, and Web Augmented Reality to create an interactive system for plant health recognition directly from a mobile browser without installing a mobile application.
