import cv2
import numpy as np

image = np.full((480,640,3), 255, np.uint8)
cv2.imshow('white', image)

image = np.full((480,640,3), (0,0,255), np.uint8)
cv2.imshow('red', image)

"""
image = np.zeros((480,640,3), np.uint8)
"""
image.fill(0)
cv2.imshow('black', image)

image[240, 160] = image[240,320] = image[240, 480] = (255,255,255)
cv2.imshow('black with white pixels', image)

image[:,:,0] = 255
cv2.imshow('blue with white pixels', image)

image[:,320,:] = 255
cv2.imshow('blue with white pixels', image)

image[100:600, 100:200, 2] =255
cv2.imshow('some pixel is red', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
