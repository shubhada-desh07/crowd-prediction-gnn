from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")


def get_live_detections():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = []

        results = model(frame)

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])

                if cls == 0:  # person
                    x1, y1, x2, y2 = box.xyxy[0]

                    cx = int((x1 + x2) / 2)
                    cy = int((y1 + y2) / 2)

                    detections.append((cx, cy))

                    # draw box
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
                    cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)

        yield detections, frame

        cv2.imshow("Live Crowd Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()