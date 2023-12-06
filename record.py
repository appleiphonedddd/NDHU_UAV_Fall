import cv2
import os
import datetime

def capture_and_save(camera_index, folder_path):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Initialize camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Can't turn on camera {camera_index}")
        return

    # Capture frame
    ret, frame = cap.read()
    if ret:
        # Use timestamp for unique filenames
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{folder_path}/camera_{camera_index}_{timestamp}.png"
        cv2.imwrite(filename, frame)  # save picture
        print(f"Image saved to {filename}")
    else:
        print(f"Can't read data from camera {camera_index}")

    # Release camera
    cap.release()

cameras = {
    1: 'camera1',
    2: 'camera2',
    3: 'camera3',
    4: 'camera4'  
}

for index, folder in cameras.items():
    capture_and_save(index, folder)

cv2.destroyAllWindows()
