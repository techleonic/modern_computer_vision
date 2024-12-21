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

# load as a grey scale
image = cv2.imread('img/download.jpg', 0)
imshow( 'gray', image)


#create a imge of one
M = np.ones(image.shape, dtype='uint8')
imshow('imagen of ones', M)

# increase brithness
added =  cv2.add(image, M)
imshow('Brithness', added)

#using simple add will clipped the imagen
add= image + M
imshow('clipping',add)

#substrac
substrac = cv2.subtract(image, M)
imshow('substrac', substrac)


#making a square
square = np.zeros((300, 300 ), np.uint8)
cv2.rectangle(square, (50,50) ,(250,250), 255, -2)
imshow('square', square)

# making a ellipse
ellipse_img=  np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse_img, (150, 150),(150,150), 30,0,180,255,-1)
imshow('ellipse', ellipse_img)

# image bitwise operation
And = cv2.bitwise_and(square, ellipse_img)
imshow('And',image=And)

Xor = cv2.bitwise_xor(square, ellipse_img)
imshow('XOR',image=Xor)

Not = cv2.bitwise_not(square)
imshow(title='not square', image=Not)

