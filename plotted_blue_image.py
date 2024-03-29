import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    Canny = cv2.Canny(blur, 50,150)
    return Canny


image = cv2.imread("test_image.jpg")
lane_image = np.copy(image)
canny = canny(lane_image)
plt.imshow(canny)
plt.show()
