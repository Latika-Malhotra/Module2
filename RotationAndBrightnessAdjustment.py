import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('example.jpg')

# Rotate the image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by +50
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()

# Save outputs
cv2.imwrite('rotated_image.jpg', rotated)
cv2.imwrite('brighter_image.jpg', brighter)
