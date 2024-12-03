import cv2
from matplotlib import pyplot as plt

# version of cv2
print(cv2.__version__)

image = cv2.imread('img/download.jpg')

# open cv uses bgr and matplolib uses rgb
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Flowers")
plt.show()

#write or save image
cv2.imwrite("output.jpg", image)

#heigth width deth
print(image.shape)