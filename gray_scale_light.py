# This import solves the import issues.
from operator import truediv
from turtle import pensize, width, window_height
from warnings import catch_warnings
import cv2 as cv
import numpy
import sys

from sniffio import current_async_library

# Try read in the image data.
try:
    img = cv.imread(cv.samples.findFile("./img/wired_cat.webp"), cv.IMREAD_UNCHANGED)
except:
    sys.exit("Image can't be found")

#Case where the images dosn't excists.
if img is None:
    sys.exit("Image not exist")

#Get images dimensions.
dimensions = img.shape
# Get height width and channels.
height = dimensions[0]
width = dimensions[1]

print(height, width)

out_of_bounds = True

smallestValue = 0
for i in range(height):
    for j in range(width):
        smallestValue = min(img[i][j][0],img[i][j][1],img[i][j][2])
        img[i][j] = [smallestValue,smallestValue,smallestValue]

# output images.
#set the window size to be controllable and fixed porpotion.    
cv.namedWindow('My Image', cv.WINDOW_NORMAL)

#display blurred image
cv.imshow('My Image', img)

#wait for keystroke in the window， then destroy
cv.waitKey(0)
cv.destroyAllWindows()

#write to output image file
cv.imwrite("out_images/line.png", img)
