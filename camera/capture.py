import cv2
import time
import os

def capture_image(store_dir):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        path = os.path.join(store_dir, f"intruder_{timestamp}.jpg")
        cv2.imwrite(path, frame)
        cap.release()
        return path

    cap.release()
    return None


def record_video(store_dir, duration=10):
    cap = cv2.VideoCapture(0)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    video_path = os.path.join(store_dir, f"intruder_{timestamp}.mp4")

    # ✅ Define codec and VideoWriter properly
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))

    start = time.time()

    while int(time.time() - start) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)

    cap.release()
    out.release()

    return video_path