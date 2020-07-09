import cv2

img = cv2.imread('data/Lena.png')
print ('original image shape: ', img.shape)
cv2.imshow('original', img)

width, height = 128, 256
resized_img = cv2.resize(img, (width, height))
print('resized to 128*256 image shape: ', resized_img.shape)
cv2.imshow('resized_img', resized_img)

w_mult, h_mult = 0.25, 0.5
resized_img = cv2.resize(img, (0,0), resized_img, w_mult, h_mult)
print('image shape: ', resized_img.shape)
cv2.imshow('resized_img2', resized_img)

w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0,0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print('half sized image shape: ', resized_img.shape)
cv2.imshow('half sized', resized_img)

img_flip_along_x = cv2.flip(img, 0)
cv2.imshow('img_flip_along_x', resized_img)

img_flip_along_y = cv2.flip(img, 1)
cv2.imshow('img_flip_along_y', resized_img)

img_flip_along_y = cv2.flip(img, -1)
cv2.imshow('img_flip_along_y', resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
