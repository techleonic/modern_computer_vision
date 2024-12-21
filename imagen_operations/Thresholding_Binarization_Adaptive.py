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

imshow('original', image=imagen)

_, tresh1 = cv2.threshold(imagen, 200, 255, cv2.THRESH_BINARY)
imshow('binary', image=tresh1)

_, tresh2 = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY_INV)
imshow('THRESH_BINARY_INV', image=tresh2)

_, tresh3 = cv2.threshold(imagen, 200, 255, cv2.THRESH_TRUNC)
imshow('THRESH_TRUNC', image=tresh3)

_, tresh4 = cv2.threshold(imagen, 200, 255, cv2.THRESH_TOZERO)
imshow('THRESH_TOZERO', image=tresh4)

_, tresh5 = cv2.threshold(imagen, 200, 255, cv2.THRESH_TOZERO_INV)
imshow('THRESH_TOZERO_INV', image=tresh5)

# ADAPTIVE THRESHOLDING
athres1 = cv2.adaptiveThreshold(imagen, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)

_, athres2 = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imshow('THRESH_OTSU',athres2)

blured = cv2.GaussianBlur(imagen, (5,5), 0)
_, athres3 = cv2.threshold(blured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imshow('GaussianBlur ', athres3)

# threshold local

from skimage.filters import threshold_local
colored_imagen =  cv2.imread('img/download.jpg')
V = cv2.split(cv2.cvtColor(colored_imagen, cv2.COLOR_BGR2HSV))[2]
T = threshold_local(V, 25, offset=15, method='gaussian')

thresh = (V > T).astype("uint8") * 255
imshow("threshold local", thresh)