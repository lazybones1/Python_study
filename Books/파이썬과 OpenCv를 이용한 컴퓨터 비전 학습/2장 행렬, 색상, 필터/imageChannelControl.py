import cv2
import numpy as np

image = cv2.imread('../data/Lena.png').astype(np.float32)/255
print('shape:', image.shape)

image[:,:,[0,2]] = image[:,:,[2,0]] #BGR2RGB
cv2.imshow('img1', image)

image[:,:,[0,2]] = image[:,:,[2,0]] #RGB2BGR
image[:,:,0] = (image[:,:,0]*0.9).clip(0,1)
cv2.imshow('img2', image)
image[:,:,1] = (image[:,:,1]*1.1).clip(0,1)
cv2.imshow('img3', image)

img = np.full((512,512,3), (255,0,0), np.uint8)
cv2.imshow('test1', img)

img[:,:,0] = (img[:,:,0]).clip(0,1)
cv2.imshow('result1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
