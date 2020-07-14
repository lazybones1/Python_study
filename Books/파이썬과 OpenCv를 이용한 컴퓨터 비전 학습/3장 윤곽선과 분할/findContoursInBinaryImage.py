import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../data/BnW.png', 0)

contours, hierarchy = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

image_external = np.zeros(image.shape, image.dtype)
print(len(contours))
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(image_external, contours, i, 255, -1)

image_interanl = np.zeros(image.shape, image.dtype)
for i in range(len(contours)):
    if hierarchy[0][i][3] != -1:
        cv2.drawContours(image_interanl, contours, i, 255, -1)

plt.figure()
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap = 'gray')

plt.subplot(132)
plt.axis('off')
plt.title('image_external')
plt.imshow(image_external, cmap = 'gray')

plt.subplot(133)
plt.axis('off')
plt.title('image_interanl')
plt.imshow(image_interanl, cmap = 'gray')

plt.tight_layout()
plt.show()
