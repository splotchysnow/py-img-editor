from fileinput import filename
from math import floor
import string
from time import time
from turtle import width
from warnings import catch_warnings
import cv2 as cv
import sys

import numpy as np

# Functions for loading images:
def loadImg(imgPath:str) -> np.ndarray:
    """
    summary: Use for loading images, given an image path from the current folder and the image then will be returned as a variable.
    """
    # Try read in the image data.
    try:
        img = cv.imread(cv.samples.findFile(imgPath), cv.IMREAD_UNCHANGED)
    except:
        sys.exit("Image can't be found")

    #Case where the images dosn't excists.
    if img is None:
        sys.exit("Image not exist")
    
    # print(type(img))
    
    return img

# Functions for exporting the dimension of image.
def dimension_img(img:np.ndarray):
    #Get images dimensions.
    dimensions = img.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    return height, width

# Functions for output file with File Name:
def outputFile(img,file_name) -> np.ndarray:
    """
    Output the file with the desired output name.
    """
    cv.imwrite("out_images/" + file_name + ".png",img)
    return img

# Calculate threashhold:
def calculate_threshold(percentage : int):
    """_summary_

    Args:
        percentage (int): out of 100, if less than or more than we discard. Represent the percentage of threshold keep,
        The higher the percentage the less the edges shown.
    """
    max_thresh = 255
    # 101 because I want to avoid div by 0;
    if(percentage == 100):
        return 0
    elif(percentage > 100 or percentage < 0):
        print("Percentage is wrong")
        return 255
    else:
        return floor(max_thresh / (percentage))
# Grab that image and detect Keep threashold above that required.
def discard_above_threshold(image:np.ndarray, threshold : int, pixel_x : int, pixel_y: int):
    """
    takes a threashold value that is an input to this function and then take in a pixel locaiton of x,y
    we want to take those value and be able to consdier if the pixel is above or below that threashold.
    if it is above that threashold, we would want to discard it...
    If it is lower than the threashold. then we want to set it to compltetly black. Therefore the image will
    then become a binary image files.
    """
    # I want the darkest thing that they have. so... Less the better?
    smallestValue = min(image[pixel_x][pixel_y][0],image[pixel_x][pixel_y][1],image[pixel_x][pixel_y][2])
    if smallestValue <= threshold:
        image[pixel_x][pixel_y] = [0,0,0]
    else:
        image[pixel_x][pixel_y] = [255,255,255]
# Use the two above function and calculate the edges on an image.
def Edge_Detection_Function(img:np.ndarray, file_name:str, percent:int) -> np.ndarray:
    """
    summary: take a copy of the orginal image, calculate threashold base on the percentage given in parameter. Then only keep edges of the image.
    The lower the percentage the more edges will be kepted.
    """
    img_ = img.copy()
    height,width = dimension_img(img_)
    tH = calculate_threshold(percent)
    for i in range(height):
        for j in range(width):
            discard_above_threshold(img_, tH, i, j)
    return outputFile(img_,file_name)

# Size down the image with a given percentage.
def down_size_image(img:np.ndarray,fileName:str,custom_percentage:int) -> np.ndarray:
    """
    _summary_ : Resize function removes a couple pixels at a time and compiling the image down to a smaller image version.
                THis file is for percentages.
    """
    # Calculate the resized dimension.
    height, width = dimension_img(img)
    custom_height = int(height/custom_percentage)
    custom_width = int(width/custom_percentage)
    #Create a new image, blank with this dimension.
    new_img = np.zeros((custom_height,custom_width,3), dtype=np.uint8)

    #Loop through new image.
    for i in range(custom_height):
        for j in range(custom_width):
            new_img[i][j] = img[i*custom_percentage][j*custom_percentage]

    return outputFile(new_img, fileName)

