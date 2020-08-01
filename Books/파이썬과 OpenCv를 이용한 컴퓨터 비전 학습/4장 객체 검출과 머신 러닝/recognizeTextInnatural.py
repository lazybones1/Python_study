"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../data/scenetext01.jpg')
det = cv2.text.TextDetectorCNN_create("../data/textbox.prototxt", "../data/TextBoxes_icdar13.caffemodel")

rects, probs = det.detect(img) #error: (-215:Assertion failed) _minSize.size() == _maxSize.size() in function 'cv::dnn::PriorBoxLayerImpl::PriorBoxLayerImpl'

THR = 0.3
for i, r in enumerate(rects):
    if probs[i] > THR:
        cv2.rectangle(img, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), (0, 255, 0), 2)

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(img[:,:,[2,1,0]])
plt.tight_layout()
plt.show()
"""
