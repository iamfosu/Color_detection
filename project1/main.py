import cv2
from PIL import Image
from utils import get_limit

cap = cv2.VideoCapture(2)

yellow = [0, 255, 255]   # yellow color in BGR
while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limit(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask1 = Image.fromarray(mask)
    bbox = mask1.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    if not ret:
        print("Failed to read Webcam")
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



