import cv2

cap = cv2.VideoCapture('data/cat.mp4')

while True:
    has_frame, frame = cap.read()
    if not has_frame:
        print('Reached the end of the video')
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(50)
    if key == 27:
        print('Pressed Esc')
        break

cv2.destroyAllWindows()
