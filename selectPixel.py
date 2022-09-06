# The implementation of detecting all same color pixels that the user selected in the chosen picture. #

# This import solves the import issues.
import cv2 as cv
import numpy as np
import sys
import tkinter as tk

# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )

# Detect mouse event
def click_event(event, x, y, flags, param):
    # Detect whether the left mouse is clicked
    # find out the specific pixel on clicked position
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"{x}, {y}")
        print("Left button clicked")
        print(f"pixel: {img[y,x]}")
        same_pixel_area(img[y,x])

# Search all the pixels on the graph
def select_same_pixels(x,y):
    list_pixels_coordinates = []
    rows,cols = img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            k = img[i,j] # pixel in the specific coordinate
            # check all the same pixel in the graph
            if (k == img[y,x]).all():  
                pair_cdn = (i,j)
                list_pixels_coordinates.append(pair_cdn)


# shows all the areas with the same pixel
def same_pixel_area(pixel = []):
    print (f"passed pixel: {pixel}")
    # create NumPy arrays to set lower and upper bound
    lower = np.array(pixel, dtype = "uint8") 
    upper = np.array(pixel, dtype = "uint8")
    
    # find all area that has the same pixel
    mask = cv.inRange(img, lower, upper)
    output = cv.bitwise_and(img, img, mask = mask)
    
    # display only the same pixel area
    cv.imshow("images", np.hstack([img, output]))
    cv.waitKey(0)
    cv.destroyAllWindows()

# Adjust the picture with aspect ratio (to prevent 
# original shape of the image get affected)
def AspectRatioResize(img, width=None, height=None, 
                      inter=cv.INTER_AREA):
    dim = None
    h, w = img.shape[:2]
    
    if width is None and height is None :
        return img
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    return cv.resize(img, dim, interpolation=inter)

# # Display the picture in the center of the window
# def displayInCenter(win_name, image):
#    win_x, win_y = GetScreenCenter(); 


img = cv.imread('img\select.jpg', cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Could not read the image. ")

window_name = 'Display Image'

WIDTH = 1000
HEIGTH = 1000

img = AspectRatioResize(img, width = WIDTH, height = HEIGTH)


cv.imshow(window_name,img)
cv.moveWindow(window_name, 480, 200)

cv.setMouseCallback(window_name, click_event)




k = cv.waitKey(0)
cv.destroyAllWindows()

# press ESC key to quit the window
if cv.waitKey(1) & k == 27:
    cv.destroyAllWindows()