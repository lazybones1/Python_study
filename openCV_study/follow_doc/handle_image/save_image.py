import cv2

img = cv2.imread('./bird.PNG', cv2.IMREAD_GRAYSCALE)
cv2.imshow('bird', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindow()
elif k == ord('s'):
    cv2.imwrite('graybird.png', img)
    cv2.destroyAllWindow()
