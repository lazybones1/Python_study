import cv2

cap = cv2.VideoCapture(0)
frame_wdith = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame width: ', frame_wdith)
print('Frame height: ', frame_height)

video = cv2.VideoWriter('data/captured_video.avi', cv2.VideoWriter_fourcc(*'X264'), 25, (frame_wdith, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print('Can\'t get frame')
        break
    video.write(frame)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed Esc')
        break

cap.release()
video.release()
cv2.destroyAllWindows()
