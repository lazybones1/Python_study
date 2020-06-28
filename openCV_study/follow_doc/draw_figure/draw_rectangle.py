import cv2
import numpy as np

img = np.zeros((512,512, 3), np.uint8)
img = cv2.rectangle(img, (120, 120), (300,300), (0,0,255), 5)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
