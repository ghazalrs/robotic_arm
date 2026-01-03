import cv2


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
