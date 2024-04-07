import cv2
import numpy as np

img = cv2.imread("image2.png")
img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite("filtered_noise.png", img)