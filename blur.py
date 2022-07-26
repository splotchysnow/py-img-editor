"""
Create the backend for the GUI.py to have functions that edits the images with the opencv modules.
"""

# This import solves the import issues.
import cv2 as cv
import numpy
import sys

#read in the image data.
img = cv.imread(cv.samples.findFile("1.jpg"), cv.IMREAD_UNCHANGED)

if img is None:
    sys.exit("Image not exist")


#print(type(img)) 
#print(img.shape)
#print(numpy.asarray(img))

#save image to rewritable array 
img_np = numpy.asarray(img)
#create np array to store the 3d array of blurred image
blur_np = img_np.copy()

#print(len(blur_np)) 
#print(len(blur_np[0])) 

#loop through the numpy 3d array
blur_np[0][0] = 1

"""
for x in range(0, len(blur_np)-1):
    for y in range(0, len(blur_np[x])-1):
        #average the upper, left, bottom, right pixels of original image and save to blur numpy array
        if (x>1 and y>1 and x<(len(blur_np)-2) and y<(len(blur_np[x])-2)):
            #print(x)
            for i in range(0,2):
                blur_np[x][y][i] = int(((int(img_np[x-1][y-1][i]))+(int(img_np[x-1][y+1][i]))+(int(img_np[x+1][y-1][i]))+(int(img_np[x+1][y+1][i])))/4)
        else:
            #save the boundarys directly from original image
            blur_np[x][y] = img_np[x][y]
"""
"""
for x in range(0, len(blur_np)-1):
    for y in range(0, len(blur_np[x])-1):
        #save the boundarys directly from original image
        if x==0 or y==0 or x==len(blur_np-1) or y ==len(blur_np[x]-1):
            blur_np[x][y] = img_np[x][y]
        else:
            #average the upper, left, bottom, right pixels of original image and save to blur numpy array
            for i in range(0,2):
                blur_np[x][y] = img_np[x][y]
                #blur_np[x][y][i] = int(((int(img_np[x-1][y-1][i]))+(int(img_np[x-1][y+1][i]))+(int(img_np[x+1][y-1][i]))+(int(img_np[x+1][y+1][i])))/4)
"""

"""
#print(blur_np[len(blur_np)-1][len(blur_np[0])-1][0])
#blur_np[0][0][2] = img_np[0][0][1]
#blur_np[len(blur_np)-1][len(blur_np[0])-1][0] = img_np[len(blur_np)-1][len(blur_np[0])-1][0]
"""

for x in range(0, len(img_np)-1):
    for y in range(0, len(img_np[x])-1):
        for i in range(0,2):
            blur_np[x][y][i] = img_np[x][y][i]
    
        

#for debug usage, print 3d array of blurred image 
#print(blur_np)

#Gaussian Blurring method testing
blur = cv.GaussianBlur(img, (25,25),0)

#set the window size to be controllable and fixed porpotion.    
cv.namedWindow('My Image', cv.WINDOW_NORMAL)

#display blurred image
cv.imshow('My Image', blur_np)

#wait for keystroke in the window， then destroy
cv.waitKey(0)
cv.destroyAllWindows()

#write to output image file
cv.imwrite("blur.png", blur)
