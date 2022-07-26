import cv2
import numpy as np


drawing=False # true if mouse is pressed
mode=True # if True, draw rectangle. Press 'm' to toggle to curve

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.circle(img,( int((x + ix)/2), int((y + iy)/2)), int(abs(x - ix)/2),(100,100,100), 3)        


img = np.zeros((600,600,1), np.uint8)
cv2.namedWindow('Window')
cv2.setMouseCallback('Window',draw_circle)
while(1):
    cv2.imshow('Window',img)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break
cv2.destroyAllWindows()







# img = cv2.imread(cv2.samples.findFile("whiteBoard.jpeg"), cv2.IMREAD_UNCHANGED)
# x = int(input("x position: "))
# y = int(input("y position: "))
# r = int(input("radius: "))
# color = (255, 0, 0)
# cv2.circle(img, (x, y), r, color, 1)

