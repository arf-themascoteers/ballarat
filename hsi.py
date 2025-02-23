import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "soil.png"
image = cv2.imread(image_path)

b, g, r = cv2.split(image)

blank = np.zeros_like(b, dtype=np.uint8)

steps = 11
wavelengths = np.linspace(450, 700, steps)
colors = []
for i in range(steps):
    if i <= 5:
        ratio = i / 5.0
        color = cv2.merge([np.uint8(b * (1 - ratio)), np.uint8(g * ratio), blank])
    else:
        ratio = (i - 5) / 5.0
        color = cv2.merge([blank, np.uint8(g * (1 - ratio)), np.uint8(r * ratio)])
    colors.append(color)
    filename = f"color_{i+1}.png"
    cv2.imwrite(filename, color)
    print(f"{filename}: ~{int(wavelengths[i])} nm")

