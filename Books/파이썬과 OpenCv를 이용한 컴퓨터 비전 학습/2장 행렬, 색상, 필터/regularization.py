import cv2
import numpy as np

image = cv2.imread('../data/Lena.png').astype(np.float32)/255

image -= image.mean()
cv2.imshow('mean', image)

image /= image.std()
cv2.imshow('std', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
