import cv2

def list_available_cameras(max_index):
    available_cameras = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

max_camera_index = 10
available_cameras = list_available_cameras(max_camera_index)
print("Available Cameras:", available_cameras)
