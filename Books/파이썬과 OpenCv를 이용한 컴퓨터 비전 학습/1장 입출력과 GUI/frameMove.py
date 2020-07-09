import cv2

cap = cv2.VideoCapture('data/cat.mp4')
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_count: ', frame_count)

print('position: ', int(cap.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = cap.read()
cv2.imshow('frame0', frame)

print('position: ', cap.get(cv2.CAP_PROP_POS_FRAMES))
_, frame = cap.read()
cv2.imshow('frame1', frame)

cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
print('position: ', int(cap.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = cap.read()
cv2.imshow('frame100', frame)

cv2.waitKey()
cv2.destroyAllWindows()
