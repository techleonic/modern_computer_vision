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

imshow('normal imagen', image)

# downscale for 75%
imagen_resize = cv2.resize(image, None ,fx=0.25, fy=0.25)
imshow('resized', imagen_resize)

imagen_scaled1 = cv2.resize(image, None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)
imshow('scaled 1', imagen_scaled1)

imagen_scaled2 = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
imshow('scale 2', imagen_scaled2)

imagen_scaled3 = cv2.resize(image, (920, 560), interpolation=cv2.INTER_NEAREST)
imshow('scale 3', imagen_scaled3)

# using piramid
small_img = cv2.pyrDown(image)
large_img = cv2.pyrUp(image)

imshow('small',small_img)
imshow('large', large_img)


# croppig de center
start_row ,start_column = int(height * .25) , int(width * .25)
end_row ,end_column  = int(height * .75), int( width * .75)
cv2.rectangle(image, (start_column,start_row),(end_column,end_row),(0,255,255),1)
imshow('rectangle', image)
imshow('cropped', image[start_row:end_row, start_column:end_column])
