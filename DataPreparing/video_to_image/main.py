import cv2
import time
import os

os.chdir('video_to_image')
video_path_list = []
video_folder = 'videos'
if 'images' not in os.listdir('.'):
    os.mkdir('images')

for file in os.listdir('videos'):
    filename, ext = file.split(".")
    if ext != 'mp4':
        continue
    video_path = os.path.join('videos', file)
    image_path = os.path.join('images', filename)
    if filename not in os.listdir('images'):
        os.mkdir(image_path)
    cap = cv2.VideoCapture(video_path)
    start_time = time.time()

    prev = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            duration = int(time.time() - start_time)
            if prev != duration:
                filename = 'image'+str(duration).zfill(5)+'.jpg'
                # print(os.path.join(image_path, 'image'+str(duration).zfill(5) + '.jpg'), frame)
                cv2.imwrite(os.path.join(image_path, filename), frame)
                prev = duration
                print("saved image: ", filename)
            # cv2.imshow('videos', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    # cv2.destroyAllWindows()
