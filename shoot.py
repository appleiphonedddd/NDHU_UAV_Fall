import cv2

def capture_and_save(camera_index, folder_path):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"cant turn on camera {camera_index}")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'{folder_path}/camera_{camera_index}.png', frame)  # save picture
    else:
        print(f"cant from {camera_index} read data")

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



