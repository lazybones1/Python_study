import cv2
import numpy as np

img = cv2.imread('./bird.png')

px = img[100, 200]
print (px)

b = img[100, 200, 0]
print(b)

r = img[100, 200, 2]
print(r)

img[100,200] = [0,0,255]

print(img.item(10,10,2))
img.itemset((10,10,2), 100)
print(img.item(10,10,2))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
