import cv2
import numpy
import sys

img = cv2.imread(cv2.samples.findFile("whiteBoard.jpeg"), cv2.IMREAD_UNCHANGED)
x = int(input("x position: "))
y = int(input("y position: "))
r = int(input("radius: "))
color = (255, 0, 0)
cv2.circle(img, (x, y), r, color, 1)




# posList = []
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#        # draw circle here (etc...)
#        posList.append((x, y))

# img = cv2.imread(cv2.samples.findFile("whiteBoard.jpeg"), cv2.IMREAD_UNCHANGED)
# img = cv2.resize(img,(320,240))

# while(True):
#     cv2.imshow("img", img)

#     cv2.setMouseCallback("img", click_event)
#     cv2.waitKey(1)
#     leng = len(posList)
#     if leng == 2:
#         pos_x = int ((posList[0][0] + posList[1][0]) / 2)
#         pos_y = int ((posList[0][1] + posList[1][1]) / 2)
#         radius = int(abs((posList[0][0] - posList[len - 2][0]) / 2))
#         color = (255,0,0)
#         cv2.circle(img, (pos_x, pos_y), radius, color, 1)

