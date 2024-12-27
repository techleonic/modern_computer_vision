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

imagen = cv2.imread('white_black.jpg')
gray_imagen =  cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imshow("letters", imagen)

_ , th1 =  cv2.threshold(gray_imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
imshow('gray thresh', th1)
"""
HOW TO USE cv2.findContours:
```cv2.findContours(image, Retrieval Mode, Approximation Method)```

**Retrieval Modes**
- **RETR_LIST** - Retrieves all the contours, but doesn't create any parent-child relationship. Parents and kids are equal under this rule, and they are just contours. ie they all belongs to same hierarchy level.
- **RETR_EXTERNAL** - eturns only extreme outer flags. All child contours are left behind.
- **RETR_CCOMP** - This flag retrieves all the contours and arranges them to a 2-level hierarchy. ie external contours of the object (ie its boundary) are placed in hierarchy-1. And the contours of holes inside object (if any) is placed in hierarchy-2. If any object inside it, its contour is placed again in hierarchy-1 only. And its hole in hierarchy-2 and so on.
- **RETR_TREE** -  It retrieves all the contours and creates a full family hierarchy list.

**Approximation Method Options**
- cv2.CHAIN_APPROX_NONE – Stores all the points along the line(inefficient!)
- cv2.CHAIN_APPROX_SIMPLE – Stores the end points of each line
"""
contours, hierarchy = cv2.findContours(th1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# Draw all contours, note this overwrites the input image (inplace operation)
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(imagen, contours, -1, (0,255,0), thickness=2)
imshow("Contours over original imagen", imagen)
print("numbers of contours found = " + str(len(contours)))