import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "soil.png"
image = cv2.imread(image_path)

b, g, r = cv2.split(image)

blank = np.zeros_like(b)

red_image = cv2.merge([blank, blank, r])
green_image = cv2.merge([blank, g, blank])
blue_image = cv2.merge([b, blank, blank])

cv2.imwrite("red.png", red_image)
cv2.imwrite("green.png", green_image)
cv2.imwrite("blue.png", blue_image)


