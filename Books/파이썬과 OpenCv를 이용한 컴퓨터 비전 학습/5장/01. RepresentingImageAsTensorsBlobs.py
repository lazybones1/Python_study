import cv2
import numpy as np

image_bgr = cv2.imread('../data/Lena.png', cv2.IMREAD_COLOR)

image_bgr_float = image_bgr.astype(np.float32)
image_rgb = image_bgr_float[::-1]
tensor_chw = np.transpose(image_rgb, (2, 0, 1))
tensor_nchw = tensor_chw[np.newaxis]

print(image_bgr.shape)
print(image_bgr_float.shape)
print(image_rgb.shape)
print(tensor_chw.shape)
print(tensor_nchw.shape)

cv2.waitKey(0);
cv2.destroyAllWindows();
