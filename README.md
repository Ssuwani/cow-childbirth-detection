# Cow Project

**Step**  
1. DataPreparing
    1. Video to Image
    2. Image Combine
    3. Labeling for Object Detection
    4. Labelme to coco format
2. Training
3. Evaluation
4. Appling with realtime video

### DataPreparing

**Video to Image** -> /video_to_image/main.py  
Video를 Image로 변환하기 위함  
각각의 video name으로 images 폴더에 생성됨

**Image Combine** -> /video_to_image/images/filename_match.py  
Video to Image를 통해 변환된 이미지 중 사용할 이미지만 고른 뒤 하나의 폴더에 합침 total_image라는 폴더로 합쳐짐

**Labeling for Object Detection** -> [labelme]('https://github.com/wkentaro/labelme#ubuntu')  
Object Detection을 위한 데이터는 class에 따른 BBox를 알려주는 annotation 파일을 필요로 한다. labelme 를 통해 BBox를 지정하여 각각의 이미지에 json 파일을 생성한다.

**Labelme to coco format** -> [labelme2coco]('https://github.com/fcakyon/labelme2coco')  
또 Object Detection Train을 위한 패키지인 Detectron, MMDetection 모두 Input 데이터 형식으로 coco format을 이용한다. labelme를 통해 만들어진 json 파일을 coco format으로 변경해줄 필요가 있다.


