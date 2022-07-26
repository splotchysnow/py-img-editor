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

while(out_of_bounds):
    try:
        # Asking for user inputs.
        #Four integers for the corrdinates where to draw the images.
        line_begin_x = int(input("Insert line-begin-x\t"))
        line_begin_y = int(input("Insert Line-begin-y\t"))
        print()
        line_end_x = int(input("Insert line-end-x\t"))
        line_end_y = int(input("Insert line-end-y\t"))
        
        #Check for out of bounds.
        if(line_begin_x > width-1 or line_end_x > width-1):
            print("x coordinate is out of bounds.", line_begin_x, line_end_x)
        elif(line_begin_y > height-1 or line_end_y > height-1):
            print("y coordinate is out of bounds.", line_begin_y, line_end_y)
        else:
            out_of_bounds = False
    except:
        out_of_bounds = True

# Pick a color with GBR:
print(img[0][0])

current_x_coordinate = line_begin_x
current_y_coordinate = line_begin_y
pen_speed = 1
pen_size = 1000
color = [255,255,255] # Black

# This draws a straight line down and right.
# while(True):
#     #drawing the coordinate.
#     img[current_x_coordinate][current_y_coordinate] = [0,0,255]
#     if(current_x_coordinate != line_end_x):
#         if(current_x_coordinate < line_end_x):
#             current_x_coordinate+= pen_speed
#         else:
#             current_x_coordinate-= pen_speed
#     elif(current_y_coordinate != line_end_y):
#         if(current_y_coordinate < line_end_y):
#             current_y_coordinate += pen_speed
#         else:
#             current_y_coordinate -= pen_speed
#     else:
#         break

# Update: EVERYTIME THE WRITE HAPPENDS< ALSO CHANGES PEN FROM LEFT TO RIGHT. and Up and down by pen_size.

while(True):
    #drawing the coordinate. two so that it draws big from left to right. up to down.
    img[current_y_coordinate][current_x_coordinate-pen_size:current_x_coordinate+pen_size] = color
    # img[current_y_coordinate-pen_size:current_y_coordinate+pen_size][current_x_coordinate] = color
    if(current_x_coordinate != line_end_x):
        if(current_x_coordinate < line_end_x):
            current_x_coordinate+= pen_speed
        else:
            current_x_coordinate-= pen_speed
    if(current_y_coordinate != line_end_y):
        if(current_y_coordinate < line_end_y):
            current_y_coordinate += pen_speed
        else:
            current_y_coordinate -= pen_speed
    if(current_x_coordinate == line_end_x and current_y_coordinate == line_end_y):
        img[current_x_coordinate][current_y_coordinate] = [0,0,255]
        break

    

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