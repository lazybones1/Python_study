import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img = cv2.putText(img, 'opencv', (10,400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 10)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
