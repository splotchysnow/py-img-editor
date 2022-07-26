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


# Normal Scaling Color test
lightScale(img,"gs_light_scale.png")
darkScale(img,"gs_dark_scale.png")
avgScale(img,"gs_avg_scale.png")
# Light Scale Color Test
lightScale_Blue(img,"gsl_blue.png")
lightScale_Green(img,"gsl_green.png")
lightScale_Red(img,"gsl_red.png")
lightScale_Cyan(img,"gsl_cyan.png")
lightScale_Pink(img,"gsl_pink.png")
lightScale_Yellow(img,"gsl_yellow.png")
# Dark Scale Color Test
lightScale_Blue(img,"gsd_blue.png")
lightScale_Green(img,"gsd_green.png")
lightScale_Red(img,"gsd_red.png")
lightScale_Cyan(img,"gsd_cyan.png")
lightScale_Pink(img,"gsd_pink.png")
lightScale_Yellow(img,"gsd_yellow.png")

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
