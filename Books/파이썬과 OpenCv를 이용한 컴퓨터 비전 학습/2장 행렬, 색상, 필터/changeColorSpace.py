import cv2
import numpy as np

image = cv2.imread('../data/Lena.png').astype(np.float32)/255
print('shape:', image.shape)
print('data type', image.dtype)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Convered to grayscale')
print('shape:', gray.shape)
print('data type', gray.dtype)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print('Convered to hsv')
print('shape:', hsv.shape)
print('data type', hsv.dtype)

hsv[:,:,2] *=2
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('Convered back to bgr from hsv')
print('shape:', from_hsv.shape)
print('data type', from_hsv.dtype)

cv2.imshow('image', image)
cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)
cv2.imshow('from_hsv', from_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
