import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='data/Lena.png', help='Image Path.')
parser.add_argument('--out_png', default='data/Lena_compressed.png', help='output image path for lossless result')
parser.add_argument('--out_jpg', default='data/Lena_compressed.jpg', help='output image path for lossy result')
params = parser.parse_args()

img = cv2.imread('data/Lena.png')
cv2.imwrite('data/Lena_compressed.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

saved_img = cv2.imread(params.out_png)
assert saved_img.all() == img.all()

cv2.imwrite('data/Lena_compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
