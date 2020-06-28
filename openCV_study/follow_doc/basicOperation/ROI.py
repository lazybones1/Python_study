import cv2
import numpy as np

img = cv2.imread('./bird.png')
tmp = img[:60, :20]
img[100:160, :20] = tmp
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
