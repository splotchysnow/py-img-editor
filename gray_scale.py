"""
Create gray scale base on the color provided: (Guan)
"""
from gray_scale_functions import *
#Load Images
img = loadImg("./img/wired_cat.webp")
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