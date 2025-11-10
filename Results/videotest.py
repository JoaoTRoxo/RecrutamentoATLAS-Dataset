from ultralytics import YOLO
import cv2

model = YOLO("weights/best100epochs32batch.pt") 

video_path = "2711128-uhd_3840_2160_24fps.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("Detecção de Pessoas - YOLO", annotated_frame)
    


cap.release()
cv2.destroyAllWindows()

