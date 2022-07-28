"""
_summary_ : Resize function removes a couple pixels at a time and compiling the image down to a smaller image version.
            THis file is for percentages.
"""

import gray_scale_functions
import cv2 as cv
import numpy as np

# Create an image:
img = gray_scale_functions.loadImg("./img/wired_cat.webp")

# Find that dimension:
dimensions = img.shape
# Get height width and channels.
height = dimensions[0]
width = dimensions[1]

# Custimize it to 10 percent.
custom_percentage = 50
custom_height = int(height/custom_percentage)
custom_width = int(width/custom_percentage)

#Create a new image, blank with this dimension.
new_img = np.zeros((custom_height,custom_width,3), dtype=np.uint8)

#Loop through new image.
for i in range(custom_height):
    for j in range(custom_width):
        new_img[i][j] = img[i*custom_percentage][j*custom_percentage]

cv.imwrite("out_images/" + "cat-resized.png",new_img)    



