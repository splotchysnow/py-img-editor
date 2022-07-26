# The implementation of detecting the all same color pixels that the user selects. #

# This import solves the import issues.
import cv2 as cv
import numpy as np
import sys

img = cv.imread('img\select.jpg', cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Could not read the image. ")

cv.imshow('Display Image',img)
k = cv.waitKey(0)

events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

if event == cv.EVENT_FLAG_LBUTTON:
    