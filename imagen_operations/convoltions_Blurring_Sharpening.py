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


image =  cv2.imread('img/download.jpg')
imshow('Original', image)

#Kernels
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# applying
blurred = cv2.filter2D(image, -1, kernel_3x3)
imshow('blured', blurred)

# blur method with open cv
blur = cv2.blur(image, (5,5))
imshow('averaging blur', blur)

gaussian = cv2.GaussianBlur(image, (5,5),0)
imshow('Gaussian blur',gaussian)

median =  cv2.medianBlur(image, 5)
imshow('median blur', median)

# bilateral Filter
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
imshow('bilateral', image)

# de-noising
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
imshow('fastNlMeansDenoisingColored',dst)

#sharping
kernel_sharp = np.array([[-1,-1,-1],
                        [-1,9,-1],
                        [-1,-1,-1]])

sharpened = cv2.filter2D(image,-1, kernel_sharp)
imshow('sharpened', sharpened)
