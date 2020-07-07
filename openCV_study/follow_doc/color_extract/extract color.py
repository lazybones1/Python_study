import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

while(1):
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_black = np.array([0, 0, 0])
        upper_black = np.array([100,100,100])

        mask = cv2.inRange(hsv, lower_black, upper_black)

        res = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    if cv2.waitKey(1) % 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
