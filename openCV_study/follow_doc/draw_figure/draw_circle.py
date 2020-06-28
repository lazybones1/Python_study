import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img = cv2.circle(img, (300,300), 100, (255,255,255), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
