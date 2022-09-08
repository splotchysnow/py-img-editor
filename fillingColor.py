from email.mime import image
from hashlib import new
from threading import stack_size
from tkinter import Y
from traceback import print_list
import cv2
import numpy
import globals
# remeber to import globals


def filling():
    xp = int(input("x position: "))
    yp = int(input("y position: "))
    
    # just import globals.img to the one you wanna edit, or you can just use globals.img as variable to process, but assign a new one would save many word. img will be the form that can be thought as img = imread(something)
    img_np = globals.img
    # img_np = numpy.array(globals.img) also works, if you prefer to make it to be numpy.array, but I don't know it in deeper

    x_limit = len(img_np) - 1
    y_limit = len(img_np[0]) - 1

    new_color = (200, 100,200)
    color = img_np[xp][yp].copy()

    visited = {(xp, yp)}
    stack = [(xp,yp)]

    tolerance = 0.3
    while len(stack) > 0:
        (x,y) = stack.pop()
        img_np[x][y] = new_color
        
        if (x - 1, y) not in visited and x > 0:
            visited.add((x - 1, y))
            if numpy.allclose(img_np[x - 1][y], color, tolerance):
                
                stack.append((x - 1, y))
        
        if (x + 1, y) not in visited and x < x_limit:
            visited.add((x + 1, y))
            if numpy.allclose(img_np[x + 1][y], color, tolerance):
                stack.append((x + 1, y))
                
        if (x, y - 1) not in visited and y > 0:
            visited.add((x, y - 1))
            if numpy.allclose(img_np[x][y - 1], color, tolerance):
                stack.append((x, y - 1))
        
        if (x, y + 1) not in visited and y < y_limit:
            visited.add((x, y + 1))
            if numpy.allclose(img_np[x][y + 1], color, tolerance):
                stack.append((x, y + 1))
                
    # in the end, you HAVE TO update it, img_np is the form of array, you can think of it as imshow(window, img_np) if that helps
    globals.update_canvas(img_np)



    


