from turtle import color
import cv2
import numpy as np

mode = 3
# 1 for line
# 2 for circle
# 3 for rectangle
drawing = False # true if mouse is pressed
color = (100,100,100)
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event == cv2.EVENT_LBUTTONUP:
        if mode == 1: # drawing line
            cv2.line(img,(ix, iy),(x,y),color, 3)
        elif mode == 2: # drawing circle
            cv2.circle(img,(int((x + ix)/2), int((y + iy)/2)), int(abs(x - ix)/2),color, 3)
        else: #drawing rectangle
            cv2.rectangle(img,(ix, iy),(x,y),color, 3)
                    
# the board to draw
img = np.zeros((600,600,1), np.uint8)
cv2.namedWindow('Window')
# to connect to mouseCall and windows
cv2.setMouseCallback('Window',draw_circle)
while(1):
    cv2.imshow('Window',img)
    k = cv2.waitKey(1)&0xFF
    if k == 27: # ESE to quit
        break
cv2.destroyAllWindows()







# img = cv2.imread(cv2.samples.findFile("whiteBoard.jpeg"), cv2.IMREAD_UNCHANGED)
# x = int(input("x position: "))
# y = int(input("y position: "))
# r = int(input("radius: "))
# color = (255, 0, 0)
# cv2.circle(img, (x, y), r, color, 1)

