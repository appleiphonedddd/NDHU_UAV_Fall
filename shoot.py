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
    6: 'camera1',
    4: 'camera2',
    2: 'camera3',
    0: 'camera4'  
}

for index, folder in cameras.items():
    capture_and_save(index, folder)

cv2.destroyAllWindows()



