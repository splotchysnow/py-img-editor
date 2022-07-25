"""
Create the backend for the GUI.py to have functions that edits the images with the opencv modules.
"""

# This import solves the import issues.
import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("1.jpg"), cv.IMREAD_UNCHANGED)
if img is None:
    sys.exit("Image not exist")
    
#cv.namedWindow('My Image', cv.WINDOW_NORMAL)
cv.imshow('My Image', img)

k = cv.waitKey(0)
cv.destroyAllWindows()
if k == ord("s"):
    cv.imwrite("starry_night.png", img)