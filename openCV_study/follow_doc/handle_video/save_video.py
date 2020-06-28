import cv2

cap = cv2.VideoCapture('./cat.mp4')

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
