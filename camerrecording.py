import cv2
import os
import datetime

def record_video(camera_index, folder_path, record_duration=10, fps=20.0):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Initialize camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Can't turn on camera {camera_index}")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    video_filename = f"{folder_path}/camera_{camera_index}_{timestamp}.avi"
    out = cv2.VideoWriter(video_filename, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

    start_time = datetime.datetime.now()
    while (datetime.datetime.now() - start_time).seconds < record_duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            print("Frame capture failed")
            break

    # Release everything
    cap.release()
    out.release()
    print(f"Video saved to {video_filename}")

cameras = {
    1: 'camera1',
    2: 'camera2',
    3: 'camera3',
    4: 'camera4'  
}

for index, folder in cameras.items():
    record_video(index, folder, record_duration=30)

cv2.destroyAllWindows()
