# Our Setup, Import Libaries, Create our Imshow Function and Download our Images
import cv2
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

# Load our image
image = cv2.imread('shapes.png')
imshow('Original Image', image)

def find_contours(image):
    # Grayscale our image
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Find Canny edges
    edged = cv2.Canny(gray, 50, 200)
    imshow('Canny Edges', edged)

    # Find contours and print how many were found
    contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("Number of contours found = ", len(contours))

    # Draw all contours over blank image
    cv2.drawContours(image, contours, -1, (0,255,0), 3)
    imshow('All Contours', image)

    def get_contour_areas(contours):
        """returns the areas of all contours as list"""
        all_areas = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            all_areas.append(area)
        return all_areas


    # Load our image
    image = cv2.imread('shapes.png')

    # Let's print the areas of the contours before sorting
    print("Contor Areas before sorting...")
    print(get_contour_areas(contours))

    # Sort contours large to small by area
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

    print("Contor Areas after sorting...")
    print(get_contour_areas(sorted_contours))

    # Iterate over our contours and draw one at a time
    for (i, c) in enumerate(sorted_contours):
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(image, str(i + 1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.drawContours(image, [c], -1, (255, 0, 0), 3)

    imshow('Contours by area', image)

find_contours(image)

