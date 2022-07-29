"""
Take one smaller photo, apply on bigger photo with adjustable transparency
"""

# This import solves the import issues.
from cgitb import small
import cv2
import numpy
import sys

drawing = False # true if mouse is pressed
# mouse callback function
def paste_picture(event,x,y,flags,param):
    global ix, iy, size
    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        #get transparency input from trackbar
        paste_t = cv2.getTrackbarPos('paste trans','Window')/100
        #get the width, height of the pasted picture
        wid = abs(x-ix)
        hgt = abs(y-iy)
        #call resize function
        resize(wid, hgt)
        #calculating the coners for coordinates to paste on background picture
        x_offset = min(ix, x) #lefttop
        y_offset = min(iy, y) #lefttop
        x_end = max(ix, x) #rightdown
        y_end = max(iy, y) #rightdown 
        #the part of the background to be blended
        roi = b_img[y_offset:y_end,x_offset:x_end]
        #blend the part of background with the pasted picture with desired transparency
        blend = cv2.addWeighted(resized,paste_t, roi, 1-paste_t, 0)
        #combine background with blended part 
        b_img[y_offset:y_end,x_offset:x_end] = blend
                    
# import the background picture to draw on
b_img = cv2.imread(cv2.samples.findFile("./img/Cat03.jpg"), cv2.IMREAD_UNCHANGED)
if b_img is None:
    sys.exit("Background image not exist")

# import the picture to paste on top  
p_img = cv2.imread(cv2.samples.findFile("./img/bird.jpg"), cv2.IMREAD_UNCHANGED)
if p_img is None:
    sys.exit("pasting image not exist")
 
#resize the picture to be pasted
def resize(width, height):
    global resized
    dim = (width, height)
    resized = cv2.resize(p_img, dim, interpolation = cv2.INTER_AREA)
    
#function for trackbar callback, does nothing
def nothing(x):
    nothing = 0
 
cv2.namedWindow('Window')
# to connect to mouseCall and windows
cv2.setMouseCallback('Window',paste_picture)
#create two trasparency bars to adjust the trasparency of both pictures 
cv2.createTrackbar('paste trans', 'Window', 0, 100, nothing)
while(1):
    cv2.imshow('Window',b_img)
    k = cv2.waitKey(1)&0xFF
    if k == 27: # ESE to quit
        break
cv2.destroyAllWindows()

#write to output image file
cv2.imwrite("imgs/final.png", b_img)




