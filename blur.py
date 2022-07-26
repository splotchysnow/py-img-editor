"""
Create the backend for the GUI.py to have functions that edits the images with the opencv modules.
"""

# This import solves the import issues.
import cv2 as cv
import numpy
import sys

#read in the image data.
img = cv.imread(cv.samples.findFile("img\kawai.jpg"), cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Image not exist")

#change file size if needed (unused)
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
#resize image (unused)
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

#save image to rewritable array 
img_np = numpy.array(img)

"""blurring whole image, controlable variables: deg
"""
#create np array to store the 3d array of whole blurred image
blur_whole = img_np.copy()

#set the blurring degree, smaller number equals more blur, deg>=0
deg = 0

#set counter to 0
i = 0
#loop through the numpy 3d array
for x in range(0, len(img_np)-1):
    for y in range(0, len(img_np[0])-1):
        if (x<(len(img_np)-4) and y<(len(img_np[x])-4)) and i >= deg: #change one every i+1 pixel
            for z in range(0,2):
                #average the upper, left, bottom, right pixels of original image and save to blur numpy array
                blur_whole[x][y][z]=(int(img_np[x-3][y-3][z])+int(img_np[x+3][y+3][z])+int(img_np[x+3][y-3][z])+int(img_np[x-3][y+3][z]))/4
            i = 0 #reset counter
        else:
            #increment counter by 1
            i += 1  
            
"""blurring partial image, controlable variables: part_x, part_y, area, lvl
""" 
#create np array to store the 3d array of partial blurred image
blur_part = img_np.copy()

p_x = 30 #x coordinate of the center of part blurring, 0 to 100 from left to right
p_y = 50 #y coordinate of the center of part blurring, 0 to 100 from top to down
area = 50 #percentage of area size to blur, 1 to 100 
lvl = 10 #higher indicated more blurred, lvl>1 (a number too high may cause a loop that goes on foreeeeevvvver)

#center of part blurring in pixels
c_x = len(img_np)*p_x/100 
c_y = len(img_np[0])*p_x/100
#radius to blur in pixels
c_area = min(len(img_np), len(img_np[0]))*area/100/2

#loop through the numpy 3d array
for level in range(1, lvl):
    for x in range(0, len(img_np)-1):
        for y in range(0, len(img_np[0])-1):
            if (x<(len(img_np)-4) and y<(len(img_np[x])-4)) and (x-c_x)**2 + (y-c_y)**2 < c_area**2: #change every pixel in range selected
                for z in range(0,2):
                    #average the upper, left, bottom, right pixels of original image and save to partial blur numpy array
                    blur_part[x][y][z]=(int(img_np[x-3][y-3][z])+int(img_np[x+3][y+3][z])+int(img_np[x+3][y-3][z])+int(img_np[x-3][y+3][z]))/4
    img_np = blur_part.copy()

       


#set the window size to be controllable and fixed porpotion.    
cv.namedWindow('My Image', cv.WINDOW_NORMAL)

#display blurred image 
cv.imshow('My Image', blur_part)

#wait for keystroke in the window， then destroy
cv.waitKey(0)
cv.destroyAllWindows()

#write blurred images to output image file
cv.imwrite("out_images/blur_whole.png", blur_whole)
cv.imwrite("out_images/blur_part.png", blur_part)
