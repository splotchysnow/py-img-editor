"""
Create gray scale base on the color provided: (Guan)
"""
from gray_scale_functions import *

# Try read in the image data.
try:
    img = cv.imread(cv.samples.findFile("./img/wired_cat.webp"), cv.IMREAD_UNCHANGED)
except:
    sys.exit("Image can't be found")

#Case where the images dosn't excists.
if img is None:
    sys.exit("Image not exist")



lightScale(img,"gs_light_scale.png")
darkScale(img,"gs_dark_scale.png")
avgScale(img,"gs_avg_scale.png")
lightScale_Blue(img,"gs_blue.png")
lightScale_Green(img,"gs_green.png")
lightScale_Red(img,"gs_red.png")
lightScale_Cyan(img,"gs_mystery_color_1.png")
lightScale_Pink(img,"gs_mystery_color_2.png")
lightScale_Yellow(img,"gs_mystery_color_3.png")

# # output images.
# #set the window size to be controllable and fixed porpotion.    
# cv.namedWindow('My Image', cv.WINDOW_NORMAL)

# #display blurred image
# cv.imshow('My Image', img)

# #wait for keystroke in the window， then destroy
# cv.waitKey(0)
# cv.destroyAllWindows()

#write to output image file
cv.imwrite("out_images/line.png", img)
