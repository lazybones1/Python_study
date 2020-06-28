import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img, (10,30), (400,400), (0,255,0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
