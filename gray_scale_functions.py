
from math import floor
from warnings import catch_warnings
import cv2 as cv
import sys
from sniffio import current_async_library
import numpy

def lightScale_Blue(img,output_file_name):
    """
    This function uses light scale and changes the whole image's hue into Blue
    Through interating the function. Must write outputFile Name in .png/jpg end.
    """
    #Deep copy that image.
    img_ = img.copy()
    # img_ = numpy.array(img)
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [smallestValue,0,0]
    cv.imwrite("out_images/" + output_file_name,img_)

def lightScale_Green(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [0,smallestValue,0]
    cv.imwrite("out_images/" + output_file_name,img_)

def lightScale_Red(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [0,0,smallestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def lightScale_Cyan(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [smallestValue,smallestValue,0]
    cv.imwrite("out_images/" + output_file_name,img_)

def lightScale_Pink(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [smallestValue,0,smallestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def lightScale_Yellow(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [0,smallestValue,smallestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def lightScale(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    smallestValue = 0
    for i in range(height):
        for j in range(width):
            smallestValue = min(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [smallestValue,smallestValue,smallestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [biggestValue,biggestValue,biggestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale_Blue(img,output_file_name):
    """
    This function uses light scale and changes the whole image's hue into Blue
    Through interating the function. Must write outputFile Name in .png/jpg end.
    """
    #Deep copy that image.
    img_ = img.copy()
    # img_ = numpy.array(img)
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [biggestValue,0,0]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale_Green(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [0,biggestValue,0]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale_Red(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [0,0,biggestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale_Cyan(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [biggestValue,biggestValue,0]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale_Pink(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [biggestValue,0,biggestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def darkScale_Yellow(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    biggestValue = 255
    for i in range(height):
        for j in range(width):
            biggestValue = max(img_[i][j][0],img_[i][j][1],img_[i][j][2])
            img_[i][j] = [0,biggestValue,biggestValue]
    cv.imwrite("out_images/" + output_file_name,img_)

def avgScale(img,output_file_name):
    #Deep copy that image.
    img_ = img.copy()
    #Get images dimensions.
    dimensions = img_.shape
    # Get height width and channels.
    height = dimensions[0]
    width = dimensions[1]
    avgValue = floor(255/3)
    for i in range(height):
        for j in range(width):
            avgValue = floor((img[i][j][0]+img[i][j][1]+img[i][j][2])/3)
            img[i][j] = [avgValue,avgValue,avgValue]
    cv.imwrite("out_images/" + output_file_name,img_)