from _image_editing_functions import *

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

#Rotate to right
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

# Invert single RGB Color:
def invert_single_rgb(img:np.ndarray, fileName:str, mode:int) -> np.ndarray:
    """ 
        Invert any single RGB.
        mode: 0 = Blue, 1 = green, 2 = red
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            img_[i][j][mode] = 255-img_[i][j][mode]
    return outputFile(img_,fileName)

# Invert Two RGB Color:
def invert_two_rgb(img:np.ndarray, fileName:str, mode1:int, mode2:int) -> np.ndarray:
    """ 
        Invert any two RGB.
        mode: 
            01 - Cyan
            02 - violet/magneta
            12 - Yellow
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            img_[i][j][mode1] = 255-img_[i][j][mode1]
            img_[i][j][mode2] = 255-img_[i][j][mode2]
    return outputFile(img_,fileName)

# Invert All color, Full inversion:
def invert_color(img:np.ndarray, fileName:str) -> np.ndarray:
    """ 
        Invert All three RGB.
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            img_[i][j][0] = 255-img_[i][j][0]
            img_[i][j][1] = 255-img_[i][j][1]
            img_[i][j][2] = 255-img_[i][j][2]
    return outputFile(img_,fileName)

# Inversion.
def invert_color_improved(img:np.ndarray, fileName:str, amount:int) -> np.ndarray:
    """ 
        Controls how much is reverted with the differences in amount. 0-255
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            offsetBlue = amount - img_[i][j][0]
            offsetGreen = amount - img_[i][j][1]
            offsetRed = amount - img_[i][j][2]
            if(offsetGreen < 0 or offsetBlue < 0 or offsetRed < 0):
                if(offsetBlue < 0):
                    img_[i][j][0] = 255-offsetBlue
                if(offsetGreen < 0):
                    img_[i][j][1] = 255-offsetGreen
                if(offsetRed < 0):
                    img_[i][j][2] = 255-offsetRed
            else:
                img_[i][j][0] = offsetBlue
                img_[i][j][1] = offsetGreen
                img_[i][j][2] = offsetRed
    return outputFile(img_,fileName)

# Chang Hue.
def change_hue_1_modes(img:np.ndarray, fileName:str, amount:int,mode1=0) -> np.ndarray:
    """ 
        Controls how much hue is changed  with the differences in amount. 0-255
        if all three mode are the same, your swapping one single rgb.
        if two mode are the same, your swapping 2 of the rgb.
        if all three mode are different your swapping all which is just inverting.
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            offsetMode1 = amount - img_[i][j][mode1]
            if(offsetMode1 < 0):
                img_[i][j][mode1] = 255-img_[i][j][mode1]+amount
            else:
                img_[i][j][mode1] = offsetMode1
    return outputFile(img_,fileName)

# Chang Hue.
def change_hue_2_modes(img:np.ndarray, fileName:str, amount:int,mode1=0,mode2=0) -> np.ndarray:
    """ 
        Controls how much hue is changed  with the differences in amount. 0-255
        if all three mode are the same, your swapping one single rgb.
        if two mode are the same, your swapping 2 of the rgb.
        if all three mode are different your swapping all which is just inverting.
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            offsetMode1 = amount - img_[i][j][mode1]
            offsetMode2 = amount - img_[i][j][mode2]
            if(offsetMode1 < 0):
                img_[i][j][mode1] = 255-img_[i][j][mode1]+amount
            else:
                img_[i][j][mode1] = offsetMode1
            if(offsetMode2 < 0):
                img_[i][j][mode2] = 255-img_[i][j][mode2]+amount
            else:
                img_[i][j][mode2] = offsetMode2
    return outputFile(img_,fileName)

# Chang Hue.
def change_hue_3_modes(img:np.ndarray, fileName:str, amount:int,mode1=0,mode2=0,mode3=0) -> np.ndarray:
    """ 
        Controls how much hue is changed  with the differences in amount. 0-255
        if all three mode are the same, your swapping one single rgb.
        if two mode are the same, your swapping 2 of the rgb.
        if all three mode are different your swapping all which is just inverting.
    """
    img_ = img.copy()
    # This is flipped on purpose.
    height, width = dimension_img(img)
    for i in range(height):
        for j in range(width):
            offsetMode1 = amount - img_[i][j][mode1]
            offsetMode2 = amount - img_[i][j][mode2]
            offsetMode3 = amount - img_[i][j][mode3]
            if(offsetMode1 < 0):
                img_[i][j][mode1] = 255-img_[i][j][mode1]+amount
            else:
                img_[i][j][mode1] = offsetMode1
            if(offsetMode2 < 0):
                img_[i][j][mode2] = 255-img_[i][j][mode2]+amount
            else:
                img_[i][j][mode2] = offsetMode2
            if(offsetMode3 < 0):
                img_[i][j][mode3] = 255-img_[i][j][mode3]+amount
            else:
                img_[i][j][mode3] = offsetMode3
    return outputFile(img_,fileName)