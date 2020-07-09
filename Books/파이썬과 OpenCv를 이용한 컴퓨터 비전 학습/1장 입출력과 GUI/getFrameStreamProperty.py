import cv2
import numpy as np

def print_capture_properties(*args):
    cap = cv2.VideoCapture(*args)
    print('Create capture:', ' '.join(map(str, args)))
    print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame rate:', capture.get(cv2.CAP_PROP_FPS))

print_capture_properties('data/cat.mp4')
print_capture_properties(0)
