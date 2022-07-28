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
import gray_scale_functions
from IPython.display import display

# open the image
img = gray_scale_functions.loadImg("./img/caokitten.jpg")
#ig = Image.open("./img/caokitten.jpg")
#pixel = ig.load()
#get the length and width for the image
length, width, channel = img.shape
# print(length, width)
#list all the pixal values in the image
#pixel_values = list(ig.getdata())
#[b, g, r] = pixel_values
# r, g, b = ig.getpixel((20,20))
#create a tuple for rgb value of the selected pixel
#bgr = img.getpixel((20,20))
bgr = img[20, 20]
#(pixel[20,20][0],pixel[20,20][1],pixel[20,20][2])
#print (pixel[20,20])
print (bgr)
arr = []
#iterate through all the pixels line by line and compare
for l in range(width):
    # print (l)
    for w in range(length):
        bgrig = img[w,l]
        if all(abs(t1 - t2)<=5 for t1, t2 in zip(bgr, bgrig)): 
          arr.append([w, l])
        #   print (img[w,l])
          img[w,l] = (0,0,255)
          
print(len(arr))

#change pixels with certain color
# for i in range(len(arr)):
#     img.putpixel((arr[i][0], arr[i][1]), (255,0,0))

# img.show()
# cv.imshow(ig, numpy.array(ig))

cv.imwrite("out_images/" + "caokitten_SP_edited.png", img)
while True:
    cv.imshow("caokitten_SP_edited", img)
    cv.waitKey(0)
    sys.exit() # to exit from all the processes
    
cv2.destroyAllWindows()
