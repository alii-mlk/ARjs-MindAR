import cv2
import numpy as np

def preprocess_leaf(image_input, debug=False):
    # Accept path or numpy image
    if isinstance(image_input, str):
        image_bgr = cv2.imread(image_input)
        if image_bgr is None:
            raise FileNotFoundError(f"Image not found: {image_input}")
    else:
        image_bgr = image_input
        if image_bgr is None or not hasattr(image_bgr, "shape"):
            raise ValueError("preprocess_leaf got invalid image array")
    
    if debug:
        cv2.imshow("Original", image_bgr)

    # Convert to HSV and apply broad leaf mask
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    lower_leaf = np.array([15, 30, 30])
    upper_leaf = np.array([100, 255, 255])
    leaf_mask = cv2.inRange(hsv, lower_leaf, upper_leaf)

    # Mask image_bgr
    leaf_only = cv2.bitwise_and(image_bgr, image_bgr, mask=leaf_mask)

    # Grayscale + smoothing
    gray = cv2.cvtColor(leaf_only, cv2.COLOR_BGR2GRAY)
    gray_filtered = cv2.medianBlur(gray, 5)

    if debug:
        cv2.imshow("Leaf Mask", leaf_mask)
        cv2.imshow("Filtered Grayscale", gray_filtered)

    return gray_filtered, leaf_mask
