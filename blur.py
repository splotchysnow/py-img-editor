"""
Bluring Features that allows the user to blur the images with customizable
"""

# This import solves the import issues.
import cv2 as cv
import numpy
import sys

#read in the image data.
img = cv.imread(cv.samples.findFile("./img/kawai.jpg"), cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Image not exist")

#change file size if needed (unused)
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
#resize image (unused)
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

"""blurring whole image, controlable variables: deg
"""
#save image to rewritable array 
img_np = numpy.array(img)

#create np array to store the 3d array of whole blurred image
blur_whole = img_np.copy()

#set the blurring degree, bigger number equals more blur, deg>=1
deg = 1

#loop through the numpy 3d array
for degree in range(0, deg):
    for x in range(0, len(img_np)-1): #x-axis of pixel
        for y in range(0, len(img_np[0])-1): #y-axis of pixel
            if (x<(len(img_np)-4) and y<(len(img_np[x])-4)):
                for z in range(0,2):
                    #average the upper, left, bottom, right pixels of original image and save to blur numpy array
                    blur_whole[x][y][z]=(int(img_np[x-3][y-3][z])+int(img_np[x+3][y+3][z])+int(img_np[x+3][y-3][z])+int(img_np[x-3][y+3][z]))/4
    img_np = blur_whole.copy()
            
"""blurring partial image, controlable variables: part_x, part_y, area, lvl
""" 
#create np array to store the 3d array of partial blurred image
img_np = numpy.array(img)
blur_part = img_np.copy()

p_x = 10 #x coordinate of the center of part blurring, 0:100 from left to right
p_y = 10 #y coordinate of the center of part blurring, 0:100 from top to down
area = 50 #percentage of area size to blur, 1:100 
lvl = 1 #higher indicated more blurred, lvl>1 (less than 10 recommended)

#center of part blurring in pixels
c_x = len(img_np)*p_x/100 
c_y = len(img_np[0])*p_x/100
#radius to blur in pixels
c_area = min(len(img_np), len(img_np[0]))*area/100/2

#loop through the numpy 3d array
for level in range(0, lvl):
    for x in range(0, len(img_np)-1): #x-axis of pixel
        for y in range(0, len(img_np[0])-1): #y-axis of pixel
            if (x<(len(img_np)-4) and y<(len(img_np[x])-4)) and (x-c_x)**2 + (y-c_y)**2 < c_area**2: #change every pixel in range selected
                for z in range(0,2):
                    #average the upper, left, bottom, right pixels of original image and save to partial blur numpy array
                    blur_part[x][y][z]=(int(img_np[x-3][y-3][z])+int(img_np[x+3][y+3][z])+int(img_np[x+3][y-3][z])+int(img_np[x-3][y+3][z]))/4
    img_np = blur_part.copy()

       
#set the window size to be controllable and fixed porpotion.    
cv.namedWindow('My Image', cv.WINDOW_NORMAL)

#display blurred image 
cv.imshow('My Image', blur_part)
cv.imshow('My Image', blur_whole)

#wait for keystroke in the window， then destroy
cv.waitKey(0)
cv.destroyAllWindows()

#write blurred images to output image file
cv.imwrite("out_images/blur_whole.png", blur_whole)
cv.imwrite("out_images/blur_part.png", blur_part)
