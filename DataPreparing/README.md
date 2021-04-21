# DataPreparing

[video download](https://drive.google.com/drive/folders/1JMNrVw1mT3RG_oeOvqmBvt9Hy4ftxwVO?usp=sharing)

**Step**

1. Video to Image
2. Image Combine
3. Labeling for Object Detection
4. Labelme to coco format

**Video to Image** -> /video_to_image/main.py  
Video를 Image로 변환하기 위함  
각각의 video name으로 images 폴더에 생성됨

**Image Combine** -> /video_to_image/images/filename_match.py  
Video to Image를 통해 변환된 이미지 중 사용할 이미지만 고른 뒤 하나의 폴더에 합침 total_image라는 폴더로 합쳐짐

**Labeling for Object Detection** -> [labelme](https://github.com/wkentaro/labelme)   
Object Detection을 위한 데이터는 class에 따른 BBox를 알려주는 annotation 파일을 필요로 한다. labelme 를 통해 BBox를 지정하여 각각의 이미지에 json 파일을 생성한다.

**Labelme to coco format** -> [labelme2coco](https://github.com/fcakyon/labelme2coco)  
또 Object Detection Train을 위한 패키지인 Detectron, MMDetection 모두 Input 데이터 형식으로 coco format을 이용한다. labelme를 통해 만들어진 json 파일을 coco format으로 변경해줄 필요가 있다.

### 1. Video to Image

**Execute**

```bash
python 1_video_to_image.py
```

**Before**

```bash
├── 1_video_to_image.py
└── videos
    ├── video1.mp4
    ├── video1.mp4
    └── video2.mp4
```

**After**

```bash
├── 1_video_to_image.py
└── videos
    ├── video1.mp4
    └── video2.mp4
├── images
│   ├── video1
│   │   ├── image00001.jpg
│   │   ├── image00002.jpg
│   │   ├── ---
│   │   └── image00036.jpg
│   └── video2
│       ├── image00001.jpg
│       ├── image00002.jpg
│       ├── --- 
│       └── image00044.jpg

```

---

### 2. Image Combine

바로 위 video_to_image를 통해서 video에서 image를 추출했다. 여기서 필요한 불필요한 이미지를 지운 뒤 하나의 폴더에 전체 이미지를 합친다.

**Execute**

```bash
python 2_image_combine.py
```

**Before**  
video1 폴더에 12개 video2 폴더에 11개의 이미지가 아래와 같이 남았다.

```bash
├── 1_video_to_image.py
├── 2_image_combine.py
├── README.md
├── images
│   ├── video1
│   │   ├── image00001.jpg
│   │   ├── image00019.jpg
│   │   ├── image00020.jpg
│   │   ├── image00022.jpg
│   │   ├── image00023.jpg
│   │   ├── image00025.jpg
│   │   ├── image00026.jpg
│   │   ├── image00027.jpg
│   │   ├── image00028.jpg
│   │   ├── image00032.jpg
│   │   ├── image00033.jpg
│   │   └── image00035.jpg
│   └── video2
│       ├── image00002.jpg
│       ├── image00020.jpg
│       ├── image00022.jpg
│       ├── image00027.jpg
│       ├── image00028.jpg
│       ├── image00029.jpg
│       ├── image00034.jpg
│       ├── image00035.jpg
│       ├── image00037.jpg
│       ├── image00042.jpg
│       └── image00043.jpg
└── videos
    ├── video1.mp4
    └── video2.mp4
```

**After**

```bash
├── 1_video_to_image.py
├── 2_image_combine.py
├── README.md
├── images
│   ├── video1
│   │   ├── image00001.jpg
│   │   ├── image00019.jpg
│   │   ├── ---
│   │   └── image00035.jpg
│   └── video2
│       ├── image00002.jpg
│       ├── image00020.jpg
│       ├── ---
│       └── image00043.jpg
├── total_images
│   ├── image00000.jpg
│   ├── image00001.jpg
│   ├── ---
│   └── image00022.jpg
└── videos
    ├── video1.mp4
    └── video2.mp4

```