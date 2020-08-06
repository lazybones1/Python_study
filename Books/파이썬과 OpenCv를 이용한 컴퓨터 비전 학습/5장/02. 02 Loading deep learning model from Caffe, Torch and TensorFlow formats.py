import cv2
import numpy as np

net_caffe = cv2.dnn.readNetFromCaffe('../data/bvlc_googlenet.prototxt',  '../data/bvlc_googlenet.caffemodel')

net_torch = cv2.dnn.readNetFromTorch('../data/torch_enet_model.net')

net_tensorflow = cv2.dnn.readNetFromTensorflow('../data/tensorflow_inception_graph.pb')
