import camera
import cv2

def main():
    cap = camera.init_camera()

    try:
        while True:
            frame_rgb = camera.capture_frame(cap)
            cv2.imshow('Camera Feed', frame_rgb)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
