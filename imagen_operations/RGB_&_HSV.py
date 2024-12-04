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

B, G, R = cv2.split(image)

print(B.shape)
print(G.shape)

imshow('Blue chanel only ', R)

# blank arrays with values of zeros with same image size
print(image.shape[:2])
zeros =  np.zeros(image.shape[:2],dtype="uint8")

# imshow('blank image', zeros)
imshow('Blue', cv2.merge([B, zeros, zeros]))
imshow('Blue', cv2.merge([zeros, G, zeros]))
imshow('Blue', cv2.merge([zeros, zeros, R]))
imshow('all colors', cv2.merge([B,G,R]))

# HSV IS DIFFERENT THE RGB OR BGR INSTEAD OF USING  COMBINATIONS OF RED BLUE AND GREE
# IT USES A COLOR MAP CALLED HUE AND VALUE( INTENSITY) AND SATURATION
# HUE 0-179 SATURATION 0-255 VALUE(INTENSITY) 0-255

hsv_image =  cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
imshow('imagen hsv', hsv_image)
imshow('Hue Color map', hsv_image[:,:,0])
imshow('intensity of color', hsv_image[:, :, 1])
imshow('value of  brightness ', hsv_image[:, :, 2])