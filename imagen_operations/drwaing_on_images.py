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


cv2.imread('img/download.jpg')
# blank image array of black
image = np.zeros((512,512,3), np.uint8)

# greysacale image
imagen_gray =  np.zeros((512,512), np.uint8)

#draw a line
cv2.line(image, (0,0), (512, 512), (255, 255, 255), 5 )
imshow('line ', image)

#create rectangule

cv2.rectangle(image, (100, 100), (300,250), (127,50,127), 10)
imshow('Black Canvas with pick reactahgule', image)


#create a circle -1 to fill the circule
cv2.circle(image, (350, 350), 100, (150, 150, 50), -1)
imshow('circle',image)

#Polygons with points
pts = np.array([[10,50], [400,50], [90,200],[50,500]], np.int32)

#reshape our points
pts = pts.reshape((-1, 1, 2))
print(pts)
cv2.polylines(image, [pts], True, (0,0,255), 3)
imshow('poligon', image)


#add text

string = "HELLO WORLD"
cv2.putText(image, string, (0,200), cv2.FONT_HERSHEY_COMPLEX, 2 , (40, 200,0), 4)
imshow('with text',image)