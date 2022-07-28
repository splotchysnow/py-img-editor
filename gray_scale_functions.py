
from _image_editing_functions import *

def lightScale_Blue(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def lightScale_Green(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def lightScale_Red(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def lightScale_Cyan(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def lightScale_Pink(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def lightScale_Yellow(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def lightScale(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale_Blue(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale_Green(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale_Red(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale_Cyan(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale_Pink(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def darkScale_Yellow(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
    return outputFile(img_, output_file_name)

def avgScale(img:np.ndarray,output_file_name:str) -> np.ndarray:
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
            avgValue = floor((img_[i][j][0]+img_[i][j][1]+img_[i][j][2])/3)
            img_[i][j] = [avgValue,avgValue,avgValue]
    return outputFile(img_, output_file_name)

def avgImprovedScale(img:np.ndarray,output_file_name:str) -> np.ndarray:
    """
        Same functionality as avg scale above but much more improved in terms of algorithm..
        TODO: CHANGE?
    """
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
            avgValue = int((img_[i][j][0]+img_[i][j][1]+img_[i][j][2])/3)
            img_[i][j] = [avgValue,avgValue,avgValue]
    return outputFile(img_, output_file_name)
