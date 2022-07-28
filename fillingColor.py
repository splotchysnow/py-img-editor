from email.mime import image
from hashlib import new
from threading import stack_size
from tkinter import Y
import cv2
import numpy





xp = int(input("x position: "))
yp = int(input("y position: "))

img = cv2.imread(cv2.samples.findFile("./img/Cat03.jpg"), cv2.IMREAD_UNCHANGED)

img_np = numpy.array(img)

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

cv2.imshow('Window',img_np)

cv2.waitKey(0)
cv2.destroyAllWindows()

    


