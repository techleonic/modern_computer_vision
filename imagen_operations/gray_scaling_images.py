import cv2
from matplotlib import pyplot as plt

def imshow(title="image", image = None, size = 10):
    w, h = image.shape[0] , image.shape[1]
    aspec_ratio = w/h
    plt.figure(figsize=(size * aspec_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('img/download.jpg')
# imshow('flowers',image, size=2)

gray_image =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imshow('gray flowers', gray_image)

