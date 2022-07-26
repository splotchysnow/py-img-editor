import tkinter as tk
import numpy as np
import globals
from globals import window, canvas, update_canvas
import popup
import tkinter as tk
# remeber to import globals


def filling():
    popup.popup_filling()
    
    # globals.canvas.focus_set()
    global xp,yp,pos
    pos = tk.IntVar()
    window.bind("<Button-1>", get_post)
    canvas.wait_variable(pos)
    # just import globals.img to the one you wanna edit, or you can just use globals.img as variable to process, but assign a new one would save many word. img will be the form that can be thought as img = imread(something)
    img_np = globals.img
    # img_np = numpy.array(globals.img) also works, if you prefer to make it to be numpy.array, but I don't know it in deeper

    x_limit = len(img_np) - 1
    y_limit = len(img_np[0]) - 1

    new_color = popup.color
    color = img_np[xp][yp].copy()

    visited = {(xp, yp)}
    stack = [(xp,yp)]

    try:
        tolerance = int(popup.tol)
    except:
        tolerance = 10
    while len(stack) > 0:
        (x,y) = stack.pop()
        img_np[x][y] = new_color
        
        if (x - 1, y) not in visited and x > 0:
            visited.add((x - 1, y))
            if compare_two_pixel(img_np[x - 1][y], color, tolerance):
            #if numpy.allclose(img_np[x - 1][y], color, tolerance):
                stack.append((x - 1, y))
        
        if (x + 1, y) not in visited and x < x_limit:
            visited.add((x + 1, y))
            if compare_two_pixel(img_np[x + 1][y], color, tolerance):
            # if numpy.allclose(img_np[x + 1][y], color, tolerance):
                stack.append((x + 1, y))
                
        if (x, y - 1) not in visited and y > 0:
            visited.add((x, y - 1))
            if compare_two_pixel(img_np[x][y - 1], color, tolerance):
            # if numpy.allclose(img_np[x][y - 1], color, tolerance):
                stack.append((x, y - 1))
        
        if (x, y + 1) not in visited and y < y_limit:
            visited.add((x, y + 1))
            if compare_two_pixel(img_np[x][y + 1], color, tolerance):
            # if numpy.allclose(img_np[x][y + 1], color, tolerance):
                stack.append((x, y + 1))
                
    # in the end, you HAVE TO update it, img_np is the form of array, you can think of it as imshow(window, img_np) if that helps
    update_canvas(img_np)

def get_post(event):

    global xp, yp
    xp = event.y
    yp = event.x
    # I may mismatch x and y in filling function, so I invert them in here
    pos.set(1)
    
    
def compare_two_pixel(curr, standard, tor):
    return np.sum(np.abs(np.subtract(curr,standard))) <= tor