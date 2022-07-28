"""

1. Grab a pixel
2. Loop and pickup all pixel
3. Store pixel location ------ 

"""


#import some libaries including python image library

from PIL import Image
import cv2 as cv
import numpy
import sys

# open the image
ig = Image.open("./img/caokitten.jpg")
pixel = ig.load()
print (ig.size)
length, width = ig.size
#list all the pixal values in the image
pixel_values = list(ig.getdata())
#[b, g, r] = pixel_values
# b = pixal[20,20][0]
# g = pixal[20,20][1]
# r = pixal[20,20][2]
bgr = {pixel[20,20][0],pixel[20,20][1],pixel[20,20][2]}
print (pixel[20,20])
#print (bgr)
