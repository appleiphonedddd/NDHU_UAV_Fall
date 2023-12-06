import cv2
import datetime

def capture_and_save(camera_index, folder_path, photo_number):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Can't turn on camera {camera_index}")
        return

    ret, frame = cap.read()
    if ret:
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add timestamp text to frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, timestamp, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        file_name = f"{folder_path}/camera_{camera_index}_{photo_number}.png"
        cv2.imwrite(file_name, frame)  # save picture
    else:
        print(f"Can't read data from {camera_index}")

    cap.release()

cameras = {
    1: 'camera1',
    2: 'camera2',
    3: 'camera3',
    4: 'camera4'  
}

photo_counts = {1: 0, 2: 0, 3: 0, 4: 0}  # initialize photo counts for each camera

number_of_photos_per_camera = 7 # Set the number of photos you want to take for each camera

for _ in range(number_of_photos_per_camera):
    for index, folder in cameras.items():
        photo_counts[index] += 1
        capture_and_save(index, folder, photo_counts[index])

cv2.destroyAllWindows()
