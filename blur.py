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

#change file size if needed
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)


#print(type(img)) 
#print(img.shape)
#print(numpy.asarray(img))

#save image to rewritable array 
img_np = numpy.array(resized)
#create np array to store the 3d array of blurred image
blur_np = img_np.copy()

#print(len(blur_np)) 
#print(len(blur_np[0])) 

#set counter to 0
i = 0
#loop through the numpy 3d array
for x in range(0, len(blur_np)-1):
    for y in range(0, len(blur_np[x])-1):
        if x<(len(blur_np)-51) and y<(len(blur_np[x])-51) and i==5: #change one every five pixel
            for z in range(0,2):
                #print("c")
                #average the upper, left, bottom, right pixels of original image and save to blur numpy array
                blur_np[x][y][z] = (((int(img_np[x-50][y-50][z]))+(int(img_np[x-50][y+50][z]))+(int(img_np[x+50][y-50][z]))+(int(img_np[x+50][y+50][z])))/4)
                i=0 #reset counter
        else:
            #increment counter by 1
            i += 1  
        

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
cv.imwrite("blur.png", blur_np)
