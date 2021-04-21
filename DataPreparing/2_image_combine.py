import os
import shutil

# images 폴더에 있는 파일과 video3에 있는 파일들 하나의 폴더에 복사해오기!
folders = os.listdir('images')
print(folders)
if 'total_images' not in os.listdir('.'):
    os.mkdir('total_images')
cnt = 0
for folder in folders:
    for file in os.listdir('images/'+folder):
        print(file)
        new_filename = 'image' + str(cnt).zfill(5) + '.jpg'
        shutil.copy(os.path.join('images', folder, file), os.path.join('total_images', new_filename))
        cnt += 1

print(cnt)
