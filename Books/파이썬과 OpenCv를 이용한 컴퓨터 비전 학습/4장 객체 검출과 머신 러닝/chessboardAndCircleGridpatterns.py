import cv2
import matplotlib.pyplot as plt

image_chess = cv2.imread('../data/chessboard.png')

found, corners = cv2.findChessboardCorners(image_chess, (6,9))
assert found == True, "can't find chessboard pattern"

dbg_image_chess = image_chess.copy();
cv2.drawChessboardCorners(dbg_image_chess, (6, 9), corners, found)
"""
plt.figure(figsize=(8,4))
plt.subplot(121)
plt.title('original')
plt.axis('off')
plt.imshow(image_chess)

plt.subplot(122)
plt.title('detected pattern')
plt.axis('off')
plt.imshow(dbg_image_chess)
plt.show()
"""

image_circles = cv2.imread('../data/circlesgrid.png')
found, corners = cv2.findCirclesGrid(image_circles, (6,6), cv2.CALIB_CB_SYMMETRIC_GRID)
assert found == True, "can't find circles grid pattern"
dbg_image_circles = image_circles.copy();
cv2.drawChessboardCorners(dbg_image_circles, (6, 6), corners, found)

plt.figure(figsize=(8,8))
plt.subplot(221)
plt.title('original')
plt.axis('off')
plt.imshow(image_chess)

plt.subplot(222)
plt.title('detected pattern')
plt.axis('off')
plt.imshow(dbg_image_chess)

plt.subplot(223)
plt.title('original')
plt.axis('off')
plt.imshow(image_circles)

plt.subplot(224)
plt.title('detected pattern')
plt.axis('off')
plt.imshow(dbg_image_circles)
plt.tight_layout()
plt.show()
