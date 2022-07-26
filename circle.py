import cv2
import numpy
import sys


posList = []
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       # draw circle here (etc...)
       posList.append((x, y))

img = cv2.imread(cv2.samples.findFile("whiteBoard.jpeg"), cv2.IMREAD_UNCHANGED)

while(True):
    cv2.imshow("img", img)

    cv2.setMouseCallback("img", click_event)
    cv2.waitKey(1)
    if len(posList) >= 2:
        pos_x = (posList[0][0] + posList[1][0]) / 2
        pos_y = (posList[0][1] + posList[1][1]) / 2
        radius = int((posList[0][0] - posList[1][0]) / 2)
        color = (255,0,0)
        cv2.circle(img, (int(pos_x), int(pos_y)), radius, color, 1)

