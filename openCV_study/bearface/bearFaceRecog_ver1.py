#https://www.youtube.com/watch?v=B4wwEw5Bm-o&list=PL-xmlFOn6TUKlxlh3PIuAzHkJakFlcDvY&index=2

import dlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from glob import glob

detector = dlib.cnn_face_detection_model_v1('./models/bearface_network.dat')
predictor = dlib.shape_predictor('./models/landmarkDetector.dat')

for img_path in glob('./img/*.jpg'):
    img = dlib.load_rgb_image(img_path)
    img_result = img.copy()

    dets = detector(img)
    fig, ax = plt.subplots(1, figsize=(16, 10))

    for det in dets:
        x, y, w, h = det.rect.left(), det.rect.top(), det.rect.width(), det.rect.height()

        rect = patches.Rectangle((x, y), w, h, linewidth=3, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        shape = predictor(img, det.rect)

        for point in shape.parts():
            circle = patches.Circle((point.x, point.y), radius=3, edgecolor='r', facecolor='r')
            ax.add_patch(circle)

    ax.imshow(img_result)
plt.show()