# TODO: YAYA CLEAN UP THIS FUNCTION. also take out function's sys exit()
# Select a pixel from the image and then finding all pixels that are related to this color.
def select_pixels(img: np.ndarray, fileName: str) -> None:
    """
        Summary: TODO: YAYA
    """
    # open the image
    length, width, channel = img.shape
    bgr = img[20, 20]
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
    #change pixels with certain color
    # for i in range(len(arr)):
    #     img.putpixel((arr[i][0], arr[i][1]), (255,0,0))
    # img.show()
    # cv.imshow(ig, numpy.array(ig))
    outputFile(img,fileName)
    while True:
        cv.imshow("caokitten_SP_edited", img)
        cv.waitKey(0)
        break
    cv.destroyAllWindows()
    sys.exit() # to exit from all the processes

# Flip top and bottom in cool visuals.
def half_reversion_bonus_UD(img:np.ndarray,fileName:str) -> np.ndarray:
    "Summary: Displays a creepy up and down reverted image."
    img_ = img.copy()
    height, width = dimension_img(img_)
    tempStorage = []
    for i in range(1,int(height/2)):
        for j in range(width):
            tempStorage = img_[i][j]
            # print(height,width,tempStorage,height-i)
            img_[i][j] = img_[height-i][j]
            img_[height-i][j] = tempStorage
    return outputFile(img_, fileName)

# Flip image left/Right in cool visuals..
def half_reversion_bonus_LR(img:np.ndarray,fileName:str) -> np.ndarray:
    "Summary: With the image being inputed, the file will be flipped left and right. and sent to output."
    img_ = img.copy()
    height, width = dimension_img(img)
    tempStorage = []
    for i in range(height):
        for j in range(1,int(width/2)):
            # The deep copy is what caused the bug.
            tempStorage = img_[i][j]
            # print(height,width,tempStorage,height-i)
            img_[i][j] = img_[i][width-j]
            img_[i][width-j] = tempStorage
    return outputFile(img_, fileName)
# Flip image upside down.
def flip_image_up_and_down(img:np.ndarray,fileName:str) -> np.ndarray:
    "Summary: With the image being inputed, the file will be flipped upside down and sent to output."
    img_ = img.copy()
    height, width = dimension_img(img_)
    tempStorage = []
    for i in range(1,int(height/2)):
        for j in range(width):
            # The deep copy is what caused the bug.
            tempStorage = img_[i][j].copy()
            # print(height,width,tempStorage,height-i)
            img_[i][j] = img_[height-i][j]
            img_[height-i][j] = tempStorage
    return outputFile(img_, fileName)

# Flip image left/Right.
def flip_image_left_and_right(img:np.ndarray,fileName:str) -> np.ndarray:
    "Summary: With the image being inputed, the file will be flipped left and right. and sent to output."
    img_ = img.copy()
    height, width = dimension_img(img_)
    tempStorage = []
    for i in range(height):
        for j in range(1,int(width/2)):
            # The deep copy is what caused the bug.
            tempStorage = img_[i][j].copy()
            # print(height,width,tempStorage,height-i)
            img_[i][j] = img_[i][width-j]
            img_[i][width-j] = tempStorage
    return outputFile(img, fileName)


def rotation_left(img:np.ndarray, fileName:str) -> np.ndarray:
    """ Rotate image to the left."""
    # This is flipped on purpose.
    width, height = dimension_img(img)
    # print(width,height)

    #Create a new image, blank with a rotated dimensions.
    new_img = np.zeros((height,width,3), dtype=np.uint8)

    for i in range(1,height):
        for j in range(width):
            new_img[i][j] = img[j][height-i]
    
    return outputFile(new_img,fileName)

def rotation_right(img:np.ndarray, fileName:str) -> np.ndarray:
    """ Rotate image to the right."""
    # This is flipped on purpose.
    width, height = dimension_img(img)

    #Create a new image, blank with a rotated dimensions.
    new_img = np.zeros((height,width,3), dtype=np.uint8)

    for i in range(height):
        for j in range(1,width):
            new_img[i][j] = img[width-j][i]
    
    return outputFile(new_img,fileName)
