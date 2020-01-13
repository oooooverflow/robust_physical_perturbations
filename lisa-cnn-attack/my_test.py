import cv2
from PIL import Image
import numpy as np

# img1 = cv2.imread('../beamng_data/3.png')
# img11 = Image.fromarray(np.uint8(img1),"RGBA")
img1 = Image.open('../beamng_data/3.png')
img2 = Image.open('misc/uw17-cropped.png')
# img2 = cv2.imread('misc/uw17-cropped.png')
# img21 = Image.fromarray(np.uint8(img2),"RGBA")
# img3 = cv2.imread('masks/octagon.png')
# img31 = Image.fromarray(np.uint8(img3),"RGBA")
print(img1.mode)
print(img2.mode)
# print(img2.shape)
# print(img21.mode)
# print(img3.shape)
# print(img31.mode)