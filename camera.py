import cv2
import numpy as np

def init_camera(index=0, width=1280, height=720):
    """
    Initialize the laptop webcam with specified resolution.
    """
    cap = cv2.VideoCapture(index)

    if not cap.isOpened():
        raise RuntimeError(f"Failed to open camera at index {index}")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    return cap

def capture_frame(cap):
    """
    Capture a single frame from the camera and convert to RGB.
    """
    ret, frame_bgr = cap.read()

    if not ret or frame_bgr is None:
        raise RuntimeError("Failed to capture frame from camera.")
    
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

    return frame_rgb
