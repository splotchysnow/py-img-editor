from typing import List
from gray_scale_functions import *

"""

    Brainstorm: The lower the image the darker.
    We take the darker image and discard anything that is considered as too light?

"""

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
def discard_above_threshold(image, threshold : int, pixel_x : int, pixel_y: int):
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


def Edge_Detection_Function(img, file_name, percent):
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
    cv.imwrite("out_images/" + file_name,img_)    

Edge_Detection_Function(loadImg("./img/wired_cat.webp"), "cat_edge_detection.png", 70)
