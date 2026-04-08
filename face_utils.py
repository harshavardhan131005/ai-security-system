import cv2
import numpy as np

def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.transpose(img, (2, 0, 1)) / 255.0
    return np.array([img])
