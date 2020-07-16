import cv2, random
import numpy as np

img = cv2.imread('../data/bw.png', cv2.IMREAD_GRAYSCALE)

contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(color, contours, -1, (0,255,0), 3)

contour = contours[0]
print('Area of contour is %.2f' % cv2.contourArea(contour))
print('Signed area of contour is %.2f' % cv2.contourArea(contour, True))
print('Signed area of contour is %.2f' % cv2.contourArea(contour[::-1], True))

print('Length of closed is %.2f'%cv2.arcLength(contour, True))
print('Length of open contour is %.2f'%cv2.arcLength(contour, False))

hull = cv2.convexHull(contour)
cv2.drawContours(color, [hull], -1, (0,0,255), 3)

print('Convex status of contour is %s'%cv2.isContourConvex(contour))
print('Convex status of its hull is %s'%cv2.isContourConvex(hull))

cv2.namedWindow('contours2')
img2 = np.copy(color)

def trackbar_callback(value):
    global img2
    epsilon = value*cv2.arcLength(contour, True)*0.1/255
    approx = cv2.approxPolyDP(contour, epsilon, True)
    img2 = np.copy(color)
    cv2.drawContours(img2, [approx], -1, (255,0,255), 3)

cv2.createTrackbar('Epsilon', 'contours2', 1, 255, lambda v:trackbar_callback(v))
while True:
    cv2.imshow('contours2', img2)
    key = cv2.waitKey(3)
    if key == 27:
        break

cv2.imshow('contours', color)
cv2.waitKey()
cv2.destroyAllWindows()
