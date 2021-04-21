import cv2
import time
import os

# image 폴더가 없으면 만든다.
if 'images' not in os.listdir('.'):
    os.mkdir('images')

for file in os.listdir('videos'):
    filename, ext = file.split(".")
    if ext != 'mp4':
        continue
    video_path = os.path.join('videos', file)
    image_path = os.path.join('images', filename)
    # images 폴더 안에 filename 폴더가 없으면 만든다
    if filename not in os.listdir('images'):
        os.mkdir(image_path)

    cap = cv2.VideoCapture(video_path)
    start_time = time.time()
    prev = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # 코드 실행 시간으로 1초마다 이미지를 저장하게 하였음
            duration = int(time.time() - start_time)
            if prev != duration:
                filename = 'image' + str(duration).zfill(5) + '.jpg'
                cv2.imwrite(os.path.join(image_path, filename), frame)
                prev = duration
                print("saved image: ", filename)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
