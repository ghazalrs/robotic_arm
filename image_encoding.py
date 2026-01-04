import cv2
import base64


def encode_image(frame_rgb, max_size=768, jpeg_quality=85):
    
    h, w = frame_rgb.shape[:2]

    # Resize
    if max(h, w) > max_size:
        if h > w:
            new_h = max_size
            new_w = int(w * (max_size / h))
        else:
            new_w = max_size
            new_h = int(h * (max_size / w))

        frame_rgb = cv2.resize(frame_rgb, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # RGB -> BGR for OpenCV JPEG encoding
    frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    # Encode as JPEG
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]
    success, buffer = cv2.imencode('.jpg', frame_bgr, encode_param)

    if not success:
        raise RuntimeError("Failed to encode image as JPEG")

    # Convert to base64
    image_b64 = base64.b64encode(buffer).decode('utf-8')

    return image_b64
