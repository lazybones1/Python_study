import cv2
import numpy as np

img = cv2.imread('./bird.png', cv2.IMREAD_GRAYSCALE)

print(img.shape)
print(img.size)
print(img.dtype)
