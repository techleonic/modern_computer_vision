import cv2
from matplotlib import pyplot as plt
import numpy as np

def imshow(title="image", image = None, size = 10):
    w, h = image.shape[0] , image.shape[1]
    aspec_ratio = w/h
    plt.figure(figsize=(size * aspec_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

# load image
image =  cv2.imread('img/download.jpg')
imshow('Original', image)

#calculate de shift cuarder of the height in x same on y
height, width = image.shape[:2]
quarter_height, quarter_width = height/4, width/4

T = np.float32([[1, 0, quarter_width],[0, 1, quarter_height]])
img_translation = cv2.warpAffine(image, T, (width, height))
imshow('Translation', img_translation)