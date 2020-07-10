import cv2
import numpy as np

mat = np.random.rand(100,100).astype(np.float32)
print('shape:', mat.shape)
print('data type:', mat.dtype)

np.savetxt('data/mat.csv', mat)

mat = np.loadtxt('data/mat.csv').astype(np.float32)
print('shape:', mat.shape)
print('data type:', mat.dtype)
