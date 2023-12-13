from ultralytics import YOLO
import cv2
import cvzone
import math
import time

# cap = cv2.VideoCapture(1)  #웹캠용
# cap.set(3, 12용)
# cap.set(4, 720)

#cap = cv2.VideoCapture("catvid1.mp4")  # 비디오파일용
cap = cv2.VideoCapture("catvid2.mp4")  # 비디오 파일용
#cap 변수를 적절히 조정해서 웹캠모드/비디오파일모드 토글
model = YOLO("./Yolo-Weights/yolov8n.pt")
# pretrained파일 다운로드해서 폴더에 추가함 혹은 나중에 fine tuned파일 제작완료되면 그걸로 바꿔서 사용
# 만약 custom train 파일이면 yaml참고해서 클래스이름 정의 
#지금은 직접 찍은 고양이 (점례, 중성, 2023/12/13 기준 나이 만 10개월 매탄동에서 엄태곤이랑 거주중) 영상에 기본 yolov8 nano 모델로 동작확인만 
#바운딩 박스에 표시할 클래스이름 리스트에 정의
classNames = ["person", "bicycle", "car", "motorbike", "aerop함lane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

prev_frame_time = 0
new_frame_time = 0
#Object Detection 로
while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # 바운딩박스 그려주는 코드
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1줌
            cvzone.cornerRect(img, (x1, y1, w, h))
            # Confidence (바운딩박스에 추측한 클래스 옆에 그것이 맞을 확률)
            conf = math.ceil((box.conf[0] * 100)) / 100
            # 클래스이름 박스에 호출
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
    #프레임마다 바운딩박스를 그려서 보여주는 구조. 실시간으로 실행하면 느리므로 그땐 nano모델이 좋음 녹화용으론 xl모델이좋음
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
