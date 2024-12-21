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

imagen = cv2.imread('img/download.jpg', 0)

#kernel size
kernel = np.ones((5,5), np.uint8)

#erosion
erosion = cv2.erode(imagen, kernel, iterations=1)
imshow('erosion', erosion)

#dilation
dilation = cv2.dilate(imagen, kernel, iterations=1)

#opening good for removing noise
opening = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)
imshow('opening',opening)

#closing good for removing noise
closing = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
imshow('closing',closing)

# EDGEING
canny = cv2.Canny(imagen, 50, 120)
imshow('canny 1', canny)

# wide more edges
canny2 = cv2.Canny(imagen, 10, 200)
imshow('canny 2', canny2)

#narrow less edges
canny3 = cv2.Canny(imagen, 200, 240)
imshow('canny 3', canny3)

canny4 = cv2.Canny(imagen, 60, 110)
imshow('canny 4', canny4)

