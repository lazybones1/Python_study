import cv2

orig = cv2.imread('data/Lena.png')
orig_size = orig.shape[0:2]
print(orig_size)

cv2.imshow('original', orig)
cv2.waitKey(0)
cv2.destroyAllWindows()
