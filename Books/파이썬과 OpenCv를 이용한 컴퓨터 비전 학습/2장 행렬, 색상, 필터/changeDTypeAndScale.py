import cv2
import numpy as np

img = cv2.imread('../data/Lena.png')
print('shape:', img.shape)
print('data Type:', img.dtype)
cv2.imshow('image', img)

img = img.astype(np.float32)/255
print('shape:', img.shape)
print('data Type:', img.dtype)
cv2.imshow('image1', img)
cv2.imshow('image2', np.clip(img*2, 0, 1))

cv2.waitKey(0)
cv2.destroyAllWindows()
