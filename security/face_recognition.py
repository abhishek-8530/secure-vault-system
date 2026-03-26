import face_recognition
import cv2

def is_authorized(frame, known_face_encoding):
    rgb = frame[:, :, ::-1]
    faces = face_recognition.face_encodings(rgb)

    for face in faces:
        match = face_recognition.compare_faces([known_face_encoding], face)
        if True in match:
            return True

    return False