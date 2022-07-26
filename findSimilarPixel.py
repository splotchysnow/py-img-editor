import cv2
from cv2 import imshow
from cv2 import waitKey
import numpy
import sys


def click_event(event, x, y, flags, param):
     if event == cv2.EVENT_LBUTTONDOWN:
         print(x, ",", y)
         
img = cv2.imread(cv2.samples.findFile("img/drawing.png"), cv2.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Image not exist")
img = cv2.resize(img,(300,300))

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyWindow


