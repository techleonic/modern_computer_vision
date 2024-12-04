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

image = cv2.imread('img/download.jpg')
height, width= image.shape[:2]

imshow('',image)
rotation = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
image_flip = cv2.warpAffine(image, rotation,(width, height) )
imshow('rotated image', image_flip)

# another way of rotated
rotated_image = cv2.transpose(image)
imshow('rotated with transpose' , rotated_image)

#flip imagen
flip_imagen = cv2.flip(image, 1)
imshow('flipped image', flip_imagen)