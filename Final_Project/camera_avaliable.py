import cv2

def list_available_cameras(max_index):
    available_cameras = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        
        # If camera can be open
        if cap.isOpened():
            available_cameras.append(i) # Append to the array
            cap.release()               # Release camera then handle next
    return available_cameras

max_camera_index = 10
available_cameras = list_available_cameras(max_camera_index)

# Print available camera on PC
print("Available Cameras:", available_cameras)
