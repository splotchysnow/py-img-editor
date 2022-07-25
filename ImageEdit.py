"""
Create the backend for the GUI.py to have functions that edits the images with the opencv modules.
"""

# This import solves the import issues.
import cv2 as cv
import numpy
import sys

#read in the image data.
img = cv.imread(cv.samples.findFile("1.jpg"), cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Image not exist")

#set the window size to be controllable and fixed porpotion.    
cv.namedWindow('My Image', cv.WINDOW_NORMAL)

#display image
cv.imshow('My Image', img)

#Wait for a keystroke in the window
cv.waitKey(0)
cv.destroyAllWindows()

#write to output image file
cv.imwrite("out.png", img);
