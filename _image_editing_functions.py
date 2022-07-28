from math import floor
import string
from time import time
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
def Edge_Detection_Function(img:np.ndarray, file_name:str, percent:int):
    """
    summary: take a copy of the orginal image, calculate threashold base on the percentage given in parameter. Then only keep edges of the image.
    The lower the percentage the more edges will be kepted.
    """
    # Loop through all pixels and get through the matrix.
    #Deep copy that image.
    img_ = img.copy()
    # img_ = numpy.array(img)
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0

    tH = calculate_threshold(percent)

    for i in range(height):
        for j in range(width):
            discard_above_threshold(img_, tH, i, j)
    cv.imwrite("out_images/" + file_name + ".png",img_)
# Size down the image with a given percentage.
def down_size_image(img:np.ndarray,fileName:str,custom_percentage:int):
    """
    _summary_ : Resize function removes a couple pixels at a time and compiling the image down to a smaller image version.
                THis file is for percentages.
    """
    # Find that dimension:
    dimensions = img.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    custom_height = int(height/custom_percentage)
    custom_width = int(width/custom_percentage)
    
    #Create a new image, blank with this dimension.
    new_img = np.zeros((custom_height,custom_width,3), dtype=np.uint8)

    #Loop through new image.
    for i in range(custom_height):
        for j in range(custom_width):
            new_img[i][j] = img[i*custom_percentage][j*custom_percentage]

    cv.imwrite("out_images/" + fileName + ".png" ,new_img)    
# Flip image upside down.
def flip_image_up_and_down(img:np.ndarray,fileName:str):
    "Summary: With the image being inputed, the file will be flipped upside down and sent to output."
