import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not has_frame:
        print('can\'t get frame')
        break
    cv2.imshow('frame', frame)
    ket = cv2.waitKey(3)
    if key == 27:
        print('pressed Esc')
        break

cap.released()
cv2.destroyAllWindows()
