# Our Setup, Import Libaries, Create our Imshow Function and Download our Images
import cv2
import numpy
import numpy as np
from matplotlib import pyplot as plt

# Define our imshow function
def imshow(title = "Image", image = None, size = 16):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image =  cv2.imread('img_1.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w, y+h), (127,0,255), 2)

imshow('Faces',image)