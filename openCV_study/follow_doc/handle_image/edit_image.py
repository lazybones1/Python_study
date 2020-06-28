import cv2

img1 = cv2.imread('./bird.PNG', cv2.IMREAD_COLOR)
img2 = cv2.imread('./bird.PNG', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('./bird.PNG', cv2.IMREAD_UNCHANGED)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
