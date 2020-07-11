import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../data/Lena.png').astype(np.float32)/255

plt.subplot(2,2,1)
noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0,1)
plt.title('noised')
plt.imshow(noised[:,:,[2,1,0]])

plt.subplot(2,2,2)
guass_blur = cv2.GaussianBlur(noised, (7,7), 0)
plt.title('gaussian')
plt.imshow(guass_blur[:,:,[2,1,0]])

plt.subplot(2,2,3)
median_blur = cv2.medianBlur((noised * 255).astype(np.uint8), 7)
plt.title('median_blur')
plt.imshow(median_blur[:,:,[2,1,0]])

plt.subplot(2,2,4)
bilat = cv2.bilateralFilter(noised, -1, 0.3, 10)
plt.title('bilat')
plt.imshow(bilat[:,:,[2,1,0]])

plt.show()
